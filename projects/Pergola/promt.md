# PythonPart Task: Pergola_ZProfil

## Description
Freistehende bioklimatische Pergola mit drehbaren Z-Profil-Lamellen als Dach. Der Anwender platziert die Pergola, stellt Abmessungen über die Palette ein und wählt die Lamellenstellung: **Geschlossen** (regendicht, 0°), **Halboffen** (Teilverschattung, 45°) oder **Offen** (maximaler Lichteinfall, 90°). Alle Lamellen drehen synchron um ihre Längsachse.

## Requirements
- Vier Pfosten (Alu-Hohlprofil, vereinfacht als Vollquadrat) tragen einen umlaufenden Rahmen
- Im Rahmen liegen parallele Z-Profil-Lamellen, gleichmäßig über die Breite verteilt
- Lamellenstellung über StringComboBox wählbar: `"Geschlossen"` (0°), `"Halboffen"` (45°), `"Offen"` (90°)
- Alle Hauptmaße (Breite, Tiefe, Höhe) über Handles interaktiv änderbar
- Lamellenanzahl, Profilmaße und Tragstruktur-Maße parametrisch über Palette steuerbar

## Geometry

### Koordinatensystem

```
        Y (Tiefe/Ausfall)
        ↑
        │   ┌───────────────────────────────────┐  ← Rahmen hinten
        │   │  ═══  ═══  ═══  ═══  ═══  ═══    │  ← Lamellen (X-verteilt)
        │   │  ═══  ═══  ═══  ═══  ═══  ═══    │
        │   └───────────────────────────────────┘  ← Rahmen vorne
        └──────────────────────────────────────→ X (Breite)

  Z = Höhe (Pfosten nach oben, Rahmen + Lamellen oben)
```

### Bauteilhierarchie

```
Pergola
├── 4× Pfosten            CreateCuboid(PfostenBreite, PfostenBreite, Hoehe)
├── 2× Längsträger (X)    CreateCuboid(Breite, RahmenBreite, RahmenHoehe)
├── 2× Querträger (Y)     CreateCuboid(RahmenBreite, Tiefe, RahmenHoehe)
└── n× Lamellen            Extrusion Z-Profil-Polygon2D entlang Y, rotiert
```

### Z-Profil-Querschnitt (XZ-Ebene, 8-Punkt-Polygon, zentriert um Ursprung)

```
  hw = LamellenBreite / 2,  hh = LamellenHoehe / 2,  t = LamellenStaerke

      P0─────────────P1        +hh
      │               │
      P3──────────────P2       +hh - t
      │
      │  (Steg, Breite = t)
      │
      P4──────────────P5       -hh + t
                      │
      P7─────────────P6        -hh

  X:  -hw            +hw

  Polygon2D Punkte:
    P0(-hw, +hh) → P1(+hw, +hh) → P2(+hw, +hh-t) → P3(-hw+t, +hh-t)
    → P4(-hw+t, -hh+t) → P5(+hw, -hh+t) → P6(+hw, -hh) → P7(-hw, -hh) → close
```

### Lamellenrotation

Jede Lamelle rotiert um ihre Längsachse (Y-Achse durch Profilmitte):

```python
achse = AllplanGeo.Line3D(
    AllplanGeo.Point3D(x_pos, 0, z_pos),
    AllplanGeo.Point3D(x_pos, 1, z_pos)
)
matrix = AllplanGeo.Matrix3D()
matrix.Rotation(achse, AllplanGeo.Angle.DegToRad(winkel))
lamelle_rotiert = AllplanGeo.Transform(lamelle_extrudiert, matrix)
```

### Lamellenverteilung

```python
spannweite = Breite - 2 * RahmenBreite
abstand = spannweite / LamellenAnzahl
x_pos = RahmenBreite + abstand / 2 + i * abstand   # i = 0..n-1
```

## Parameters (Palette)

| Name | Type | Default | Description |
|------|------|---------|------------|
| Breite | Length | 4000 | Gesamtbreite X (mm), Min 1000, Max 12000 |
| Tiefe | Length | 3000 | Gesamttiefe Y (mm), Min 1000, Max 8000 |
| Hoehe | Length | 2500 | Pfostenhöhe Z (mm), Min 2000, Max 4000 |
| PfostenBreite | Length | 120 | Querschnitt Pfosten quadratisch (mm), Min 80, Max 200 |
| RahmenHoehe | Length | 100 | Höhe Rahmenprofil Z (mm), Min 50, Max 200 |
| RahmenBreite | Length | 80 | Breite/Tiefe Rahmenprofil (mm), Min 50, Max 200 |
| LamellenBreite | Length | 200 | Sichtbare Breite Z-Profil (mm), Min 100, Max 300 |
| LamellenHoehe | Length | 40 | Profilhöhe Z-Querschnitt (mm), Min 15, Max 80 |
| LamellenStaerke | Length | 2 | Wandstärke Aluminium (mm), Min 1, Max 5 |
| LamellenAnzahl | Integer | 15 | Anzahl Lamellen im Feld, Min 3, Max 50 |
| LamellenStellung | StringComboBox | Geschlossen | Geschlossen\|Halboffen\|Offen |

**Palette-Gliederung:** Zwei Expander — `TragstrukturExpander` (Breite bis RahmenBreite) und `LamellenExpander` (LamellenBreite bis LamellenStellung).

## Contract Type
Standard PythonPart — rein palette-gesteuert, keine Interaktion nötig.

## Special Notes

### Scope-Ausschlüsse (NICHT implementieren)
- Keine Regenrinnen / Wasserableitung
- Kein Antrieb / Motor-Darstellung
- Keine Seitenelemente (ZIP-Screens, Glas)
- Keine Wandanschluss-Variante (nur freistehend)
- Keine Beleuchtung, Heizstrahler, Sensoren, Fundamente

### Anti-Hallucination — verbotene Aufrufe
```python
# ❌ EXISTIERT NICHT:
AllplanGeo.Box3D(...)              # → CreateCuboid
AllplanGeo.Cylinder(...)           # → existiert nicht
AllplanGeo.CreateExtrusion(...)    # → CreatePolyhedron(polygon2d, vector3d)
geom.Transform(matrix)            # → AllplanGeo.Transform(geom, matrix)
model_list.add(...)                # → append_geometry_3d()
Polyhedron3D.CreateBox(...)        # → CreateCuboid
build_ele.get_parameter(...)       # → build_ele.ParamName.value
```

### Verifizierte API-Aufrufe
```python
AllplanGeo.Polyhedron3D.CreateCuboid(l, w, h)              # Pfosten, Rahmen
AllplanGeo.Polygon2D() + polygon += Point2D(x, z)         # Z-Profil
err, poly = AllplanGeo.CreatePolyhedron(polygon2d, vec3d)  # Extrusion
AllplanGeo.Matrix3D()                                       # Transformation
matrix.Translate(AllplanGeo.Vector3D(dx, dy, dz))          # Verschiebung
matrix.Rotation(line3d_achse, angle)                        # Rotation
AllplanGeo.Transform(geometry, matrix)                      # FREIE Funktion
AllplanGeo.Angle.DegToRad(grad)                            # Winkel
```

### Einheiten: IMMER Millimeter
1 Meter = 1000.0, Lamellenstärke 2mm = 2.0

### Akzeptanztests
1. PythonPart lädt und platziert → 4 Pfosten + Rahmen + Lamellen sichtbar
2. ComboBox "Geschlossen" → Lamellen horizontal (0°)
3. ComboBox "Halboffen" → Lamellen auf ~45°
4. ComboBox "Offen" → Lamellen senkrecht (90°)
5. Handle Breite/Tiefe ziehen → Pergola skaliert, Lamellen bleiben gleichmäßig
6. LamellenAnzahl 15→10 → weniger Lamellen, größerer Abstand
7. Debug-Log unter `~/Documents/Pergola_ZProfil_debug.log`

## References
- `references/anti_hallucination.md` — vor Code schreiben lesen
- `references/geometry.md` — Extrusion, Transform, Rotation
- `references/palette.md` — PYP-Struktur, StringComboBox
- `references/elements.md` — ModelEleList, CommonProperties, Handles
- `templates/standard_template.py` + `.pyp` — Codebasis

---
*Execution: "Read this prompt.md and implement it with $allplan-pythonparts"*