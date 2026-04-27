import os
import traceback
from datetime import datetime

import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_BasisElements as AllplanBasisEle

from BuildingElement import BuildingElement
from CreateElementResult import CreateElementResult
from PythonPartUtil import PythonPartUtil
from HandleProperties import HandleProperties
from HandleParameterData import HandleParameterData
from HandleParameterType import HandleParameterType
from HandleDirection import HandleDirection


DEBUG_LOG_PATH = os.path.join(os.path.expanduser("~"), "Documents", "Pergola_ZProfil_debug.log")


def _log(message: str) -> None:
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    try:
        with open(DEBUG_LOG_PATH, "a", encoding="utf-8") as log_file:
            log_file.write(f"[{timestamp}] {message}\n")
    except Exception:
        pass


def check_allplan_version(_build_ele: BuildingElement, version: float) -> bool:
    return float(version) >= 2026.0


def create_element(build_ele: BuildingElement, _doc) -> CreateElementResult:
    try:
        element = PergolaZProfil(build_ele)
        return element.create()
    except Exception:
        _log("create_element failed")
        _log(traceback.format_exc())
        return CreateElementResult()


def create_preview(build_ele: BuildingElement, doc) -> CreateElementResult:
    return create_element(build_ele, doc)


def move_handle(
    build_ele: BuildingElement,
    handle_prop: HandleProperties,
    input_pnt: AllplanGeo.Point3D,
    doc,
) -> CreateElementResult:
    try:
        HandleProperties.update_property_value(build_ele, handle_prop, input_pnt)
    except Exception:
        _log(f"move_handle failed for {getattr(handle_prop, 'handle_id', 'unknown')}")
        _log(traceback.format_exc())
    return create_element(build_ele, doc)


class PergolaZProfil:
    def __init__(self, build_ele: BuildingElement):
        self.build_ele = build_ele

        self.breite = self._read_float("Breite", 4000.0, 1000.0, 12000.0)
        self.tiefe = self._read_float("Tiefe", 3000.0, 1000.0, 8000.0)
        self.hoehe = self._read_float("Hoehe", 2500.0, 2000.0, 4000.0)

        self.pfosten_breite = self._read_float("PfostenBreite", 120.0, 80.0, 200.0)
        self.rahmen_hoehe = self._read_float("RahmenHoehe", 100.0, 50.0, 200.0)
        self.rahmen_breite = self._read_float("RahmenBreite", 80.0, 50.0, 200.0)

        self.lamellen_breite = self._read_float("LamellenBreite", 200.0, 100.0, 300.0)
        self.lamellen_hoehe = self._read_float("LamellenHoehe", 20.0, 15.0, 80.0)
        self.lamellen_staerke = self._read_float("LamellenStaerke", 2.0, 1.0, 5.0)
        self.lamellen_anzahl = self._read_int("LamellenAnzahl", 15, 3, 50)
        self.lamellen_stellung = self._read_str("LamellenStellung", "Geschlossen")

    def _read_raw_value(self, param_name: str, default_value):
        parameter = getattr(self.build_ele, param_name, None)
        if parameter is None:
            return default_value
        return getattr(parameter, "value", default_value)

    def _read_float(self, param_name: str, default_value: float, min_value: float, max_value: float) -> float:
        raw_value = self._read_raw_value(param_name, default_value)
        try:
            value = float(raw_value)
        except Exception:
            value = float(default_value)
        return max(min_value, min(max_value, value))

    def _read_int(self, param_name: str, default_value: int, min_value: int, max_value: int) -> int:
        raw_value = self._read_raw_value(param_name, default_value)
        try:
            value = int(raw_value)
        except Exception:
            value = int(default_value)
        return max(min_value, min(max_value, value))

    def _read_str(self, param_name: str, default_value: str) -> str:
        raw_value = self._read_raw_value(param_name, default_value)
        if raw_value is None:
            return default_value
        value = str(raw_value).strip()
        return value if value else default_value

    @staticmethod
    def _make_common_properties(color: int, pen: int = 1) -> AllplanBaseEle.CommonProperties:
        com_prop = AllplanBaseEle.CommonProperties()
        com_prop.GetGlobalProperties()
        com_prop.Color = int(color)
        com_prop.Pen = int(pen)
        return com_prop

    @staticmethod
    def _append_cuboid(model_elements: list, com_prop: AllplanBaseEle.CommonProperties, x: float, y: float, z: float,
                       length: float, width: float, height: float) -> None:
        if length <= 0.0 or width <= 0.0 or height <= 0.0:
            return
        placement = AllplanGeo.AxisPlacement3D(AllplanGeo.Point3D(x, y, z))
        cuboid = AllplanGeo.BRep3D.CreateCuboid(placement, length, width, height)
        model_elements.append(AllplanBasisEle.ModelElement3D(com_prop, cuboid))

    def _get_lamella_angle_deg(self) -> float:
        angle_by_stellung = {
            "Geschlossen": 5.0,
            "Halboffen": 45.0,
            "Offen": 90.0,
        }
        return angle_by_stellung.get(self.lamellen_stellung, 0.0)

    def _validate_geometry(self) -> bool:
        if self.breite <= 2.0 * self.rahmen_breite:
            _log("Invalid geometry: Breite <= 2 * RahmenBreite")
            return False

        if self.tiefe <= 2.0 * self.rahmen_breite:
            _log("Invalid geometry: Tiefe <= 2 * RahmenBreite")
            return False

        if self.pfosten_breite > min(self.breite, self.tiefe):
            _log("Invalid geometry: PfostenBreite too large")
            return False

        if self.lamellen_staerke >= 0.5 * self.lamellen_hoehe:
            _log("Invalid geometry: LamellenStaerke too large for LamellenHoehe")
            return False

        return True

    def _create_posts(self, model_elements: list, com_prop: AllplanBaseEle.CommonProperties) -> None:
        z0 = 0.0
        x_back = self.breite - self.pfosten_breite
        y_back = self.tiefe - self.pfosten_breite

        self._append_cuboid(model_elements, com_prop, 0.0, 0.0, z0,
                            self.pfosten_breite, self.pfosten_breite, self.hoehe)
        self._append_cuboid(model_elements, com_prop, x_back, 0.0, z0,
                            self.pfosten_breite, self.pfosten_breite, self.hoehe)
        self._append_cuboid(model_elements, com_prop, 0.0, y_back, z0,
                            self.pfosten_breite, self.pfosten_breite, self.hoehe)
        self._append_cuboid(model_elements, com_prop, x_back, y_back, z0,
                            self.pfosten_breite, self.pfosten_breite, self.hoehe)

    def _create_frame(self, model_elements: list, com_prop: AllplanBaseEle.CommonProperties) -> None:
        z0 = self.hoehe

        self._append_cuboid(model_elements, com_prop, 0.0, 0.0, z0,
                            self.breite, self.rahmen_breite, self.rahmen_hoehe)
        self._append_cuboid(model_elements, com_prop, 0.0, self.tiefe - self.rahmen_breite, z0,
                            self.breite, self.rahmen_breite, self.rahmen_hoehe)

        self._append_cuboid(model_elements, com_prop, 0.0, 0.0, z0,
                            self.rahmen_breite, self.tiefe, self.rahmen_hoehe)
        self._append_cuboid(model_elements, com_prop, self.breite - self.rahmen_breite, 0.0, z0,
                            self.rahmen_breite, self.tiefe, self.rahmen_hoehe)

    def _create_lamella_local_parts(self, lamella_length: float, lamella_span: float, tip_clearance: float) -> list:
        half_span = 0.5 * lamella_span
        thickness = self.lamellen_staerke
        y0 = -0.5 * lamella_length
        lip_height = max(thickness, self.lamellen_hoehe - tip_clearance)
        web_z_min = -0.5 * thickness

        # Zielkontur je Lamelle (in XZ) nach Skizze:
        # links Steg nach unten, mittig Horizontalsteg, rechts Steg nach oben.
        horizontal_web = AllplanGeo.BRep3D.CreateCuboid(
            AllplanGeo.AxisPlacement3D(AllplanGeo.Point3D(-half_span, y0, web_z_min)),
            lamella_span,
            lamella_length,
            thickness,
        )

        left_downstand = AllplanGeo.BRep3D.CreateCuboid(
            AllplanGeo.AxisPlacement3D(AllplanGeo.Point3D(-half_span, y0, web_z_min - lip_height)),
            thickness,
            lamella_length,
            lip_height,
        )

        right_upstand = AllplanGeo.BRep3D.CreateCuboid(
            AllplanGeo.AxisPlacement3D(AllplanGeo.Point3D(half_span - thickness, y0, web_z_min + thickness)),
            thickness,
            lamella_length,
            lip_height,
        )

        return [horizontal_web, left_downstand, right_upstand]

    def _create_lamellas(self, model_elements: list, com_prop: AllplanBaseEle.CommonProperties) -> None:
        inner_width = self.breite - 2.0 * self.rahmen_breite
        inner_depth = self.tiefe - 2.0 * self.rahmen_breite

        if inner_width <= 0.0 or inner_depth <= 0.0:
            _log("Lamellas skipped: no inner frame area")
            return

        pitch = inner_width / float(self.lamellen_anzahl)
        interlock_gap = 2.5  # mm: gewuenschte Luftfuge im geschlossenen Zustand (2-3 mm)
        interlock_extra_width = 8.0  # mm: zusaetzliche Profilbreite fuer sicheres Ineinandergreifen
        tip_clearance = interlock_gap  # mm: gleicher Abstand an den markierten Profilenden
        # Span so waehlen, dass die gegenueberliegenden Steg-Innenflaechen benachbarter Lamellen
        # im geschlossenen Zustand mit ca. interlock_gap getrennt bleiben und Enden tiefer ineinander greifen.
        lamella_span = max(
            self.lamellen_breite + interlock_extra_width,
            pitch + 2.0 * self.lamellen_staerke - interlock_gap + interlock_extra_width,
        )
        center_y = self.tiefe * 0.5
        center_z = self.hoehe + 0.5 * self.rahmen_hoehe

        local_parts = self._create_lamella_local_parts(inner_depth, lamella_span, tip_clearance)

        axis = AllplanGeo.Line3D(
            AllplanGeo.Point3D(0.0, 0.0, 0.0),
            AllplanGeo.Point3D(0.0, 1.0, 0.0),
        )
        rotation_matrix = AllplanGeo.Matrix3D()
        angle = AllplanGeo.Angle.FromDeg(self._get_lamella_angle_deg())
        rotation_ok = rotation_matrix.Rotation(axis, angle)
        if not rotation_ok:
            _log("Lamella rotation matrix could not be created")

        for index in range(self.lamellen_anzahl):
            x_pos = self.rahmen_breite + (0.5 + index) * pitch

            move_matrix = AllplanGeo.Matrix3D()
            move_matrix.Translate(AllplanGeo.Vector3D(x_pos, center_y, center_z))

            for local_part in local_parts:
                rotated_part = AllplanGeo.Transform(local_part, rotation_matrix)
                placed_part = AllplanGeo.Transform(rotated_part, move_matrix)
                model_elements.append(AllplanBasisEle.ModelElement3D(com_prop, placed_part))

    def _create_handles(self) -> list[HandleProperties]:
        return [
            HandleProperties(
                handle_id="BreiteHandle",
                handle_point=AllplanGeo.Point3D(self.breite, 0.0, 0.0),
                ref_point=AllplanGeo.Point3D(0.0, 0.0, 0.0),
                handle_param_data=[HandleParameterData("Breite", HandleParameterType.X_DISTANCE)],
                handle_move_dir=HandleDirection.X_DIR,
            ),
            HandleProperties(
                handle_id="TiefeHandle",
                handle_point=AllplanGeo.Point3D(0.0, self.tiefe, 0.0),
                ref_point=AllplanGeo.Point3D(0.0, 0.0, 0.0),
                handle_param_data=[HandleParameterData("Tiefe", HandleParameterType.Y_DISTANCE)],
                handle_move_dir=HandleDirection.Y_DIR,
            ),
            HandleProperties(
                handle_id="HoeheHandle",
                handle_point=AllplanGeo.Point3D(0.0, 0.0, self.hoehe),
                ref_point=AllplanGeo.Point3D(0.0, 0.0, 0.0),
                handle_param_data=[HandleParameterData("Hoehe", HandleParameterType.Z_DISTANCE)],
                handle_move_dir=HandleDirection.Z_DIR,
            ),
        ]

    def create(self) -> CreateElementResult:
        if not self._validate_geometry():
            return CreateElementResult()

        angle_deg = self._get_lamella_angle_deg()
        _log(
            "create Pergola_ZProfil: "
            f"Breite={self.breite}, Tiefe={self.tiefe}, Hoehe={self.hoehe}, "
            f"LamellenAnzahl={self.lamellen_anzahl}, LamellenStellung={self.lamellen_stellung}, Winkel={angle_deg}"
        )

        structure_prop = self._make_common_properties(color=8, pen=1)
        lamella_prop = self._make_common_properties(color=3, pen=1)

        model_elements = []
        self._create_posts(model_elements, structure_prop)
        self._create_frame(model_elements, structure_prop)
        self._create_lamellas(model_elements, lamella_prop)

        if not model_elements:
            _log("No geometry generated")
            return CreateElementResult()

        pyp_util = PythonPartUtil(structure_prop)
        pyp_util.add_pythonpart_view_2d3d(model_elements)
        created_elements = pyp_util.create_pythonpart(self.build_ele)

        handles = self._create_handles()
        _log(f"Geometry generated successfully: solids={len(model_elements)}, handles={len(handles)}")
        return CreateElementResult(elements=created_elements, handles=handles)
