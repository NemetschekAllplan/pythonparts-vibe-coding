---
title: "NemAll_Python_IFW_ElementAdapter"
source: "PythonPartsFramework\InterfaceStubs\NemAll_Python_IFW_ElementAdapter.pyi"
type: "stub"
category: "02_API_Referenz"
tags:
  - dokumentation
related:
  -
last_updated: "2026-02-20"
---


# NemAll_Python_IFW_ElementAdapter

> **Pfad:** `PythonPartsFramework\InterfaceStubs\NemAll_Python_IFW_ElementAdapter.pyi`  
> **Typ:** `stub`  
> **Tags:** `dokumentation`

## Inhalt

```text
# pylint: disable=invalid-name
# pylint: disable=used-before-assignment
# pylint: disable=too-many-public-methods
# pylint: disable=c-extension-no-member
# pylint: disable=import-self
# pylint: disable=empty-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=wildcard-import
# pylint: disable=unused-wildcard-import
# pylint: disable=line-too-long
# pylint: disable=unused-argument
# pylint: disable=redefined-builtin
# pylint: disable=anomalous-backslash-in-string
# pylint: disable=too-few-public-methods
# pylint: disable=function-redefined
# pylint: disable=eq-without-hash
# pylint: disable=too-many-lines
# pylint: disable=too-many-arguments

"""Exposed classes and functions from NemAll_IFW_ElementAdapter"""

from __future__ import annotations

import typing

import enum
import collections.abc

import NemAll_Python_BaseElements
import NemAll_Python_Geometry


__all__ = [
    "AbsoluteElevationDimension_TypeUUID",
    "AlignmentDimension_TypeUUID",
    "AngleDimension_TypeUUID",
    "AnimationLight_TypeUUID",
    "Any3DFoundation_TypeUUID",
    "Arc3D_TypeUUID",
    "ArcDimension_TypeUUID",
    "ArchElementType",
    "ArchitectureAdditionalFinishElement_TypeUUID",
    "ArchitectureArea3D_TypeUUID",
    "ArchitectureBRep3D_Surface_TypeUUID",
    "ArchitectureBRep3D_Volume_TypeUUID",
    "ArchitectureBRep3D_Wire_TypeUUID",
    "ArchitectureBaseboard_TypeUUID",
    "ArchitectureBitmap_TypeUUID",
    "ArchitectureCeilingSurface_TypeUUID",
    "ArchitectureCircle_TypeUUID",
    "ArchitectureComponentLinkage_TypeUUID",
    "ArchitectureComponent_TypeUUID",
    "ArchitectureCylinder3D_TypeUUID",
    "ArchitectureElevation_TypeUUID",
    "ArchitectureFacestyle_TypeUUID",
    "ArchitectureFilling_TypeUUID",
    "ArchitectureFloorSurface_TypeUUID",
    "ArchitectureHatching_TypeUUID",
    "ArchitectureHyperElement_TypeUUID",
    "ArchitectureLine_TypeUUID",
    "ArchitectureOpeningPlane_TypeUUID",
    "ArchitecturePointSymbol3D_TypeUUID",
    "ArchitecturePointSymbol_TypeUUID",
    "ArchitecturePolyline_TypeUUID",
    "ArchitectureSphere3D_TypeUUID",
    "ArchitectureTextBlock_TypeUUID",
    "ArchitectureVariableTextBlock_TypeUUID",
    "ArchitectureVariableText_TypeUUID",
    "ArchitectureVerticalSurface_TypeUUID",
    "ArchitectureVolume3D_TypeUUID",
    "Area3D_TypeUUID",
    "Article_TypeUUID",
    "AssocViewElementAdapter",
    "AssociativeReportAreaVisualisation_TypeUUID",
    "AssociativeReportParameter_TypeUUID",
    "AssociativeReport_TypeUUID",
    "AssociativeViewAbsoluteElevationDimension_TypeUUID",
    "AssociativeViewCartesianGrid_TypeUUID",
    "AssociativeViewDimensions_TypeUUID",
    "AssociativeViewFrame_TypeUUID",
    "AssociativeViewIntersectionBody_TypeUUID",
    "AssociativeViewLinearDimension_TypeUUID",
    "AssociativeView_TypeUUID",
    "Associative_AbsoluteElevationDimension_TypeUUID",
    "Associative_AlignmentDimension_TypeUUID",
    "Associative_AngleDimension_TypeUUID",
    "Associative_CurveDimension_TypeUUID",
    "Associative_ElevationDimension_TypeUUID",
    "Associative_LinearDimension_TypeUUID",
    "Associative_RadiusDimension_TypeUUID",
    "AttributeContainer_TypeUUID",
    "AxisElementAdapter",
    "BRep3D_Surface_TypeUUID",
    "BRep3D_Volume_TypeUUID",
    "BRep3D_Wire_TypeUUID",
    "BarsAreaDefinition_TypeUUID",
    "BarsAreaPlacement_TypeUUID",
    "BarsAreaRepresentationLine_TypeUUID",
    "BarsAreaRepresentation_TypeUUID",
    "BarsCircle_TypeUUID",
    "BarsCircularPlacement_TypeUUID",
    "BarsDefinition_TypeUUID",
    "BarsEndBendingPlacement_TypeUUID",
    "BarsLine_TypeUUID",
    "BarsLinearMultiPlacement_TypeUUID",
    "BarsLinearPlacement_TypeUUID",
    "BarsPlacementConnection_TypeUUID",
    "BarsPolyline_TypeUUID",
    "BarsRepresentationLine_TypeUUID",
    "BarsRepresentation_TypeUUID",
    "BarsRotationalPlacement_TypeUUID",
    "BarsRotationalSolidPlacement_TypeUUID",
    "BarsSchemaCircularPlacement_TypeUUID",
    "BarsSchemaPlacement_TypeUUID",
    "BarsSchemaRepresentation_TypeUUID",
    "BarsSpiralPlacement_TypeUUID",
    "BarsTangentionalPlacement_TypeUUID",
    "BaseElementAdapter",
    "BaseElementAdapterChildElementsService",
    "BaseElementAdapterList",
    "BaseElementAdapterParentElementService",
    "BaseElementAdapterService",
    "BaseElementAdapterVector",
    "Baseboard_TypeUUID",
    "BeamPolygonalRecessTier_TypeUUID",
    "BeamPolygonalRecess_TypeUUID",
    "Beam_TypeUUID",
    "BendedMeshDefinition_TypeUUID",
    "BendedMeshSchemaPlacement_TypeUUID",
    "BendedMeshSchemaRepresentation_TypeUUID",
    "BendingScheduleListHead_TypeUUID",
    "Bitmap_TypeUUID",
    "BuildingSolid_TypeUUID",
    "CadastralGeneralGroupFixture_TypeUUID",
    "CadastralLineFixture_TypeUUID",
    "CadastralPlaneFixture_TypeUUID",
    "CadastralPointFixture_TypeUUID",
    "CartesianGridWithDimension_TypeUUID",
    "CartesianGrid_TypeUUID",
    "CeilingSurface_TypeUUID",
    "CeilingSystemSmartSymbol_TypeUUID",
    "CeilingSystem_TypeUUID",
    "CellButton_TypeUUID",
    "Chain2DParallel_TypeUUID",
    "Chain2DStationing_TypeUUID",
    "Chain2DText_TypeUUID",
    "Chain2D_TypeUUID",
    "Chimney_TypeUUID",
    "Circle2D_TypeUUID",
    "CircularUpstandTier_TypeUUID",
    "CircularUpstand_TypeUUID",
    "CircularWallTier_TypeUUID",
    "CircularWall_TypeUUID",
    "Clash_TypeUUID",
    "ClippingPathBody_TypeUUID",
    "ClippingPathRepresentation_TypeUUID",
    "ClippingPathText_TypeUUID",
    "ClippingPath_TypeUUID",
    "Clothoid2D_TypeUUID",
    "ClothoidDimension_TypeUUID",
    "CollarBeam_TypeUUID",
    "CollarTie_TypeUUID",
    "Column_TypeUUID",
    "CornerWindowComposite_TypeUUID",
    "CornerWindowReveal_TypeUUID",
    "CornerWindowTier_TypeUUID",
    "CornerWindow_TypeUUID",
    "CurveDimension_TypeUUID",
    "Cylinder3D_TypeUUID",
    "DTMAreaLabel_TypeUUID",
    "DTMArea_TypeUUID",
    "DTMContourLineLabel_TypeUUID",
    "DTMContourLine_TypeUUID",
    "DTMCrossSection_TypeUUID",
    "DTMElevationLabel_TypeUUID",
    "DTMElevation_TypeUUID",
    "DTMGridLabel_TypeUUID",
    "DTMGrid_TypeUUID",
    "DTMLine_TypeUUID",
    "DTMLongitudinalSection_TypeUUID",
    "DTMPointSymbol3D_TypeUUID",
    "DTMPointSymbol_TypeUUID",
    "DTMProfile_TypeUUID",
    "DefaultPlane_TypeUUID",
    "DeliverySymbol_TypeUUID",
    "DemolitionSolid_TypeUUID",
    "DimensionText_TypeUUID",
    "DocumentAdapter",
    "DocumentNameService",
    "DoorOpeningSmartPart_TypeUUID",
    "DoorOpeningSmartSymbol_TypeUUID",
    "DoorReveal_TypeUUID",
    "DoorSill_TypeUUID",
    "DoorSwing_TypeUUID",
    "DoorTier_TypeUUID",
    "Door_TypeUUID",
    "DrawingFileAttributes_TypeUUID",
    "DynamicGroupFixture_TypeUUID",
    "ElementAdapterType",
    "ElementAdapterTypeData",
    "ElementAdapterTypeGroup",
    "ElementGroupNode_TypeUUID",
    "ElementGroup_TypeUUID",
    "ElementNumber_TypeUUID",
    "ElementUpstandTier_TypeUUID",
    "ElementUpstand_TypeUUID",
    "ElementWallTier_TypeUUID",
    "ElementWall_TypeUUID",
    "ElevationDimension_TypeUUID",
    "Ellipse2D_TypeUUID",
    "EngineerDimensionLineOverlap_TypeUUID",
    "EngineerDimensionLine_TypeUUID",
    "EngineerLabel_TypeUUID",
    "EngineerSymbol2D_TypeUUID",
    "EngineerTextPointer_TypeUUID",
    "EngineeringPathElement_TypeUUID",
    "EnvelopingSurface_TypeUUID",
    "EquipmentSmartPart_TypeUUID",
    "ExtendedElement_TypeUUID",
    "FacadeSmartSymbol_TypeUUID",
    "Facade_TypeUUID",
    "Facestyle_TypeUUID",
    "FacingComposite_TypeUUID",
    "Facing_TypeUUID",
    "FemAreaLoad_TypeUUID",
    "FemBarLine_TypeUUID",
    "FemContours_TypeUUID",
    "FemLineLoad_TypeUUID",
    "FemLineSupport_TypeUUID",
    "FemPlateElementLine_TypeUUID",
    "FemPointLoad_TypeUUID",
    "FemSmartSymbolFormwork_TypeUUID",
    "FemSmartSymbolMeshFormwork_TypeUUID",
    "FemSpring_TypeUUID",
    "FillLine_TypeUUID",
    "Filling2D_TypeUUID",
    "FixtureDefinition_TypeUUID",
    "FloorSurface_TypeUUID",
    "FlushPierTier_TypeUUID",
    "FlushPier_TypeUUID",
    "GUID",
    "GeneralGroupFixture_TypeUUID",
    "GeneralObject_TypeUUID",
    "GeneralVariableTextBlock_TypeUUID",
    "GeneralVariableText_TypeUUID",
    "GradientFilling2D_TypeUUID",
    "Hatching2D_TypeUUID",
    "Header_TypeUUID",
    "HipRafter_TypeUUID",
    "HyperRoofCovering_TypeUUID",
    "HyperRoofFrame_TypeUUID",
    "IndividualFoundation_TypeUUID",
    "InstallationComponent_TypeUUID",
    "InternalElement_TypeUUID",
    "JointTier_TypeUUID",
    "Joint_TypeUUID",
    "JoistPlaced_TypeUUID",
    "LandscapingPathBaseboard_TypeUUID",
    "LandscapingPathFloorSurface_TypeUUID",
    "LandscapingPlantsBaseboard_TypeUUID",
    "LandscapingPlantsFloorSurface_TypeUUID",
    "LayoutBorderMaster_TypeUUID",
    "LayoutBorder_TypeUUID",
    "LayoutClipRegion_TypeUUID",
    "LayoutElement_TypeUUID",
    "LayoutFreeElement_TypeUUID",
    "LayoutIntersection_TypeUUID",
    "LayoutMaster_TypeUUID",
    "LayoutSheet_TypeUUID",
    "LayoutWindow_TypeUUID",
    "LegendEndSum_TypeUUID",
    "LegendIntermediateSum_TypeUUID",
    "LegendRow_TypeUUID",
    "LegendStamp_TypeUUID",
    "Legend_TypeUUID",
    "LightdomeSmartPart_TypeUUID",
    "Line2D_TypeUUID",
    "Line3D_TypeUUID",
    "LineFixture_TypeUUID",
    "LineObject_TypeUUID",
    "LineSupport_TypeUUID",
    "LineUpstandTier_TypeUUID",
    "LineUpstand_TypeUUID",
    "LinearDimension_TypeUUID",
    "Link_TypeUUID",
    "Lintel_TypeUUID",
    "MaskText_TypeUUID",
    "MaskingPlane_TypeUUID",
    "MeshAreaBorder_TypeUUID",
    "MeshAreaPlacement_TypeUUID",
    "MeshAreaRepresentation_TypeUUID",
    "MeshBorder_TypeUUID",
    "MeshDefinition_TypeUUID",
    "MeshDiagonal_TypeUUID",
    "MeshPlacementDefinition_TypeUUID",
    "MeshPlacement_TypeUUID",
    "MeshRepresentation_TypeUUID",
    "MeshScheduleListHead_TypeUUID",
    "MeshScheduleListPoint_TypeUUID",
    "MeshScheduleMaskPoint_TypeUUID",
    "MeshScheduleMeshPlaced_TypeUUID",
    "MeshScheduleMesh_TypeUUID",
    "MeshSchedule_TypeUUID",
    "MultiLine3DGroup_TypeUUID",
    "MultiLine3D_TypeUUID",
    "MultiSlab_TypeUUID",
    "NULL_TypeUUID",
    "NetStorey_TypeUUID",
    "NicheReveal_TypeUUID",
    "NicheSmartSymbol_TypeUUID",
    "NicheTier_TypeUUID",
    "Niche_TypeUUID",
    "OLEElement_TypeUUID",
    "OleSmartSymbolDefinition_TypeUUID",
    "OpeningPartDoorGroup_TypeUUID",
    "OpeningPartDoor_TypeUUID",
    "OpeningPartGroup_TypeUUID",
    "OpeningPartWindowGroup_TypeUUID",
    "OpeningPartWindow_TypeUUID",
    "OpeningPart_TypeUUID",
    "OutdoorFacilitiesObject_TypeUUID",
    "ParapetSmartSymbol_TypeUUID",
    "Pattern2D_TypeUUID",
    "PipeBundleGroup_TypeUUID",
    "PipeBundle_TypeUUID",
    "PipeWorkGroup_TypeUUID",
    "PipeWork_TypeUUID",
    "PlaneFixture_TypeUUID",
    "PlanePairArea_TypeUUID",
    "PlantSmartSymbol_TypeUUID",
    "Point2D_TypeUUID",
    "PointBuiltInElementSmartPart_TypeUUID",
    "PointFixture_TypeUUID",
    "PointSymbol2D_TypeUUID",
    "PointSymbol3D_TypeUUID",
    "PolarGrid_TypeUUID",
    "PolyInstallationComponent_TypeUUID",
    "PolygonUpstand_TypeUUID",
    "PolygonWallTier_TypeUUID",
    "PolygonWall_TypeUUID",
    "PolygonalNicheTier_TypeUUID",
    "PolygonalNiche_TypeUUID",
    "PolygonalRecessTier_TypeUUID",
    "PolygonalRecess_TypeUUID",
    "Polyline2D_TypeUUID",
    "Polyline3D_TypeUUID",
    "PositionPlanProject_TypeUUID",
    "PositionPlan_TypeUUID",
    "Post_TypeUUID",
    "PrecastBaseReinforcement_TypeUUID",
    "PrecastBrickCompositeFloor_TypeUUID",
    "PrecastBrickFloor_TypeUUID",
    "PrecastBrickSolidFloor_TypeUUID",
    "PrecastBrickWall_TypeUUID",
    "PrecastBubbleFloor_TypeUUID",
    "PrecastCobiaxSlab_TypeUUID",
    "PrecastConnectionElement_TypeUUID",
    "PrecastConnectorPlacement_TypeUUID",
    "PrecastConnector_TypeUUID",
    "PrecastConstructiveElement_TypeUUID",
    "PrecastCrane_TypeUUID",
    "PrecastDesignGeneral_TypeUUID",
    "PrecastDesign_TypeUUID",
    "PrecastDoubleWall_TypeUUID",
    "PrecastElementBricksWall_TypeUUID",
    "PrecastElementCompositeFormworkWall_TypeUUID",
    "PrecastElementDoubleWall_TypeUUID",
    "PrecastElementGeneral_TypeUUID",
    "PrecastElementNLayersWall_TypeUUID",
    "PrecastElementPlanElement_TypeUUID",
    "PrecastElementPlan_TypeUUID",
    "PrecastElementSandwichWall_TypeUUID",
    "PrecastElementSolidWall_TypeUUID",
    "PrecastElementThermoWall_TypeUUID",
    "PrecastElement_TypeUUID",
    "PrecastElementation_TypeUUID",
    "PrecastFloorManagerElement_TypeUUID",
    "PrecastFormWorkConstructiveElementManual_TypeUUID",
    "PrecastFormWorkConstructiveElement_TypeUUID",
    "PrecastFormWorkConstructiveHelpElement_TypeUUID",
    "PrecastFormworkCoupler_TypeUUID",
    "PrecastFormworkElement_TypeUUID",
    "PrecastFormworkPlacement_TypeUUID",
    "PrecastFormworkSmartSymbol_TypeUUID",
    "PrecastFormworkView_TypeUUID",
    "PrecastGirderDefinition_TypeUUID",
    "PrecastGirderPlacement_TypeUUID",
    "PrecastGridAxis_TypeUUID",
    "PrecastGridRegion_TypeUUID",
    "PrecastGrid_TypeUUID",
    "PrecastHalfFloor_TypeUUID",
    "PrecastHollowCoreElement_TypeUUID",
    "PrecastLayer_TypeUUID",
    "PrecastMWSReinforcement_TypeUUID",
    "PrecastOptima_TypeUUID",
    "PrecastPIPanel_TypeUUID",
    "PrecastPanelComponent_TypeUUID",
    "PrecastPrestHollowCoreElement_TypeUUID",
    "PrecastPropertiesService",
    "PrecastRecessAttributeBricksWall_TypeUUID",
    "PrecastRecessAttributeCompositeFormworkWall_TypeUUID",
    "PrecastRecessAttributeDoubleWall_TypeUUID",
    "PrecastRecessAttributeNLayersWall_TypeUUID",
    "PrecastRecessAttributeSandwichWall_TypeUUID",
    "PrecastRecessAttributeSolidWall_TypeUUID",
    "PrecastRecessAttributeThermoWall_TypeUUID",
    "PrecastRecessAttribute_TypeUUID",
    "PrecastReinforcementAttribute_TypeUUID",
    "PrecastReinforcementBricksWall_TypeUUID",
    "PrecastReinforcementCompositeFormworkWall_TypeUUID",
    "PrecastReinforcementDoubleWall_TypeUUID",
    "PrecastReinforcementGroup_TypeUUID",
    "PrecastReinforcementNLayersWall_TypeUUID",
    "PrecastReinforcementSandwichWall_TypeUUID",
    "PrecastReinforcementSolidWall_TypeUUID",
    "PrecastReinforcementThermoWall_TypeUUID",
    "PrecastSingleAxis_TypeUUID",
    "PrecastSlabMandatoryDivision_TypeUUID",
    "PrecastSlabPlacementPolygon_TypeUUID",
    "PrecastSlabPlacement_TypeUUID",
    "PrecastSlabRecessRepresentation_TypeUUID",
    "PrecastSlabRecess_TypeUUID",
    "PrecastSlabSupport_TypeUUID",
    "PrecastSolidFloor_TypeUUID",
    "PrecastSolidWall_TypeUUID",
    "PrecastSpecialLoadSmartSymbolDefinition_TypeUUID",
    "PrecastSpecialLoad_TypeUUID",
    "PrecastStaticSupportLine_TypeUUID",
    "PrecastStaticSupport_TypeUUID",
    "PrecastText_TypeUUID",
    "PrecastVisibleSideSymbol_TypeUUID",
    "PrecastWallConnector_TypeUUID",
    "PrecastWallDesign_TypeUUID",
    "PrecastWallElementTier_TypeUUID",
    "PrecastWallManagerElement_TypeUUID",
    "PrecastWallPanelElementTier_TypeUUID",
    "PrecastWallPanelElement_TypeUUID",
    "PrecastWallPanel_TypeUUID",
    "ProfileWallTier_TypeUUID",
    "ProfileWall_TypeUUID",
    "ProxyObject_TypeUUID",
    "Purlin_TypeUUID",
    "PythonPartGroup_TypeUUID",
    "PythonPart_TypeUUID",
    "RabbetComposite_TypeUUID",
    "Rabbet_TypeUUID",
    "RadiusDimension_TypeUUID",
    "RafterPlaced_TypeUUID",
    "RafterPurlin_TypeUUID",
    "Rafter_TypeUUID",
    "RailSmartSymbol_TypeUUID",
    "Rail_TypeUUID",
    "RecessReveal_TypeUUID",
    "RecessSmartSymbol_TypeUUID",
    "RecessTier_TypeUUID",
    "Recess_TypeUUID",
    "ReferenceSurface_TypeUUID",
    "ReinforcementExtrudeRebarAlongPath",
    "ReinforcementFFUnit_TypeUUID",
    "ReinforcementGroup_TypeUUID",
    "ReinforcementPlaceBarsAlongSurface_TypeUUID",
    "ReinforcementPropertiesReader",
    "ReinforcementRobotSmartPart_TypeUUID",
    "ReinforcementStampPoint_TypeUUID",
    "ReinforcementStructuralStarterBars_TypeUUID",
    "ReinforcementSweepBarsAlongPath",
    "RevisionCloud_TypeUUID",
    "RollerBlind_TypeUUID",
    "RoofCovering_TypeUUID",
    "RoofFrame_TypeUUID",
    "RoofSurfaceContour_TypeUUID",
    "RoofSurface_TypeUUID",
    "RoofWindowSmartPart_TypeUUID",
    "RoomGroup_TypeUUID",
    "RoomOccupancy_TypeUUID",
    "Room_TypeUUID",
    "SAAP_ElevationDimension_TypeUUID",
    "ScanelementColor_TypeUUID",
    "ScanelementMono_TypeUUID",
    "SecondaryReinforcementGroup_TypeUUID",
    "SectionAlongPath_TypeUUID",
    "SectionPathStationing_TypeUUID",
    "SectionPath_TypeUUID",
    "SillBothSides_TypeUUID",
    "SillSmartPart_TypeUUID",
    "Sill_TypeUUID",
    "SkeletonAxis_TypeUUID",
    "SkeletonBeamSystem_TypeUUID",
    "SkeletonBeam_TypeUUID",
    "SkeletonBrace_TypeUUID",
    "SkeletonColumn_TypeUUID",
    "SkeletonGrid_TypeUUID",
    "SkeletonPortalFrameStructure_TypeUUID",
    "SkeletonPortalFrame_TypeUUID",
    "SkeletonPurlinSystem_TypeUUID",
    "SkeletonPurlin_TypeUUID",
    "SkeletonSolidElementSystem_TypeUUID",
    "SkylightSmartSymbol_TypeUUID",
    "Skylight_TypeUUID",
    "SlabFoundationTier_TypeUUID",
    "SlabFoundation_TypeUUID",
    "SlabOpeningSmartSymbol_TypeUUID",
    "SlabOpening_TypeUUID",
    "SlabRecessSmartSymbol_TypeUUID",
    "SlabRecess_TypeUUID",
    "Slab_TypeUUID",
    "Slope_TypeUUID",
    "SmartFit2D_TypeUUID",
    "SmartPartGroup_TypeUUID",
    "SmartPart_TypeUUID",
    "SmartSymbolDefinition_TypeUUID",
    "SmartSymbolElementGroup_TypeUUID",
    "SmartSymbolFoil_TypeUUID",
    "SmartSymbol_TypeUUID",
    "SolarScreenSmartPart_TypeUUID",
    "Sphere3D_TypeUUID",
    "Spline2D_TypeUUID",
    "Spline3D_TypeUUID",
    "SplineDimension_TypeUUID",
    "StairModeler_TypeUUID",
    "StairsDirectionSymbol_TypeUUID",
    "StairsDoubleQuarterLanding_TypeUUID",
    "StairsDoubleQuarterTurn_TypeUUID",
    "StairsElementContainer_TypeUUID",
    "StairsElement_TypeUUID",
    "StairsHalfTurn_TypeUUID",
    "StairsQuarterLanding_TypeUUID",
    "StairsSpiral_TypeUUID",
    "StairsStraightFlight_TypeUUID",
    "StairsTripleQuarterTurn_TypeUUID",
    "StairsUType_TypeUUID",
    "StairsWinder_TypeUUID",
    "Stairs_TypeUUID",
    "StoreyGroup_TypeUUID",
    "Storey_TypeUUID",
    "StripFoundation_TypeUUID",
    "SubCeilingSystem_TypeUUID",
    "SubFacade_TypeUUID",
    "SubOpeningPartDoor_TypeUUID",
    "SubOpeningPartWindow_TypeUUID",
    "SubOpeningPart_TypeUUID",
    "SubPipeBundle_TypeUUID",
    "SubPipeWork_TypeUUID",
    "SubPythonPart_TypeUUID",
    "SubRail_TypeUUID",
    "SubSmartPart_TypeUUID",
    "SurfaceObject_TypeUUID",
    "SurveyPoint_TypeUUID",
    "TentRoofFrame_TypeUUID",
    "TentRoofPlane_TypeUUID",
    "TextBlock_TypeUUID",
    "TextPointer_TypeUUID",
    "Timber_TypeUUID",
    "UVSClippingPathSymbol_TypeUUID",
    "UVSLabeling_TypeUUID",
    "Undefined_TypeUUID",
    "UnifiedSection_TypeUUID",
    "UnifiedView_TypeUUID",
    "Upstand_TypeUUID",
    "UrbanPlanningBuilding_TypeUUID",
    "UrbanPlanningDrawingBaseboard_TypeUUID",
    "UrbanPlanningDrawingFloorSurface_TypeUUID",
    "UrbanPlanningDrawingObject_TypeUUID",
    "UrbanPlanningPlotFloorSurface_TypeUUID",
    "UrbanPlanningSpacingArea_TypeUUID",
    "UserDefinedSolidOpening_TypeUUID",
    "UserDefinedSolid_TypeUUID",
    "ValleyRafter_TypeUUID",
    "VerticalSurface_TypeUUID",
    "Volume3D_TypeUUID",
    "WallAxisArc_TypeUUID",
    "WallAxisChain_TypeUUID",
    "WallAxisClothoid_TypeUUID",
    "WallAxisLine_TypeUUID",
    "WallAxisPolyline_TypeUUID",
    "WallAxisSpline_TypeUUID",
    "WallAxis_TypeUUID",
    "WallInfraction_TypeUUID",
    "WallTier_TypeUUID",
    "Wall_TypeUUID",
    "WindowDoorReveal_TypeUUID",
    "WindowDoorTier_TypeUUID",
    "WindowDoor_TypeUUID",
    "WindowOpeningSmartPart_TypeUUID",
    "WindowOpeningSmartSymbol_TypeUUID",
    "WindowReveal_TypeUUID",
    "WindowTier_TypeUUID",
    "Window_TypeUUID",
    "XRefDocumentClipped_TypeUUID",
    "XRefDocumentEmbedded_TypeUUID",
    "XRefDocument_TypeUUID",
    "XRefFreeDocumentClipped_TypeUUID",
    "XRefFreeDocumentEmbedded_TypeUUID",
    "XRefFreeDocument_TypeUUID",
    "ZoomWindow_TypeUUID"
]


class ArchElementType(enum.Enum):
    """Architecture element types

    tInvalid: Invalid type
    tWire   : Arch element has a edges only.
    tSheet  : Arch element has a faces.
    tSolid  : Arch element has a volume.
    """

    names = {tInvalid: tInvalid,
             tWire: tWire,
             tSheet: tSheet,
             tSolid: tSolid}
    tInvalid = 0
    tSheet = 2
    tSolid = 3
    tWire = 1

    values = {0: tInvalid,
              1: tWire,
              2: tSheet,
              3: tSolid}

    def __getitem__(self, key: (str | int | float)) -> ArchElementType:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class BaseElementAdapter():
    """Implementation of the base element adapter

    BaseElementAdapter is used inside the IFW as general element class, e.g. as result
    of an element selection. The class is created as adapter to avoid future IFW changes
    if the internal CAD data structure will be changed.

    The class has some member functions to get the general element data like name, geometry,
    common properties, ...

    The adapter includes also the DocumentAdapter, which can be used to get the access to the
    internal CAD data structure.
    """
    @staticmethod
    def FromGUID(guid: GUID, doc: DocumentAdapter) -> BaseElementAdapter:
        """Get elements from GUID

        Args:
            guid: GUID of the element
            doc:  Document

        Returns:
             Document
        """
    @staticmethod
    def FromNOIGUID(guidstr: str, doc: DocumentAdapter) -> BaseElementAdapter:
        """Get elements from NOI GUID

        Args:
            guidStr: NOI-GUID string of the element
            doc:     Document

        Returns:
             Document
        """
    def GetArchElementType(self) -> ArchElementType:
        """Check the type of an architectural element (PRGBER_ELEM_ARCH)

        Returns:
            Arch Element type
        """
    def GetAttributes(self, readState: NemAll_Python_BaseElements.eAttibuteReadState) -> list[tuple[int, (int | float | str)]]:
        """Get the attributes

        Args:
            readState: Attribute read state

        Returns:
            Attributes
        """
    def GetCommonProperties(self) -> NemAll_Python_BaseElements.CommonProperties:
        """Get the common properties of the element

        Returns:
            Common properties of the element
        """
    def GetDisplayName(self) -> str:
        """Get the displace name of the element

        Returns:
            Display name of the element
        """
    def GetDocument(self) -> DocumentAdapter:
        """Get the document

        Returns:
            Document
        """
    def GetDrawingfileNumber(self) -> int:
        """Get the drawing file number of the element

        Returns:
            Drawing file number of the element / negative means drawing is in passive mode
        """
    def GetElementAdapterType(self) -> ElementAdapterType:
        """Get the type of the element

        Returns:
            Type ID of the element
        """
    def GetElementUUID(self) -> GUID:
        """Get the UUID of the element

        Returns:
            UUID of the element
        """
    def GetGeometry(self) -> typing.Any:
        """Get elements geometry

        Returns:
            Geometry
        """
    def GetGroundViewArchitectureElementGeometry(self) -> typing.Any:
        """Get ground view geometry of an architecture element (if exist)

        Returns:
             Geometry
        """
    def GetModelElementUUID(self) -> GUID:
        """Get the UUID of the model element

        Returns:
            UUID of the element
        """
    def GetModelGeometry(self) -> typing.Any:
        """Get element model geometry

        Returns:
             Geometry
        """
    def GetNOIGUID(self) -> str:
        """Get the NOI GUID

        Returns:
             NOI GUID as string
        """
    def GetParentElementAdapterType(self) -> ElementAdapterType:
        """Get the type of the parent element

        Returns:
            Type ID of the parent element
        """
    def GetPureArchitectureElementGeometry(self) -> typing.Any:
        """Get the pure geometry of an architecture element (if exist).
        The geometry is without openings, ...

        Returns:
             Geometry
        """
    def GetTimeStamp(self) -> int:
        """Get the time stamp of the element

        Returns:
             Time stamp of the element creation
        """
    def Is3DElement(self) -> bool:
        """Get the 3D state of the element

        Returns:
            Element is a 3D element: true/false
        """
    def IsActive(self) -> bool:
        """Get the activation state of the element

        Returns:
            True, if the element is activated
        """
    def IsChildParentType(self, childType: GUID, parentType: GUID) -> bool:
        """Check for child (current element) and parent type connection

        Args:
            childType:  Type of the element
            parentType: Type of the parent element

        Returns:
            Child and parent are connected by the define types
        """
    def IsDeleted(self) -> bool:
        """Get the deleted state of the element

        Returns:
            True, if the element is deleted
        """
    def IsGeneralElement(self) -> bool:
        """Check if element is general (PRGBER_ELEM_ALLG)

        Returns:
            Element is general (PRGBER_ELEM_ALLG)
        """
    def IsInActiveDocument(self) -> bool:
        """If element is in active document return true.

        Returns:
            true if element is in active document
        """
    def IsInActiveLayer(self) -> bool:
        """If element is in active layer return true.

        Returns:
            true if element is in active layer.
        """
    def IsInMacro(self) -> bool:
        """Check if element has parent object

        Returns:
            Element has parent
        """
    def IsLabelElement(self) -> bool:
        """Check if element is a part of some label (Variables Textbild)

        Returns:
            Element is a part of some label: true/false
        """
    def IsNull(self) -> bool:
        """Check for an empty element

        Returns:
            Element is empty: true/false
        """
    def IsValid(self) -> bool:
        """check if element is valid

        Returns:
            bool, if it's possible to work with it
        """
    def IsValidForSelectFace(self) -> bool:
        """Check if element is valid for face select

        Returns:
            Element is valid for face select
        """
    def SetVisibilityState(self, visible: bool):
        """Set the visibility state of the element

        Args:
            visible: She visibility state to set
        """
    @typing.overload
    def __eq__(self, element: BaseElementAdapter) -> bool:
        """Equal operator

        Args:
            element: Element to compare

        Returns:
            Elements are equal: true/false
        """
    @typing.overload
    def __eq__(self, eleTypeUUID: GUID) -> bool:
        """Equal operator for checking the element adapter type UUID

        Args:
            eleTypeUUID: Element type UUID

        Returns:
            Element has the type: true/false
        """
    def __eq__(self) -> bool:
        """ Overloaded function. See individual overloads.
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, element: BaseElementAdapter):
        """Copy constructor

        Args:
            element: Element
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    @typing.overload
    def __ne__(self, eleType: BaseElementAdapter) -> bool:
        """Not equal operator for checking the element type

        Args:
            eleType: Element type

        Returns:
            Element has not the type: true/false
        """
    @typing.overload
    def __ne__(self, eleType: GUID) -> bool:
        """Not equal operator for checking the element type

        Args:
            eleType: Element type

        Returns:
            Element has not the type: true/false
        """
    def __ne__(self) -> bool:
        """ Overloaded function. See individual overloads.
        """
    def __repr__(self) -> str:
        """Convert to string
        """

class AxisElementAdapter(BaseElementAdapter):
    """Implementation of the axis element adapter
    """
    def GetAxis(self) -> typing.Any:
        """Get wall axis

        Returns:
            IGeometry2D arbitrary curve pointer
        """
    def GetGeometry(self) -> typing.Any:
        """Get elements geometry

        Returns:
            Geometry
        """
    def GetOffset(self) -> float:
        """Get the element offset from the axis

        Returns:
            Element offset from the axis
        """
    def GetThickness(self) -> float:
        """Get the element thickness

        Returns:
            Element thickness
        """
    def GetTierThickness(self) -> NemAll_Python_Utility.VecDoubleList:
        """Get the thickness of the tiers

        Returns:
            Thickness of the tiers
        """
    def GetTiersCount(self) -> int:
        """Get the amount of tiers

        Returns:
            number of tiers of this axis element
        """
    def HasAxis(self) -> bool:
        """Check, if this element has an axis

        Returns:
            true, if axis element has an axis
        """
    def IsElementParallelToAxis(self) -> bool:
        """Is element direction parallel to axis direction

        Returns:
            Is element direction parallel to axis direction state
        """
    def IsNull(self) -> bool:
        """Check for an empty element

        Returns:
            Element is empty: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, element: BaseElementAdapter):
        """Constructor

        Args:
            element: Element
        """
    @typing.overload
    def __init__(self, element: AxisElementAdapter):
        """Copy constructor

        Args:
            element: Element to copy
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """

class AssocViewElementAdapter(BaseElementAdapter):

    def GetTransformationMatrix(self) -> NemAll_Python_Geometry.Matrix3D:
        """Get the transformation matrix of the associative view

        Returns:
             Transformation matrix of the associative view
        """
    def IsNull(self) -> bool:
        """Check for an empty element

        Returns:
             Element is empty: true/false
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @staticmethod
    @typing.overload
    def __init__(: object):
        """Constructor
        """
    @typing.overload
    def __init__(self, ele: BaseElementAdapter):
        """Constructor

        Args:
            ele: Base element adapter
        """
    @staticmethod
    def __init__():
        """ Overloaded function. See individual overloads.
        """

class BaseElementAdapterChildElementsService():
    """Implementation of the service functions for the child elements determination of a base element adapter
    """
    @staticmethod
    def GetChildElements(ele: BaseElementAdapter, hiddenElements: bool) -> BaseElementAdapterVector:
        """Get the child elements of the element (includes the childs which have the same model element)

        Args:
            ele:            Element
            hiddenElements: Include hidden elements: true/false

        Returns:
            Child elements
        """
    @staticmethod
    @typing.overload
    def GetChildModelElements(ele: BaseElementAdapter) -> BaseElementAdapterList:
        """Get the child model elements of the element

        Args:
            ele: BaseElementAdapter
                 Element

        Returns:
            True, if element pass and can be selected
            Child elements of the element
        """
    @staticmethod
    @typing.overload
    def GetChildModelElements(ele: BaseElementAdapter, hiddenElements: bool) -> BaseElementAdapterList:
        """Get the child model elements of the element

        Args:
            ele:            Element
            hiddenElements: Include hidden elements: true/false

        Returns:
            Child elements including hidden elements of the element
        """
    @staticmethod
    def GetChildModelElements() -> BaseElementAdapterList:
        """ Overloaded function. See individual overloads.
        """
    @staticmethod
    def GetChildModelElementsFromTree(ele: BaseElementAdapter) -> BaseElementAdapterList:
        """Get the child model elements from the complete child tree of the element

        Args:
            ele: Element

        Returns:
            Child model elements from the complete child tree of the element
        """
    @staticmethod
    def GetChildPropertyElements(ele: BaseElementAdapter, modifyState: object, propGroup: object) -> BaseElementAdapterVector:
        """Get the child property elements

        Args:
            ele:         Element
            modifyState: Modify state
            propGroup:   Property group

        Returns:
            Child property elements
        """
    @staticmethod
    def GetTierElements(ele: BaseElementAdapter) -> BaseElementAdapterVector:
        """Get the tier elements from an element

        Args:
            ele: Element

        Returns:
            Tier elements
        """
    @staticmethod
    def GetTierNumber(ele: BaseElementAdapter) -> int:
        """Get the tier number from an element

        Args:
            ele: Element

        Returns:
            Tier number
        """

class BaseElementAdapterList():
    """Implementation of the base element adapter list

    The BaseElementAdapterList is a general container for the BaseElementAdapter
    """
    def __getitem__(self, index: int) -> BaseElementAdapter:
        """Get the item for the index
        """
    def __iadd__(self, elements: BaseElementAdapterList) -> BaseElementAdapterList:
        """Add elements to the list

        Args:
            elements: Elements.
        """
    @typing.overload
    def __init__(self):
        """Initialize
        """
    @typing.overload
    def __init__(self, elements: typing.List[BaseElementAdapter]):
        """Constructor

        Args:
            elements: Initializer list with the elements
        """
    @typing.overload
    def __init__(self, eleList: BaseElementAdapterList):
        """Copy constructor

        Args:
            eleList: List to move
        """
    def __init__(self):
        """ Overloaded function. See individual overloads.
        """
    def __iter__(self) -> typing.Iterator[BaseElementAdapter]:
        """Get the iterator
        """
    def __len__(self) -> int:
        """Get the length of the list

        Returns:
            Length of the list
        """
    def __repr__(self) -> str:
        """Get a string from the list items
        """
    def append(self, element: BaseElementAdapter):
        """Append an element

        Args:
            element:    Element to append
        """
    def clear(self):
        """Clear the list
        """

class BaseElementAdapterParentElementService():

    @staticmethod
    def GetParentElement(ele: BaseElementAdapter) -> BaseElementAdapter:
        """Get the parent element adapter from the element adapter

        Args:
            ele: Element

        Returns:
             Parent element adapter
        """

class BaseElementAdapterService():
    """Implementation of the base element adapter service
    """
    @staticmethod
    def AdaptElementsAfterTransaction(elements: BaseElementAdapterList) -> BaseElementAdapterList:
        """Adapt the elements after a transaction (set new address, ...)

        Args:
            elements: Elements to adapt

        Returns:
            Adapted elements
        """
    @staticmethod
    def GetConnectedElements(ele: BaseElementAdapter) -> BaseElementAdapterList:
        """Get the connected elements (ivk2)

        Args:
            ele: Element

        Returns:
            Connected elements
        """
    @staticmethod
    def GetDocumentIndex(ele: BaseElementAdapter) -> int:
        """Get the internal index of the element-document

        Args:
            ele: Element

        Returns:
            Internal index of the element-document
        """
    @staticmethod
    def GetLinkedElements(ele: BaseElementAdapter) -> BaseElementAdapterVector:
        """Get the linked elements

        Args:
            ele: Element

        Returns:
            Linked elements
        """
    @staticmethod
    def GetMacroElementAddress(ele: BaseElementAdapter) -> int:
        """Get the array address of macro element, if exist

        Args:
            ele: Element

        Returns:
            Address of macro if exist, otherwise 0
        """
    @staticmethod
    def IsConnectedElement(ele1: BaseElementAdapter, ele2: BaseElementAdapter) -> bool:
        """Check, whether the two elements are connected

        Args:
            ele1: First element
            ele2: Second element

        Returns:
            Elements are connected: true/false
        """
    @staticmethod
    def IsElementFromElementGroup(ele: BaseElementAdapter) -> bool:
        """Check, whether the element is inside an element group

        Args:
            ele: Element

        Returns:
            Element is inside an element group
        """
    @staticmethod
    def IsElementOrChildDeleted(ele: BaseElementAdapter) -> bool:
        """Check, whether the element or a child element is deleted

        Args:
            ele: Element to check

        Returns:
            Element or child element is deleted
        """
    @staticmethod
    def IsElementVisible(ele: BaseElementAdapter) -> bool:
        """Check, whether the element is visible

        Args:
            ele: Element

        Returns:
            Element is visible: true/false
        """
    @staticmethod
    def IsPostActivation(ele: BaseElementAdapter) -> bool:
        """Get the post activation state from the element

        Args:
            ele: Element

        Returns:
            Element with post activation: true/false
        """
    @staticmethod
    def IsTypeConnectedElement(ele: BaseElementAdapter, eleTypes: object) -> bool:
        """Check, whether the element is a type connected element

        Args:
            ele:      Element
            eleTypes: Type(s) of the connection element

        Returns:
            Text connected element: true/false
        """

class BaseElementAdapterVector():

    def __getitem__(self, index: int) -> BaseElementAdapter:
        """Get a list item

        Args:
            index: Index of the item

        Returns:
            Value for the index
        """
    def __iadd__(self, elements: BaseElementAdapterVector) -> BaseElementAdapterVector:
        """Add elements to the list

        Args:
            elements: Elements.
        """
    def __init__(self):
        """Initialize
        """
    def __iter__(self) -> collections.abc.Iterator:
        """List iterator

        Returns:
            List iterator
        """
    def __len__(self) -> int:
        """Get the list length

        Returns:
            Length of the list
        """
    def __repr__(self) -> str:
        """Convert the list to a string

        Returns:
            List values as string
        """
    def append(self, value: BaseElementAdapter):
        """Append a list item

        Args:
            value: Value to append
        """
    def clear(self):
        """
        """

class DocumentAdapter():

    def GetDocumentID(self) -> int:
        """Get the document ID

        Returns:
             Document ID
        """
    def GetScalingFactor(self) -> float:
        """Get the scaling factor

        Returns:
             Scaling factor
        """
    def __init__(self):
        """Initialize
        """

class DocumentNameService():

    @staticmethod
    def GetActiveDocumentName() -> str:
        """Get the name of the active document

        Returns:
            Name of the active document
        """
    @staticmethod
    def GetDocumentName(ele: BaseElementAdapter, withNumber: bool, withLabel: bool, delimiter: str) -> str:
        """Get the name of the element

        Args:
            ele:        Element
            withNumber: Add the document number: true/false
            withLabel:  Add the label: true/false
            delimiter:  Delimiter between number and name

        Returns:
            Name of the document
        """
    @staticmethod
    def GetDocumentNameByFileIndex(fileIndex: int, withNumber: bool, withLabel: bool, delimiter: str) -> str:
        """Get the document name by the document index (load index)

        Args:
            fileIndex:  Document file index
            withNumber: Add the document number: true/false
            withLabel:  Add the label: true/false
            delimiter:  Delimiter between number and name

        Returns:
            Document name
        """
    @staticmethod
    def GetDocumentNameByFileNumber(fileNumber: int, withNumber: bool, withLabel: bool, delimiter: str) -> str:
        """Get the document name by the file number

        Args:
            fileNumber: Document file number
            withNumber: Add the document number: true/false
            withLabel:  Add the label: true/false
            delimiter:  Delimiter between number and name

        Returns:
            Document name
        """
    @staticmethod
    def GetLoadedDocumentsNameData() -> list[tuple[str, int]]:
        """Get the names and file numbers of the loaded documents

        Returns:
            Names of the loaded documents
        """

class ElementAdapterType():
    """Implementation of the element type
    """
    def GetDisplayName(self) -> str:
        """Get the display name of the element

        Returns:
            Display name
        """
    def GetGuid(self) -> GUID:
        """Get the GUID

        Returns:
            GUID of the element type
        """
    def GetModelType(self) -> GUID:
        """Get the model type

        Returns:
            Model type
        """
    def GetTypeName(self) -> str:
        """Get the type name of the element

        Returns:
            Type name of the element
        """
    def GetZoomState(self) -> object:
        """Get the zoom state of the element type

        Returns:
            Zoom state
        """
    def Is3DElement(self) -> bool:
        """Get the 3D element state

        Returns:
            Element has 3D geometry: true/false
        """
    def IsInfoFromParent(self) -> bool:
        """Get the element state for the element info

        Returns:
            Use the element info from the parent element: true/false
        """
    def IsTypeGroup(self, typeGroup: ElementAdapterTypeGroup) -> bool:
        """Check for the type group

        Args:
            typeGroup: Type group to check

        Returns:
            Element is in the type group: true/false
        """
    def __eq__(self, guid: GUID) -> bool:
        """Equal operator

        Args:
            guid: Type to compare

        Returns:
            Types are equal: true/false
        """
    def __ne__(self, guid: GUID) -> bool:
        """Not equal operator

        Args:
            guid: Type to compare

        Returns:
            Types are equal: true/false
        """
    @property
    def DisplayName(self) -> str:
        """Get the display name of the element
        """
    @DisplayName.setter
    def DisplayName(self, displayName: str) -> None:
        """Set the display name

        Args:
            displayName: Display name
        """
    @property
    def Guid(self) -> GUID:
        """Get the GUID
        """
    @Guid.setter
    def Guid(self, guid: GUID) -> None:
        """Set the GUID

        Args:
            guid: GUID
        """
    @property
    def IsVisible(self) -> bool:
        """Get the visible state of the element type
        """
    @IsVisible.setter
    def IsVisible(self, bVisible: bool) -> None:
        """Set the visible state of the element type

        Args:
            bVisible: Element type is visible on the screen: true/false
        """

class ElementAdapterTypeData():

    @staticmethod
    def GetElementAdapterType(uuid: GUID) -> ElementAdapterType:
        """Get the element adapter type for the defined UUID

        Args:
            uuid: Type UUID

        Returns:
             Element adapter
        """

class ElementAdapterTypeGroup(enum.Enum):
    """Implementation of the element adapter type groups

    eNO_GROUP                       : No type group
    eBREPS3D_GROUP                  : Group with the BReps elements
    eBREPS3D_SURFACE_GROUP          : Group with the BReps surface elements
    eLINES3D_GROUP                  : Group with the 3D lines
    eCURVES3D_GROUP                 : Group with the 3D Curves
    eAREAS3D_GROUP                  : Group with the 3D Areas
    eVOLUMES3D_GROUP                : Group with the 3D volumes
    eTEXT_GROUP                     : Group with the text elements
    eDIMENSION_GROUP                : Group with the dimension elements
    eSMART_SYMBOL_GROUP             : Group with the smart symbol elements
    eSMART_PART_GROUP               : Group with the smart part elements
    eFIXTURE_GROUP                  : Group with the fixture elements
    eREVEAL_GROUP                   : Group with the reveal elements
    eXREF_GROUP                     : Group with the XRef elements
    ePYTHON_PART_GROUP              : Group with the python part elements
    ePIPEWORK_GROUP                 : Group with the pipework elements
    ePIPEBUNDLE_GROUP               : Group with the pipebundle elements
    eAXIS_ELEMENT_GROUP             : Group with the axis elements
    eBARS_PLACEMENT_GROUP           : Group with the bar placement elements
    eDEFECT_ELEMENT_GROUP           : Group with the defect elements
    eWALL_OPENING_GROUP             : Group with the wall openings
    eWALL_OPENING_SUB_ELEMENTS_GROUP: Group with the sub elements of the wall opening (tiers, lintel, ...)
    ePRECAST_GROUP                  : Precast elements
    eHYPERELEMENT_GROUP             : Group with composite elements
    eOPENINGPART_GROUP              : Group with openingpart elements
    eHYPERELEMENT_TIER_GROUP        : Group with tier elements of hyper elements
    eLAST_GROUP                     : Index of the last group
    """
    eAREAS3D_GROUP = 5
    eAXIS_ELEMENT_GROUP = 17
    eBARS_PLACEMENT_GROUP = 18
    eBREPS3D_GROUP = 1
    eBREPS3D_SURFACE_GROUP = 2
    eCURVES3D_GROUP = 4
    eDEFECT_ELEMENT_GROUP = 19
    eDIMENSION_GROUP = 8
    eFIXTURE_GROUP = 11
    eHYPERELEMENT_GROUP = 23
    eHYPERELEMENT_TIER_GROUP = 25
    eLAST_GROUP = 31
    eLINES3D_GROUP = 3
    eNO_GROUP = 0
    eOPENINGPART_GROUP = 24
    ePIPEBUNDLE_GROUP = 16
    ePIPEWORK_GROUP = 15
    ePRECAST_GROUP = 22
    ePYTHON_PART_GROUP = 14
    eREVEAL_GROUP = 12
    eSMART_PART_GROUP = 10
    eSMART_SYMBOL_GROUP = 9
    eTEXT_GROUP = 7
    eVOLUMES3D_GROUP = 6
    eWALL_OPENING_GROUP = 20
    eWALL_OPENING_SUB_ELEMENTS_GROUP = 21
    eXREF_GROUP = 13

    names = {eNO_GROUP: eNO_GROUP,
             eBREPS3D_GROUP: eBREPS3D_GROUP,
             eBREPS3D_SURFACE_GROUP: eBREPS3D_SURFACE_GROUP,
             eLINES3D_GROUP: eLINES3D_GROUP,
             eCURVES3D_GROUP: eCURVES3D_GROUP,
             eAREAS3D_GROUP: eAREAS3D_GROUP,
             eVOLUMES3D_GROUP: eVOLUMES3D_GROUP,
             eTEXT_GROUP: eTEXT_GROUP,
             eDIMENSION_GROUP: eDIMENSION_GROUP,
             eSMART_SYMBOL_GROUP: eSMART_SYMBOL_GROUP,
             eSMART_PART_GROUP: eSMART_PART_GROUP,
             eFIXTURE_GROUP: eFIXTURE_GROUP,
             eREVEAL_GROUP: eREVEAL_GROUP,
             eXREF_GROUP: eXREF_GROUP,
             ePYTHON_PART_GROUP: ePYTHON_PART_GROUP,
             ePIPEWORK_GROUP: ePIPEWORK_GROUP,
             ePIPEBUNDLE_GROUP: ePIPEBUNDLE_GROUP,
             eAXIS_ELEMENT_GROUP: eAXIS_ELEMENT_GROUP,
             eBARS_PLACEMENT_GROUP: eBARS_PLACEMENT_GROUP,
             eDEFECT_ELEMENT_GROUP: eDEFECT_ELEMENT_GROUP,
             eWALL_OPENING_GROUP: eWALL_OPENING_GROUP,
             eWALL_OPENING_SUB_ELEMENTS_GROUP: eWALL_OPENING_SUB_ELEMENTS_GROUP,
             ePRECAST_GROUP: ePRECAST_GROUP,
             eHYPERELEMENT_GROUP: eHYPERELEMENT_GROUP,
             eOPENINGPART_GROUP: eOPENINGPART_GROUP,
             eHYPERELEMENT_TIER_GROUP: eHYPERELEMENT_TIER_GROUP,
             eLAST_GROUP: eLAST_GROUP}

    values = {0: eNO_GROUP,
              1: eBREPS3D_GROUP,
              2: eBREPS3D_SURFACE_GROUP,
              3: eLINES3D_GROUP,
              4: eCURVES3D_GROUP,
              5: eAREAS3D_GROUP,
              6: eVOLUMES3D_GROUP,
              7: eTEXT_GROUP,
              8: eDIMENSION_GROUP,
              9: eSMART_SYMBOL_GROUP,
              10: eSMART_PART_GROUP,
              11: eFIXTURE_GROUP,
              12: eREVEAL_GROUP,
              13: eXREF_GROUP,
              14: ePYTHON_PART_GROUP,
              15: ePIPEWORK_GROUP,
              16: ePIPEBUNDLE_GROUP,
              17: eAXIS_ELEMENT_GROUP,
              18: eBARS_PLACEMENT_GROUP,
              19: eDEFECT_ELEMENT_GROUP,
              20: eWALL_OPENING_GROUP,
              21: eWALL_OPENING_SUB_ELEMENTS_GROUP,
              22: ePRECAST_GROUP,
              23: eHYPERELEMENT_GROUP,
              24: eOPENINGPART_GROUP,
              25: eHYPERELEMENT_TIER_GROUP,
              31: eLAST_GROUP}

    def __getitem__(self, key: (str | int | float)) -> ElementAdapterTypeGroup:
        """ get the item for a key

        Args:
            key: value key

        Returns:
            value for the key
        """
        return self.values[key]


class GUID():

    @staticmethod
    def FromString(strGuid: str) -> GUID:
        """Create a GUID from a string

        Args:
            strGuid:GUID as string

        Returns:
            GUID from the string
        """
    def __eq__(self, compGuid: GUID) -> bool:
        """Compare a GUID

        Args:
            compGuid:GUID to compare

        Returns:
            GUIDs are equal: True/False
        """
    def __hash__(self) -> int:
        """Create a hash from the GUID

        Returns:
            hash from the GUID
        """
    def __init__(self):
        """Initialize
        """
    def __repr__(self) -> str:
        """Create a string from the GUID

        Returns:
            string from the GUID
        """

class PrecastPropertiesService():

    @staticmethod
    def GetPositionNumber() -> str:
        """Get the precast element position number

        Returns:
             position number
        """
    @staticmethod
    def GetPositionNumberPure() -> int:
        """Get the precast element position number

        Returns:
             position number
        """
    @staticmethod
    def GetPrecastElementTypeDescription(arg2: bool) -> str:
        """Get the precast element description (new wall system)

        Returns:
             description
        """

class ReinforcementPropertiesReader():

    @staticmethod
    def GetPositionNumber(ele: BaseElementAdapter) -> int:
        """Get the position number

        Args:
            ele: Element

        Returns:
             Position number
        """
    @staticmethod
    def GetPositionNumberFromRepresentation(ele: BaseElementAdapter) -> int:
        """Get the position number from a representation element

        Args:
            ele: Element

        Returns:
             Position number
        """

AbsoluteElevationDimension_TypeUUID: GUID # value = b2d2ee44-d64a-4186-ab1f-5be3f75d0481
AlignmentDimension_TypeUUID: GUID # value = 278ff28e-054f-42fd-aad2-db60c1398570
AngleDimension_TypeUUID: GUID # value = 560cd9bb-cad2-45ab-9e32-df835e636d4e
AnimationLight_TypeUUID: GUID # value = 898dd5da-700f-4208-bd7e-6fddc263e0a7
Any3DFoundation_TypeUUID: GUID # value = 16436b0e-db8f-4f7d-879e-d6c3ab3b7ba2
Arc3D_TypeUUID: GUID # value = d911f9af-662a-47c4-b0f4-c4a11024464e
ArcDimension_TypeUUID: GUID # value = 853ab835-e653-4504-84d9-f56b9fcd2e97
ArchitectureAdditionalFinishElement_TypeUUID: GUID # value = bc4b00cf-0bfe-40fa-be03-f12e94f35456
ArchitectureArea3D_TypeUUID: GUID # value = 0b4b39e4-6ad6-47fb-a3af-e1711364ae43
ArchitectureBRep3D_Surface_TypeUUID: GUID # value = 0d557edf-88d7-4019-8653-c34e9f55e93e
ArchitectureBRep3D_Volume_TypeUUID: GUID # value = a90d1a5b-4b9d-4470-a10f-8af3d2779aaf
ArchitectureBRep3D_Wire_TypeUUID: GUID # value = 1d9d3802-a4e2-4123-88dd-fb6b3858b8a9
ArchitectureBaseboard_TypeUUID: GUID # value = 6f269337-ea9c-4f3c-9954-43ceeded5346
ArchitectureBitmap_TypeUUID: GUID # value = c694e8da-b459-48e6-bd77-f74cc0c474f3
ArchitectureCeilingSurface_TypeUUID: GUID # value = 8a7acf3c-df4a-4eee-b9e9-c5df1e323821
ArchitectureCircle_TypeUUID: GUID # value = 407a202e-833c-4ddd-b950-586a5f161824
ArchitectureComponentLinkage_TypeUUID: GUID # value = c73cd501-6077-49c8-a0ae-90989231b6fe
ArchitectureComponent_TypeUUID: GUID # value = 1d214802-5dab-4c17-8218-c2c9925cccc4
ArchitectureCylinder3D_TypeUUID: GUID # value = b636bed2-71ed-43a4-8955-a4d59c573bb5
ArchitectureElevation_TypeUUID: GUID # value = 91076ceb-760d-4671-b48c-6269bf3f881b
ArchitectureFacestyle_TypeUUID: GUID # value = dca42e99-1f34-4508-b556-a9629d2b1b0a
ArchitectureFilling_TypeUUID: GUID # value = 0fec0fb3-69ec-4fa1-868b-7f6507ea0221
ArchitectureFloorSurface_TypeUUID: GUID # value = 7e2e75ba-c860-41b7-95cd-b117b491c892
ArchitectureHatching_TypeUUID: GUID # value = e6aec957-e43c-4fad-b00f-772ff69669b2
ArchitectureHyperElement_TypeUUID: GUID # value = ccfd364a-b926-4078-b488-9c6052920ae2
ArchitectureLine_TypeUUID: GUID # value = 62cb0553-84c5-4dde-a940-72caea5356ea
ArchitectureOpeningPlane_TypeUUID: GUID # value = 7f8dc969-7cd5-4ab2-b849-360076784a18
ArchitecturePointSymbol3D_TypeUUID: GUID # value = 48a3d7b0-b55c-49b3-91f5-d652c0105e86
ArchitecturePointSymbol_TypeUUID: GUID # value = e63a10af-bc9c-4477-b3f9-de2896f3e125
ArchitecturePolyline_TypeUUID: GUID # value = 77e2a7a0-11b9-47dc-b868-9da8f515d734
ArchitectureSphere3D_TypeUUID: GUID # value = ce976223-44e0-4fbb-86ac-8960a9949974
ArchitectureTextBlock_TypeUUID: GUID # value = 3ac0b626-1e0c-4075-8eed-05ed981a3b51
ArchitectureVariableTextBlock_TypeUUID: GUID # value = f67f01da-1d35-4b38-9441-c75976d8cd41
ArchitectureVariableText_TypeUUID: GUID # value = 2264ac00-2853-409a-88e4-cdb6ff327de6
ArchitectureVerticalSurface_TypeUUID: GUID # value = 1619d9a5-de0e-444c-af5f-5e242523c8e5
ArchitectureVolume3D_TypeUUID: GUID # value = 9479bfe8-5a51-4c66-8a57-67f285eb2587
Area3D_TypeUUID: GUID # value = 89c02990-a819-4786-8712-7f27f0263607
Article_TypeUUID: GUID # value = a0fc53cf-dd56-4fbc-8f91-6fd32bb36890
AssociativeReportAreaVisualisation_TypeUUID: GUID # value = 3016e269-b6b5-415f-914b-9c18d5482839
AssociativeReportParameter_TypeUUID: GUID # value = f539ef10-2819-4382-be97-56fcf095e083
AssociativeReport_TypeUUID: GUID # value = 0a39bc26-6a3e-4807-aeb5-4bc8612a9917
AssociativeViewAbsoluteElevationDimension_TypeUUID: GUID # value = 77b95ccc-2557-4e71-b490-70b61846414e
AssociativeViewCartesianGrid_TypeUUID: GUID # value = 75706783-1fc9-40d4-a659-8f7f22330d65
AssociativeViewDimensions_TypeUUID: GUID # value = 7cda107e-8e49-4cd1-839d-4a0321b3d453
AssociativeViewFrame_TypeUUID: GUID # value = d0f57dea-8678-4190-b3e7-bc73707911ad
AssociativeViewIntersectionBody_TypeUUID: GUID # value = 186458db-1a4b-488a-90e2-747366ba26dd
AssociativeViewLinearDimension_TypeUUID: GUID # value = 529bcee0-de7d-48d0-bbb7-6b49c2e5b5f3
AssociativeView_TypeUUID: GUID # value = dddd0892-91a6-4eb6-aacd-d60e08661550
Associative_AbsoluteElevationDimension_TypeUUID: GUID # value = 1ebf6357-dd76-40c1-af96-6b02a0870728
Associative_AlignmentDimension_TypeUUID: GUID # value = 92be2b90-d4ca-407a-acc6-7b1d3a4c8f8f
Associative_AngleDimension_TypeUUID: GUID # value = 69037cad-c96f-462a-adf9-7866588e2a27
Associative_CurveDimension_TypeUUID: GUID # value = 954249ec-89fe-4f93-b552-ed528b55cca6
Associative_ElevationDimension_TypeUUID: GUID # value = 5eb603f6-fbab-4112-841c-687c5c53ab82
Associative_LinearDimension_TypeUUID: GUID # value = 3a40bab4-c9ed-4203-aebe-8a9afed8fec3
Associative_RadiusDimension_TypeUUID: GUID # value = 1a977710-4924-4db9-b709-c6498c8e0d98
AttributeContainer_TypeUUID: GUID # value = 572686a1-0ae5-4d22-88d1-35eeaea3f234
BRep3D_Surface_TypeUUID: GUID # value = 5897b7a9-47be-44a2-99a2-bc2474072080
BRep3D_Volume_TypeUUID: GUID # value = a01400b0-4a94-4257-a48a-3dd5628c9999
BRep3D_Wire_TypeUUID: GUID # value = 0ee77489-a131-4d96-a9db-13279190f128
BarsAreaDefinition_TypeUUID: GUID # value = 719b381b-6307-4c86-8e57-87247699e15e
BarsAreaPlacement_TypeUUID: GUID # value = 26f558e2-49ab-4de9-a8b2-7ed80845f08f
BarsAreaRepresentationLine_TypeUUID: GUID # value = 73e5b84d-4ed6-4aec-823e-0b94c8486da7
BarsAreaRepresentation_TypeUUID: GUID # value = f506e6ce-91a0-4a3e-8848-347f3c903c0f
BarsCircle_TypeUUID: GUID # value = 0653f81d-5d23-466b-84f3-9f143433a7fc
BarsCircularPlacement_TypeUUID: GUID # value = 9fd713b5-54a8-4690-89fe-50d20f712f4c
BarsDefinition_TypeUUID: GUID # value = 9e68330c-b5e7-40e5-a480-4e3453b673a5
BarsEndBendingPlacement_TypeUUID: GUID # value = 7cf9681f-9eaa-45d2-bf6d-3addb3e5d42e
BarsLine_TypeUUID: GUID # value = 1a4297a3-53f5-4429-8b2a-4d92780b4c2b
BarsLinearMultiPlacement_TypeUUID: GUID # value = 099d64b9-9a26-4f0e-9d8d-e8192fb73dff
BarsLinearPlacement_TypeUUID: GUID # value = abc63117-224c-4db8-a81f-86137af401f4
BarsPlacementConnection_TypeUUID: GUID # value = fb330c62-411b-4039-8b41-c6bc11df9f6f
BarsPolyline_TypeUUID: GUID # value = dab294bb-adf6-4d5b-87c7-12256f150a25
BarsRepresentationLine_TypeUUID: GUID # value = 365b9902-585a-48fb-802e-309ae9ee3719
BarsRepresentation_TypeUUID: GUID # value = 691c6352-0d48-4950-8bec-aed5a3769318
BarsRotationalPlacement_TypeUUID: GUID # value = 8de31a50-dbd7-46fa-b448-897d5f01f526
BarsRotationalSolidPlacement_TypeUUID: GUID # value = cf324c6a-a13f-4da0-9cac-2321c63e772b
BarsSchemaCircularPlacement_TypeUUID: GUID # value = 2009b41e-5552-4dee-bc49-998631f83526
BarsSchemaPlacement_TypeUUID: GUID # value = 5e03b3fd-ca08-4181-898a-ce60a51f5a34
BarsSchemaRepresentation_TypeUUID: GUID # value = 3339f5ab-93c1-433a-b367-135e717aff2f
BarsSpiralPlacement_TypeUUID: GUID # value = 49eba7e3-fc11-41af-a327-c0e696dd87cb
BarsTangentionalPlacement_TypeUUID: GUID # value = ee8d45a6-3ff1-4bf1-bc60-0f83a8afae92
Baseboard_TypeUUID: GUID # value = 457e903d-4a84-4539-a532-5b2fa1d4491a
BeamPolygonalRecessTier_TypeUUID: GUID # value = fc360f0b-f188-4071-933a-e022c67e39c3
BeamPolygonalRecess_TypeUUID: GUID # value = df23b17c-af0e-4ea3-8e55-1ff48671bf13
Beam_TypeUUID: GUID # value = 2b866eae-9440-4ba8-a86d-b40563e211c2
BendedMeshDefinition_TypeUUID: GUID # value = 8e069806-cc7a-4ecd-a8c1-256a9e995c5a
BendedMeshSchemaPlacement_TypeUUID: GUID # value = c47dd29f-788e-4df2-b1a6-fc8593760a3f
BendedMeshSchemaRepresentation_TypeUUID: GUID # value = c100867a-6965-4bc0-aa79-8105d9dfe123
BendingScheduleListHead_TypeUUID: GUID # value = 08d6b73b-da6e-4b37-a2c9-7682ca67fe9f
Bitmap_TypeUUID: GUID # value = cbf2f592-88d1-405b-bb5e-9edf6cc4c692
BuildingSolid_TypeUUID: GUID # value = 26fd721a-0e43-493c-b74e-8b0148482acc
CadastralGeneralGroupFixture_TypeUUID: GUID # value = 9ea8b5a8-404a-4db1-a26b-b2411f318c47
CadastralLineFixture_TypeUUID: GUID # value = a684f840-b37e-41a2-b702-ef9b88dc18af
CadastralPlaneFixture_TypeUUID: GUID # value = 374b667c-dd33-423b-b1e1-65ac8f3440ab
CadastralPointFixture_TypeUUID: GUID # value = 75b5a2b1-b09d-44e2-951a-8cf97480006c
CartesianGridWithDimension_TypeUUID: GUID # value = 2a4523bc-f8f7-4057-a907-8054e590d40b
CartesianGrid_TypeUUID: GUID # value = ad9eeeb0-3188-4844-8e99-eeaf525e0d2b
CeilingSurface_TypeUUID: GUID # value = 8601ea71-6af8-4e36-940a-46e7638f4292
CeilingSystemSmartSymbol_TypeUUID: GUID # value = f76a7a29-3539-49c9-b6f7-e2b5ff4ecae2
CeilingSystem_TypeUUID: GUID # value = 38607790-dc1d-42db-8223-c75c2c372ce2
CellButton_TypeUUID: GUID # value = 98820c74-7ba8-483f-a42d-da5f28242360
Chain2DParallel_TypeUUID: GUID # value = 36d07b6f-5d55-417a-af16-766d09160aeb
Chain2DStationing_TypeUUID: GUID # value = 35696d28-a78c-4c77-b380-7f4e90898c89
Chain2DText_TypeUUID: GUID # value = ff948e93-81e7-4138-81d0-ebb25f29c9f7
Chain2D_TypeUUID: GUID # value = 37510d6b-040b-4532-b397-2097df682cf7
Chimney_TypeUUID: GUID # value = b5a1beda-2075-43f2-9e01-3bdf944de77c
Circle2D_TypeUUID: GUID # value = ed420869-371e-45de-932a-4e21611b99e8
CircularUpstandTier_TypeUUID: GUID # value = ceb05412-54fb-42b6-8fe2-670903d6df89
CircularUpstand_TypeUUID: GUID # value = 00856462-6448-475a-85e7-6e420e690954
CircularWallTier_TypeUUID: GUID # value = 47f43445-681f-40b7-8248-094ded1e3d6e
CircularWall_TypeUUID: GUID # value = 53c4f607-d02c-4547-ae5a-4ffac62a4e8d
Clash_TypeUUID: GUID # value = bb3e0339-cfcc-4992-b71a-b554e503ad8d
ClippingPathBody_TypeUUID: GUID # value = c5008f24-780e-48cf-9f6c-ffe7bf9cf454
ClippingPathRepresentation_TypeUUID: GUID # value = fc546bc7-4193-4bec-8468-3548dfbea41b
ClippingPathText_TypeUUID: GUID # value = da48e80a-3b33-4e32-b6bc-3244029f58c6
ClippingPath_TypeUUID: GUID # value = 54ca8377-8af0-4030-8f1c-b4224dc28da4
Clothoid2D_TypeUUID: GUID # value = 2323ffa3-b8bf-4610-b355-c890a71f677a
ClothoidDimension_TypeUUID: GUID # value = e69b7a09-d247-4add-a812-6b76a040f7c9
CollarBeam_TypeUUID: GUID # value = 3e8a807d-a576-46fd-a331-22ec1cebdee9
CollarTie_TypeUUID: GUID # value = ac0a3b9d-8222-42ef-9cd4-91048107e1f5
Column_TypeUUID: GUID # value = ac9415e3-4337-4860-8cd4-2f0d48596f12
CornerWindowComposite_TypeUUID: GUID # value = c4e583b1-fc1f-47bb-8c57-daf4b1b9bd15
CornerWindowReveal_TypeUUID: GUID # value = 1d0f5ae9-2592-4245-8699-2548fe6a7935
CornerWindowTier_TypeUUID: GUID # value = 2f6f5025-fde4-4255-8382-1dfbd66363ce
CornerWindow_TypeUUID: GUID # value = 72444818-c114-4e96-909d-9d45e5ec33cf
CurveDimension_TypeUUID: GUID # value = e04bc2b2-a805-4cfc-a106-94c97fc0cb7b
Cylinder3D_TypeUUID: GUID # value = 0536725b-2491-4e6c-abcf-2525cadefeb3
DTMAreaLabel_TypeUUID: GUID # value = 0d18fc6e-a145-4bcc-adf3-c30faf63c34f
DTMArea_TypeUUID: GUID # value = 67e2ec4c-6b7f-4960-998f-431b3358f5cc
DTMContourLineLabel_TypeUUID: GUID # value = be7fba01-db56-4b90-903a-e20eb751d639
DTMContourLine_TypeUUID: GUID # value = 3b681ecd-fb6f-485b-a744-694da55b798e
DTMCrossSection_TypeUUID: GUID # value = 448be08c-eb5c-4279-9a30-811636ab2c7d
DTMElevationLabel_TypeUUID: GUID # value = 13307bdb-061c-4592-879b-5ded9e6554c5
DTMElevation_TypeUUID: GUID # value = 00980a74-4e08-4d8a-a6f5-67673d067726
DTMGridLabel_TypeUUID: GUID # value = b064befd-580a-4cff-90f6-d0a6fe7c412a
DTMGrid_TypeUUID: GUID # value = bf9b85b6-a3b9-4d92-9921-bc404d64de74
DTMLine_TypeUUID: GUID # value = 689005ca-6680-407e-a3a5-5cf6f73417dc
DTMLongitudinalSection_TypeUUID: GUID # value = 84899e0a-e12b-40d5-bb4d-5a974e44d5e9
DTMPointSymbol3D_TypeUUID: GUID # value = c5f0f3f5-0e82-4afd-94ac-593a87649d53
DTMPointSymbol_TypeUUID: GUID # value = c18a3aee-3570-468e-9880-4fdf83003f50
DTMProfile_TypeUUID: GUID # value = ba2f060b-ec6f-442c-bb03-2fc3f297ae0f
DefaultPlane_TypeUUID: GUID # value = 4cf8babf-d002-40df-aec5-3aad0f5bb689
DeliverySymbol_TypeUUID: GUID # value = 745777e5-f001-40b4-865a-cc6238f7372d
DemolitionSolid_TypeUUID: GUID # value = 37650af7-96d8-48da-9f31-983012ccc5f7
DimensionText_TypeUUID: GUID # value = f672f428-dbaa-48bd-92f1-6841ad44f9b7
DoorOpeningSmartPart_TypeUUID: GUID # value = ed80b415-f961-4c28-b706-76be21d68e89
DoorOpeningSmartSymbol_TypeUUID: GUID # value = ba94ff69-a019-4948-a4f0-39f20c73561f
DoorReveal_TypeUUID: GUID # value = 38be8300-226a-4ed5-80f4-6663fb09997e
DoorSill_TypeUUID: GUID # value = 793b4bdd-55c6-46a9-8491-88472ccb8ed8
DoorSwing_TypeUUID: GUID # value = 9f47fc5a-2727-4ddd-8598-7aeb8d4dff35
DoorTier_TypeUUID: GUID # value = a062752a-0653-488f-9c2e-a57462e5cac3
Door_TypeUUID: GUID # value = 2290eb05-627e-44b9-919a-89f563ec0c39
DrawingFileAttributes_TypeUUID: GUID # value = 9367b011-a1ea-4471-8091-d649f2b5d5ea
DynamicGroupFixture_TypeUUID: GUID # value = 664a947b-b755-46ac-b816-98a3a476c74d
ElementGroupNode_TypeUUID: GUID # value = be06a4dd-e723-4f50-afd3-65e73ec20c8a
ElementGroup_TypeUUID: GUID # value = c040ef81-2c4c-42a2-b980-80e974a35fe0
ElementNumber_TypeUUID: GUID # value = 5954162f-f7e8-4331-bf5d-1269441349e7
ElementUpstandTier_TypeUUID: GUID # value = b7016f4a-b40e-43c7-bdae-23cc2b5d7b83
ElementUpstand_TypeUUID: GUID # value = 1fd1f313-f7ad-4524-ae4b-ee775fc84903
ElementWallTier_TypeUUID: GUID # value = 60f092ab-b782-4e3c-bb8c-e788fcbb032f
ElementWall_TypeUUID: GUID # value = bef805c4-315b-4cae-b791-e426481329ef
ElevationDimension_TypeUUID: GUID # value = fe64b9f0-0f7c-4078-b351-c718da7ec3ca
Ellipse2D_TypeUUID: GUID # value = e25f9106-635f-4893-9917-4bebf8706e6b
EngineerDimensionLineOverlap_TypeUUID: GUID # value = 19f11030-5c29-4044-a0ed-00a809f9bf54
EngineerDimensionLine_TypeUUID: GUID # value = 45e659a4-003e-4f52-8503-7e16a4a8399a
EngineerLabel_TypeUUID: GUID # value = 5e530af7-b15f-4db6-97d0-106c0f11dc51
EngineerSymbol2D_TypeUUID: GUID # value = 01f1e97a-5c76-47e2-90a9-c28053b44ff0
EngineerTextPointer_TypeUUID: GUID # value = 5c8e764f-b85b-4920-8bf2-42586898b324
EngineeringPathElement_TypeUUID: GUID # value = a24f771b-a64e-46bf-9234-0b2e235f9d15
EnvelopingSurface_TypeUUID: GUID # value = d92a5adf-a8ad-476c-952d-e62f8c8b51bc
EquipmentSmartPart_TypeUUID: GUID # value = 56421350-0607-467a-940c-0c2bf3169d35
ExtendedElement_TypeUUID: GUID # value = 689289fe-9b70-462d-840e-cbc6361f58d0
FacadeSmartSymbol_TypeUUID: GUID # value = 6b60fc79-bcfc-4f26-9f1e-394a4da392f1
Facade_TypeUUID: GUID # value = 1dac1a9d-d28f-438f-a3a0-8d92f8785a91
Facestyle_TypeUUID: GUID # value = 754372fb-a7de-4639-94d6-cfede4f3236d
FacingComposite_TypeUUID: GUID # value = dba9403d-faef-4570-889e-cf3aa6fbebc6
Facing_TypeUUID: GUID # value = 0691e297-58d1-499b-b827-ed7732dff111
FemAreaLoad_TypeUUID: GUID # value = 19cd45a5-7fb0-4ca0-bb5d-3beffbab903d
FemBarLine_TypeUUID: GUID # value = 315a1fd9-2fdc-408e-8bc5-226854745d3a
FemContours_TypeUUID: GUID # value = 32e2e566-e8cd-493e-8567-b8e1376e0867
FemLineLoad_TypeUUID: GUID # value = f3a48135-d668-43a4-a59e-e79aa05ade92
FemLineSupport_TypeUUID: GUID # value = 52ffd334-ec0f-475c-9d1e-124fa98859ad
FemPlateElementLine_TypeUUID: GUID # value = 749aa635-0f9f-4df4-bc02-f07b4f7f3c62
FemPointLoad_TypeUUID: GUID # value = 7f5adc6a-d13d-4031-ade0-10f6246c60cb
FemSmartSymbolFormwork_TypeUUID: GUID # value = 9d6002ad-c500-42c4-bcb0-61287e7d0977
FemSmartSymbolMeshFormwork_TypeUUID: GUID # value = 6518e36f-ef6b-49f0-a996-7a6dbb8ea4ba
FemSpring_TypeUUID: GUID # value = 8e050fc5-d73a-42f2-a63e-95e38ddb20d6
FillLine_TypeUUID: GUID # value = 183a5082-1eac-46ac-8411-e3aa3840efc6
Filling2D_TypeUUID: GUID # value = cf3f556e-7d90-46a0-9175-598f93c9768e
FixtureDefinition_TypeUUID: GUID # value = 5fd09a6e-d52f-41e2-bb6d-debc6d4576f9
FloorSurface_TypeUUID: GUID # value = 34e75c2e-9cf0-4ac4-bd58-6479e5d981aa
FlushPierTier_TypeUUID: GUID # value = d1714704-53f9-4cb7-afbf-38144c7efd8b
FlushPier_TypeUUID: GUID # value = 303fdda8-ead7-4ae9-aab8-12c64e46f00d
GeneralGroupFixture_TypeUUID: GUID # value = 5b5fc673-16f8-463c-abe2-87b8f35b9a95
GeneralObject_TypeUUID: GUID # value = ded20def-e15c-4348-a582-383f117e1948
GeneralVariableTextBlock_TypeUUID: GUID # value = 6aa35170-4c84-4b4f-9e70-e48768d91a07
GeneralVariableText_TypeUUID: GUID # value = ab41d13c-410f-4b8e-8673-13c57e8737c3
GradientFilling2D_TypeUUID: GUID # value = eeab9269-b284-41eb-8490-2ded8a95987b
Hatching2D_TypeUUID: GUID # value = 1e56e515-4717-4805-bb03-3e1486d1edf7
Header_TypeUUID: GUID # value = 8cf99be4-e524-46a0-b16a-7780fc2af9cc
HipRafter_TypeUUID: GUID # value = 58e0148a-12f4-45a3-8bcb-e4f1db87ad0d
HyperRoofCovering_TypeUUID: GUID # value = 775be225-8799-4977-8844-7b371a4a052b
HyperRoofFrame_TypeUUID: GUID # value = 1b133fc8-0f4b-4fa5-8098-4861882d160c
IndividualFoundation_TypeUUID: GUID # value = 4e3b142e-f4d5-4d79-bade-3a6b17f32c22
InstallationComponent_TypeUUID: GUID # value = 954b8810-b6e8-4627-a5b4-36dcf9568837
InternalElement_TypeUUID: GUID # value = 10ccd15a-7bf5-4f90-8ccc-775fc7a41bb6
JointTier_TypeUUID: GUID # value = 9fe71c38-53a7-496b-89b6-e835e275d9f8
Joint_TypeUUID: GUID # value = c4a7103f-64dc-4684-89bf-eb9c0e96a58c
JoistPlaced_TypeUUID: GUID # value = 8cf4a99a-e619-45c9-9321-0d89401c521e
LandscapingPathBaseboard_TypeUUID: GUID # value = b81ae1c1-3dfb-4d03-bdbc-6c1f151af8b7
LandscapingPathFloorSurface_TypeUUID: GUID # value = 2df54e0e-ad3d-4472-8018-117ad8fa7962
LandscapingPlantsBaseboard_TypeUUID: GUID # value = 0f70d460-0b52-46ca-8d4b-2c21fdf90b22
LandscapingPlantsFloorSurface_TypeUUID: GUID # value = f264ce83-9d99-4d44-885e-020b25f5c0c2
LayoutBorderMaster_TypeUUID: GUID # value = f6ec40d4-0122-4397-8b64-e0421b6c3193
LayoutBorder_TypeUUID: GUID # value = 30f80217-1363-4b91-a31b-8a7969f59c1e
LayoutClipRegion_TypeUUID: GUID # value = b4336bc0-b035-4ab5-aa06-85d471dfbb39
LayoutElement_TypeUUID: GUID # value = a04745f8-0342-49f5-8369-dd367a1ca3fb
LayoutFreeElement_TypeUUID: GUID # value = c43bda6e-24d3-46af-90c0-3dddb6c07d6c
LayoutIntersection_TypeUUID: GUID # value = 610b04f8-2223-4889-b5bc-de5ce1d118b9
LayoutMaster_TypeUUID: GUID # value = bdeafad2-5124-4e4f-91a1-fe069e4a8915
LayoutSheet_TypeUUID: GUID # value = f2a769ea-9c51-48ba-9a45-c934b6e5cc09
LayoutWindow_TypeUUID: GUID # value = c4789823-7d45-4508-9ee4-2f250c0e2e75
LegendEndSum_TypeUUID: GUID # value = 2dea83d2-4ed7-4c57-9d90-273ab5908ffd
LegendIntermediateSum_TypeUUID: GUID # value = 7a2fb444-bffa-4b1a-ad59-d8a7ff1f1329
LegendRow_TypeUUID: GUID # value = 2fee6453-04db-41ee-953d-e7828c42dc11
LegendStamp_TypeUUID: GUID # value = 7110f684-18f9-48d7-a128-c48af32a6485
Legend_TypeUUID: GUID # value = da11e599-90a4-4a35-b503-776dbd6ab257
LightdomeSmartPart_TypeUUID: GUID # value = d0d5f17d-010a-4850-b095-f6c265754fc2
Line2D_TypeUUID: GUID # value = 86c4d395-9807-4e01-947b-3f55c23f07c4
Line3D_TypeUUID: GUID # value = 7c9630cb-1c36-43a2-839c-ed95011e5583
LineFixture_TypeUUID: GUID # value = b699c31e-2902-4d76-a391-64c87d523fe1
LineObject_TypeUUID: GUID # value = 3452db23-52a0-4525-8bba-063cbb50fd5b
LineSupport_TypeUUID: GUID # value = 9de2eecb-599a-4e79-ab6d-cdcf8ad43922
LineUpstandTier_TypeUUID: GUID # value = 28b57684-0ba8-4f63-b699-f6dd5384dce9
LineUpstand_TypeUUID: GUID # value = c09ec0b9-6738-4aa4-9cff-15ea2b564986
LinearDimension_TypeUUID: GUID # value = 6cefc778-8aca-48db-9794-d7d73394d873
Link_TypeUUID: GUID # value = 20bfb51b-57c1-4438-8521-5a9f8cf1fe60
Lintel_TypeUUID: GUID # value = b6bb4be5-f5b1-4fac-a8a8-5301c9f2f84a
MaskText_TypeUUID: GUID # value = da534a63-6bda-419c-a4aa-feca6785c1f5
MaskingPlane_TypeUUID: GUID # value = 46e9f2b8-8daf-4bad-bc7c-b19b5118ba61
MeshAreaBorder_TypeUUID: GUID # value = 9cbb6264-64fc-4271-89b6-34e44d5685b3
MeshAreaPlacement_TypeUUID: GUID # value = 0d5dd3f0-bb36-452d-a38a-a13935c8092b
MeshAreaRepresentation_TypeUUID: GUID # value = 1fdd23b2-d0a0-48c2-852a-19ae02da4d6b
MeshBorder_TypeUUID: GUID # value = 53e08cec-0e63-46de-9f5f-607da969a0c4
MeshDefinition_TypeUUID: GUID # value = 3ff54b7e-fe1c-4131-a857-c6f7dc6d0d47
MeshDiagonal_TypeUUID: GUID # value = 6d878c7a-304e-4e06-8300-001d1e8563f9
MeshPlacementDefinition_TypeUUID: GUID # value = d852e01d-541e-432b-8801-ffaccd5ea43e
MeshPlacement_TypeUUID: GUID # value = 5e4f46d9-ff63-40c7-81d3-9f2cf365cdee
MeshRepresentation_TypeUUID: GUID # value = c94b1bab-96a4-47fb-ab4f-0fbf914050c8
MeshScheduleListHead_TypeUUID: GUID # value = 077c8d84-c58b-48a0-bcc2-15df4218651b
MeshScheduleListPoint_TypeUUID: GUID # value = d439b483-b697-49b6-a450-83bc960e3e5f
MeshScheduleMaskPoint_TypeUUID: GUID # value = 1dd5e371-aeba-48a0-8e9f-cfa795fedf65
MeshScheduleMeshPlaced_TypeUUID: GUID # value = ea8f8607-cc58-4aec-bc8d-8ecec8f71505
MeshScheduleMesh_TypeUUID: GUID # value = 2e47f2a2-b1a6-43cc-a40d-141d084fdf62
MeshSchedule_TypeUUID: GUID # value = 8f0aeda7-812b-4d1c-ba33-06399b203d12
MultiLine3DGroup_TypeUUID: GUID # value = 111ad06c-37ca-4312-b113-fe2e99d4a93b
MultiLine3D_TypeUUID: GUID # value = deaf16ce-fa9f-44a4-a111-bdbdbca9de2e
MultiSlab_TypeUUID: GUID # value = 40910db6-25b8-43e3-8704-8bbf285143aa
NULL_TypeUUID: GUID # value = 00000000-0000-0000-0000-000000000000
NetStorey_TypeUUID: GUID # value = f3bccd7b-3ff4-4c74-a074-34ce4df09a50
NicheReveal_TypeUUID: GUID # value = 0b1dc1e1-76e8-4ac9-83ab-618e543a9ab9
NicheSmartSymbol_TypeUUID: GUID # value = e40b413d-52c6-4cf3-9493-5e4f7958362f
NicheTier_TypeUUID: GUID # value = 5b8c7282-d8aa-4962-9b1a-5895cbb69c8d
Niche_TypeUUID: GUID # value = 40b48a03-f66b-42ef-80c8-fda56cc4ccbd
OLEElement_TypeUUID: GUID # value = bec990dc-3e33-46bf-82e3-ec7bb18d15ca
OleSmartSymbolDefinition_TypeUUID: GUID # value = 36d19ea3-6dfd-43dd-8c71-3feb45459766
OpeningPartDoorGroup_TypeUUID: GUID # value = 5b505bb6-fd13-431f-a325-7111a3161929
OpeningPartDoor_TypeUUID: GUID # value = 8ecdfe40-558f-4853-be17-1764fc4e2d84
OpeningPartGroup_TypeUUID: GUID # value = 2bc52caf-03e0-47e3-9e7f-8d15ac5b0e32
OpeningPartWindowGroup_TypeUUID: GUID # value = 2296d05a-08e3-4cfd-9630-f9cbb3bdca4f
OpeningPartWindow_TypeUUID: GUID # value = ed6223cc-f9c5-41c1-b483-5632fc7743f0
OpeningPart_TypeUUID: GUID # value = d3dee89e-2c40-489b-b982-d63a556c9342
OutdoorFacilitiesObject_TypeUUID: GUID # value = 373c62e8-ef0d-4334-8033-f208750c6134
ParapetSmartSymbol_TypeUUID: GUID # value = eb01412d-7763-4c14-9eba-b1408e5dbfe4
Pattern2D_TypeUUID: GUID # value = 0324ac52-cc4a-4032-973b-ef16ddc3c643
PipeBundleGroup_TypeUUID: GUID # value = a26ce8ca-7955-49d8-acf2-1d4c7a93e3c6
PipeBundle_TypeUUID: GUID # value = c59637b2-ff57-4428-960e-bce06ebc5683
PipeWorkGroup_TypeUUID: GUID # value = ad4b3f2f-1ad0-4bc1-ae45-06834f88b69f
PipeWork_TypeUUID: GUID # value = eb75bf83-cd10-4c74-9dec-156a33dce70e
PlaneFixture_TypeUUID: GUID # value = 16ab80a4-71e8-40c1-aac9-d39b3119322b
PlanePairArea_TypeUUID: GUID # value = aa192c2a-5d90-4651-95ce-e6c9998ac4bb
PlantSmartSymbol_TypeUUID: GUID # value = 83868ee3-506a-45dd-8fd5-de3d4fed5ec1
Point2D_TypeUUID: GUID # value = dce0ab56-7cb0-40ec-90dd-222a92decadb
PointBuiltInElementSmartPart_TypeUUID: GUID # value = 217af506-d8c1-44dd-818b-a432dee1bdb0
PointFixture_TypeUUID: GUID # value = 78ec2a3a-3e29-44e4-a229-b89b680f8d49
PointSymbol2D_TypeUUID: GUID # value = 14a41c20-0dd2-4023-a742-c315dc145d97
PointSymbol3D_TypeUUID: GUID # value = 30669022-60a5-40f4-9e88-c8c431e6a645
PolarGrid_TypeUUID: GUID # value = db163629-82de-4b6f-80df-2958e3ed42fa
PolyInstallationComponent_TypeUUID: GUID # value = 4a51992a-f4e1-49d8-b824-9aaaeb16e136
PolygonUpstand_TypeUUID: GUID # value = ffb7d35b-0b34-45b5-90dc-d7fdf4dac90d
PolygonWallTier_TypeUUID: GUID # value = 6cb9c0fc-f35a-4583-be84-454ba1e58251
PolygonWall_TypeUUID: GUID # value = 97fe6ddc-7e8a-4fd0-b1ed-edeafebfaade
PolygonalNicheTier_TypeUUID: GUID # value = 66c99815-fc56-4770-b2dd-b312f343e037
PolygonalNiche_TypeUUID: GUID # value = cd2df13f-90cd-4159-a94f-5c680bb972fc
PolygonalRecessTier_TypeUUID: GUID # value = b3509666-c1cd-40d9-9e8b-b7078ee84856
PolygonalRecess_TypeUUID: GUID # value = 90e62c0f-e152-415e-a34a-ee64828cc089
Polyline2D_TypeUUID: GUID # value = 766ed693-4321-406e-a8fe-d601dbd93c5f
Polyline3D_TypeUUID: GUID # value = c420cbaa-287f-492d-b54d-12e3d7207447
PositionPlanProject_TypeUUID: GUID # value = b5727a7b-0764-468d-b4d3-a2c55547649b
PositionPlan_TypeUUID: GUID # value = 8cbac057-783a-4486-ba59-1634ce60bbad
Post_TypeUUID: GUID # value = c785e627-d78a-4c4e-ad5a-c9085c024a42
PrecastBaseReinforcement_TypeUUID: GUID # value = d149b108-b1b7-459b-a68a-1ac36054ac37
PrecastBrickCompositeFloor_TypeUUID: GUID # value = 8309835f-702e-4a69-b852-760419c1c155
PrecastBrickFloor_TypeUUID: GUID # value = 5f283778-1df0-4737-b075-e032453ade30
PrecastBrickSolidFloor_TypeUUID: GUID # value = db484fc8-71c1-4f0c-86c4-4c94418cb46f
PrecastBrickWall_TypeUUID: GUID # value = 3c3d6508-353f-4544-b806-1b384b1c9141
PrecastBubbleFloor_TypeUUID: GUID # value = 439e6712-b081-4491-be71-5da184294ae0
PrecastCobiaxSlab_TypeUUID: GUID # value = 9daa3a7c-51f4-420a-b9da-c228be0941da
PrecastConnectionElement_TypeUUID: GUID # value = eefd4f77-b3ef-4ab2-b85a-9332fb2e2d95
PrecastConnectorPlacement_TypeUUID: GUID # value = eb3df10d-a47c-47d2-a7c0-a6ee11139f1c
PrecastConnector_TypeUUID: GUID # value = cd773313-b429-41fb-a025-77c6d9a0c8e5
PrecastConstructiveElement_TypeUUID: GUID # value = bb151975-59e7-4b73-a45e-2474e1b20b3f
PrecastCrane_TypeUUID: GUID # value = 048823af-cd61-49ef-9e31-793379b56fb0
PrecastDesignGeneral_TypeUUID: GUID # value = e51fcaef-ecf7-4063-b47f-9e9804fa8952
PrecastDesign_TypeUUID: GUID # value = 1c4b9355-dcce-4d43-85a8-19ad2d9528c5
PrecastDoubleWall_TypeUUID: GUID # value = 521d3409-998d-4285-a958-d15b51e7233d
PrecastElementBricksWall_TypeUUID: GUID # value = 2e305380-372b-4ef8-8896-06a9acb80c46
PrecastElementCompositeFormworkWall_TypeUUID: GUID # value = 3fc744a9-81ab-4d0e-a574-f760a84d6334
PrecastElementDoubleWall_TypeUUID: GUID # value = a47d760f-c1f5-430a-9c4f-ab60441eb6aa
PrecastElementGeneral_TypeUUID: GUID # value = e34ecb93-5dc7-4966-b4e7-8d1161937bb8
PrecastElementNLayersWall_TypeUUID: GUID # value = faad1dc8-9de4-4b8a-9ffa-99f6ad9d188f
PrecastElementPlanElement_TypeUUID: GUID # value = 696313fd-f81c-4356-83fa-47cb04bc111e
PrecastElementPlan_TypeUUID: GUID # value = 49cc24d5-7729-43e1-b6a6-4b3a7bb357ed
PrecastElementSandwichWall_TypeUUID: GUID # value = 5a37db02-363b-4bc5-a870-7c365f6249d4
PrecastElementSolidWall_TypeUUID: GUID # value = 3222c381-f0a5-4ba2-9ace-33b0856abd8c
PrecastElementThermoWall_TypeUUID: GUID # value = a36a286e-4d86-42bd-83a6-1782a4fb1c9f
PrecastElement_TypeUUID: GUID # value = a9835eb5-c3cd-4fb6-a05d-09f3e44be26c
PrecastElementation_TypeUUID: GUID # value = b7c312cf-2b9d-461c-a02f-4a5d56572040
PrecastFloorManagerElement_TypeUUID: GUID # value = 5d96c8ea-dc98-4298-81fc-1f664076bac7
PrecastFormWorkConstructiveElementManual_TypeUUID: GUID # value = 340fed30-7c87-43a9-8461-e4241604b812
PrecastFormWorkConstructiveElement_TypeUUID: GUID # value = bc8901c7-5f78-4b3f-ab42-c525e23684b6
PrecastFormWorkConstructiveHelpElement_TypeUUID: GUID # value = 6f1c3e9f-cbed-41f3-9d98-db0b20cf1944
PrecastFormworkCoupler_TypeUUID: GUID # value = 0a13511c-cb30-4945-9cb4-80f2db3523b0
PrecastFormworkElement_TypeUUID: GUID # value = 6dd5227e-467a-4784-9ff1-78039162bc4d
PrecastFormworkPlacement_TypeUUID: GUID # value = 6251a99b-1812-4dd4-a291-66028644bfdc
PrecastFormworkSmartSymbol_TypeUUID: GUID # value = 0e39618c-b307-42e6-bed8-f0dee69007ae
PrecastFormworkView_TypeUUID: GUID # value = f0a8595b-4fc7-42b0-af62-2f688081c846
PrecastGirderDefinition_TypeUUID: GUID # value = afc943df-a4af-4e6a-8dd5-76ff81284305
PrecastGirderPlacement_TypeUUID: GUID # value = b3eafc13-3fd5-4b8a-a89b-acedc638abb4
PrecastGridAxis_TypeUUID: GUID # value = 6b40b3a7-9a93-466e-8d1f-3f675bfc666f
PrecastGridRegion_TypeUUID: GUID # value = 2e5f2c5b-cbf7-49df-bf4a-db7a39f09351
PrecastGrid_TypeUUID: GUID # value = deb61a60-3dab-40ee-8ac8-d4211673a466
PrecastHalfFloor_TypeUUID: GUID # value = e61f0082-c766-40bd-b7ad-a8ff1e5caff3
PrecastHollowCoreElement_TypeUUID: GUID # value = 251dd7e5-1cca-4f71-bcfa-ffd244fb0512
PrecastLayer_TypeUUID: GUID # value = 34486042-48ba-4fd5-86cc-c8c616b31546
PrecastMWSReinforcement_TypeUUID: GUID # value = cbf61666-8383-4268-8bba-ded5681289f2
PrecastOptima_TypeUUID: GUID # value = 51ce576f-31a7-4706-a8ba-c7ac7aef792e
PrecastPIPanel_TypeUUID: GUID # value = 1fe02314-3713-4317-9511-94738d6e949f
PrecastPanelComponent_TypeUUID: GUID # value = db43c0b9-8996-4a32-bc5f-528a0d485e11
PrecastPrestHollowCoreElement_TypeUUID: GUID # value = 79a38663-e94a-49e9-b0f5-60928200fec4
PrecastRecessAttributeBricksWall_TypeUUID: GUID # value = db5c946a-d0bf-4451-a7fb-787d889489b1
PrecastRecessAttributeCompositeFormworkWall_TypeUUID: GUID # value = ab5c5e62-6be3-414f-8c92-79efd758603d
PrecastRecessAttributeDoubleWall_TypeUUID: GUID # value = e9c39a3b-8934-4117-a3a2-e1a87c76461b
PrecastRecessAttributeNLayersWall_TypeUUID: GUID # value = 6496783a-3c94-44e9-ad7d-c7f72c3cee83
PrecastRecessAttributeSandwichWall_TypeUUID: GUID # value = 50ddce5d-ef2a-4d66-a364-faf2acbab37c
PrecastRecessAttributeSolidWall_TypeUUID: GUID # value = d37d662b-6afb-4062-98ba-db895f0e185e
PrecastRecessAttributeThermoWall_TypeUUID: GUID # value = 84270316-803c-4558-936f-fe8940726499
PrecastRecessAttribute_TypeUUID: GUID # value = e1fcf8ea-bc9a-431b-93df-f18e0365c8d9
PrecastReinforcementAttribute_TypeUUID: GUID # value = 3c06cc4e-702f-49f4-9844-223906443717
PrecastReinforcementBricksWall_TypeUUID: GUID # value = 2ec2deb9-3580-45b9-bdcb-9e186706296a
PrecastReinforcementCompositeFormworkWall_TypeUUID: GUID # value = 72be7547-a151-422c-b5c5-683f90374fd3
PrecastReinforcementDoubleWall_TypeUUID: GUID # value = 6243ce15-b069-44a3-bf02-2a90d2d846a1
PrecastReinforcementGroup_TypeUUID: GUID # value = 8c91fac0-b3fd-4d02-88fe-c7e496c9b14a
PrecastReinforcementNLayersWall_TypeUUID: GUID # value = ce656191-6c0c-4bd3-907d-3724a0196aa2
PrecastReinforcementSandwichWall_TypeUUID: GUID # value = 4486192c-d313-440a-a9ca-996dfeabd4a7
PrecastReinforcementSolidWall_TypeUUID: GUID # value = 11a0bcfe-b5b6-429a-ba88-b32ae57dd5d9
PrecastReinforcementThermoWall_TypeUUID: GUID # value = a3e49416-b709-416a-a577-91bf234e91bd
PrecastSingleAxis_TypeUUID: GUID # value = ad19fd2e-ebfc-4ad5-a2a9-0c8ac1f1baab
PrecastSlabMandatoryDivision_TypeUUID: GUID # value = 5c48aa87-bf4e-4947-8639-3bcc5a524426
PrecastSlabPlacementPolygon_TypeUUID: GUID # value = e081053f-f4fc-4d0c-aad3-67a5f66dbb5b
PrecastSlabPlacement_TypeUUID: GUID # value = 6b7c14fd-2f5e-4999-88ef-3bb765910072
PrecastSlabRecessRepresentation_TypeUUID: GUID # value = 85110529-173e-4278-bf64-52ce7bc46a57
PrecastSlabRecess_TypeUUID: GUID # value = ae55755f-de44-41c0-95a0-376f8c5b0ba3
PrecastSlabSupport_TypeUUID: GUID # value = 67e4aa5d-08e3-4b0f-8aa7-c299b1b19f12
PrecastSolidFloor_TypeUUID: GUID # value = cea0a9d3-76dc-4b94-ad49-df2adee10fe8
PrecastSolidWall_TypeUUID: GUID # value = e74aec23-c46f-43b5-9b7e-a7914ba7128b
PrecastSpecialLoadSmartSymbolDefinition_TypeUUID: GUID # value = d8717b50-af03-44be-9dbc-7c031cb77e65
PrecastSpecialLoad_TypeUUID: GUID # value = 51f777c1-754d-4509-9b9f-f41ac6ca566b
PrecastStaticSupportLine_TypeUUID: GUID # value = b6e39601-1eb3-4b39-bc06-95358bbed308
PrecastStaticSupport_TypeUUID: GUID # value = d4e889fd-df2f-411c-b628-0d2614def9a2
PrecastText_TypeUUID: GUID # value = a8c099ae-06ee-4f6a-9a97-1c4a732e200d
PrecastVisibleSideSymbol_TypeUUID: GUID # value = 3533af87-1254-42f2-aae5-96dd339b8dbe
PrecastWallConnector_TypeUUID: GUID # value = 11ba8641-5718-45c5-8d2b-514f0e4eae57
PrecastWallDesign_TypeUUID: GUID # value = 99ae0df6-c471-4153-abe0-4cc15232281e
PrecastWallElementTier_TypeUUID: GUID # value = 9fcbcdb9-d558-4d18-88bf-6249d616271c
PrecastWallManagerElement_TypeUUID: GUID # value = 7443be7f-cf3c-4da2-ae51-948bf1c14e52
PrecastWallPanelElementTier_TypeUUID: GUID # value = f170c9a1-2ccb-452b-8012-b6602a945b15
PrecastWallPanelElement_TypeUUID: GUID # value = bfa544e3-9ef1-40c5-82f3-8936294459ee
PrecastWallPanel_TypeUUID: GUID # value = 26e01494-277e-4b76-8809-f6317323e97c
ProfileWallTier_TypeUUID: GUID # value = 099b8ba3-a56a-4ed8-94eb-82b35f49890f
ProfileWall_TypeUUID: GUID # value = 1bfffcaf-c2cc-4250-a8ab-3ed7cadfadb4
ProxyObject_TypeUUID: GUID # value = 3df6b6cb-32e0-4c8b-84e9-c7b153702948
Purlin_TypeUUID: GUID # value = 18941632-f9c3-456a-8eff-a298d02ebfdb
PythonPartGroup_TypeUUID: GUID # value = 16be81ab-98cb-4f84-bd11-0be5eb2dfd73
PythonPart_TypeUUID: GUID # value = 40ea8f00-1fa8-406f-9f88-7b48d87e9dce
RabbetComposite_TypeUUID: GUID # value = 984716f5-9b9f-416c-a19d-ad5698a613fa
Rabbet_TypeUUID: GUID # value = 2c9e7741-ffbc-4c14-9128-765346782592
RadiusDimension_TypeUUID: GUID # value = 7d08d8af-646a-477f-9b3a-70285b20a848
RafterPlaced_TypeUUID: GUID # value = d91eb280-fc67-43cb-80ee-74041946bd36
RafterPurlin_TypeUUID: GUID # value = 85028cff-e1af-4929-ade9-e3f08db26614
Rafter_TypeUUID: GUID # value = 1ea7d460-1927-476a-9d1c-5c72b582ae02
RailSmartSymbol_TypeUUID: GUID # value = 235a2ec4-912f-481a-a861-e95850cbac1a
Rail_TypeUUID: GUID # value = e86333d6-df79-4227-ae05-79dd55b1b30e
RecessReveal_TypeUUID: GUID # value = 02963d77-984d-4b08-9ddc-e06e319dac50
RecessSmartSymbol_TypeUUID: GUID # value = 8b9830cf-37a8-4ee4-800c-d3fca7aa2660
RecessTier_TypeUUID: GUID # value = b7c929c3-fc6b-4bc5-8931-000e19e3e8ef
Recess_TypeUUID: GUID # value = 29dac2a0-d39e-401f-b233-5c7848ae73ce
ReferenceSurface_TypeUUID: GUID # value = 04b9a96f-72cc-4d00-8b42-97d152b80aaf
ReinforcementExtrudeRebarAlongPath: GUID # value = 95285021-f9e2-406f-aa2b-be6f728d77c3
ReinforcementFFUnit_TypeUUID: GUID # value = 81d152f8-abec-400f-b76a-4ae3c625bc22
ReinforcementGroup_TypeUUID: GUID # value = 99aa716f-2174-421d-8e42-f9395ed7b72d
ReinforcementPlaceBarsAlongSurface_TypeUUID: GUID # value = ce90c1cb-c19d-4faf-9a02-086f48159044
ReinforcementRobotSmartPart_TypeUUID: GUID # value = 68b93fe6-387e-4d79-bb49-d958b05bf78e
ReinforcementStampPoint_TypeUUID: GUID # value = df2c62f2-106a-4586-8ea4-22682a8e45a3
ReinforcementStructuralStarterBars_TypeUUID: GUID # value = 5bd2dcc5-1d2e-4ade-961f-b42a17c37a93
ReinforcementSweepBarsAlongPath: GUID # value = ecac8fb4-a848-4201-9bac-71ce9601dd3e
RevisionCloud_TypeUUID: GUID # value = d67dc8f6-fe4a-4dca-a8e9-43e8be0145ed
RollerBlind_TypeUUID: GUID # value = 84cb3842-5ad9-4cb3-9c5f-be49985d4a5b
RoofCovering_TypeUUID: GUID # value = f3e61354-9373-46d4-86d5-006499b66cb1
RoofFrame_TypeUUID: GUID # value = bdbf0f1a-ea96-4d7d-9ce7-d93d4294fd8a
RoofSurfaceContour_TypeUUID: GUID # value = 00a5b5ab-8fc2-4bae-b744-c9735ce3d30f
RoofSurface_TypeUUID: GUID # value = c2ff7440-8a55-4dd7-8156-40656964d7f1
RoofWindowSmartPart_TypeUUID: GUID # value = 74912b3b-eccf-464b-a80e-de94174bdb8a
RoomGroup_TypeUUID: GUID # value = aa6b1b41-c9ab-48d5-b175-dc81d1642413
RoomOccupancy_TypeUUID: GUID # value = e378553f-777c-40c0-b4e4-7e0756aafba9
Room_TypeUUID: GUID # value = bc38ee7e-2ee2-49aa-a931-c15f7364a934
SAAP_ElevationDimension_TypeUUID: GUID # value = b7211ab2-61f6-430b-a6bc-e1cc25d3ada8
ScanelementColor_TypeUUID: GUID # value = 60d18d70-6147-482e-a28c-11778177f9b9
ScanelementMono_TypeUUID: GUID # value = 3242dbda-fb53-428f-acb2-3ec3fe341165
SecondaryReinforcementGroup_TypeUUID: GUID # value = ca1c70d6-a158-42b7-a6d0-afd6deffe473
SectionAlongPath_TypeUUID: GUID # value = 9ae597f7-3d7b-43a9-9b24-89a5d4dcb20e
SectionPathStationing_TypeUUID: GUID # value = 4c903449-8274-41da-9d39-28499d2a610d
SectionPath_TypeUUID: GUID # value = 911b09ed-fb99-4352-aa14-d76644604e8f
SillBothSides_TypeUUID: GUID # value = f8b0c9dc-092d-4b4d-a3d0-d3d41fe8445c
SillSmartPart_TypeUUID: GUID # value = 9b51506d-2b20-4703-961c-a9490ffb725b
Sill_TypeUUID: GUID # value = fceba8f3-58b9-486c-a1e7-2862fe0b06fe
SkeletonAxis_TypeUUID: GUID # value = fe1247bf-f5f8-41d2-93c5-b7dfc6f0d693
SkeletonBeamSystem_TypeUUID: GUID # value = d2a95d93-f7f7-42d0-b5bb-32c7b25bf030
SkeletonBeam_TypeUUID: GUID # value = 53808df6-89e0-427e-81d6-1bd662823db1
SkeletonBrace_TypeUUID: GUID # value = 00251c83-2ecf-407b-a972-38d668f3385a
SkeletonColumn_TypeUUID: GUID # value = 12680299-3f43-4eb3-921d-76d4cddec6ae
SkeletonGrid_TypeUUID: GUID # value = 0956939c-d16a-4db8-a3d2-7ed7fb9edbb3
SkeletonPortalFrameStructure_TypeUUID: GUID # value = ec994b3d-05e1-4707-9787-1d0b5a9d090f
SkeletonPortalFrame_TypeUUID: GUID # value = 90b89593-8ade-455c-ac5a-937362d93764
SkeletonPurlinSystem_TypeUUID: GUID # value = c051bf5b-38d2-463e-af5a-54a7ec1fbc22
SkeletonPurlin_TypeUUID: GUID # value = e7daffe0-ec29-4689-8c55-98e64b16a833
SkeletonSolidElementSystem_TypeUUID: GUID # value = 6b37f919-1aae-4995-b576-5a5dd6377b62
SkylightSmartSymbol_TypeUUID: GUID # value = 9d65b823-3656-4c6d-bb08-20cd291499b5
Skylight_TypeUUID: GUID # value = 509194f6-f46e-4993-b589-f07254feb9b7
SlabFoundationTier_TypeUUID: GUID # value = 4e86608e-5017-468b-b423-ec09485c2f14
SlabFoundation_TypeUUID: GUID # value = 4799fbff-5587-447b-85d4-33cc8f485549
SlabOpeningSmartSymbol_TypeUUID: GUID # value = e634c583-9dea-4594-8eaf-5066d076877d
SlabOpening_TypeUUID: GUID # value = 2d9bf5e1-471e-460f-afd8-64dfe898a7c4
SlabRecessSmartSymbol_TypeUUID: GUID # value = 35d17ff6-3bd9-40bb-9a7f-f161103153f8
SlabRecess_TypeUUID: GUID # value = 4c812b70-0e87-4d78-a572-f1f7d7b4ee0b
Slab_TypeUUID: GUID # value = 48722469-d049-4617-b171-4286eb0037c5
Slope_TypeUUID: GUID # value = 99664d7f-904d-4ba4-a2b8-4428c211021f
SmartFit2D_TypeUUID: GUID # value = cff6444b-8194-4b58-b1be-19df42dedfab
SmartPartGroup_TypeUUID: GUID # value = a9c921bd-c4a0-4646-96ab-62a5447df482
SmartPart_TypeUUID: GUID # value = c306c684-2018-4df3-a486-c7c37dfd390e
SmartSymbolDefinition_TypeUUID: GUID # value = aafd70ae-3651-475e-ba95-cec3968b9f17
SmartSymbolElementGroup_TypeUUID: GUID # value = 2501651b-1173-4415-baed-503fc6f42e09
SmartSymbolFoil_TypeUUID: GUID # value = 182b3856-469f-4215-b4ee-e239af85d0ac
SmartSymbol_TypeUUID: GUID # value = 574034e5-0389-40d5-8791-894fc0df010f
SolarScreenSmartPart_TypeUUID: GUID # value = 19a6b889-81e1-4991-813a-de1cf50d4523
Sphere3D_TypeUUID: GUID # value = 12680299-3f43-4eb3-921d-76d46341c6ae
Spline2D_TypeUUID: GUID # value = 5314de8e-138c-4c13-875b-7080b43c507a
Spline3D_TypeUUID: GUID # value = ae9f4867-e81b-41d5-804c-f28acdaf4045
SplineDimension_TypeUUID: GUID # value = ab587f06-433d-49f4-8b1e-b5a1419c5896
StairModeler_TypeUUID: GUID # value = 9f1a757f-015e-406d-b8be-95e961148959
StairsDirectionSymbol_TypeUUID: GUID # value = 2034cd7d-ae93-48bb-adb6-7edf71bdd905
StairsDoubleQuarterLanding_TypeUUID: GUID # value = 891da53c-a3ea-48f0-a403-c4656f84127b
StairsDoubleQuarterTurn_TypeUUID: GUID # value = ed2f6dda-be82-455d-b1ba-befd5bbfea84
StairsElementContainer_TypeUUID: GUID # value = 727365f1-05c3-4d6f-aaf2-25eae32dbce4
StairsElement_TypeUUID: GUID # value = 4b23633a-469a-4389-ae24-0acd2cd4ea93
StairsHalfTurn_TypeUUID: GUID # value = 121dda9f-9340-4618-86bd-49e8232d5674
StairsQuarterLanding_TypeUUID: GUID # value = cd43a649-cb3f-4168-a7f1-d604720d8bba
StairsSpiral_TypeUUID: GUID # value = 2869ef38-4c91-4de7-814c-d47d1d40e480
StairsStraightFlight_TypeUUID: GUID # value = c0fce142-4b03-41e9-a948-aed507f04209
StairsTripleQuarterTurn_TypeUUID: GUID # value = 3859eeab-5c58-4c94-9a68-e2aaffec7341
StairsUType_TypeUUID: GUID # value = d4b08575-66df-4856-82b6-d3f302f833c3
StairsWinder_TypeUUID: GUID # value = b3397252-ea44-435c-81d3-d5364f73e2bb
Stairs_TypeUUID: GUID # value = 44b56108-62c2-4a39-a6ae-a2eacc52d898
StoreyGroup_TypeUUID: GUID # value = 7f2f2240-a596-4726-ae07-a5f2185445eb
Storey_TypeUUID: GUID # value = a3a7a87c-9521-43c9-9ae3-be2aacc9ef65
StripFoundation_TypeUUID: GUID # value = 54b5a44e-7bcd-4b69-811c-3bf3c5a5ece6
SubCeilingSystem_TypeUUID: GUID # value = 81633e57-77e3-48e4-94aa-08cafb6c00e1
SubFacade_TypeUUID: GUID # value = 60963deb-d845-40f7-aaa8-bdfe3135718c
SubOpeningPartDoor_TypeUUID: GUID # value = 900a565d-793f-478f-ae3a-4446b1894de2
SubOpeningPartWindow_TypeUUID: GUID # value = 5a919942-6aa2-4c43-abc8-c961d0f79a84
SubOpeningPart_TypeUUID: GUID # value = b511a298-4256-4a9c-a4d9-89785f06cc72
SubPipeBundle_TypeUUID: GUID # value = ebf26d02-55ac-4057-94e1-4fdc76910c12
SubPipeWork_TypeUUID: GUID # value = b262fdae-7819-4d21-8db4-584f25cf8a7d
SubPythonPart_TypeUUID: GUID # value = 8046d496-61dd-403c-a4d6-4f30587bcf8a
SubRail_TypeUUID: GUID # value = 85b2ee5b-cbe0-4ae4-aeb0-4a3050ade537
SubSmartPart_TypeUUID: GUID # value = 54ae4b0e-8be2-4ffe-abb2-25a27f030db5
SurfaceObject_TypeUUID: GUID # value = 559df84e-bd5a-4e9c-9bd1-51c3a8d68133
SurveyPoint_TypeUUID: GUID # value = 2cc4de1e-7d9a-422c-8f87-03170b5e11f5
TentRoofFrame_TypeUUID: GUID # value = 41ff8483-b052-4d93-8bed-df0c56acf646
TentRoofPlane_TypeUUID: GUID # value = 549961af-7650-443c-8cc4-8e6b99fabd31
TextBlock_TypeUUID: GUID # value = 702d2e64-e2eb-4433-a165-30c754506b2e
TextPointer_TypeUUID: GUID # value = 8e121682-04be-4ce1-b8d2-8a87b38aa099
Timber_TypeUUID: GUID # value = 3b5ba25a-e635-4d4e-b398-3e246fcf64fc
UVSClippingPathSymbol_TypeUUID: GUID # value = 605ee794-0fad-4791-aa94-5ca61ea1bdd0
UVSLabeling_TypeUUID: GUID # value = f9f320d3-f9bb-4db6-95cb-db92f8744d2c
Undefined_TypeUUID: GUID # value = 4a1aa685-4a12-4908-b35e-8b917e513ce5
UnifiedSection_TypeUUID: GUID # value = f7efa1a6-918b-4b5b-a4e5-1f6b4cd04904
UnifiedView_TypeUUID: GUID # value = 7e57b57c-8364-4d89-84ee-f344a25c2d62
Upstand_TypeUUID: GUID # value = 4d4755f4-9e3e-479a-bf5d-95eb40ce36eb
UrbanPlanningBuilding_TypeUUID: GUID # value = bdb5626f-0406-49d0-bb94-bc0017b6128f
UrbanPlanningDrawingBaseboard_TypeUUID: GUID # value = d1c1ccaf-4f52-4cf6-b957-8feb4318d672
UrbanPlanningDrawingFloorSurface_TypeUUID: GUID # value = f4d8128e-dd9d-445f-9899-4837174731c1
UrbanPlanningDrawingObject_TypeUUID: GUID # value = 62ef3af2-c9b0-44ae-9f70-333c05a2859a
UrbanPlanningPlotFloorSurface_TypeUUID: GUID # value = 69e83efa-27b6-4e8a-90c5-3816081c6c53
UrbanPlanningSpacingArea_TypeUUID: GUID # value = bd621486-dba9-4e16-a6ce-e34d933a60bc
UserDefinedSolidOpening_TypeUUID: GUID # value = b4c5f81a-0f28-4587-a9e8-839385915f21
UserDefinedSolid_TypeUUID: GUID # value = 55062743-c900-468d-8b3d-43da24fd3da7
ValleyRafter_TypeUUID: GUID # value = 971a6c41-7f2f-4bc2-b2bc-68e9bdcaf203
VerticalSurface_TypeUUID: GUID # value = 2f6a8803-cf48-4566-8575-81ca1395530d
Volume3D_TypeUUID: GUID # value = fe417b11-20d2-4b3b-8fa7-03e9ad743b21
WallAxisArc_TypeUUID: GUID # value = ce672cfc-d48a-4eab-916d-517416ebd82e
WallAxisChain_TypeUUID: GUID # value = 66dab4d9-d913-413e-a700-6b9581be65b5
WallAxisClothoid_TypeUUID: GUID # value = 85ba3521-e2ea-45c8-827a-882b01c38543
WallAxisLine_TypeUUID: GUID # value = c177d94b-4121-4a20-b70c-da7baed2fe12
WallAxisPolyline_TypeUUID: GUID # value = c270fcaa-50b2-40c3-a8fb-b412002eb44f
WallAxisSpline_TypeUUID: GUID # value = 812d57cb-ecf2-4ddc-bde4-b09d88a93c8a
WallAxis_TypeUUID: GUID # value = b7b85ac6-3b03-4b81-a353-153216f8ae4d
WallInfraction_TypeUUID: GUID # value = 6390a5be-f41b-4cc0-a72c-6102f775c2c0
WallTier_TypeUUID: GUID # value = a7fae808-845c-4491-9f44-3757c493e673
Wall_TypeUUID: GUID # value = ec7f50b0-1a27-49d6-b6a2-007b854513c7
WindowDoorReveal_TypeUUID: GUID # value = 0c263cc4-4ede-415c-b3ea-f114d92b6cb1
WindowDoorTier_TypeUUID: GUID # value = f31e3225-5679-4ed8-855a-8952029ce751
WindowDoor_TypeUUID: GUID # value = 8cec1045-4d53-4058-a897-aca6635e1ce3
WindowOpeningSmartPart_TypeUUID: GUID # value = 4da7c6fa-69e7-4ae4-8264-c937bf053e75
WindowOpeningSmartSymbol_TypeUUID: GUID # value = 2aaaab30-0459-47d7-8233-7c97936ec4d4
WindowReveal_TypeUUID: GUID # value = 62c499a2-3179-4ca5-942b-60233db816c1
WindowTier_TypeUUID: GUID # value = 9f99d406-ad3f-4d92-a85d-15b7751270b1
Window_TypeUUID: GUID # value = 3bed6979-9374-4f66-8d6c-75560064d997
XRefDocumentClipped_TypeUUID: GUID # value = 8fcfcd08-e00f-4fbc-a696-cf7ad5edb16d
XRefDocumentEmbedded_TypeUUID: GUID # value = 76113e2e-5db4-48a1-81f5-4703a6d55118
XRefDocument_TypeUUID: GUID # value = c67e81af-1cd3-42ba-bafb-980574b12bc8
XRefFreeDocumentClipped_TypeUUID: GUID # value = 2d799dfa-5d0e-46be-8e2b-fb11ad9bc817
XRefFreeDocumentEmbedded_TypeUUID: GUID # value = fd96de6c-9e83-4d6a-a072-5578738804eb
XRefFreeDocument_TypeUUID: GUID # value = 0d1d0bae-df24-4852-9440-db00b8972408
ZoomWindow_TypeUUID: GUID # value = 70f4262b-5b75-47b3-92aa-61b7585f5cea

```