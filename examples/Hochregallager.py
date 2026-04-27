import NemAll_Python_Geometry as AllplanGeo
import NemAll_Python_BaseElements as AllplanBaseElements
import NemAll_Python_BasisElements as AllplanBasisElements
import traceback

from BuildingElement import BuildingElement
from CreateElementResult import CreateElementResult
from PythonPartUtil import PythonPartUtil
from HandleProperties import HandleProperties
from HandleParameterData import HandleParameterData
from HandleParameterType import HandleParameterType
from HandleDirection import HandleDirection


def check_allplan_version(build_ele: BuildingElement, version: str) -> bool:
    del build_ele
    del version
    return True


def create_element(build_ele: BuildingElement, doc) -> CreateElementResult:
    del doc
    try:
        element = Hochregallager(build_ele)
        return element.create()
    except Exception:
        print("Hochregallager: create_element failed")
        traceback.print_exc()
        return CreateElementResult()


def create_preview(build_ele: BuildingElement, doc) -> CreateElementResult:
    return create_element(build_ele, doc)


def move_handle(build_ele: BuildingElement, handle_prop: HandleProperties, input_pnt: AllplanGeo.Point3D, doc) -> CreateElementResult:
    try:
        HandleProperties.update_property_value(build_ele, handle_prop, input_pnt)
    except Exception:
        print("Hochregallager: move_handle update failed")
        traceback.print_exc()
    return create_element(build_ele, doc)


class Hochregallager:
    def __init__(self, build_ele: BuildingElement):
        self.build_ele = build_ele

        self.field_count_x = int(self._read_param("FieldCountX", 3))
        self.field_count_y = int(self._read_param("FieldCountY", 1))
        self.level_count_z = int(self._read_param("LevelCountZ", 3))

        self.field_width = float(self._read_param("FieldWidth", 2700.0))
        self.field_depth = float(self._read_param("FieldDepth", 1100.0))
        self.level_height = float(self._read_param("LevelHeight", 1800.0))

        self.double_rack = self._read_bool("DoubleRack", False)
        self.aisle_width = float(self._read_param("AisleWidth", 3000.0))
        self.row_spacing = float(self._read_param("RowSpacing", 3000.0))

        self.post_width = float(self._read_param("PostWidth", 80.0))
        self.post_depth = float(self._read_param("PostDepth", 83.0))
        self.beam_height = float(self._read_param("BeamHeight", 120.0))
        self.beam_depth = float(self._read_param("BeamDepth", 50.0))
        self.beam_capacity = float(self._read_param("BeamCapacity", 3000.0))

        self.show_ground_beams = self._read_bool("ShowGroundBeams", False)

        self.show_shelves = self._read_bool("ShowShelves", True)
        self.shelf_thickness = float(self._read_param("ShelfThickness", 20.0))
        self.show_ground_shelf = self._read_bool("ShowGroundShelf", False)

        self.show_bracing = self._read_bool("ShowBracing", True)
        self.bracing_depth = float(self._read_param("BracingDepth", 30.0))
        self.bracing_width = float(self._read_param("BracingWidth", 30.0))

        self.show_base_plates = self._read_bool("ShowBasePlates", True)
        self.base_plate_length = float(self._read_param("BasePlateLength", 150.0))
        self.base_plate_width = float(self._read_param("BasePlateWidth", 118.0))
        self.base_plate_thickness = float(self._read_param("BasePlateThickness", 5.0))

        self.show_pallets = self._read_bool("ShowPallets", True)
        self.pallet_length = float(self._read_param("PalletLength", 1200.0))
        self.pallet_width = float(self._read_param("PalletWidth", 800.0))
        self.pallet_height = float(self._read_param("PalletHeight", 144.0))
        self.pallets_per_field = int(self._read_param("PalletsPerField", 2))
        self.pallet_gap_x = float(self._read_param("PalletGapX", 100.0))
        self.pallet_gap_y = float(self._read_param("PalletGapY", 50.0))

        self.weight_per_level = self._normalize_weight_list(
            self._read_param("WeightPerLevel", [1000.0, 1000.0, 800.0])
        )

        self.color_posts = int(self._read_param("ColorPosts", 1))
        self.pen_posts = int(self._read_param("PenPosts", 1))
        self.color_beams = int(self._read_param("ColorBeams", 3))
        self.pen_beams = int(self._read_param("PenBeams", 1))
        self.color_shelves = int(self._read_param("ColorShelves", 6))
        self.pen_shelves = int(self._read_param("PenShelves", 1))
        self.color_bracing = int(self._read_param("ColorBracing", 5))
        self.pen_bracing = int(self._read_param("PenBracing", 1))
        self.color_base_plates = int(self._read_param("ColorBasePlates", 4))
        self.pen_base_plates = int(self._read_param("PenBasePlates", 1))
        self.color_pallets = int(self._read_param("ColorPallets", 4))
        self.pen_pallets = int(self._read_param("PenPallets", 1))

    def _read_param(self, param_name: str, default_value):
        param_obj = getattr(self.build_ele, param_name, None)
        if param_obj is None:
            return default_value
        return getattr(param_obj, "value", default_value)

    def _read_bool(self, param_name: str, default_value: bool) -> bool:
        raw_value = self._read_param(param_name, default_value)
        if isinstance(raw_value, bool):
            return raw_value
        return str(raw_value).strip().lower() in ("true", "1", "yes", "ja")

    @staticmethod
    def _is_positive(value) -> bool:
        return value is not None and value > 0

    @staticmethod
    def _make_com_prop(color: int, pen: int) -> AllplanBaseElements.CommonProperties:
        com_prop = AllplanBaseElements.CommonProperties()
        com_prop.GetGlobalProperties()
        com_prop.Color = int(color)
        com_prop.Pen = int(pen)
        return com_prop

    @staticmethod
    def _append_cuboid(model_elements, common_properties, placement, length, width, height):
        if length <= 0 or width <= 0 or height <= 0:
            return
        cuboid = AllplanGeo.BRep3D.CreateCuboid(placement, length, width, height)
        model_elements.append(AllplanBasisElements.ModelElement3D(common_properties, cuboid))

    def _normalize_weight_list(self, raw_value):
        values = []
        if isinstance(raw_value, list):
            values = raw_value
        elif isinstance(raw_value, tuple):
            values = list(raw_value)
        elif isinstance(raw_value, str):
            stripped = raw_value.strip().strip("[]")
            if stripped:
                parts = stripped.split(",")
                for part in parts:
                    try:
                        values.append(float(part.strip()))
                    except Exception:
                        values.append(1000.0)
        else:
            values = [1000.0] * self.level_count_z

        normalized = []
        for value in values:
            try:
                normalized.append(float(value))
            except Exception:
                normalized.append(1000.0)

        while len(normalized) < self.level_count_z:
            normalized.append(1000.0)
        if len(normalized) > self.level_count_z:
            normalized = normalized[: self.level_count_z]

        return normalized

    def _get_rack_offsets(self):
        if self.double_rack:
            return [0.0, self.field_depth + self.aisle_width]
        step = self.field_depth + self.row_spacing
        return [row * step for row in range(self.field_count_y)]

    def _get_load_color(self, weight_kg: float) -> int:
        if self.beam_capacity <= 0:
            return self.color_pallets

        ratio = weight_kg / self.beam_capacity
        if ratio <= 0.5:
            return 6
        if ratio <= 0.75:
            return 5
        if ratio <= 1.0:
            return 3
        return 2

    def _get_total_dimensions(self):
        total_length = self.field_count_x * self.field_width + self.post_width
        if self.double_rack:
            total_depth = 2.0 * self.field_depth + self.aisle_width
        else:
            total_depth = self.field_count_y * self.field_depth + max(0, self.field_count_y - 1) * self.row_spacing
        total_height = self.level_count_z * self.level_height + self.post_width
        return total_length, total_depth, total_height

    def _calculate_and_set_info(self):
        total_length, total_depth, total_height = self._get_total_dimensions()

        rack_count = len(self._get_rack_offsets())
        total_weight = sum(self.weight_per_level) * self.field_count_x * rack_count
        max_beam_load = max(self.weight_per_level) if self.weight_per_level else 0.0
        total_slots = self.field_count_x * self.level_count_z * self.pallets_per_field * rack_count

        warning = "OK"
        for idx, weight in enumerate(self.weight_per_level):
            if self.beam_capacity > 0 and weight > self.beam_capacity:
                warning = (
                    f"WARNUNG: Ebene {idx + 1} ueberlastet "
                    f"({weight:.0f}kg > {self.beam_capacity:.0f}kg)"
                )
                break

        for name, value in (
            ("TotalLength", total_length),
            ("TotalDepth", total_depth),
            ("TotalHeight", total_height),
            ("TotalWeight", total_weight),
            ("MaxBeamLoad", max_beam_load),
            ("TotalPalletSlots", total_slots),
            ("OverloadWarning", warning),
        ):
            param_obj = getattr(self.build_ele, name, None)
            if param_obj is not None:
                param_obj.value = value

    def _create_posts(self, model_elements, com_prop, y_offset: float, total_height: float) -> None:
        for i in range(self.field_count_x + 1):
            x_start = i * self.field_width

            placement_front = AllplanGeo.AxisPlacement3D(AllplanGeo.Point3D(x_start, y_offset, 0.0))
            self._append_cuboid(model_elements, com_prop, placement_front, self.post_width, self.post_depth, total_height)

            placement_back = AllplanGeo.AxisPlacement3D(
                AllplanGeo.Point3D(x_start, y_offset + self.field_depth - self.post_depth, 0.0)
            )
            self._append_cuboid(model_elements, com_prop, placement_back, self.post_width, self.post_depth, total_height)

    def _create_cross_beams(self, model_elements, com_prop, y_offset: float) -> None:
        cross_length = self.field_depth - 2.0 * self.post_depth
        if cross_length <= 0:
            return

        start_level = 0 if self.show_ground_beams else 1
        for i in range(self.field_count_x + 1):
            x_start = i * self.field_width
            cross_x = x_start + (self.post_width - self.beam_depth) / 2.0
            cross_y = y_offset + self.post_depth

            for j in range(start_level, self.level_count_z + 1):
                z_pos = j * self.level_height
                placement_cross = AllplanGeo.AxisPlacement3D(AllplanGeo.Point3D(cross_x, cross_y, z_pos))
                self._append_cuboid(model_elements, com_prop, placement_cross, self.beam_depth, cross_length, self.beam_height)

    def _create_long_beams(self, model_elements, com_prop, y_offset: float) -> None:
        beam_length = self.field_width - self.post_width
        if beam_length <= 0:
            return

        start_level = 0 if self.show_ground_beams else 1
        for i in range(self.field_count_x):
            x_start = i * self.field_width + self.post_width

            for j in range(start_level, self.level_count_z + 1):
                z_pos = j * self.level_height

                placement_front = AllplanGeo.AxisPlacement3D(AllplanGeo.Point3D(x_start, y_offset, z_pos))
                self._append_cuboid(model_elements, com_prop, placement_front, beam_length, self.beam_depth, self.beam_height)

                placement_back = AllplanGeo.AxisPlacement3D(
                    AllplanGeo.Point3D(x_start, y_offset + self.field_depth - self.beam_depth, z_pos)
                )
                self._append_cuboid(model_elements, com_prop, placement_back, beam_length, self.beam_depth, self.beam_height)

    def _create_shelves(self, model_elements, com_prop, y_offset: float) -> None:
        shelf_length = self.field_width - self.post_width
        shelf_depth = self.field_depth - 2.0 * self.post_depth
        if shelf_length <= 0 or shelf_depth <= 0:
            return

        start_level = 0 if self.show_ground_shelf else 1
        for i in range(self.field_count_x):
            x_start = i * self.field_width + self.post_width
            y_start = y_offset + self.post_depth

            for j in range(start_level, self.level_count_z + 1):
                if j == 0:
                    z_start = 0.0
                else:
                    z_start = j * self.level_height + self.beam_height
                placement = AllplanGeo.AxisPlacement3D(AllplanGeo.Point3D(x_start, y_start, z_start))
                self._append_cuboid(model_elements, com_prop, placement, shelf_length, shelf_depth, self.shelf_thickness)

    @staticmethod
    def _append_bracing_diagonal(model_elements, com_prop, x_center, y_start, z_start, y_end, z_end, depth, width):
        """Diagonale als orientierter Quaderstab (Quadratrohr-Charakter)."""
        if depth <= 0 or width <= 0:
            return

        dy = y_end - y_start
        dz = z_end - z_start
        diag_len = (dy * dy + dz * dz) ** 0.5
        if diag_len <= 1e-6:
            return

        # Lokale y-Achse folgt der Diagonalen (Y/Z), lokale x-Achse bleibt global X.
        unit_y = dy / diag_len
        unit_z = dz / diag_len
        z_dir = AllplanGeo.Vector3D(0.0, -unit_z, unit_y)

        # Ursprung so versetzen, dass die Diagonale auf der Profilmitte liegt.
        origin = AllplanGeo.Point3D(
            x_center,
            y_start - 0.5 * width * z_dir.Y,
            z_start - 0.5 * width * z_dir.Z,
        )

        placement = AllplanGeo.AxisPlacement3D()
        placement.Set(origin, AllplanGeo.Vector3D(1.0, 0.0, 0.0), z_dir)
        bar = AllplanGeo.BRep3D.CreateCuboid(placement, depth, diag_len, width)
        model_elements.append(AllplanBasisElements.ModelElement3D(com_prop, bar))

    def _create_bracing(self, model_elements, com_prop, y_offset: float) -> None:
        y_front = y_offset + self.post_depth
        y_back = y_offset + self.field_depth - self.post_depth
        if y_back <= y_front:
            return

        for i in range(self.field_count_x + 1):
            x_center = i * self.field_width + (self.post_width - self.bracing_depth) / 2.0

            for level_idx in range(self.level_count_z):
                z_low = level_idx * self.level_height
                z_high = (level_idx + 1) * self.level_height

                # X-Austeifung: beide Diagonalen erzeugen
                self._append_bracing_diagonal(
                    model_elements, com_prop,
                    x_center, y_front, z_low, y_back, z_high,
                    self.bracing_depth, self.bracing_width
                )
                self._append_bracing_diagonal(
                    model_elements, com_prop,
                    x_center, y_back, z_low, y_front, z_high,
                    self.bracing_depth, self.bracing_width
                )

    def _create_base_plates(self, model_elements, com_prop, y_offset: float) -> None:
        offset_x = (self.base_plate_length - self.post_width) / 2.0
        offset_y = (self.base_plate_width - self.post_depth) / 2.0

        for i in range(self.field_count_x + 1):
            x_post = i * self.field_width
            for y_post in (y_offset, y_offset + self.field_depth - self.post_depth):
                placement = AllplanGeo.AxisPlacement3D(
                    AllplanGeo.Point3D(x_post - offset_x, y_post - offset_y, -self.base_plate_thickness)
                )
                self._append_cuboid(
                    model_elements,
                    com_prop,
                    placement,
                    self.base_plate_length,
                    self.base_plate_width,
                    self.base_plate_thickness,
                )

    def _create_pallets(self, model_elements, y_offset: float) -> None:
        field_inner_width = self.field_width - self.post_width
        inner_depth = self.field_depth - 2.0 * self.post_depth
        total_pallets_width = (
            self.pallets_per_field * self.pallet_length
            + max(0, self.pallets_per_field - 1) * self.pallet_gap_x
        )

        if total_pallets_width > field_inner_width:
            warning_param = getattr(self.build_ele, "OverloadWarning", None)
            if warning_param is not None and str(warning_param.value) == "OK":
                warning_param.value = "WARNUNG: Paletten passen nicht in Feldbreite"
            return

        if self.pallet_width + 2.0 * self.pallet_gap_y > inner_depth:
            warning_param = getattr(self.build_ele, "OverloadWarning", None)
            if warning_param is not None and str(warning_param.value) == "OK":
                warning_param.value = "WARNUNG: Paletten passen nicht in Regaltiefe"
            return

        start_level = 0 if self.show_ground_shelf else 1
        for i in range(self.field_count_x):
            field_inner_start_x = i * self.field_width + self.post_width
            x_offset = (field_inner_width - total_pallets_width) / 2.0

            for j in range(start_level, self.level_count_z + 1):
                level_weight = 0.0
                if j > 0 and j - 1 < len(self.weight_per_level):
                    level_weight = self.weight_per_level[j - 1]

                load_color = self._get_load_color(level_weight)
                pallet_com_prop = self._make_com_prop(load_color, self.pen_pallets)

                if j == 0:
                    z_start = 0.0
                else:
                    z_start = j * self.level_height + self.beam_height
                if self.show_shelves:
                    z_start += self.shelf_thickness

                pallet_y = y_offset + self.post_depth + self.pallet_gap_y

                for k in range(self.pallets_per_field):
                    pallet_x = field_inner_start_x + x_offset + k * (self.pallet_length + self.pallet_gap_x)
                    placement = AllplanGeo.AxisPlacement3D(AllplanGeo.Point3D(pallet_x, pallet_y, z_start))
                    self._append_cuboid(
                        model_elements,
                        pallet_com_prop,
                        placement,
                        self.pallet_length,
                        self.pallet_width,
                        self.pallet_height,
                    )

    def _create_single_rack(self, model_elements, com_props: dict, y_offset: float) -> None:
        total_height = self.level_count_z * self.level_height + self.post_width
        self._create_posts(model_elements, com_props["posts"], y_offset, total_height)
        self._create_cross_beams(model_elements, com_props["beams"], y_offset)
        self._create_long_beams(model_elements, com_props["beams"], y_offset)

        if self.show_shelves:
            self._create_shelves(model_elements, com_props["shelves"], y_offset)

        if self.show_pallets:
            self._create_pallets(model_elements, y_offset)

        if self.show_bracing:
            self._create_bracing(model_elements, com_props["bracing"], y_offset)

        if self.show_base_plates:
            self._create_base_plates(model_elements, com_props["base_plates"], y_offset)

    def _create_handles(self, total_length: float, total_height: float):
        handles = []

        handles.append(
            HandleProperties(
                handle_id="FieldWidthHandle",
                handle_point=AllplanGeo.Point3D(total_length, 0.0, 0.0),
                ref_point=AllplanGeo.Point3D(total_length - self.field_width, 0.0, 0.0),
                handle_param_data=[HandleParameterData("FieldWidth", HandleParameterType.X_DISTANCE)],
                handle_move_dir=HandleDirection.X_DIR,
            )
        )

        handles.append(
            HandleProperties(
                handle_id="FieldDepthHandle",
                handle_point=AllplanGeo.Point3D(0.0, self.field_depth, 0.0),
                ref_point=AllplanGeo.Point3D(0.0, 0.0, 0.0),
                handle_param_data=[HandleParameterData("FieldDepth", HandleParameterType.Y_DISTANCE)],
                handle_move_dir=HandleDirection.Y_DIR,
            )
        )

        handles.append(
            HandleProperties(
                handle_id="LevelHeightHandle",
                handle_point=AllplanGeo.Point3D(0.0, 0.0, total_height),
                ref_point=AllplanGeo.Point3D(0.0, 0.0, total_height - self.level_height),
                handle_param_data=[HandleParameterData("LevelHeight", HandleParameterType.Z_DISTANCE)],
                handle_move_dir=HandleDirection.Z_DIR,
            )
        )

        return handles

    def create(self) -> CreateElementResult:
        if self.field_count_x < 1 or self.field_count_y < 1 or self.level_count_z < 1:
            print("Hochregallager: FieldCountX/FieldCountY/LevelCountZ must be >= 1")
            return CreateElementResult()

        if self.pallets_per_field < 1:
            print("Hochregallager: PalletsPerField must be >= 1")
            return CreateElementResult()

        required_positive = [
            self.field_width,
            self.field_depth,
            self.level_height,
            self.post_width,
            self.post_depth,
            self.beam_height,
            self.beam_depth,
            self.pallet_length,
            self.pallet_width,
            self.pallet_height,
        ]

        if self.show_shelves:
            required_positive.append(self.shelf_thickness)
        if self.show_bracing:
            required_positive.extend([self.bracing_depth, self.bracing_width])
        if self.show_base_plates:
            required_positive.extend([self.base_plate_length, self.base_plate_width, self.base_plate_thickness])
        if not all(self._is_positive(value) for value in required_positive):
            print("Hochregallager: all geometric parameters must be > 0")
            return CreateElementResult()

        if self.double_rack and self.aisle_width <= 0:
            print("Hochregallager: AisleWidth must be > 0 when DoubleRack is enabled")
            return CreateElementResult()

        if not self.double_rack and self.field_count_y > 1 and self.row_spacing <= 0:
            print("Hochregallager: RowSpacing must be > 0 when multiple rows")
            return CreateElementResult()

        if self.show_pallets and (self.pallet_gap_x < 0 or self.pallet_gap_y < 0):
            print("Hochregallager: pallet gaps must be >= 0")
            return CreateElementResult()

        self._calculate_and_set_info()
        total_length, _, total_height = self._get_total_dimensions()

        com_props = {
            "posts": self._make_com_prop(self.color_posts, self.pen_posts),
            "beams": self._make_com_prop(self.color_beams, self.pen_beams),
            "shelves": self._make_com_prop(self.color_shelves, self.pen_shelves),
            "bracing": self._make_com_prop(self.color_bracing, self.pen_bracing),
            "base_plates": self._make_com_prop(self.color_base_plates, self.pen_base_plates),
            "pallets": self._make_com_prop(self.color_pallets, self.pen_pallets),
        }

        model_elements = []
        for y_offset in self._get_rack_offsets():
            self._create_single_rack(model_elements, com_props, y_offset)

        if not model_elements:
            print("Hochregallager: no valid geometry created")
            return CreateElementResult()

        pyp_util = PythonPartUtil(com_props["posts"])
        pyp_util.add_pythonpart_view_2d3d(model_elements)
        handles = self._create_handles(total_length, total_height)

        return CreateElementResult(elements=pyp_util.create_pythonpart(self.build_ele), handles=handles)
