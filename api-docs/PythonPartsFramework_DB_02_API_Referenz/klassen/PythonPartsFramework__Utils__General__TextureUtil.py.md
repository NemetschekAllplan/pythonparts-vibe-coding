---
title: "TextureUtil"
source: "PythonPartsFramework\Utils\General\TextureUtil.py"
type: "class"
category: "02_API_Referenz"
tags:
  - utility
related:
  -
last_updated: "2026-02-20"
---


# TextureUtil

> **Pfad:** `PythonPartsFramework\Utils\General\TextureUtil.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `utility`

## Übersicht

implementation of the texture utility

- create bitmap definition and add to the dictionary
- create texture from bitmap definition and add to the dictionary
- create texture mapping
- get texture from the dictionary
- create texture from diffuse color

## Abhängigkeiten

- `NemAll_Python_AllplanSettings`
- `NemAll_Python_BaseElements`
- `NemAll_Python_BasisElements`
- `NemAll_Python_IFW_ElementAdapter`
- `dataclasses`
- `math`

## Klassen

### `SurfaceData`

implementation of the texture data
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

### `TextureUtil`

implementation of the texture utility
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| `__init__` | `self, document: AllplanEleAdapter.DocumentAdapter` | `None` | constructor  Args:     document: document |
| `create_bitmap_definition` | `self, bmp_def_name: str, bmp_file_name: str, scale_u: float, scale_v: float, alpha: float, angle: float` | `None` | create a bitmap definition  Args:     bmp_def_name:  name of the bitmap definition     bmp_file_name: full path to the bitmap file     scale_u:       scale factor in u direction     scale_v:       scale factor in v direction     alpha:         alpha value of the bitmap, 0-255     angle:         angle of the bitmap in degrees |
| `create_texture` | `self, texture_name: str, diffuse_color: AllplanBasisEle.ARGB, roughness: float=0, transparency: int=0, reflection: int=0, bmp_def_name: str=''` | `None` | create a texture from a bitmap definition  Args:     texture_name:  name of the texture to create     diffuse_color: diffuse color of the texture, ARGB format     roughness:     roughness of the texture, 0-100     transparency:  transparency of the texture     reflection:    reflection of the texture, 0-100     bmp_def_name:  name of the bitmap definition |
| `create_texture_mapping` | `self, mapping_type: AllplanBasisEle.TextureMappingType, mapping_angle: float, x_scale: float, y_scale: float, x_offset: float, y_offset: float, phong_angle: float, ref_face: int, ref_edge: int` | `AllplanBasisEle.TextureMapping` | create a texture mapping  Args:     mapping_type:  mapping type     mapping_angle: mapping angle in degrees     x_scale:       scale factor in x direction     y_scale:       scale factor in y direction     x_offset:      offset in x direction     y_offset:      offset in y direction     phong_angle:   phong angle in degrees     ref_face:      reference face index     ref_edge:      reference edge index  Returns:     texture mapping |
| `get_texture` | `self, texture_name: str` | `AllplanBasisEle.TextureDefinition` | get a texture by name  Args:     texture_name: name of the texture  Returns:     texture definition |
| `create_diffuse_color_texture` | `self, diffuse_color: int` | `AllplanBasisEle.TextureDefinition` | create a texture from a diffuese color  Args:     diffuse_color: diffuse color of the texture  Returns:     texture definition with the diffuse color |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the texture utility

    - create bitmap definition and add to the dictionary
    - create texture from bitmap definition and add to the dictionary
    - create texture mapping
    - get texture from the dictionary
    - create texture from diffuse color
"""

from dataclasses import dataclass

import math

import NemAll_Python_AllplanSettings as AllplanSettings
import NemAll_Python_BaseElements as AllplanBaseEle
import NemAll_Python_BasisElements as AllplanBasisEle
import NemAll_Python_IFW_ElementAdapter as AllplanEleAdapter


TEXTURE_MAPPING_TYPES = {0: AllplanBasisEle.TextureMappingType.eCube,
                         1: AllplanBasisEle.TextureMappingType.eWall,
                         2: AllplanBasisEle.TextureMappingType.eRoof,
                         3: AllplanBasisEle.TextureMappingType.eGround,
                         4: AllplanBasisEle.TextureMappingType.eCylinder,
                         5: AllplanBasisEle.TextureMappingType.eSphere}


@dataclass
class SurfaceData():
    """ implementation of the texture data
    """

    bitmap_def: AllplanBasisEle.BitmapDefinition
    scale_u   : float
    scale_v   : float
    alpha     : float
    angle     : float


class TextureUtil():
    """ implementation of the texture utility
    """

    def __init__(self,
                 document: AllplanEleAdapter.DocumentAdapter):
        """ constructor

        Args:
            document: document
        """

        self.document     = document
        self.surface_path = f"{AllplanSettings.AllplanPaths.GetCurPrjPath()}design"

        self.texture_dict      = dict[str, AllplanBasisEle.TextureDefinition]()
        self.surface_data_dict = dict[str, SurfaceData]()

        self.texture_mapping : AllplanBasisEle.TextureMapping | None = None


    def create_bitmap_definition(self,
                                 bmp_def_name : str,
                                 bmp_file_name: str,
                                 scale_u      : float,
                                 scale_v      : float,
                                 alpha        : float,
                                 angle        : float):
        """ create a bitmap definition

        Args:
            bmp_def_name:  name of the bitmap definition
            bmp_file_name: full path to the bitmap file
            scale_u:       scale factor in u direction
            scale_v:       scale factor in v direction
            alpha:         alpha value of the bitmap, 0-255
            angle:         angle of the bitmap in degrees
        """

        bitmap_def = AllplanBasisEle.BitmapDefinition.Create(bmp_file_name)

        self.surface_data_dict[bmp_def_name] = SurfaceData(bitmap_def, scale_u, scale_v, alpha, angle)


    def create_texture(self,
                       texture_name : str,
                       diffuse_color: AllplanBasisEle.ARGB,
                       roughness    : float = 0,
                       transparency : int   = 0,
                       reflection   : int   = 0,
                       bmp_def_name : str   = ""):
        """ create a texture from a bitmap definition

        Args:
            texture_name:  name of the texture to create
            diffuse_color: diffuse color of the texture, ARGB format
            roughness:     roughness of the texture, 0-100
            transparency:  transparency of the texture
            reflection:    reflection of the texture, 0-100
            bmp_def_name:  name of the bitmap definition
        """

        mat_surface = AllplanBasisEle.SurfaceDefinition.Create()

        mat_surface.DiffuseColor = diffuse_color
        mat_surface.Roughness    = roughness
        mat_surface.Reflection   = reflection

        if bmp_def_name:
            bitmap_data = self.surface_data_dict[bmp_def_name]

            bitmap_def = bitmap_data.bitmap_def

        else:
            bitmap_def = AllplanBasisEle.BitmapDefinition.Create("")

            bitmap_data = SurfaceData(bitmap_def, 1.0, 1.0, 0.0, 0.0)

        bitmaps = {AllplanBasisEle.SurfaceDefinition.SurfaceTextureID.eDIFFUSE_SPRING : bitmap_def,
                   AllplanBasisEle.SurfaceDefinition.SurfaceTextureID.eDIFFUSE_SUMMER : bitmap_def,
                   AllplanBasisEle.SurfaceDefinition.SurfaceTextureID.eDIFFUSE_AUTUMN : bitmap_def,
                   AllplanBasisEle.SurfaceDefinition.SurfaceTextureID.eDIFFUSE_WINTER : bitmap_def}

        mat_surface.SetScale(bitmap_data.scale_u, bitmap_data.scale_v)

        mat_surface.Rotation     = bitmap_data.angle
        mat_surface.Transparency = transparency

        if transparency:
            mat_surface.ColorKey          = AllplanBasisEle.ARGB(255, 255, 255, 0)
            mat_surface.ColorKeyTolerance = 255

        unique_surface_name = AllplanBaseEle.DocumentResourceService.CreateSurface(self.document, self.surface_path,
                                                                                   texture_name, mat_surface, True, bitmaps)

        self.texture_dict[texture_name] = AllplanBasisEle.TextureDefinition(unique_surface_name)


    def create_texture_mapping(self,
                               mapping_type : AllplanBasisEle.TextureMappingType,
                               mapping_angle: float,
                               x_scale      : float,
                               y_scale      : float,
                               x_offset     : float,
                               y_offset     : float,
                               phong_angle  : float,
                               ref_face     : int,
                               ref_edge     : int) -> AllplanBasisEle.TextureMapping:
        """ create a texture mapping

        Args:
            mapping_type:  mapping type
            mapping_angle: mapping angle in degrees
            x_scale:       scale factor in x direction
            y_scale:       scale factor in y direction
            x_offset:      offset in x direction
            y_offset:      offset in y direction
            phong_angle:   phong angle in degrees
            ref_face:      reference face index
            ref_edge:      reference edge index

        Returns:
            texture mapping
        """

        texture_mapping = AllplanBasisEle.TextureMapping()

        texture_mapping.MappingType   = mapping_type
        texture_mapping.MappingAngle  = math.radians(mapping_angle)
        texture_mapping.XScale        = x_scale
        texture_mapping.YScale        = y_scale
        texture_mapping.XOffset       = x_offset
        texture_mapping.YOffset       = y_offset
        texture_mapping.PhongAngle    = math.radians(phong_angle)
        texture_mapping.ReferenceFace = ref_face
        texture_mapping.ReferenceEdge = ref_edge

        self.texture_mapping = texture_mapping

        return texture_mapping


    def get_texture(self,
                   texture_name: str) -> AllplanBasisEle.TextureDefinition:
        """ get a texture by name

        Args:
            texture_name: name of the texture

        Returns:
            texture definition
        """

        if texture_name not in self.texture_dict:
            return AllplanBasisEle.TextureDefinition(texture_name)

        return self.texture_dict[texture_name]


    def create_diffuse_color_texture(self,
                                     diffuse_color: int) -> AllplanBasisEle.TextureDefinition:
        """ create a texture from a diffuese color

        Args:
            diffuse_color: diffuse color of the texture

        Returns:
            texture definition with the diffuse color
        """

        mat_surface = AllplanBasisEle.SurfaceDefinition.Create()

        mat_surface.DiffuseColor = AllplanBaseEle.GetColorById(diffuse_color)

        texture_name = f"DiffuseColor_{diffuse_color}"

        unique_surface_name = AllplanBaseEle.DocumentResourceService.CreateSurface(self.document, self.surface_path,
                                                                                   texture_name, mat_surface, True, {})

        return AllplanBasisEle.TextureDefinition(unique_surface_name)

```

</details>