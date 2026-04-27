---
title: "AttributeIdEnums"
source: "PythonPartsFramework\GeneralScripts\Utilities\AttributeIdEnums.py"
type: "class"
category: "02_API_Referenz"
tags:
  - script
  - utility
related:
  -
last_updated: "2026-02-20"
---


# AttributeIdEnums

> **Pfad:** `PythonPartsFramework\GeneralScripts\Utilities\AttributeIdEnums.py`  
> **Typ:** Klasse/Modul  
> **Tags:** `script`, `utility`

## Übersicht

implementation of the attribute enumerations

## Abhängigkeiten

- `enum`

## Klassen

### `AttributeIdEnums`

implementation of the attribute enumerations
    

#### Methoden

| Methode | Parameter | Rückgabe | Beschreibung |
|---|---|---|---|
| - | - | - | - |

## Funktionen

Keine Funktionen vorhanden.

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
""" implementation of the attribute enumerations
"""

#pylint: disable=line-too-long

import enum

class AttributeIdEnums(enum.IntEnum):
    """ implementation of the attribute enumerations
    """

    PRIMARY_KEY = 1
    """ PrimaryKey (please do not rename it), type=int"""

    FILE_ID = 4
    """ File ID (drawing file number/name), type=int"""

    ALLRIGHT_COMP_ID = 10
    """ Unique component ID + file ID + component code, type=string"""

    COMPONENT_ID = 12
    """ Component ID, type=int"""

    PROJECT_STATUS = 15
    """ Project status, type=string"""

    ATTRIBUTE_VALUE = 17
    """ Attribute value - data record, type=string"""

    NAMENUMBER_OF_STAIR_COMPONENT = 18
    """ Name/number of stair component, type=int"""

    NUMBER_OF_STEP = 19
    """ Number of step, type=int"""

    USER_NAME = 20
    """ Username (login), type=string"""

    BOTANICAL_NAME = 22
    """ Bruns: botanical name, type=string"""

    PLANT_SPECIES = 23
    """ Plants: species, type=string"""

    PLANTS_SHAPE = 24
    """ Plants: shape, type=string"""

    PLANTS_GROWTH = 25
    """ Plants: growth, type=string"""

    PLANTS_QUALITY = 26
    """ Plants: quality, type=string"""

    BRUNS_PRICE = 27
    """ Plants: price, type=float """

    PLANT_GROUP = 28
    """ Plant group, type=string"""

    PLANTS_GERMAN_NAME = 29
    """ Plants: German name, type=string"""

    PLANTS_MATCH_CODE = 30
    """ Plants: match code, type=string"""

    DIAMETER_OF_TRUNK = 31
    """ Diameter of trunk, type=float """

    DIAMETER_OF_TOP = 32
    """ Diameter of top, type=float """

    RETAIN = 33
    """ retain, type=float """

    PLANT = 34
    """ plant, type=float """

    CLEAR = 35
    """ fell/clear, type=float """

    BRUNS_PRICE_FOR_TEN_OR_MORE_PLANTS = 36
    """ Plants: price for ten or more pieces, type=float """

    BRUNS_PRICE_FOR_50_OR_MORE_PLANTS = 37
    """ Plants: price for 50 or more pieces, type=float """

    AGE = 40
    """ Age, type=int"""

    VITALITY = 41
    """ Vitality, type=string"""

    DATE_ADDED = 42
    """ Date added, type=float """

    HIGHLIGHT = 43
    """ Marking type, type=int"""

    SOLID_2D_INTERACTION = 45
    """ Solids 2D interaction, type=int"""

    NBS_REFERENCE_DESCRIPTION = 46
    """ Categorization - NBS Reference Description, type=string"""

    CSI_MASTER_FORMAT_CODE = 47
    """ Classification - CSI MasterFormat Code, type=string"""

    CSI_MASTER_FORMAT_TITLE = 48
    """ classification - CSI MasterFormat Title, type=string"""

    STATUS = 49
    """ IFC: Status, type=string"""

    IN_HIERARCHY = 53
    """ Level 1 in hierarchy, type=int"""

    PARTIAL_AREA_FORMAT = 54
    """ Returns user-defined format string for reports, type=string"""

    CSI_UNI_FORMAT_II_CODE = 56
    """ Categorization - CSI UniFormat II Code, type=string"""

    CSI_UNI_FORMAT_II_TITLE = 57
    """ Categorization - CSI UniFormat II Title, type=string"""

    BIMPLUS_LAYER = 67
    """ BimPlus Layer (Discipline), type=string"""

    FLOOR_AREA = 68
    """ Floor area depending on current setting, type=float """

    E_MAIL = 69
    """ Office: email address, type=string"""

    LOGO = 70
    """ Company logo: default in $ETC/Allplan_Logo_204_77.png, type=string"""

    INHERITANCE = 72

    UNIT_1 = 73

    REVEAL_DEPTH = 74
    """ Reveal depth, type=float """

    CALCULATION_RULE = 75
    """ Calculation rule, type=string"""

    OBJECT_FILTER = 76
    """ Object filter, type=string"""

    FILTER_BY_SURROUNDING_ELEMENTS_SUBTR = 77
    """ Filters by surrounding elements to be subtracted, type=string"""

    FORMWORK_AREA = 78
    """ Formwork area, type=float """

    REVEAL_ANALYSIS = 79
    """ Reveal analysis, type=int"""

    VOB_LENGTH = 80
    """ Trade-dependent length calculation, type=float """

    VOB_AREA = 81
    """ Trade-dependent area calculation, type=float """

    VOB_VOLUME = 82
    """ Trade-dependent volume calculation, type=float """

    CODE_TEXT = 83
    """ Code text for TAI program assignment, type=string"""

    COLUMN_PROJECTING = 84
    """ Projecting column, type=string"""

    COLUMN_FLUSH_WITH_WALL = 85
    """ Column flush with wall, type=int"""

    VOLUME_DIN277 = 86
    """ Volume in accordance with DIN277, type=float """

    SVG_MAP = 87
    """ SVG map: 2D geodetic info, type=string"""

    NUMBER_OF_RISER = 88
    """ Stair: number of rises, type=int"""

    RISE = 89
    """ Stair: rise, type=float """

    TREAD_LENGTH = 90
    """ Stair: tread run, type=float """

    NUMBER_INSIDE_CORNERS = 91
    """ Number of inside corners, type=int"""

    NUMBER_OUTSIDE_CORNERS = 92
    """ Number of outside corners, type=int"""

    BASE_AREA_ACCORDING_TO_DIN277 = 93
    """ Base area in accordance with DIN277, type=float """

    DYN_UNIT_PRICE = 95
    """ Dynamic unit price, type=string"""

    DYN_MATERIAL = 96
    """ Dynamic material, type=string"""

    BOTTOM = 97
    """ Bottom level of component, type=float """

    COMPONENT_TOP_LEVEL = 98
    """ Top level of component, type=float """

    NET_QUANTITY = 99
    """ Net quantity, type=float """

    VOB_QUANTITY = 100
    """ VOB qantity, type=float """

    RADIUS = 107
    """ Radius, type=float """

    PRIORITY = 110
    """ Priority, type=int"""

    BOTTOM_LEVEL = 112
    """ Applied to openings, this attribute returns the offset to the bottom level of the wall; otherwise, this attribute returns the bottom level, type=float """

    TOP_LEVEL = 113
    """ Top level, type=float """

    CALCULATION_MODE = 120
    """ Calculation mode, type=int"""

    RISE_TOP = 127
    """ Rise at top, type=float """

    RISE_BOTTOM = 129
    """ Rise at bottom, type=float """

    OFFSET_LEFT = 131
    """ Offset on the right, type=float """

    OFFSET_RIGHT = 132
    """ Offset on the left, type=float """

    LAYER = 141
    """ Layer, type=int"""

    X_COORDINATE = 163
    """ x-coordinate, type=float """

    Y_COORDINATE = 164
    """ y-coordinate, type=float """

    Z_COORDINATE = 165
    """ z-coordinate, type=float """

    OFFSET_TOP = 167
    """ Offset at the top, type=float """

    COMPONENT_DEPTH = 179
    """ Component depth, type=float """

    FLOOR_AREA_LESS_PERCENTAGE = 193
    """ Floor area (unfinished dimensions including amount to subtract), type=float """

    MARK_NUMBER = 194
    """ Mark number, type=int"""

    CATALOG_BRANCH = 195
    """ Catalog branch, type=string"""

    FLOOR_AREA_UNFINISHED_DIMENSIONS = 196
    """ Floor area (unfinished dimensions), type=float """

    FLOOR_AREA_FINISHED_DIMENSIONS = 197
    """ Floor area (finished dimensions), type=float """

    ABSOLUTE_LENGTH = 198
    """ Absolute length, type=float """

    ABSOLUTE_THICKNESS = 199
    """ Absolute thickness, type=float """

    QUANTITY = 201
    """ Quantity, type=float """

    UNIT = 202
    """ Unit, type=string"""

    UNIT_PRICE = 203
    """ Unit price, type=float """

    ABSOLUTE_HEIGHT = 204
    """ Maximum height of architectural components, type=float """

    SEQUENCE_NUMBER = 206
    """ Serial number, type=int"""

    SHORT_TEXT = 207
    """ Short text, type=string"""

    FULL_TEXT = 208
    """ Full text, type=string"""

    TRADE = 209
    """ Trade, type=string"""

    LAYER_NUMBER = 210
    """ Layer number, type=int"""

    LAYER_THICKNESS = 211
    """ Layer thickness, type=float """

    REVEAL_AREA = 212
    """ Reveal on the inside; analysis: reveal area, type=float """

    REVEAL_LENGTH = 213
    """ Reveal on the outside; analysis: reveal length, type=float """

    ARCHITECTURAL_COMPONENT = 214
    """ Architectural component number, type=string"""

    PIECE = 215
    """ Piece, type=int"""

    V6 = 216
    """ V6 - V9 --&gt; smart symbol, type=float """

    V7 = 217
    """ V6 - V9 --&gt; smart symbol, type=float """

    V8 = 218
    """ V6 - V9 --&gt; smart symbol, type=float """

    V9 = 219
    """ V6 - V9 --&gt; smart symbol, type=float """

    LENGTH = 220
    """ Length, type=float """

    THICKNESS = 221
    """ Thickness, type=float """

    HEIGHT = 222
    """ Mean height (volume, base area), type=float """

    VOLUME = 223
    """ Volume, type=float """

    BASE_AREA = 224
    """ Base area, type=float """

    DIMENSIONS = 225
    """ Dimensions, type=string"""

    NET_VOLUME = 226
    """ Net volume, type=float """

    LESS_VOLUME = 227
    """ Volume to be subtracted, type=float """

    PERIMETER = 228
    """ Perimeter, type=float """

    AREA = 229
    """ Area, type=float """

    FACTOR = 230
    """ Factor, type=float """

    ROOM_ENCLOSURE = 231
    """ DIN277: room enclosure, type=string"""

    AREA_TYPE_277 = 232
    """ DIN277: area type, type=string"""

    AREA_TYPE_FLOOR_SPACE = 233
    """ Area type: floor area, type=int"""

    BAU_NVO_FA = 234
    """ BauNVO: story included in calculation of base area, type=int"""

    OCCUPANCY_TYPE_DIN277 = 235
    """ DIN277: occupancy type, type=string"""

    LOCAL_CODE_ROOM_NAME = 236
    """ Local code: room name, type=string"""

    LOCAL_CODE_SUBROOM_NUMBER = 237
    """ Local code: number of subroom, type=string"""

    CONCRETING_SECTION = 238
    """ Concreting section, type=int"""

    INITIALCLOSING_FORM = 239
    """ Formwork closer, type=string"""

    LONG_NAME_FOR_FORMWORK = 240
    """ Full name of formwork, type=string"""

    ARTICLE_NUMBER = 241
    """ Article number, type=string"""

    EFA = 242
    """ DIN277: EFA, type=float """

    ERC = 243
    """ DIN277: ERC, type=float """

    DIN277_GROSS_FLOOR_AREA = 244
    """ DIN277: GFA, type=float """

    DIN277_GROSS_ROOM_VOLUME = 245
    """ DIN277: GRV, type=float """

    LOCAL_CODE_STORY_NAME = 246
    """ Local code: story name, type=string"""

    LOCAL_CODE_SUBSTORY_NUMBER = 247
    """ Local code: substory number, type=string"""

    DIN277_NET_ROOM_AREA = 248
    """ DIN277_2016: net room area, type=float """

    DIN277_NET_ROOM_VOLUME = 249
    """ DIN277: NRV, type=float """

    BAU_NVO_FS = 250
    """ BauNVO: story included in calculation of story area, type=int"""

    SPACE_BELOW_STAIRS_FLR_SPC_ONLY_GT_2M = 251
    """ Space below stair included in floor area &gt; 2.0 m, type=int"""

    FACTOR_FLOOR_AREA_ROOM = 264
    """ Room factor: floor area, type=float """

    FACTOR_277 = 266
    """ DIN277: factor 277, type=float """

    OFFSET_TO_PARAPET = 269
    """ Smart window sill symbols: offset to parapet, type=float """

    RADIUS_FLUE = 270
    """ Diameter of flue 1, type=float """

    FLUE_WIDTH = 271
    """ Width of flue 1, type=float """

    FLUE_THICKNESS = 272
    """ Thickness of flue 1, type=float """

    RADIUS_FLUE2 = 273
    """ Diameter of flue 2, type=float """

    WIDTH_FLUE2 = 274
    """ Width of flue 2, type=float """

    THICKNESS_FLUE2 = 275
    """ Thickness of flue 2, type=float """

    WIDTH_VENTSTACK = 276
    """ Width of ventilation stack 1, type=float """

    DEPTH_VENTSTACK = 277
    """ Thickness of ventilation stack 1, type=float """

    WIDTH_VENTSTACK2 = 278
    """ Width of ventilation stack 2, type=float """

    THICKNESS_VENTSTACK2 = 279
    """ Thickness of ventilation stack 2, type=float """

    INVENTORY_NUMBER_FORMWORK = 281
    """ Inventory number of formwork element, type=string"""

    FORMWORK_ELEMENT_WEIGHT = 282
    """ Weight of formwork element, type=float """

    FORMWORK_ELEMENT_AREA = 283
    """ Area of formwork element, type=float """

    FORMWORK_ELEMENT_VALUE_NEW = 284
    """ New value of formwork element, type=float """

    SUPPLEMENT_FOR_FWK_ELEMENT = 285
    """ Supplement for formwork element, type=float """

    NOTE_FOR_FORMWORK_ELEMENT = 286
    """ Note for formwork element, type=string"""

    ELEMENT_GROUP_FORMWORK = 287
    """ Element group for formwork element, type=int"""

    NUMBER_IN_ELEMENT_PLAN = 288
    """ Number in element plan, type=int"""

    COUNTRY = 289
    """ Project attribute: country, type=string"""

    STATE = 290
    """ Project attribute: state, type=string"""

    COST_GROUP_II = 291
    """ Cost group of level 2, type=string"""

    COST_GROUP_III = 292
    """ Cost group of level 3, type=string"""

    FLOOR_SURFACE = 293
    """ Floor surface, type=float """

    CEILING_SURFACE = 294
    """ Ceiling surface, type=float """

    VERTICAL_SURFACE = 295
    """ Vertical surface, type=float """

    MEAN_AREA = 296
    """ Mean area, type=float """

    PRICE_FACTOR = 297
    """ DIN276: price factor, type=float """

    ALLFA_COST_CENTER_ABBR__PATH_NAME = 301
    """ Allfa cost center (abbreviated path name), type=string"""

    TELEPHONE_NUMBER = 302
    """ Telephone number, type=string"""

    ALLFA__ORGANIZAT__UNITABBR__PATH_NAME = 303
    """ Allfa organizational unit: abbreviated path name, type=string"""

    EMPLOYEE_NAME = 304
    """ Employee name, type=string"""

    PERSONNEL_NUMBER = 305
    """ Personnel number, type=string"""

    ALLFA_ORGANIZATION_ABBR__NAME = 306
    """ Allfa organization (abbreviated name), type=string"""

    OBJECT_NUMBER = 307
    """ Object number, type=string"""

    ALLFA_POSITION_NAME = 308
    """ Allfa position (description), type=string"""

    ALLFA_OCCUPANCY_NAME = 315
    """ Allfa occupancy (description), type=string"""

    ALLFA_CLEANING_CATEGORY_SHORT_DES__PATH = 316
    """ Allfa cleaning category: abbreviated path name, type=string"""

    ALLFA_ORGANIZATION_NAME = 317
    """ Allfa organization (description), type=string"""

    ALLFA_ORGANIZATIONAL_UNIT_NAME = 318
    """ Allfa organizational unit (description), type=string"""

    ALLFA_POSITION_ABBR__NAME = 319
    """ Allfa position (abbreviated name), type=string"""

    ALLFA_EQUIPMENT_ABBR__NAME = 320
    """ Allfa equipment: abbreviated name, type=string"""

    ALLFA_COST_CENTER_NAME = 321
    """ Allfa cost center (name), type=string"""

    ALLFA_OCCUPANCY_ABBR__PATH_NAME = 322
    """ Allfa occupancy type: abbreviated path name, type=string"""

    ALLFA_ARTICLE_ABBR__PATH_NAME = 324
    """ Allfa article: abbreviated path name, type=string"""

    ALLFA_ROOM_NAME = 327
    """ Allfa room (description), type=string"""

    RIDGE_LENGTH = 340
    """ Ridge length, type=float """

    ARRIS_LENGTH = 341
    """ Arris length, type=float """

    VALLEY_LENGTH = 342
    """ Valley length, type=float """

    EAVES_LENGTH = 343
    """ Eaves length, type=float """

    VERGE_LENGTH = 344
    """ Verge length, type=float """

    SMART_SYMBOL_HAS_A_TIMBER_FRAME = 358
    """ Smart symbol designer: smart symbol with wooden frame, type=int"""

    BIT_SEQUENCE_LEAF_DINLEFT__DINRIGHT = 363
    """ Smart symbol designer: bit flags, leaf DINleft, type=int"""

    FRAME_POSITION = 366
    """ Smart symbol designer: position of frame, type=int"""

    ALLFA_CLEANING_CATEGORY_NAME = 367
    """ Allfa cleaning category (description), type=string"""

    PROJECT_AVAILABILITY = 368
    """ Project availability, type=string"""

    NOTE_GENERAL = 372

    CHECKER_NAME = 374
    """ Person who checks the layout, type=string"""

    LAYOUT_FORMAT = 375

    SCALE = 376

    FILE_NAME_SYMBOL = 378
    """ Name of symbol file, type=string"""

    NEXT__NAME_SYMBOL = 379
    """ Symbol name, type=string"""

    POSITION_INSIDEOUTSIDE = 384
    """ Window sill: on the inside or outside, type=int"""

    SPLAY = 385
    """ Window sill: splay, type=float """

    APPROVAL_DATE = 386
    """ Release date, type=float """

    CHECKER_DATE = 387
    """ Release date, type=float """

    CHECKER_NOTE = 388
    """ Checker, type=string"""

    INDEX = 389
    """ Layout index, type=string"""

    BLDG_PROPOSAL_COSTS_PER_M3 = 394
    """ Building cost per m3, type=float """

    CHECKED_BY = 395
    """ Person who checks the layout, type=string"""

    INDEX_CREATED_BY = 396
    """ Person who edits the layout, type=string"""

    INDEX_DATE = 397
    """ Date of change, type=float """

    PERFORMANCE_PLANNING_STAGE = 398
    """ Service phase, planning phase, type=string"""

    CITY_STREET = 399
    """ City and street, type=string"""

    CONSTRUCTION_STAGE = 400
    """ Construction stage, type=string"""

    CURRENT_DATE = 401
    """ Current date, type=float """

    CURRENT_TIME = 402
    """ Current time, type=string"""

    COMPUTER = 403
    """ Computer name, type=string"""

    CURRENCY = 404
    """ Current currency, type=string"""

    PROJECT_NAME = 405
    """ Project name, type=string"""

    BLDG_PROPOSAL_STRUCTURE = 406
    """ Cost of unfinished structure for lists in building proposal, type=float """

    BLDG_PROPOSAL_FINISHING_COSTS = 407
    """ Cost of finished structure for lists in building proposal, type=float """

    FILESET_NUMBER = 408
    """ Fileset number, type=string"""

    FILESET_NAME = 409
    """ Fileset name, type=string"""

    OFFICE_NAME = 410
    """ Customer name, lines 1 - 2, type=string"""

    OFFICE_ADDRESS = 411
    """ Customer name, lines 1 - 2, type=string"""

    ENGINEERING_PROJECT = 413
    """ Engineering project, type=string"""

    CONTRACT_SECTION = 414
    """ Lot, type=string"""

    LAYOUT_VERSION = 415
    """ Layout version, type=string"""

    FILE_NAME = 416
    """ File name, type=string"""

    SEQUENCE_NAME = 417
    """ Sequence name, type=string"""

    SL_CONSTRUCTION_PROJECT = 418
    """ Construction project, type=string"""

    COMPONENT = 419
    """ Component, type=string"""

    STEEL_LIST_NUMBER = 420
    """ Steel list number as saved in drawing file header , type=string"""

    NAME_OF_CROSS_SECTION_CATALOG = 421
    """ Name of cross-section catalog, type=string"""

    STEEL_GRADE_OF_CROSS_SECTION_CATALOG = 422
    """ Steel grade of cross-section catalog, type=string"""

    NUMBER_OF_TIMES = 423
    """ Number of instances, type=int"""

    STEEL_STRENGTH_CATEGORY = 424
    """ Steel strength class, type=string"""

    DRAWING_FILE_NAME = 425
    """ Drawing file name, type=string"""

    INDEX_TYPE = 426

    DOOR_SWING = 427
    """ Direction of door swing, type=string"""

    APPROVAL_NAME = 428
    """ Approval name, type=string"""

    FILE_SIZE = 429
    """ Size plus unit (character), type=string"""

    HIERARCHIC_CODE = 430
    """ Hierarchical code, type=string"""

    OWNER = 431
    """ Owner, type=string"""

    CREATED_ON = 432
    """ Date of creation, type=float """

    DATE_OF_CHANGE = 433
    """ Date of change, type=float """

    DISPLAY_MODE = 434
    """ Display mode, type=float """

    INDEX_OLD = 435
    """ Layout index in V2011 and earlier versions, type=string"""

    FILE_SIZE_BYTES = 436
    """ File size in bytes, type=int"""

    HIDDENSECTION = 437
    """ Hidden/section, type=string"""

    LAYOUT_TYPE = 438
    """ Layout type, type=string"""

    LAYOUT_DESCRIPTION = 439
    """ Layout description, type=string"""

    NUMBER_CHANGES = 440
    """
, type=int"""

    WRITE_PERMISSION = 441
    """ Write permission, type=string"""

    LAYOUT_RELEASE_DATE = 443
    """ Release date, type=float """

    CHECKER = 444
    """ Checker, type=string"""

    LAYOUT_NAME = 445
    """ Full layout name, type=string"""

    LAYOUT_NUMBER = 446
    """ Layout number, type=int"""

    INDEX_NOTE = 447
    """ Change notice, type=string"""

    REFERENCE_SCALE = 448
    """ Reference scale, type=float """

    RELEASE = 449
    """ Program version, release, type=string"""

    TOPOLOGY_STRUCTURE = 450
    """ Building topology, structure, type=string"""

    TOPOLOGY_BUILDING = 451
    """ Building topology, building, type=string"""

    TOPOLOGY_STORY = 452
    """ Building topology, floor level, type=string"""

    TOPOLOGY_ROOM = 453
    """ Topology, room, type=string"""

    SELECTION_CONDITION_5 = 454
    """ Selection condition 5, type=string"""

    SELECTION_CONDITION_6 = 455
    """ Selection condition 6, type=string"""

    SELECTION_CONDITION_7 = 456
    """ Selection condition 7, type=string"""

    SELECTION_CONDITION_8 = 457
    """ Selection condition 8, type=string"""

    SELECTION_CONDITION_9 = 458
    """ Selection condition 9, type=string"""

    SELECTION_CONDITION_10 = 459
    """ Selection condition 10, type=string"""

    CLIENT = 460
    """ Client, type=string"""

    OCCUPANTS = 461
    """ Occupant, type=string"""

    BUILDING_TYPE = 462
    """ Building type, type=string"""

    TYPE_OF_CONSTRUCTION_LOAD_BEARING_STRUCTURE = 463
    """ Type of construction, load-bearing structure, type=string"""

    CONSTRUCTION_VOLUME = 464
    """ Project attribute: construction volume in €, type=string"""

    GROSS_FLOOR_AREA = 465
    """ Project attribute: gross floor area, type=string"""

    FLOOR_AREA_RATIO = 466
    """ Project attribute: floor area ratio, type=string"""

    USABLE_FLOOR_AREA = 467
    """ Project attribute: usable floor area, type=string"""

    NO__OF_FLOOR_LEVELS = 468
    """ Project attribute: number of floor levels, type=string"""

    NO__OF_RESIDENTIAL_UNITS = 469
    """ Project attribute: number of residential units, type=string"""

    RESIDENTIAL_BUILDING_DEVELOPMENT = 470
    """ Residential building development, type=string"""

    OFFICE_SPACE = 471
    """ Office space, type=string"""

    OFFICE_DEVELOPMENT = 472
    """ Office development, type=string"""

    YEAR_OF_COMPLETION = 473
    """ Year of completion, type=string"""

    LOCATION_PLOT = 474
    """ Location, plot, type=string"""

    AUTHORIZING_AGENCY = 475
    """ Approving authority, type=string"""

    DATE_APPROVED = 476
    """ Date of approval, type=string"""

    LOT = 477
    """ Lot, type=string"""

    PROJECT_MANAGER = 478
    """ Project manager, type=string"""

    ARCHITECT = 479
    """ Architect, type=string"""

    STRUCTURAL_ANALYSIS = 480
    """ Structural analysis, type=string"""

    LAYOUT_CREATED_BY = 481
    """ Person who creates the layout, type=string"""

    ELECTRICAL_INSTALLATION = 482
    """ Electrical installations, type=string"""

    HEATING = 483
    """ Heating, type=string"""

    VENTILATION = 484
    """ Ventilation, type=string"""

    SANITARY_FACILITIES = 485
    """ Sanitary facilities, type=string"""

    BUILDING_PHYSICS = 486
    """ Building physics, type=string"""

    ARCHITECTURAL_ACOUSTICS = 487
    """ Architectural acoustics, type=string"""

    OPEN_AREA_PLANNING = 488
    """ Open area planning, type=string"""

    INFRASTRUCTURE_PLANNING = 489
    """ Infrastructure planning, type=string"""

    INTERIOR_DESIGN = 490
    """ Interior design, type=string"""

    CONSTRUCTION_SUPERVISION = 491
    """ Construction supervision, type=string"""

    PROJECT_MANAGEMENT = 492
    """ Project management, type=string"""

    COST_CONTROL = 493
    """ Cost controlling, type=string"""

    PRECAST_FACTORY = 494
    """ Precast factory, type=string"""

    SHORT_NAME_FOR_STEEL_GRADE = 495
    """ Steel grade, short name, type=string"""

    NO__OF_CROSS_SECTION_CATALOG = 496
    """ Number of cross-section catalog, type=int"""

    LESS_PERCENTAGE_FLOOR_AREA = 497
    """ Former floor area factor; percentage to be subtracted from floor area , type=int"""

    OBJECT_NAME = 498
    """ Object name, type=string"""

    PAGE_NUMBER = 499
    """ Page, type=int"""

    BLDG_PROPOSAL_PLOT_AREA = 500
    """ Plot area for lists in building proposal, type=float """

    TEXT1 = 501
    """ Text1, type=string"""

    TEXT2 = 502
    """ Text2, type=string"""

    TEXT3 = 503
    """ Text3, type=string"""

    TEXT4 = 504
    """ Text4, type=string"""

    TEXT5 = 505
    """ Text5, type=string"""

    FUNCTION = 506
    """ Function, type=string"""

    NAME = 507
    """ Name, type=string"""

    MATERIAL = 508
    """ Material, type=string"""

    FILE_NUMBER_IDAT = 511
    """ File number (idat), type=int"""

    DRAWING_FILE_NUMBER_ITBNR = 512
    """ File number (itbnr), type=int"""

    REINFORCEMENT_PERCENTAGE = 514
    """ Reinforcement percentage, type=float """

    SEGMENT_NUMBER = 515
    """ Segment number, type=int"""

    DOCUMENT_UUID = 523
    """ UUID of document, layout or project   , type=string"""

    LINE_NUMBER = 532
    """ Table analysis, type=int"""

    PLUGIN_NAME = 538
    """ Plugin name, type=string"""

    PLUGIN_OBJECT_NAME = 539
    """ Plugin object name, type=string"""

    BUILDABLE_AREA = 548
    """ Project attribute: area available for building, type=string"""

    MAXIMUM_BUILDING_HEIGHT = 549
    """ Project attribute: maximum building height, type=string"""

    GROSS_PLOT_AREA = 550
    """ Project attribute: gross plot area, type=string"""

    CODE_OCCUPANCY = 551
    """ Urban planning: land-use type, type=string"""

    BUILDING_METHOD = 552
    """ Urban planning: construction method, type=string"""

    MAX__SITE_AREA_RATIO = 553
    """ Urban planning: maximum site area ratio, type=float """

    NUMBER_OF_PLOT = 554
    """ Urban planning: plot number, type=string"""

    MAX__SITE_OCCUPANCY_INDEX = 555
    """ Urban planning: maximum site occupancy index, type=float """

    MIN__FLOOR_AREA_RATIO = 556
    """ Urban planning: minimum floor area ratio, type=float """

    MAX__FLOOR_AREA_RATIO = 557
    """ Urban planning: maximum floor area ratio, type=float """

    MIN__NO__OF_FULL_STORIES = 558
    """ Urban planning: minimum number of full stories, type=string"""

    MAX__NO__OF_FULL_STORIES = 559
    """ Urban planning: maximum number of full stories, type=string"""

    ROOF_PITCH_AND_SHAPE = 560
    """ Urban planning: roof pitch and roof shape, type=string"""

    DRAWING_SYMBOL_GROUP = 561
    """ Urban planning: drawing symbol group, type=string"""

    DRAWING_SYMBOL_REGULATIONS = 562
    """ Drawing symbol, type=string"""

    LEGAL_BASIS_FOR_GROUP = 563
    """ Legal basis for drawing symbol group, type=string"""

    LEGAL_BASIS_FOR_REGULATION = 564
    """ Legal basis for drawing symbol regulations, type=string"""

    NUMBER_OF_FULL_STORIES = 565
    """ Number of full stories, type=float """

    BUILDING_STORY_SAFA = 566
    """ Urban planning: consider floor area ratio and site occupancy index (yes, no), type=string"""

    NUMBER_OF_RESIDENTIAL_UNITS = 567
    """ Number of residential units, type=int"""

    NUMBER_OF_TOP_FLOORS = 568
    """ Number of upper floors, type=int"""

    PARKING_SPACE_FOR_N_CARS = 569
    """ Parking space for n cars, type=int"""

    ARCHITECTURE_MATERIAL = 570
    """ Architectural material, type=string"""

    STRUCTURAL_ANALYSIS_MATERIAL = 571
    """ Structural analysis material, type=string"""

    LOAD_BEARING = 573
    """ Structural behavior, , BuildingSmart: load bearing, type=int"""

    BUILDING_PHYSICS_MATERIAL = 574
    """ Building physics material , type=string"""

    PRODUCTION_TYPE = 575
    """ Production type, type=string"""

    MEAN_SEA_LEVEL = 585
    """ Project attribute: heights above mean sea level, type=string"""

    TOPOLOGY_SITE = 586
    """ Building topology, site, type=string"""

    TOPOLOGY_STORY_REGION = 587
    """ Building topology, substory, type=string"""

    TOPOLOGY_ANY_STRUCTURAL_LEVEL = 588
    """ Building topology, any structural level, type=string"""

    TOPOLOGY_ENTIRE_HIERARCHY = 589
    """ Building topology, entire hierarchy including all nodes, type=string"""

    NUMBER_OF_INTERSECTED_TILES = 590
    """ Smart fit: number of intersected tiles, type=int"""

    NUMBER_OF_WHOLE_TILES = 591
    """ Smart fit: number of whole tiles, type=int"""

    SURFACE_COMPRISED_BY_INTERSECTED_TILES = 592
    """ Smart fit: area covered by intersected tiles, type=float """

    SURFACE_COMPRISED_BY_WHOLE_TILES = 593
    """ Smart fit: area covered by whole tiles, type=float """

    TOTAL_PRICE = 594
    """ Total price, type=float """

    LEFT_HAUNCH = 595
    """ Foundations, left haunch, type=float """

    RIGHT_HAUNCH = 596
    """ Foundations, right haunch, type=float """

    FRONT_HAUNCH = 597
    """ Foundations, front haunch, type=float """

    REAR_HAUNCH = 598
    """ Rear haunch, type=float """

    VTB_INFO = 599
    """ VTB 19, type=float """

    STEPCHAMFER_WIDTH = 601
    """ Foundations, width of step chamfer, type=float """

    STEPCHAMFER_HEIGHT = 602
    """ Foundations, height of step chamfer, type=float """

    STEP_BOUNCE = 603
    """ Foundations, step chamfer, type=float """

    STEPCHAMFER_ECCENTRICITY = 605
    """ Foundations, eccentricity of step chamfer, type=float """

    CENTER_OF_GRAVITY_X = 612
    """ X center of gravity, type=float """

    CENTER_OF_GRAVITY_Y = 613
    """ Y center of gravity, type=float """

    CENTER_OF_GRAVITY_Z = 614
    """ Z center of gravity, type=float """

    DEFAULT_PLANE_BL = 615
    """ Bottom level of default plane, type=float """

    DEFAULT_PLANE_TL = 616
    """ Top level of default plane, type=float """

    NOI_ID = 617
    """ NOI ID , type=string"""

    IS_EXTERNAL = 618
    """ Classification -&gt; Ifc exterior component, type=string"""

    GLASS_TYPE = 619
    """ Glass type, type=string"""

    SHADING_COEFFICIENT = 620
    """ Shading Coefficient, type=int"""

    GLAZING_AREA_FRACTION_CONSIDER = 621
    """ Consider GlazingAreaFraction for Smt reports, type=int"""

    ABSORPTION_COEFFICIENT_HEAT_INSIDE = 622
    """ Absorption coefficient of heat, inside, type=float """

    ABSORPTION_COEFFICIENT_HEAT_OUTSIDE = 623
    """ Absorption coefficient of heat, outside, type=float """

    TEMPERATURE = 624
    """ Temperature, type=float """

    ROOM_ZONE_ACC__TO_DIN_18599 = 625
    """ Room zone (in accordance with DIN 18599), type=string"""

    LIGHT_REFLECTION_COEFFICIENT_OF_CEILING = 626
    """ Light reflection coefficient, type=float """

    GROUND = 645
    """ Ground, type=int"""

    LAMBDA_VALUE = 657
    """ Lambda value (thermal conductivity nominal value λ), type=float """

    IFC_ID = 683
    """ IFC ID, type=string"""

    IFC_ENTITY = 684
    """ IFC object type, type=string"""

    ASSIGNMENT_TO_FIRE_COMPARTMENT = 685
    """ Assignment to fire compartment, type=string"""

    RAFTER_PARAMETERS = 689

    SWITCH_B_IS_FS = 690

    SWITCH_TF_IS_FS = 691

    MIN_HEIGHT_SO_THAT_FS = 692

    HEIGHT_ABOVE_TERRAIN_SO_THAT_B_IS_FS = 693

    BUILDING_ID = 696
    """ Project attribute: building ID, type=string"""

    PRODUCT_MANUFACTURER = 708
    """ MEP: manufactrurer, type=string"""

    WEIGHT = 721
    """ Weight, type=float """

    SURFACE = 722
    """ Surface, type=float """

    BAR_LENGTH_BS_8666 = 740
    """ Bending dimensions (length of each bar) BS 8666:2005, type=int"""

    BENDING_DIMENSIONS_BS_86662005_A_E = 741
    """ Bending dimensions (a, type=int"""

    DEFAULT_PATH_FOLDER = 742
    """ Main nodes of the Allplan default paths (etc,std,...), type=string"""

    LAYOUT_STRUCTURE_ENTIRE_HIERARCHY = 743
    """ Entire layout structure, type=string"""

    LAYOUT_STRUCTURE_SUPERORDINATE_NODE = 744
    """ Superordinate node of the layout structure, type=string"""

    PROJECT_TEMPLATE = 747
    """ Type of project template, type=string"""

    SCHEDULE_OUTPUT___GROSS_WEIGHTNET_WEIGHT = 750
    """ Gross weight and net weight, type=string"""

    MESH_NAME = 751
    """ Mesh identifier, type=string"""

    LONGITUDINAL_CONCRETE_OVERLAP_M = 752
    """ Longitudinal mesh overlap, type=int"""

    TRANSVERSE_CONCRETE_OVERLAP_M = 753
    """ Transverse mesh overlap, type=int"""

    MAX__LONGITUDINAL_AS = 754
    """ Maximum value for As longitudinal, type=float """

    MAX__TRANSVERSE_AS = 755
    """ Maximum value for As transverse, type=float """

    WEIGHT_OF_MESHBAR = 756
    """ Weight of one mesh or bar, type=float """

    MESH_OR_BAR_LENGTH_SINGLE = 757
    """ Length of one mesh or bar, type=float """

    WIDTH = 758
    """ Width, type=float """

    DIAMETER = 759
    """ Diameter, type=float """

    TOTAL_LENGTH = 760
    """ Total length [m], type=float """

    COMMENT_ON_BAR_X_SECTION_CATALOG = 761
    """ Comment on bar cross-section catalog, type=string"""

    BENDING_DIMENSIONS_ISO_4066_A_E = 762
    """ Bending dimensions (a, type=int"""

    BAR_SHAPE_KEY_ISO_4066 = 763
    """ Bar shape key ISO4066, type=string"""

    TYPE = 764
    """ Type, type=string"""

    TOTAL_WEIGHT = 765
    """ Total weight, type=float """

    NO__OF_WWMREINFORCING_BARS = 766
    """ Number of meshes or reinforcing bars, type=int"""

    WWMREINF__BAR_MARKS = 767
    """ Mark number of meshes or reinforcing bars, type=int"""

    BAR_SPACING___LONGITUDINAL_MM = 768
    """ Bar spacing, longitudinal, type=float """

    BAR_SPACING___TRANSVERSE_MM = 769
    """ Bar spacing, transverse, type=float """

    INSIDE_DIA__DS1_LONGITUDINAL = 770
    """ Inside diameter ds1 longitudinal, type=float """

    INSIDE_DIA__DS3_TRANSVERSE = 771
    """ Inside diameter ds3 transverse, type=float """

    DM_EDGE_DS2_LONGIT = 772
    """ Edge diameter ds2 longitudinal, type=float """

    EDGE_DIAMETER_DS4_TRANSVERSE = 773
    """ Edge diameter ds4 transverse, type=float """

    NUMBER___LEFT_EDGE_NL = 774
    """ Number of bars, left edge nl, type=int"""

    NUMBER___RIGHT_EDGE_NR = 775
    """ Number of bars, right edge nr, type=int"""

    NUMBER___START_EDGE_MA = 776
    """ Number of bars, start edge ma, type=int"""

    NUMBER___END_EDGE_ME = 777
    """ Number of bars, end edge me, type=int"""

    DS1_DOUBLE_BAR_OR_SECONDARY = 778
    """ Double bar char*1 "d" only for ds1, type=string"""

    EXCESS___START_OF_MESH_UE1 = 779
    """ Projection at start Ue1, type=float """

    EXCESS___END_OF_MESH_UE2 = 780
    """ Projection at end Ue2, type=float """

    EXCESS___LEFT_UE3 = 781
    """ Projection on the left Ue3, type=float """

    EXCESS___RIGHT_UE4 = 782
    """ Projection on the right Ue4, type=float """

    OFFSET_SHORT_BARS_AK = 783
    """ Length as far as short bar ak, type=float """

    LENGTH_OF_SHORT_BARS_LK = 784
    """ Length of short bar lk, type=float """

    DIAMETERMESH_NAME = 785
    """ Diameter, mesh identifier, type=string"""

    BAR_SHAPE_BS_8666 = 786
    """ Bar shape key BS 8666, type=string"""

    MESH_SHAPE = 787
    """ Mesh shape, planar or bent, type=int"""

    VERSION = 789
    """ Version, type=string"""

    MARK_SPACING_M = 790
    """ Mark spacing [m]- string, type=string"""

    MARK_SPACING_CM = 791
    """ Mark spacing [cm] - string, type=string"""

    FILTER_BY_REINF__PLACED_POLYGONALLY = 792
    """ Filter by reinforcement placed polygonally, type=int"""

    FILTER_BY_REINF__BAR_ELE = 793
    """ Filter by bar reinforcement, type=int"""

    MARK_NUMBER_WITH_INDEX_MESHESBARS = 795
    """ Mark number with index (meshes, bars), type=string"""

    LENGTH_CM_METERAGE = 796
    """ Length [cm] (per meter) - string, type=string"""

    LENGTH_M_METERAGE = 797
    """ Length [m] (per meter) - string, type=string"""

    VARIABLE_LENGTH_A_B_C___ = 798
    """ Variable length (a b c ...), type=int"""

    STRAIGHTBENT_UP_BARS = 799
    """ Bars, straight or bent, type=int"""

    POINT_NUMBER = 800
    """ Point number, type=int"""

    REFERENCE_HEIGHT = 801
    """ Reference height, type=float """

    DELTA_HEIGHT = 802
    """ Delta height, type=float """

    PRISM_NUMBER = 803
    """ Prism number, type=int"""

    POINT_NUMBER_2 = 804
    """ Point number 2, type=int"""

    POINT_NUMBER_3 = 805
    """ Point number 3, type=int"""

    AVERAGE_HEIGHT = 806
    """ Mean height, type=float """

    ANALYSIS = 807
    """ Analysis, type=string"""

    QUESTION_1 = 808
    """ Fixture question 1, type=string"""

    QUESTION_2 = 809
    """ Fixture question 2, type=string"""

    QUESTION_3 = 810
    """ Fixture question 3, type=string"""

    QUESTION_4 = 811
    """ Fixture question 4, type=string"""

    QUESTION_5 = 812
    """ Fixture question 5, type=string"""

    ANSWER_1 = 813
    """ Fixture answer 1, type=string"""

    ANSWER_2 = 814
    """ Fixture answer 2, type=string"""

    ANSWER_3 = 815
    """ Fixture answer 3, type=string"""

    ANSWER_4 = 816
    """ Fixture answer 4, type=string"""

    ANSWER_5 = 817
    """ Fixture answer 5, type=string"""

    FIXTURE_UNIT_1 = 818
    """ Fixture unit 1, type=string"""

    FIXTURE_UNIT_2 = 819
    """ Fixture unit 2, type=string"""

    FIXTURE_UNIT_3 = 820
    """ Fixture unit 3, type=string"""

    FIXTURE_UNIT_4 = 821
    """ Fixture unit 4, type=string"""

    FIXTURE_UNIT_5 = 822
    """ Fixture unit 5, type=string"""

    PLAN_TEXT = 823
    """ EB plan text, type=string"""

    CONTRACT_NUMBER = 824
    """ Contract number, type=string"""

    CONTRACTING_AUTHORITY = 825
    """ Contracting authority, type=string"""

    CONSTRUCTION_PROJECT = 826
    """ Construction project, type=string"""

    CONSTRUCTION_SITE = 827
    """ Construction site, type=string"""

    EDITED_BY = 828
    """ Person who edits the layout, type=string"""

    SLAB_OVER = 829
    """ Precast slab over, type=string"""

    PROJECT_LAYOUT_NUMBER = 830
    """ Layout number, type=string"""

    DELIVERY_ADDRESS = 831
    """ Delivery address, type=string"""

    DELIVERY_STREET = 832
    """ Delivery street, type=string"""

    DELIVERY_ZIP_CODECITY = 833
    """ Delivery ZIP code/city, type=string"""

    INVOICE_ADDRESS = 834
    """ Invoice address, type=string"""

    INVOICE_STREET = 835
    """ Invoice street, type=string"""

    BUILDING_CONTRACTOR_ADDRESS = 836
    """ Building contractor, address, type=string"""

    BUILDING_CONTRACTOR_STREET = 837
    """ Building contractor, street, type=string"""

    BUILDING_CONTRACTOR_ZIP_CODECITY = 838
    """ Building contractor, ZIP code/city, type=string"""

    CLIENT_ADDRESS = 839
    """ Client, address, type=string"""

    CLIENT_STREET = 840
    """ Client, street, type=string"""

    CLIENT_ZIP_CODECITY = 841
    """ Client, ZIP code/city, type=string"""

    INVOICE_ZIP_CODECITY = 842
    """ Invoice, ZIP code/city, type=string"""

    ALLFA_VALUE_01 = 843
    """ ALLFA: value 01, type=string"""

    ALLFA_VALUE_02 = 844
    """ ALLFA: value 02, type=string"""

    ALLFA_VALUE_03 = 845
    """ ALLFA: value 03, type=string"""

    ALLFA_VALUE_04 = 846
    """ ALLFA: value 04, type=string"""

    ALLFA_VALUE_05 = 847
    """ ALLFA: value 05, type=string"""

    ALLFA_VALUE_06 = 848
    """ ALLFA: value 06, type=string"""

    ALLFA_VALUE_07 = 849
    """ ALLFA: value 07, type=string"""

    ALLFA_VALUE_08 = 850
    """ ALLFA: value 08, type=string"""

    ALLFA_VALUE_09 = 851
    """ ALLFA: value 09, type=string"""

    ALLFA_VALUE_10 = 852
    """ ALLFA: value10, type=string"""

    ALLFA_VALUE_11 = 853
    """ ALLFA: value 11, type=string"""

    ALLFA_VALUE_12 = 854
    """ ALLFA: value 12, type=string"""

    ALLFA_VALUE_13 = 855
    """ ALLFA: value 13, type=string"""

    ALLFA_VALUE_14 = 856
    """ ALLFA: value 14, type=string"""

    ALLFA_VALUE_15 = 857
    """ ALLFA: value 15, type=string"""

    ALLFA_VALUE_16 = 858
    """ ALLFA: value 16, type=string"""

    ALLFA_VALUE_17 = 859
    """ ALLFA: value 17, type=string"""

    ALLFA_VALUE_18 = 860
    """ ALLFA: value 18, type=string"""

    ALLFA_VALUE_19 = 861
    """ ALLFA: value 19, type=string"""

    ALLFA_VALUE_20 = 862
    """ ALLFA: value 20, type=string"""

    ALLFA_FEATURE_01 = 863
    """ ALLFA: attribute 01, type=string"""

    ALLFA_FEATURE_02 = 864
    """ ALLFA: attribute 02, type=string"""

    ALLFA_FEATURE_03 = 865
    """ ALLFA: attribute 03, type=string"""

    ALLFA_FEATURE_04 = 866
    """ ALLFA: attribute 04, type=string"""

    ALLFA_FEATURE_05 = 867
    """ ALLFA: attribute 05, type=string"""

    ALLFA_FEATURE_06 = 868
    """ ALLFA: attribute 06, type=string"""

    ALLFA_FEATURE_07 = 869
    """ ALLFA: attribute 07, type=string"""

    ALLFA_FEATURE_08 = 870
    """ ALLFA: attribute 08, type=string"""

    ALLFA_FEATURE_09 = 871
    """ ALLFA: attribute 09, type=string"""

    ALLFA_FEATURE_10 = 872
    """ ALLFA: attribute 10, type=string"""

    ALLFA_FEATURE_11 = 873
    """ ALLFA: attribute 11, type=string"""

    ALLFA_FEATURE_12 = 874
    """ ALLFA: attribute 12, type=string"""

    ALLFA_FEATURE_13 = 875
    """ ALLFA: attribute 13, type=string"""

    ALLFA_FEATURE_14 = 876
    """ ALLFA: attribute 14, type=string"""

    ALLFA_FEATURE_15 = 877
    """ ALLFA: attribute 15, type=string"""

    ALLFA_FEATURE_16 = 878
    """ ALLFA: attribute 16, type=string"""

    ALLFA_FEATURE_17 = 879
    """ ALLFA: attribute 17, type=string"""

    ALLFA_FEATURE_18 = 880
    """ ALLFA: attribute 18, type=string"""

    ALLFA_FEATURE_19 = 881
    """ ALLFA: attribute 19, type=string"""

    ALLFA_FEATURE_20 = 882
    """ ALLFA: attribute 20, type=string"""

    CHANGE_PARAMETERS = 883
    """ Attributes of structural bearings, type=float """

    CLASS_NO_ = 885
    """ Fixtures, class number, type=string"""

    STATION = 894
    """ Station, type=float """

    OFFSET_DTM = 895
    """ Offset, type=float """

    BULK_DENSITY = 897
    """ Bulk density, type=float """

    DELIVERY_UNIT_STATUS = 902
    """ Delivery unit status, type=int"""

    MARK_NUMBER_OF_PRECAST_ELEMENT = 903
    """ Mark number of precast element, type=int"""

    SLOPE = 909
    """ Slope, type=float """

    CUSTOMER_STREET = 910
    """ Customer, street, type=string"""

    CUSTOMER_ZIP_CODECITY = 911
    """ Customer, ZIP code/city, type=string"""

    ORDERER_ADDRESS = 912
    """ Orderer, address, type=string"""

    ORDERER_STREET = 913
    """ Orderer, street, type=string"""

    ORDERER_ZIP_CODECITY = 914
    """ Orderer, ZIP code/city, type=string"""

    CHECKING_STRUCTURAL_ENGINEER_ADDRESS = 915
    """ Structural inspection engineer, address, type=string"""

    CHECKING_STRUCTURAL_ENGINEER_STREET = 916
    """ Structural inspection engineer, street, type=string"""

    CHECKING_STRUCTURAL_ENGINEER_ZIP_CODECITY = 917
    """ Structural inspection engineer, ZIP code/city, type=string"""

    ARCHITECT_ADDRESS = 918
    """ Architect, address, type=string"""

    ARCHITECT_STREET = 919
    """ Architect, street, type=string"""

    ARCHITECT_ZIP_CODECITY = 920
    """ Architect, ZIP code/city, type=string"""

    ADDRESS_OF_CONSTRUCTION_PROJECT = 921
    """ Construction project, address, type=string"""

    CONSTRUCTION_PROJECT_STREET = 922
    """ Construction project, street, type=string"""

    CONSTRUCTION_PROJECT_ZIP_CODECITY = 923
    """ Construction project, ZIP code/city, type=string"""

    LAYOUTS = 924
    """ Layouts, type=string"""

    CALCULATION_STANDARD = 925
    """ Calculation standard, type=string"""

    SERVICE_CENTER = 926
    """ Service center, type=string"""

    MOUNTING_HOOKS = 927
    """ Mounting anchors, type=string"""

    STORAGE = 928
    """ Storage type, type=string"""

    PRODUCTION_PLANT = 929
    """ Production plant, type=string"""

    DELIVERY_YEAR = 930
    """ Delivery year, type=string"""

    DELIVERY_WEEK = 931
    """ Delivery week, type=string"""

    PRECAST_ELEMENT_TYPE = 932
    """ Element type of precast element, type=string"""

    FIRE_RATING = 935
    """ Fire rating, type=string"""

    PROJECT_NUMBER = 936
    """ Project number, type=string"""

    SALES_ORGANIZATION = 937
    """ Sales organization, type=string"""

    SALES_CHANNEL = 938
    """ Sales channel, type=string"""

    DELIVERY_CONDITIONS = 939
    """ Delivery conditions, type=string"""

    CLERK_TELEPHONE_NUMBER = 940
    """ Clerk, telephone number, type=string"""

    CUSTOMER_TELEPHONE_NUMBER = 941
    """ Customer, telephone number, type=string"""

    CUSTOMER_FAX_NUMBER = 942
    """ Customer, fax number, type=string"""

    CUSTOMER_NUMBER = 943
    """ Customer, number, type=string"""

    ORDERER_TELEPHONE_NUMBER = 944
    """ Customer, telephone number, type=string"""

    ORDERER_FAX_NUMBER = 945
    """ Orderer, fax number, type=string"""

    CHECKING_STRUCTURAL_ENGINEER_TELEPHONE_NUMBER = 946
    """ Structural inspection engineer, telephone number, type=string"""

    CHECKING_STRUCTURAL_ENGINEER_FAX_NUMBER = 947
    """ Structural inspection engineer, fax number, type=string"""

    STRUCTURAL_ENGINEER_NAME = 948
    """ Structural engineer, name, type=string"""

    STRUCTURAL_ENGINEER_ADDRESS = 949
    """ Structural engineer, address, type=string"""

    STRUCTURAL_ENGINEER_ZIP_CODECITY = 950
    """ Structural engineer, ZIP code/city, type=string"""

    STRUCTURAL_ENGINEER_TELEPHONE_NUMBER = 951
    """ Structural engineer, telephone number, type=string"""

    STRUCTURAL_ENGINEER_FAX_NUMBER = 952
    """ Structural engineer, fax number, type=string"""

    ARCHITECT_TELEPHONE_NUMBER = 953
    """ Architect, telephone number, type=string"""

    ARCHITECT_FAX_NUMBER = 954
    """ Architect, fax number, type=string"""

    BUILDING_SITE_TELEPHONE_NUMBER = 955
    """ Building site, telephone number, type=string"""

    BUILDING_SITE_FAX_NUMBER = 956
    """ Building site, fax number, type=string"""

    PHASE_NUMBER = 957
    """ Phase number, type=string"""

    PLACE_OF_MANUFACTURE = 958
    """ Place of manufacture, type=int"""

    DEAD_LOAD = 959
    """ Dead load, type=float """

    VISIBLE_SIDE = 960
    """ Visible side, type=int"""

    AREA_FACTOR = 961
    """ Area factor, type=float """

    LOAD_TRANSMISSION = 962
    """ Load transmission, type=int"""

    INSERTION_DEPTH_1 = 963
    """ Insertion depth 1, type=float """

    INSERTION_DEPTH_2 = 964
    """ Insertion depth 2, type=float """

    OFFSET_TO_OPENING = 965
    """ Offset to opening, type=float """

    LONGITUDINAL_JOINT_WIDTH = 966
    """ Longitudinal joint width, type=float """

    TRANSVERSE_JOINT_WIDTH = 967
    """ Transverse joint width, type=float """

    REVEAL_ANCHOR_TYPE = 968
    """ Reveal anchor, left (top) or right (bottom), type=int"""

    FRAME_TYPE = 969
    """ Frame type, type=int"""

    FRAME_WIDTH = 970
    """ Frame width, type=string"""

    FRAME_HEIGHT = 971
    """ Frame height, type=string"""

    SUPPORT_LENGTH_1 = 972
    """ Support length 1, type=string"""

    SUPPORT_LENGTH_2 = 973
    """ Support length 2, type=string"""

    SUPPORT_LENGTH_3 = 974
    """ Support length 3, type=string"""

    SUPPORT_LENGTH_4 = 975
    """ Support length 4, type=string"""

    FRAME_DIRECTION = 976
    """ Frame direction, type=float """

    AREA_TYPE = 980
    """ Envelope surfaces: area type, type=string"""

    THERMAL_TRANSMITTANCE = 981
    """ Envelope surfaces: U-value, type=float """

    ENVELOPE_SURFACE_NAME = 982
    """ Envelope surfaces: name, type=string"""

    ENVELOPE_SURFACE_ORIENTATION = 983
    """ Envelope surfaces: orientation, type=int"""

    ENVELOPE_SURFACE_TYPE = 984
    """ Envelope surfaces: type, type=int"""

    PROJECT = 985
    """ Envelope surfaces: project, type=string"""

    HEAT_BRIDGE = 986
    """ Envelope surfaces: heat bridge, type=int"""

    FACTOR_HEAT_REQUIREMENT = 987
    """ Envelope surfaces: factor, type=string"""

    POSITION_OF_SURFACE = 988
    """ Envelope surfaces: position, type=string"""

    COMPONENT_FILE = 989
    """ Envelope surfaces: component file, type=string"""

    INPUT_AREA = 990
    """ Envelope surfaces: input area, type=int"""

    PROJECT_DESCRIPTION = 991
    """ Project description (project attribute), type=string"""

    FACTORY = 992
    """ Factory (project attribute), type=string"""

    PART_OF_FACTORY = 993
    """ Part of factory (project attribute), type=string"""

    ALLFA_ROOM_ABBR__NAME = 994
    """ Allfa room (abbreviated name), type=string"""

    BAR_SHAPE_NEN_6146 = 996
    """ Bar shape key NEN 6146, type=int"""

    BENDING_DIMENSIONS_NEN_6146_A_F = 997
    """ Bending dimensions NEN 6146 [a-f], type=int"""

    NETHERLANDS_X1 = 998
    """ Netherlands: X1, type=int"""

    NETHERLANDS_Y1 = 999
    """ Netherlands: Y1, type=int"""

    GLASS_SURFACE = 1000
    """ Glazing area in m², type=float """

    STEEL_GRADE_OF_CROSS_SECTION_CATALOG_WITHOUT_COUPLER = 1001
    """ Steel grade of cross-section catalog without couplers, type=string"""

    COUPLER_TYPE = 1002
    """ Coupler type, type=string"""

    COUPLER_DIAMETER = 1003
    """ Coupler diameter, type=float """

    CHECK_QUESTION_1 = 1008
    """ Check fixture question 1, type=int"""

    CHECK_QUESTION_2 = 1009
    """ Check fixture question 2, type=int"""

    CHECK_QUESTION_3 = 1010
    """ Check fixture question 3, type=int"""

    CHECK_QUESTION_4 = 1011
    """ Check fixture question 4, type=int"""

    CHECK_QUESTION__5 = 1012
    """ Check fixture question 5, type=int"""

    DIMENSION_STRING_INDEX = 1013
    """ Dimension string, type=int"""

    CHAMFER___USER_ENTRY = 1014
    """ Chamfer: text for supplement, type=string"""

    PALLET_SIDE___USER_ENTRY = 1015
    """ Pallet side: text for supplement, type=string"""

    SMOOTH_FILLING_SIDE___USER_ENTRY = 1016
    """ Smooth filling side: text for supplement, type=string"""

    FILLING_SIDE_SB___USER_ENTRY = 1017
    """ Filling side SB: text for supplement, type=string"""

    STRUCTURE___USER_ENTRY = 1018
    """ Structure: text for supplement, type=string"""

    WASHED_CONCRETE___USER_ENTRY = 1019
    """ Washed concrete: text for supplement, type=string"""

    STRUCTURAL_POSITION___USER_ENTRY = 1020
    """ Structural position: text for supplement, type=string"""

    ELEMENT_NAME = 1021
    """ Element name: text for supplement, type=string"""

    FILESET_NAME___USER_ENTRY = 1022
    """ Fileset name: text for supplement, type=string"""

    PROJECT_NAME___USER_ENTRY = 1023
    """ Project name: text for supplement, type=string"""

    COMPONENT_SUPPLEMENT = 1024
    """ Component: text for supplement, type=string"""

    FILESET_NUMBER___USER_ENTRY = 1025
    """ Fileset number: text for supplement, type=string"""

    SUBTYPE = 1026
    """ Fixture subtype, type=string"""

    CUSTOMER_ADDRESS = 1029
    """ Customer address (project attribute), type=string"""

    REFERENCE_ALLFA = 1030
    """ Associated with group for Unido (Allfa), type=string"""

    EXPOSURE_CLASS = 1031
    """ Exposure class, type=string"""

    EXPOSURE_CLASS_VISIBLE = 1032
    """ Exposure class, visible, type=string"""

    EXPOSURE_CLASS_INVISIBLE = 1033
    """ Exposure class, invisible, type=string"""

    OFFSET_BOTTOM = 1035
    """ Offset at bottom, type=float """

    VARIABLE_SMART_FIXTURE_SYMBOL = 1038
    """ Variable smart fixture symbol, type=int"""

    DIMENSON_TEXT = 1040
    """ Dimenson text, type=string"""

    FF_STIRRUP_CAGES_FILTER = 1044
    """ FF stirrup cages, filter (is it a FF stirrup cage? 0/1), type=int"""

    FF_STIRRUP_CAGES_CODE = 1045
    """ FF stirrup cages, code (describing the stirrup cage, for example 2495M001/002/SC16), type=string"""

    FF_STIRRUP_CAGES_SORTING_NUMBER = 1046
    """ FF stirrup cages, sorting number = stack# * 1 000 000 000 + stack height*1 000 000 + element# *1000 + SC#, type=int"""

    FF_STIRRUP_CAGES_REINFORCEMENT_TYPE_1 = 1047
    """ FF stirrup cages, filter by stock item, type=int"""

    FF_STIRRUP_CAGES_REINFORCEMENT_TYPE_2 = 1048
    """ FF stirrup cages, filter by special reinforcement, type=int"""

    TYPE_OF_INTERSECTION = 1049
    """ Type of intersection for FF reinforcement, type=int"""

    FF_STIRRUP_CAGES_FILTER_FOR_PLACEMENT = 1050
    """ FF stirrup cages, filter by installation site = building site, type=int"""

    REINFORCEMENT_TYPE_3_FILTER = 1051
    """ Reinforcement type 3, filter: returns all bars and stirrups with the installation site = building site, type=int"""

    OFFSET_TO_BL_OF_PRECAST_ELEMENT = 1052
    """ Offset of fixture to bottom level of precast element, type=float """

    OFFSET_TO_TL_OF_PRECAST_ELEMENT = 1053
    """ Offset of fixture to top level of precast element, type=float """

    OFFSETS_TO_FF_REINFORCEMENT_COMPONENT = 1054
    """ Parts of FF reinforcement component, type=string"""

    OFFSET_TO_BL_OF_ARCHITECTURAL_COMPONENT = 1055
    """ Offset of fixture to bottom level of architectural component, type=float """

    OFFSET_TO_TL_OF_ARCHITECTURAL_COMPONENT = 1056
    """ Offset of fixture to top level of architectural component, type=float """

    FACTORY_NUMBER = 1057
    """ Factory number, type=int"""

    STEEL_WEIGHT = 1058
    """ Steel weight, type=float """

    FACING_THICKNESS_OF_VISIBLE_LEAF = 1059
    """ Facing thickness of visible leaf, type=float """

    FACING_THICKNESS_OF_INVISIBLE_LEAF = 1060
    """ Facing thickness of invisible leaf, type=float """

    CONCRETE_COVER_AT_BOTTOMINVISIBLE = 1061
    """ Concrete cover at bottom/invisible, type=float """

    CONCRETE_COVER_AT_TOPVISIBLE = 1062
    """ Concrete cover at top/visible, type=float """

    MATERIAL_OF_PRECAST_ELEMENT = 1063
    """ Material of precast element layer, type=string"""

    CONCRETE_GRADE_OF_VISIBLE_LEAF = 1064
    """ Concrete grade of visible leaf --&gt; included for compatibility reasons only! Use 3201147, type=string"""

    CONCRETE_GRADE_OF_INVISIBLE_LEAF = 1065
    """ Concrete grade of invisible leaf --&gt; included for compatibility reasons only! Use 3201147, type=string"""

    CONCRETE_GRADE_OF_VISIBLE_OUTER_LEAF = 1066
    """ Concrete grade of visible outer leaf, type=string"""

    CONCRETE_GRADE_OF_INVISIBLE_OUTER_LEAF = 1067
    """ Concrete grade of invisible outer leaf, type=string"""

    VISIBLE_SURFACE = 1068
    """ Visible surface, type=string"""

    INVISIBLE_SURFACE = 1069
    """ Invisible surface, type=string"""

    REINFORCEMENT_TYPE = 1070
    """ Reinforcement type, type=string"""

    VISIBLE_REINFORCEMENT_TYPE = 1071
    """ Visible reinforcement type, type=string"""

    INVISIBLE_REINFORCEMENT_TYPE = 1072
    """ Invisible reinforcement type, type=string"""

    ADDITIONAL_TEXT_FOR_MARK_NUMBER = 1073
    """ Additional text for mark number, type=string"""

    MRK__NO__FOR_STACK_LIST = 1074
    """ Mark number for stack list (including sign), type=int"""

    PRECAST_TYPE = 1075
    """ Type of precast element, type=string"""

    HEIGHT_OF_PRECAST_ELEMENT_IN_TRANSPORT_STACK = 1076
    """ Height of precast element in transport stack (including sign), type=int"""

    DIMENSIONS_OF_PRECAST_ELEMENT_M = 1077
    """ Dimensions of precast element [m], type=string"""

    THICKNESS_OF_PRECAST_ELEMENT_CM = 1078
    """ Thickness of precast element [cm], type=float """

    STACK_NUMBER = 1079
    """ Stack number, type=int"""

    SORTING_ID_OF_STACK_LIST = 1080
    """ Sorting ID of stack list, type=int"""

    TOTAL_WEIGHT_OF_STIRRUP_CAGE = 1081
    """ Total weight of stirrup cage, type=float """

    ELEMENT_TYPE = 1082
    """ Element type - split type of element, type=int"""

    CUSTOM_ATTRIBUTE_01 = 1083
    """ Precast elements: custom attribute 01 --&gt; included for compatibility reasons only! Use 1947!, type=string"""

    CUSTOM_ATTRIBUTE_02 = 1084
    """ Precast elements: custom attribute 02 --&gt; included for compatibility reasons only! Use 1947!, type=string"""

    CUSTOM_ATTRIBUTE_03 = 1085
    """ Precast elements: custom attribute 03 --&gt; included for compatibility reasons only! Use 1947!, type=string"""

    CUSTOM_ATTRIBUTE_04 = 1086
    """ Precast elements: custom attribute 04 --&gt; included for compatibility reasons only! Use 1947!, type=string"""

    CUSTOM_ATTRIBUTE_05 = 1087
    """ Precast elements: custom attribute 05 --&gt; included for compatibility reasons only! Use 1947!, type=string"""

    PANEL_TYPE = 1088
    """ Panel type, name or description, type=string"""

    GENERAL_CONSTRUCTION_PROJECT = 1091
    """ Construction project, general information, type=string"""

    STORY = 1092
    """ Story, type=string"""

    CONSTRUCTION_PROJECT_NAME = 1093
    """ Construction project, name, type=string"""

    CONSTRUCTION_PROJECT_ADDRESS = 1094
    """ Construction project, address, type=string"""

    ADDRESS_FOR_INVOICE = 1095
    """ Invoice address, type=string"""

    FF_STIRRUP_CAGES_INSTALLATION_WORKS = 1096
    """ Installation site = factory (1 otherwise 0), type=int"""

    FF_STIRRUP_CAGES_INSTALLATION_SITE = 1097
    """ Installation site = building site (1 otherwise 0), type=int"""

    START_OF_SHORTENING = 1098
    """ Start of shortening, type=float """

    END_OF_SHORTENING = 1099
    """ End of shortening, type=float """

    NAME_NUMBER = 1100
    """ Name, number, type=string"""

    OCCUPANCY_TYPE = 1101
    """ Occupancy type, type=string"""

    HIERARCHIC__FUNCTION = 1102
    """ Function in hierarchy, type=string"""

    PIPE_SECTION_TYPE = 1103
    """ Pipe section, type=string"""

    WIDTH_DIAMETER = 1104
    """ Width, diameter, type=float """

    CLEAR_HEIGHT = 1105
    """ Clear height of rooms (finishing surfaces being subtracted), type=float """

    START_HEIGHT = 1106
    """ Start height, type=float """

    END_HEIGHT = 1107
    """ End height, type=float """

    HEIGHT_DEFINITION = 1108
    """ Height definition, type=string"""

    LOCATION = 1109
    """ Location, type=string"""

    STATUS_CADASTRE = 1110
    """ Status, type=string"""

    YEAR_OF_CONSTRUCTION = 1111
    """ Year of construction, type=string"""

    HYDRAULIC_FUNCTION = 1112
    """ Hydraulic function, type=string"""

    CONNECTION_TYPE = 1113
    """ Connection type, type=string"""

    PROFILE_FIXTURES = 1114
    """ Profile fixtures, type=string"""

    FOUNDATION_ENVELOPE = 1115
    """ Foundation, envelope, type=string"""

    DRAINAGE_SYSTEM = 1116
    """ Drainage system, type=string"""

    INCLINATION = 1117
    """ Inclination, type=float """

    LENGTHS = 1118
    """ Effective length, type=float """

    OWNERS = 1119
    """ Owner, type=string"""

    LAST_MODIFICATION = 1120
    """ Last modification, type=string"""

    HEIGHTS = 1122
    """ Height, type=float """

    TYPE_FUNCTION = 1123
    """ Type, function, type=string"""

    DIMENSION1 = 1124
    """ Dimension 1, type=float """

    DIMENSION2 = 1125
    """ Dimension 2, type=float """

    BASE_HEIGHT = 1126
    """ Base level, type=float """

    FOUNDATION_HEIGHT = 1127
    """ Floor level, type=float """

    ACCESS_AID = 1128
    """ Access aid, type=string"""

    ACCESSIBILITY = 1129
    """ Accessibility, type=string"""

    NOMINAL_VOLUME = 1130
    """ Nominal volume, type=float """

    DIRECTION = 1131
    """ Effective direction, type=string"""

    POSITION_IN_CONDUIT = 1132
    """ Position in conduit, type=string"""

    POSITION = 1133
    """ Position, type=string"""

    HEIGHT_DIFFERENCE = 1134
    """ Height difference, lift, type=string"""

    OVERFLOW_HEIGHT = 1135
    """ Height, overflow, type=string"""

    MANUFACTURER = 1136
    """ Manufacturer, type=string"""

    CHARACTERISTICS = 1137
    """ Characteristics, type=string"""

    INSTALLATION_DATE = 1138
    """ Installation date, type=string"""

    LAST_CHECK = 1139
    """ Last check, type=string"""

    INSULATION_ON_OUTSIDE = 1140
    """ Insulation on the outside, type=string"""

    COATING_ON__INSIDE = 1141
    """ Coating on the inside, type=string"""

    SHEAR_RESTRAINT = 1142
    """ Shearing protection, type=string"""

    PLACING_MODE = 1143
    """ Placing mode, type=string"""

    COVER = 1144
    """ Cover, type=string"""

    OPERATING_PRESSURE = 1145
    """ Operating pressure, type=string"""

    EXTENSION_TYPE = 1146
    """ Extension type, type=string"""

    SWITCHING_STATE = 1147
    """ Switching state, type=string"""

    SWITCHING_OPERATION = 1148
    """ Switching operation, type=string"""

    FUNCTION_GENERAL = 1149
    """ Function, general, type=string"""

    YEAR_OF_INSTALLATION = 1150
    """ Year of installation, type=string"""

    DIMENSION = 1151
    """ Unit, type=float """

    OPERATOR = 1152
    """ Operator, type=string"""

    CONCESSIONER = 1153
    """ Concessionaire, type=string"""

    LIABILITY_FOR_MAINTENANCE = 1154
    """ Liability for maintenance, type=string"""

    NODE_TYPE = 1155
    """ Node type of a tree structure (root, node, item), type=string"""

    OPERATING_PRESSURE_OF_SYSTEM = 1156
    """ Operating pressure of system, type=string"""

    MAX_OPERATING_PRESSURE = 1157
    """ Maximum operating pressure, type=string"""

    PRESSURE_ZONE = 1158
    """ Pressure zone, type=string"""

    DOCUMENTS = 1159
    """ Documents, type=string"""

    WATER_QUALITY = 1160
    """ Water quality, type=string"""

    VOLUMETRIC_CAPACITY = 1162
    """ Volumetric capacity, type=float """

    PROCESS_WATER_RESERVES = 1163
    """ Process water reserves, type=float """

    WATER_RESERVES_FOR_FIREFIGHTING = 1164
    """ Water reserves for firefighting, type=float """

    NUMBER = 1165
    """ Number, type=string"""

    NAMING = 1166
    """ Name, type=string"""

    COMMENT = 1167
    """ Comment, type=string"""

    FROM_MANHOLE = 1174
    """ From manhole, type=string"""

    TO_MANHOLE = 1175
    """ To manhole, type=string"""

    INNER_DIAMETER = 1176
    """ Inside diameter, type=string"""

    OUTER_DIAMETER = 1177
    """ Outside diameter, type=string"""

    HEIGHT_OF_MANHOLE = 1178
    """ Height of manhole, type=float """

    MATERIAL_OF_MANHOLE = 1179
    """ Material of manhole, type=string"""

    SHAPE_OF_MANHOLE = 1180
    """ Shape of manhole, type=string"""

    SIZE_OF_MANHOLE_COVER = 1181
    """ Size of manhole cover, type=float """

    MATERIAL_OF_MANHOLE_COVER = 1182
    """ Material of manhole cover, type=string"""

    HOUSE_NUMBER = 1183
    """ House number, type=string"""

    LOT_OF_LAND_NO_ = 1184
    """ Lot number, type=string"""

    MANHOLE_COVER = 1185
    """ Manhole cover, type=string"""

    STREET = 1186
    """ Street, type=string"""

    SIZE_OF_MANHOLE = 1189
    """ Size of manhole, type=string"""

    STATE_OF_MANHOLE_1 = 1190
    """ MS_1 (state 1 of manhole), type=string"""

    STATE_OF_MANHOLE_2 = 1191
    """ MS_2 (state 2 of manhole), type=string"""

    STATE_OF_MANHOLE_3 = 1192
    """ MS_3 (state 3 of manhole), type=string"""

    STATE_OF_MANHOLE_4 = 1193
    """ MS_4 (state 4 of manhole), type=string"""

    STATE_OF_MANHOLE_5 = 1194
    """ MS_5 (state 5 of manhole), type=string"""

    STATE_OF_MANHOLE_6 = 1195
    """ MS_6 (state 6 of manhole), type=string"""

    STATE_OF_MANHOLE_7 = 1196
    """ MS_7 (state 7 of manhole), type=string"""

    STATE_OF_MANHOLE_8 = 1197
    """ MS_8 (state 8 of manhole), type=string"""

    STATE_OF_MANHOLE_9 = 1198
    """ MS_9 (state 9 of manhole), type=string"""

    NETHERLANDS_X2 = 1200
    """ Netherlands: X2, type=int"""

    NETHERLANDS_Y2 = 1201
    """ Netherlands: Y2, type=int"""

    NETHERLANDS_BUIG_MIDDELL_ = 1202
    """ Netherlands: Buig middell., type=int"""

    NETHERLANDS_SPIRAAL_AANT_WIND_ = 1203
    """ Netherlands: Spiraal-aant.wind., type=int"""

    NETHERLANDS_SPIRAAL_SPOED = 1204
    """ Netherlands: Spiraal-spoed, type=int"""

    NETHERLANDS_U = 1205
    """ Netherlands: U, type=int"""

    NETHERLANDS_H1 = 1206
    """ Netherlands: H1, type=int"""

    NETHERLANDS_H2 = 1207
    """ Netherlands: H2, type=int"""

    TYPE_AMP_SIZE_FOR_BRITISH_STANDARD = 1208
    """ Reinforcement schedule based on British Standard: type and size, type=string"""

    COMMENT_WITH_DEFAULT_VALUE = 1209
    """ Comment with default value, type=string"""

    FILTER_BY_MESH = 1210
    """ Filter by mesh, type=int"""

    NUMBER_OF_LONGITUDINAL_BARS = 1211
    """ Number of longitudinal bars in mesh, type=int"""

    NUMBER_OF_CROSS_BARS = 1212
    """ Number of cross bars in mesh, type=int"""

    MESH_TYPE = 1213
    """ Mesh type, type=int"""

    TYPE_OF_LONGITUDINAL_BAR_DIAMETER = 1214
    """ Reinforcement schedule based on British Standard: type and longitudinal bar diameter, type=string"""

    TYPE_OF_CROSS_BAR_DIAMETER = 1215
    """ Reinforcement schedule based on British Standard: type and cross bar diameter, type=string"""

    SUMMARY_OF_REMARKS = 1216
    """ Comment, summary, type=string"""

    LONGITUDE = 1217
    """ Project attribute: longitude, type=string"""

    LATITUDE = 1218
    """ Project attribute: latitude, type=string"""

    NET_VOLUME_OF_CONCRETE = 1219
    """ Net volume of concrete, type=float """

    FF_STIRRUP_CAGES_AVAILABILITY_STOCK_ITEMS = 1220
    """ FF stirrup cages, availability of stock items (1/0), type=int"""

    FF_STIRRUP_CAGES_AVAILABILITY_SPECIAL_REINFORCEMENT = 1221
    """ FF stirrup cages, availability of special reinforcement (1/0), type=int"""

    FF_STIRRUP_CAGES_SUPPLIER_EXTERNAL = 1222
    """ FF stirrup cages, external supplier (1/0), type=int"""

    FF_STIRRUP_CAGES_SUPPLIER_WORKS = 1223
    """ FF stirrup cages, supplied by factory (1/0), type=int"""

    FF_STIRRUP_CAGES_PRODUCER_EXTERNAL = 1224
    """ FF stirrup cages, external producer (1/0), type=int"""

    FF_STIRRUP_CAGES_PRODUCER_WORKS = 1225
    """ FF stirrup cages, produced by factory (1/0), type=int"""

    LAYER_ADJUSTMENT_TL = 1226
    """ Layer adjustment at top level [m], type=float """

    LAYER_ADJUSTMENT_BL = 1227
    """ Layer adjustment at bottom level [m], type=float """

    HEIGHT_WINDOW_SILL_OUTSIDE = 1228
    """ Height of outside window sill, type=float """

    HEIGHT_WINDOW_SILL_INSIDE = 1229
    """ Height of inside window sill, type=float """

    OFFSET_OPENING_BOTTOM = 1230
    """ Tolerance for calculating the lower dimensions of windows and doors, type=float """

    OFFSET_OPENING_TOP = 1231
    """ Tolerance for calculating the upper dimensions of windows and doors, type=float """

    OFFSET_OPENING_LEFT = 1232
    """ Tolerance for calculating the left dimensions of windows and doors, type=float """

    OFFSET_OPENING_RIGHT = 1233
    """ Tolerance for calculating the right dimensions of windows and doors, type=float """

    ASSOCIATION_WITH_GROUP = 1246
    """ Associated with fixture group, type=int"""

    STONE_TYPE = 1247
    """ Tile type, type=string"""

    DAMAGE_1_CHANNEL = 1250
    """ Damage 1 (conduit), type=string"""

    DAMAGE_2_CHANNEL = 1251
    """ Damage 2 (conduit), type=string"""

    DAMAGE_3_CHANNEL = 1252
    """ Damage 3 (conduit), type=string"""

    DAMAGE_4_CHANNEL = 1253
    """ Damage 4 (conduit), type=string"""

    DAMAGE_5_CHANNEL = 1254
    """ Damage 5 (conduit), type=string"""

    DAMAGE_6_CHANNEL = 1255
    """ Damage 6 (conduit), type=string"""

    DAMAGE_7_CHANNEL = 1256
    """ Damage 7 (conduit), type=string"""

    DAMAGE_8_CHANNEL = 1257
    """ Damage 8 (conduit), type=string"""

    DAMAGE_9_CHANNEL = 1258
    """ Damage 9 (conduit), type=string"""

    COMMENT_SB = 1259
    """ Comment (MD), type=string"""

    COMMENT_KZ = 1260
    """ Comment (CS), type=string"""

    COMMENT_KB = 1261
    """ Comment (CD), type=string"""

    COMMENT_SZ = 1262
    """ Comment (MS), type=string"""

    CODE_MANHOLE = 1263
    """ Code, manhole, type=int"""

    CODE_CHANNEL = 1264
    """ Code, conduit, type=int"""

    POSITION_1_CHANNEL = 1265
    """ Position 1 (conduit), type=float """

    POSITION_2_CHANNEL = 1266
    """ Position 2 (conduit), type=float """

    POSITION_3_CHANNEL = 1267
    """ Position 3 (conduit), type=float """

    POSITION_4_CHANNEL = 1268
    """ Position 4 (conduit), type=float """

    POSITION_5_CHANNEL = 1269
    """ Position 5 (conduit), type=float """

    POSITION_6_CHANNEL = 1270
    """ Position 6 (conduit), type=float """

    POSITION_7_CHANNEL = 1271
    """ Position 7 (conduit), type=float """

    POSITION_8_CHANNEL = 1272
    """ Position 8 (conduit), type=float """

    POSITION_9_CHANNEL = 1273
    """ Position 9 (conduit), type=float """

    DEDUCTION_OPENING_BOTTOM = 1274
    """ Constant offset at the bottom for calculating the clear width, type=float """

    CONDUIT_MATERIAL = 1275
    """ Conduit material, type=string"""

    CONDUIT_DIMENSION = 1276
    """ Conduit dimension, type=string"""

    COMMENT__WL = 1277
    """ Comment (TC), type=string"""

    L_DIM__DN = 1278
    """ L Dim (DN), type=int"""

    L_DIM__DI = 1279
    """ L Dim (di), type=float """

    L_DIM__DE = 1280
    """ L Dim (de), type=float """

    DATE_OF_REVISION = 1281
    """ Date of revision, type=string"""

    TYPE_OF_HYDRANT = 1282
    """ Type of hydrant, type=string"""

    OUTFLOW_OF_HYDRANTS = 1283
    """ Outflow of hydrants, type=string"""

    HYDRANT_NO_ = 1284
    """ Hydrant number, type=int"""

    SLIDE_NO_ = 1285
    """ Slide number, type=int"""

    TYPE_OF_SLIDE = 1286
    """ Type of slide, type=string"""

    LOCATION_OF_DAMAGE = 1287
    """ Location of damage, type=string"""

    KIND_OF_DAMAGE = 1288
    """ Kind of damage, type=string"""

    DAMAGE_TO_OBJECT = 1289
    """ Damage to object, type=string"""

    REPAIR_COSTS = 1290
    """ Repair costs, type=float """

    SEWER_GRID_ELEMENT_REF = 1291
    """ Reference element of sewer network, type=string"""

    OUTFLOW_COEFFICIENT = 1292
    """ Outflow coefficient, type=float """

    MATERIAL_CODE = 1293
    """ Material code, type=string"""

    OCCUPANCY_TYPE_ID = 1294
    """ Occupancy type ID, type=string"""

    DELTA_VALUE_FOR_INITIAL_HEIGHT = 1295
    """ Delta value for initial height, type=float """

    DELTA_VALUE_FOR_FINAL_HEIGHT = 1296
    """ Delta value for final height, type=float """

    MANHOLE_REF = 1297
    """ Reference manhole, type=string"""

    CONDUIT_REF = 1298
    """ Reference conduit, type=string"""

    CALCULATION_OF_LENGTH = 1299
    """ Calculation of length, type=string"""

    INLET_1 = 1300
    """ Inlet 1, type=float """

    INLET_2 = 1301
    """ Inlet 2, type=float """

    INLET_3 = 1302
    """ Inlet 3, type=float """

    SHAFT_OUTLET = 1303
    """ Outlet, type=float """

    STOREY = 1304
    """ Story, type=string"""

    SITE_AREA_RATIO = 1305
    """ Site area ratio, type=float """

    LEVEL_OF_SENSITIVITY = 1306
    """ Level of sensitivity, type=string"""

    SYMBOL_ORI = 1307
    """ Symbol orientation, type=float """

    SPECIAL_BUILDING_REF = 1308
    """ Special building reference, type=string"""

    TEXT = 1310
    """ Text (for export), type=string"""

    TEXT_POS = 1311
    """ Text position, type=string"""

    STAGE = 1312

    TEXT_HALI = 1313
    """ Text, horizontally aligned, type=int"""

    TEXT_VALI = 1314
    """ Text, vertically aligned, type=int"""

    INLET = 1315
    """ Inlet, type=float """

    OUTLET = 1316
    """ Outlet, type=float """

    OBJ_ID = 1319
    """ Internal Allplan object ID(Guid), type=string"""

    SEALING_FACTOR = 1320
    """ Sealing factor, type=int"""

    POPULATION_DENSITY = 1321
    """ Population density, type=int"""

    MD_DATA_ADMINISTRATOR = 1322
    """ Data administrator, type=string"""

    SUPERCLASS = 1323
    """ Superclass, type=string"""

    INNER_PROTECTION = 1324
    """ Internal treatment, type=string"""

    FRICTION_COEFFICIENT = 1325
    """ Friction coefficient, type=int"""

    WALL_ROUGHNESS = 1326
    """ Wall roughness, type=float """

    SEEPAGE = 1327
    """ Seepage, type=string"""

    CATALOG_REFERENCE = 1332
    """ Catalog reference, type=string"""

    MATCHCODE = 1333
    """ Fixtures: match code, type=string"""

    ASSOCIATED_PRECAST_ELEMENT = 1334
    """ Fixtures: associated with precast element, type=int"""

    ASSOCIATED_PRECAST_WALL_ELEMENT = 1335
    """ Fixtures: associated with precast wall element, type=int"""

    ASSOCIATED_PRECAST_SLAB_ELEMENT = 1336
    """ Fixtures: associated with precast slab element, type=int"""

    ASSOCIATED_STRUCTURAL_PRECAST_ELEMENT = 1337
    """ Fixtures: associated with structural precast element, type=int"""

    ASSOCIATED_ARCHITECTURAL_WALL = 1338
    """ Fixtures: associated with architectural wall, type=int"""

    ASSOCIATED_ARCHITECTURAL_SLAB = 1339
    """ Fixtures: associated with architectural slab, type=int"""

    INTERFACE_TYPE = 1340

    STIRRUP_LENGTH = 1341

    LONGIT__BAR_LENGTH = 1342

    STIRRUP_DIAMETER = 1343

    LONGIT__BAR_DIAMETER = 1344

    OFFSET_AT_START = 1345

    STIRRUP_NUMBER = 1346

    STIRRUP_SPACING = 1347

    DOMED_ROOF_LIGHT_CURB_HEIGHT = 1348
    """ Domed roof-light, curb height, type=float """

    DOMED_ROOF_LIGHT_DOME_HEIGHT = 1349
    """ Domed roof-light, rise, type=float """

    CATALOG_LIST_TEXT = 1350
    """ List text from fixture catalog for precast elements, type=string"""

    UNSPSC_NAME = 1352
    """ Categorization - UNSPSC Name, type=string"""

    UNSPSC_CODE = 1353
    """ Categorization - UNSPSC Code, type=string"""

    UNICLASS_1_4_CODE = 1354
    """ Categorization - Uniclass 1.4 Code, type=string"""

    TYPE_OF_MATERIAL = 1355
    """ Material type (concrete...0, insulation...1, in-situ concrete...2, bricks/tiles...3), type=int"""

    UNICLASS_1_4_DESCRIPTION = 1356
    """ Categorization - Uniclass 1.4 Beschreibung, type=string"""

    UNICLASS_2_0_CODE = 1357
    """ Categorization - Uniclass 2.0 Code, type=string"""

    UNICLASS_2_0_DESCRIPTION = 1358
    """ Categorization - Uniclass 2.0 Beschreibung, type=string"""

    NBS_REFERENCE_CODE = 1359
    """ Categorization - NBS Reference Code, type=string"""

    MESH_STEEL_WEIGHT = 1365
    """ Reinforcing mesh weight, type=float """

    BAR_STEEL_WEIGHT = 1366
    """ Reinforcing bar weight, type=float """

    LATTICE_GIRDER_STEEL_WEIGHT = 1367
    """ Lattice girder weight, type=float """

    DEDUCTION_OPENING_LEFT = 1368
    """ Constant offset on the left for calculating the clear width, type=float """

    DEDUCTION_OPENING_RIGHT = 1369
    """ Constant offset on the right for calculating the clear width, type=float """

    DEDUCTION_OPENING_TOP = 1370
    """ Constant offset at the top for calculating the clear width, type=float """

    COMBUSTIBLE = 1371
    """ BuildingSmart: Combustible, type=int"""

    SURFACE_SPREAD_OF_FLAME = 1372
    """ Behavior under fire, type=string"""

    ACOUSTIC_RATING = 1373
    """ Sound transmission class, type=string"""

    SPAN = 1374
    """ Span, type=float """

    BARRIER_FREE = 1375
    """ Handicapped accessible, type=int"""

    FIRE_EXIT_STAIR = 1376
    """ Means of egress, type=int"""

    REQUIRED_HEADROOM = 1377
    """ Ifc: RequiredHeadroom, type=float """

    REQUIRED_SLOPE = 1378
    """ RequiredSlope, type=float """

    SMOKE_STOP = 1379
    """ IFC: SmokeStop, type=int"""

    SELF_CLOSING = 1380
    """ Self-closing, type=int"""

    FIRE_EXIT = 1381
    """ Emergency exit, type=int"""

    MODEL_NUMBER = 1382
    """ IFC: ModelReference, type=float """

    MODEL_LABEL = 1383
    """ IFC: ModelLabel, type=string"""

    ARCHITECT_MOBILE_NUMBER = 1384
    """ Architect, mobile number, type=string"""

    ARCHITECT_HOMEPAGE = 1385
    """ Web address of architect, type=string"""

    CLIENT_HOMEPAGE = 1386
    """ Web address of client, type=string"""

    BUILDING_CONTRACTOR_HOMEPAGE = 1387
    """ Web address of a building contractor, type=string"""

    CONSTRUCTION_PROJECT_HOMEPAGE = 1388
    """ Web address of construction project, type=string"""

    CHECKING_STRUCTURAL_ENGINEER_HOMEPAGE = 1389
    """ Web address of structural inspection engineer, type=string"""

    STRUCTURAL_ENGINEER__HOMEPAGE = 1390
    """ Web address of structural engineer, type=string"""

    PLOT_AREA_WITH_BUILDING = 1391

    SECURITY_RATING = 1392

    PRODUCTION_YEAR = 1393

    FINISH = 1394

    CLASSIFICATION_KEY = 1395

    COMPARTMENTATION = 1396
    """ BuildingSmart: Compartmentation, type=int"""

    PROJECTED_AREA = 1397

    FIRE_RISK_FACTOR = 1398

    SPRINKLER_PROTECTION = 1399

    ARTIFICIAL_LIGHTING = 1400

    SPACE_HUMIDITY = 1401

    NATURAL_VENTILATION = 1402

    AIR_CONDITIONED = 1403

    SPACE_TEMPERATURE_MAX = 1404

    SPACE_TEMPERATURE_MIN = 1405

    HAS_NON_SKID_SURFACE = 1406
    """ Adjustment to BuildingSmart: HasNonSkidSurface, type=int"""

    MARK_NUMBERS_OF_MESHESBARSFIXTURES_IN_ELEMENT_PLAN = 1412
    """ Mark numbers of meshes/bars/fixtures in element plan, type=string"""

    SIDE_OF_PRECAST_ELEMENT_LAYER = 1413
    """ Side of precast element layer, type=int"""

    TYPE_OF_REINFORCEMENT = 1415
    """ Filter for reinforcement type (bar type, mesh type, girder type), type=int"""

    STANDARD_FORMWORK_ELEMENT_BOTTOM_STEP_NAME = 1416
    """ Standard formwork element, bottom step, name, type=string"""

    STANDARD_FORMWORK_ELEMENT_NORMAL_AREA_NAME = 1417
    """ Standard formwork element, normal area, name, type=string"""

    STANDARD_FORMWORK_ELEMENT_TOP_STEP_NAME = 1418
    """ Standard formwork element, top step, name, type=string"""

    STANDARD_FORMWORK_ELEMENT_BOTTOM_STEP_LENGTH = 1419
    """ Standard formwork element, bottom step, length, type=float """

    STANDARD_FORMWORK_ELEMENT_NORMAL_AREA_LENGTH = 1420
    """ Standard formwork element, normal area, length, type=float """

    STANDARD_FORMWORK_ELEMENT_TOP_STEP_LENGTH = 1421
    """ Standard formwork element, top step, length, type=float """

    PROFILE_NAME = 1426

    PBB_REQUIREMENTS_1 = 1427

    PBB_REQUIREMENTS_2 = 1428

    PBB_REQUIREMENTS_3 = 1429

    PBB_REQUIREMENTS_4 = 1430

    PBB_REQUIREMENTS_5 = 1431

    BENDING_DIMENSIONS_ISO_3766_A_E = 1437
    """ Bending dimensions (a, type=int"""

    BAR_SHAPE_CODE_ISO_3766 = 1438
    """ Bar shape key ISO 3766, type=string"""

    WEIGHTM = 1439
    """ Steel construction attribute describing the weight of a steel section that is one meter long, type=float """

    SHELL_SURFACEM = 1440
    """ Steel construction attribute describing the surface of a steel section that is one meter long, type=float """

    PURPOSE = 1441
    """ IFC Purpose: Indication of the purpose for that opening, e.g. "ventilation" acc. to BuildingSmart, type=string"""

    EXTEND_TO_STRUCTURE = 1442
    """ IFC ExtendToStructure acc. to BuildingSmart, type=int"""

    FORMWORK_TYPE = 1443
    """ Formwork types 1 to 4, type=string"""

    IFC_PREDEFINED_TYPE = 1444
    """ IFC object subtype, type=string"""

    GLAZING_AREA_FRACTION = 1445
    """ IFC GlazingAreaFraction acc. to BuildingSmart, type=float """

    CROSS_SECTIONAL_AREA = 1446
    """ Cross-sectional area according to steel construction, type=float """

    CHARACTERISTIC_VALUE_OF_DEAD_LOAD = 1447
    """ Characteristic value of dead load according to steel construction, type=float """

    DESCRIPTION = 1448
    """ Description for Ifc mapping, type=string"""

    NAME_OF_CONNECTION = 1450
    """ Name of connection, type=string"""

    NUMBER_OF_CONNECTIONS = 1451
    """ Number of connections, type=float """

    SECONDARY_REINFORCEMENT_AT_CONNECTION = 1452
    """ Analyzes secondary reinforcement, type=string"""

    WEIGHT_OF_CONNECTION = 1453
    """ Analyzes the weight of the connection, type=float """

    WALL_THICKNESS_AT_CONNECTION = 1454
    """ Analyzes the wall thickness of the connection, type=float """

    MRK_NO_OF_ELEMENTS = 1455
    """ Mark number of cage elements of the connection, type=int"""

    DETAIL_DRAWING_FILE_NUMBER = 1458
    """ Drawing file number of associated detail precast element, type=int"""

    MODEL_DRAWING_FILE_NUMBERS = 1459
    """ Drawing file numbers of associated model precast elements, type=string"""

    MRK_NO_WITH_PREFIX_FOR_FIXTURES = 1460
    """ Mark number with prefix of fixtures, type=string"""

    LATTICE_GIRDER_NAME = 1461
    """ Name of lattice girder type, type=string"""

    LATTICE_GIRDER_TOTAL_WEIGHT = 1462
    """ Total weight of lattice girders, type=float """

    LATTICE_GIRDER_WEIGHT = 1463
    """ Weight of lattice girder, type=float """

    ADDITIONAL_ID = 1464
    """ Additional ID of precast element, type=string"""

    NUMBER_OF_PAGES = 1465
    """ Total number of pages in element plan, type=string"""

    ADDITIONAL_IDS_SAME_MARK_NUMBER = 1466
    """ Additional IDs of precast element group (same mark number), type=string"""

    INSULATING_STRIP_VOLUME = 1467
    """ Volume of insulating strip, type=float """

    STEEL_GRADE_OF_MESHES_BARS_IN_PRECAST_ELEMENT = 1468
    """ Steel grade of meshes, bars in precast element, type=string"""

    MODEL_DRAWING_FILE_NAME = 1469
    """ Drawing file name of model drawing file name, type=string"""

    ASSEMBLY_GROUP_NAME = 1470
    """ Name of associated assembly, type=string"""

    NUMBER_OF_BAR_SPACING = 1471
    """ Number of bar spacing in placement, type=int"""

    TOTAL_BAR_SPACING = 1472
    """ Total bar spacing in placement, type=float """

    NUMBER_OF_ELEMENTS_IN_DIMENSION_LINE_OF_ELEMENT_PLAN = 1473
    """ Number of elements in dimension line of element plan, type=string"""

    INVOICE_ITEM_NAME = 1477
    """ Text of order item, type=string"""

    INVOICE_ITEM_NUMBER = 1478
    """ Number within confirmation of order, type=string"""

    INVOICE_ITEM_ID = 1479
    """ ID within confirmation of order, type=string"""

    PAGE_NAME = 1480
    """ Page name of element plan page, type=string"""

    LEAF_1__FORMWORK_BOTTOM = 1481
    """ Leaf 1 / formwork bottom, type=int"""

    OMNI_CLASS_NUMBER = 1482
    """ no matter what, type=string"""

    OMNI_CLASS_TITLE = 1483
    """ no matter what, type=string"""

    UNICLASS_2015_CODE = 1484
    """ Categorization - till 2017: Uniclass-Number, type=string"""

    UNICLASS_2015_DESCRIPTION = 1485
    """ Categorization - Uniclass 2015 Description, type=string"""

    LAND_REGISTER___DISTRICT = 1486
    """ Land register - district, type=string"""

    LAND_REGISTER___SUBDISTRICT = 1487
    """ Land register - subdistrict, type=string"""

    LAND_REGISTER____SHEET_NUMBER = 1488
    """ Land register -  sheet number, type=string"""

    LAND_REGISTER___PARCEL_NUMBER = 1489
    """ Land register - parcel number, type=string"""

    STANDARD_ROOM_ASSIGNMENT = 1500
    """ Standard room assignment of Smartparts, type=int"""

    FIGURE01 = 1830
    """ ALLFA: figure 01, type=float """

    FIGURE02 = 1831
    """ ALLFA: figure 02, type=float """

    FIGURE03 = 1832
    """ ALLFA: figure 03, type=float """

    FIGURE04 = 1833
    """ ALLFA: figure 04, type=float """

    FIGURE05 = 1834
    """ ALLFA: figure 05, type=float """

    FIGURE06 = 1835
    """ ALLFA: figure 06, type=float """

    FIGURE07 = 1836
    """ ALLFA: figure 07, type=float """

    FIGURE08 = 1837
    """ ALLFA: figure 08, type=float """

    FIGURE09 = 1838
    """ ALLFA: figure 09, type=float """

    FIGURE10 = 1839
    """ ALLFA: figure 10, type=float """

    NUMBER01 = 1840
    """ ALLFA: number 01, type=int"""

    NUMBER02 = 1841
    """ ALLFA: number 02, type=int"""

    NUMBER03 = 1842
    """ ALLFA: number 03, type=int"""

    NUMBER04 = 1843
    """ ALLFA: number 04, type=int"""

    NUMBER05 = 1844
    """ ALLFA: number 05, type=int"""

    DATE01 = 1845
    """ ALLFA: date 01, type=float """

    DATE02 = 1846
    """ ALLFA: date 02, type=float """

    DATE03 = 1847
    """ ALLFA: date 03, type=float """

    DATE04 = 1848
    """ ALLFA: date 04, type=float """

    DATE05 = 1849
    """ ALLFA: date 05, type=float """

    SCIA_LENGTH = 1850
    """ SCIA length, type=float """

    SCIA_SURFACE = 1851
    """ SCIA surface, type=float """

    SCIA_VOLUME = 1852
    """ SCIA volume, type=float """

    SCIA_WEIGHT = 1853
    """ SCIA weight, type=float """

    SCIA_VERSION = 1854
    """ SCIA version, type=int"""

    SCIA_TYPE = 1855
    """ SCIA type, type=int"""

    TRUCK_NUMBER = 1857
    """ Truck number, type=int"""

    MIRROR_FIRST_HOLE = 1858
    """ Fixtures, steel section - mirror first hole in section, type=int"""

    SECTION_ORIENTATION = 1859
    """ Fixtures, steel section - section orientation (beam), type=int"""

    DOUBLE_SECTION = 1860
    """ Fixtures, steel section - double section, type=int"""

    MOVE_HOLE = 1861
    """ Fixtures, steel section - dx hole in steel section, type=float """

    SECTION_TYPE = 1862
    """ Fixtures, steel section - steel section type (reference to catalog), type=int"""

    CONSTRUCTION_METHOD = 1864
    """ IFC ConstructionMethod, Excution (In-situ, Precast), type=int"""

    PRODUCT_DATA_LINK = 1865
    """ Product data link for BIMobject cooperation in 2017-1-1, type=string"""

    THICKNESS_OF_VISIBLE_LEAF = 1866
    """ Thickness of visible leaf, type=float """

    THICKNESS_OF_INVISIBLE_LEAF = 1867
    """ Thickness of invisible leaf, type=float """

    HEIGHT_OF_VISIBLE_LEAF = 1868
    """ Height of visible leaf, type=float """

    HEIGHT_OF_INVISIBLE_LEAF = 1869
    """ Height of invisible leaf, type=float """

    WIDTH_OF_VISIBLE_LEAF = 1870
    """ Width of visible leaf, type=float """

    WIDTH_OF_INVISIBLE_LEAF = 1871
    """ Width of invisible leaf, type=float """

    STANDARD_GIRDER_TYPE = 1872
    """ Standard type of lattice girder, type=string"""

    MINIMUM_OFFSET_TO_EDGE = 1873
    """ Minimum offset to edge, type=float """

    ADDITIONAL_TEXT_FOR_KEY_PLAN = 1875
    """ Additional text for key plan, type=string"""

    CONCR__TOPPING = 1876
    """ Concrete topping, type=float """

    PRECAST_ID = 1877
    """ Unique ID for precast elements, type=int"""

    C_I_NUT_TYPE = 1878
    """ Assembly - type of cast-in nut, type=int"""

    REQUIRED_ASX_AT_TOPVISIBLE = 1879
    """ Required longitudinal as-value at top/visible, type=float """

    REQUIRED_ASX_AT_BOTTOMINVISIBLE = 1880
    """ Required longitudinal as-value at bottom/invisible, type=float """

    EXISTING_ASX_AT_TOPVISIBLE = 1881
    """ Existing longitudinal as-value at top/visible, type=float """

    EXISTING_ASX_AT_BOTTOMINVISIBLE = 1882
    """ Existing longitudinal as-value at bottom/invisible, type=float """

    REQUIRED_ASY_AT_TOPVISIBLE = 1883
    """ Required transverse as-value at top/visible, type=float """

    REQUIRED_ASY_AT_BOTTOMINVISIBLE = 1884
    """ Required transverse as-value at bottom/invisible, type=float """

    EXISTING_ASY_AT_TOPVISIBLE = 1885
    """ Existing transverse as-value at top/visible, type=float """

    EXISTING_ASY_AT_BOTTOMINVISIBLE = 1886
    """ Existing transverse as-value at bottom/invisible, type=float """

    DATE_ON_WHICH_DATA_WAS_TRANSFERRED_TO_PRODUCTION = 1887
    """ Date on which data was transferred to production, type=string"""

    STATUS_NAME = 1889
    """ Name of precast element status, type=string"""

    STATUS_DESCRIPTION = 1890
    """ Description of precast element status, type=string"""

    STATUS_SEQUENCE = 1891
    """ Sequence of precast element status, type=int"""

    SLAB_THICKNESS = 1892
    """ Slab thickness, type=float """

    COMPONENT_NAME = 1893
    """ Name of precast element, type=string"""

    INVOICE_TEXT = 1894
    """ Invoice item of precast element, type=string"""

    CUSTOM_ATTRIBUTE_06 = 1895
    """ Precast elements: custom attribute 06 --&gt; included for compatibility reasons only! Use 1947!, type=string"""

    CUSTOM_ATTRIBUTE_07 = 1896
    """ Precast elements: custom attribute 07 --&gt; included for compatibility reasons only! Use 1947!, type=string"""

    CUSTOM_ATTRIBUTE_08 = 1897
    """ Precast elements: custom attribute 08 --&gt; included for compatibility reasons only! Use 1947!, type=string"""

    CUSTOM_ATTRIBUTE_09 = 1898
    """ Precast elements: custom attribute 09 --&gt; included for compatibility reasons only! Use 1947!, type=string"""

    CUSTOM_ATTRIBUTE_10 = 1899
    """ Precast elements: custom attribute 10 --&gt; included for compatibility reasons only! Use 1947!, type=string"""

    CUSTOM_ATTRIBUTE_11 = 1900
    """ Precast elements: custom attribute 11 --&gt; included for compatibility reasons only! Use 1947!, type=string"""

    CUSTOM_ATTRIBUTE_12 = 1901
    """ Custom attribute 12 -&gt; only necessary due to compatibility! Use 1947, type=string"""

    CUSTOM_ATTRIBUTE_13 = 1902
    """ Custom attribute 13 -&gt; only necessary due to compatibility! Use 1947, type=string"""

    CUSTOM_ATTRIBUTE_14 = 1903
    """ Custom attribute 14 -&gt; only necessary due to compatibility! Use 1947, type=string"""

    CUSTOM_ATTRIBUTE_15 = 1904
    """ Custom attribute 15 -&gt; only necessary due to compatibility! Use 1947, type=string"""

    CONCRETE_STRENGTH_GRADE = 1905
    """ Concrete strength grade, type=string"""

    VALUE_FOR_FOUNDATION_MODULUS = 1906
    """ FEA PLT: foundation modulus, type=float """

    INTERNAL_DIM__1 = 1907
    """ FEA PLT: internal dimension 1, type=float """

    INTERNAL_DIM__2 = 1908
    """ FEA PLT: internal dimension 2, type=float """

    EFFECTIVE_WIDTH = 1909
    """ FEA PLT: effective slab width, type=float """

    REINFORCEMENT_LAYER = 1910
    """ FEA PLT: layer, type=string"""

    MESH = 1911
    """ FEA PLT: mesh, type=string"""

    AS_1 = 1912
    """ FEA PLT: as 1, type=float """

    AS_2 = 1913
    """ FEA PLT: as 2, type=float """

    FZ = 1914
    """ FEA PLT: Fz, type=float """

    MX = 1915
    """ FEA PLT: Mx, type=float """

    MY = 1916
    """ FEA PLT: My, type=float """

    FEM_PLT_QZ = 1917
    """ FEA PLT: qz [kN/m], type=float """

    FEM_PLT_QZ_2 = 1918
    """ FEA PLT: qz 2, type=float """

    M = 1919
    """ FEA PLT: m, type=float """

    M_2 = 1920
    """ FEA PLT: m 2, type=float """

    FEM_PLT_QZ_3 = 1921
    """ FEA PLT: qz [kN/m2], type=float """

    TEMPERATURE_AT_TOP = 1922
    """ FEA PLT: temperature at top, type=float """

    TEMPERATURE_AT_BOTTOM = 1923
    """ FEA PLT: temperature at bottom, type=float """

    MATERIAL_TYPE = 1924
    """ FEA PLT: material type, type=string"""

    FEM_PLT_WIDTH = 1925
    """ FEA PLT: width, type=float """

    FEM_PLT_DIAMETER = 1926
    """ FEA PLT: diameter, type=float """

    FEM_PLT_TYPE = 1927
    """ FEA PLT: type, type=string"""

    FEM_PLT_ANGLE = 1928
    """ FEA PLT: angle, type=float """

    PRECAST_IDS_SAME_MARK_NO_ = 1929
    """ Precast elements: precast IDs (same mark number), type=string"""

    SPAN_DIRECTION = 1930
    """ Precast elements: span direction, type=float """

    NUMBER_OF_SAME_FOUNDATIONS = 1931
    """ Number of same foundations, type=int"""

    CONSECUTIVE_NUMBER = 1932
    """ Consecutive number, type=int"""

    BOTTOM_EDGE_OF_FOUNDATION = 1933
    """ Bottom level of foundation, type=float """

    FOUNDATION_DIMENSIONS_M = 1934
    """ Foundation dimensions [m], type=string"""

    BOTTOM_EDGE_OF_COLUMN_____FOUNDATION = 1935
    """ Bottom level of column ... foundation, type=string"""

    SYMBOL = 1936
    """ Symbol, type=string"""

    PILE_LOAD_K_N = 1937
    """ Pile load [kN], type=string"""

    PILE_DIAMETER_M = 1938
    """ Pile diameter [m], type=float """

    TOP_OF_PILE_M = 1939
    """ Top level of pile [m], type=float """

    NUMBER_OF_SAME_PILES = 1940
    """ Number of same piles, type=int"""

    NAME_OF_FILLING_OBJECT = 1941
    """ Precast elements: name of filling object, type=string"""

    NUMBER_OF_FILLING_OBJECTS = 1942
    """ Precast elements: number of filling objects, type=int"""

    MRK__NO__OF_MESHESBARS_IN_ELEMENT_PLAN = 1943
    """ Mark number of meshes, bars in element plan, type=int"""

    NAME_OF_PROFILE = 1944
    """ Sleeve foundation - support foot - name of profiling, type=string"""

    HEIGHT_OF_PROFILE = 1945
    """ Sleeve foundation - support foot - height of profiling, type=float """

    NUMBER_OF_MESHESBARSFIXTURES_IN_ELEMENT_PLAN = 1946
    """ Number of meshes, bars, fixtures in element plan, type=int"""

    CUSTOM_ATTRIBUTE = 1947
    """ Precast elements: custom attributes (including index 1-n), type=string"""

    WEIGHT_OF_MESHESBARS_IN_ELEMENT_PLAN = 1948
    """ Weight of meshes, bars in element plan, type=float """

    LD_TYPE = 1949

    MARK_NUMBER_LIST = 1950

    FILLING_OBJECT_DIAMETER = 1951

    BRICK_NAME = 1952

    BRICK_LENGTH = 1953

    GRID_DIMENSION = 1954

    LENGTH_OF_BARS_IN_ELEMENT_PLAN = 1955
    """ Length of bars in element plan [m], type=float """

    IN_SITU_CONCRETE_GRADE = 1956
    """ Concrete grade of in-situ concrete layer, type=string"""

    ROLL = 1957
    """ Roll(IfcPlaneAngleMeasure), type=float """

    PITCH_ANGLE = 1958
    """ PitchAngle(IfcPlaneAngleMeasure), type=float """

    GROSS_PLANNED_AREA = 1959
    """ GrossPlannedArea(IfcAreaMeasure), type=float """

    NET_PLANNED_AREA = 1960
    """ NetPlannedArea(IfcAreaMeasure), type=float """

    PUBLICLY_ACCESSIBLE = 1961
    """ PubliclyAccessible(IfcBoolean), type=int"""

    PROTECTED_OPENING = 1962
    """ ProtectedOpening(IfcBoolean), type=int"""

    INFILTRATION = 1963
    """ Infiltration(IfcVolumetricFlowRateMeasure), type=float """

    HAS_DRIVE = 1964
    """ HasDrive(IfcBoolean), type=int"""

    WATER_TIGHTNESS_RATING = 1965
    """ WaterTightnessRating(IfcLabel), type=string"""

    MECHANICAL_LOAD_RATING = 1966
    """ MechanicalLoadRating(IfcLabel), type=string"""

    WIND_LOAD_RATING = 1967
    """ WindLoadRating(IfcLabel), type=string"""

    WALKING_LINE_OFFSET = 1968
    """ WalkingLineOffset(IfcPositiveLenghtMeasure), type=float """

    TREAD_LENGTH_AT_OFFSET = 1969
    """ TreadLengthAtOffset(IfcPositiveLenghtMeasure), type=float """

    FRAGILITY_RATING = 1970
    """ FragilityRating(IfcLabel), type=string"""

    MINIMUM_WAIST_THICKNESS = 1971
    """ WaistThickness(IfcPositiveLenghtMeasure), type=float """

    NUMBER_OF_DRAFTS = 1972
    """ NumberOfDrafts(IfcCountMeasure), type=int"""

    NOSING_LENGTH = 1973
    """ NosingLength(IfcLengthMeasure), type=float """

    TREAD_LENGTH_AT_INNER_SIDE = 1974
    """ TreadLengthAtInnerSide(IfcPositiveLenghtMeasure), type=float """

    HAS_SILL_EXTERNAL = 1975
    """ HasSillExternal(IfcBoolean), type=int"""

    HAS_SILL_INTERNAL = 1976
    """ HasSillInternal(IfcBoolean), type=int"""

    NUMBER_OF_TREADS = 1977
    """ NumberOfTreads(IfcCountMeasure), type=int"""

    LENGTHINCH_PER_M = 1980
    """ Length [inch] (per meter) - string, type=string"""

    LAYER_NUMBER_OF_PRECAST_ELEMENT = 1981
    """ Layer number of precast element, type=float """

    MWS_REINFORCEMENT_GROUP_FILTER = 1982
    """ MWS reinforcement group filter (is it a group? 0/1), type=int"""

    STACK_NAME = 1983
    """ Stack name: text for stack name, type=string"""

    ARCHITECT_EMAIL = 1984
    """ Architect, email, type=string"""

    CLIENT_FAX_NUMBER = 1985
    """ Client, fax number, type=string"""

    CLIENT_TELEPHONE_NUMBER = 1986
    """ Client, telephone number, type=string"""

    CLIENT_MOBILE_NUMBER = 1987
    """ Client, mobile number, type=string"""

    CLIENT_EMAIL = 1988
    """ Client, email, type=string"""

    BUILDING_CONTRACTOR = 1989
    """ Building contractor, type=string"""

    BUILDING_CONTRACTOR_FAX_NUMBER = 1990
    """ Building contractor, fax number, type=string"""

    BUILDING_CONTRACTOR_TELEPHONE_NUMBER = 1991
    """ Building contractor, telephone number, type=string"""

    BUILDING_CONTRACTOR_MOBILE_NUMBER = 1992
    """ Building contractor, mobile number, type=string"""

    BUILDING_CONTRACTOR_EMAIL = 1993
    """ Building contractor, email, type=string"""

    CONSTRUCTION_PROJECT_MOBILE_NUMBER = 1994
    """ Construction project, mobile number, type=string"""

    CONSTRUCTION_PROJECT_EMAIL = 1995
    """ Construction project, email, type=string"""

    CHECKING_STRUCTURAL_ENGINEER_MOBILE_NUMBER = 1996
    """ Structural inspection engineer, mobile number, type=string"""

    CHECKING_STRUCTURAL_ENGINEER_EMAIL = 1997
    """ Structural inspection engineer, email, type=string"""

    STRUCTURAL_ENGINEER_MOBILE_NUMBER = 1998
    """ Structural engineer, mobile number, type=string"""

    STRUCTURAL_ENGINEER_EMAIL = 1999
    """ Structural engineer, email, type=string"""

    DO_NOT_SPLIT_IN_IFC = 18001
    """ Prevents the splitting of multilayer elements, type=int"""

    INNER_WEB_HEIGHT = 18002

    MINIMUM_BEARING_SEAT_DEPTH = 18003

    UNIT_WARPING_AT_FLANGE_ROOT_WM1 = 18004

    RADIUS_R3 = 18005

    INTERNAL_BOLT_DISTANCE = 18006

    FLANGE_THICKNESS_BOTTOM = 18007

    INNER_RADIUS__R_ = 18008

    WIDTH__B_ = 18009

    WEB_THICKNESS__TD_ = 18010

    THICKNESS__S_ = 18011

    RADIUS_R1 = 18012

    UNIT_WARPING_AT_FLANGE_TOE = 18013

    OUTER_RADIUS = 18014

    FLANGE_WIDTH_BOTTOM = 18015

    DEPTH_OF_WEB = 18016

    BOLT_DISTANCE_W3 = 18017

    FLANGE_SLOPE__A_ = 18018

    PLUSLIP_ANGLE__A2_ = 18019

    INTERMEDIATE_BOTTOM_HEIGHT_F2 = 18020

    WEB_THICKNESS__S_ = 18021

    PLUSLIP = 18022

    INNER_LENGTH = 18023

    PLUSLIP_ANGLE__A_ = 18024

    WIDTH_TOP = 18025

    INTERMEDIATE_TOP_HEIGHT__H2_ = 18026

    LIP_TOP = 18027

    LIP = 18028

    WEB_DEPRESSION = 18029

    FLANGE_THICKNESS__T_ = 18030

    FLANGE_SLOPE__A1_ = 18031

    THICKNESS__T_ = 18032

    RADIUS_R2 = 18033

    INTERMEDIATE_WIDTH__B2_ = 18034

    FLANGE_WIDTH_TOP = 18035

    LIP_ANGLE = 18036

    INTERMEDIATE_WIDTH__B3_ = 18037

    THICKNESS__W_ = 18038

    BOLT_DISTANCE_W1 = 18039

    FLANGE_ANGLE = 18040

    FLANGE_THICKNESS__TB_ = 18041

    INNER_RADIUS__R1 = 18042

    UNIT_WARPING_AT_FLANGE_TOE_WM2 = 18043

    RADIUS_AT_FLANGE_TOE = 18044

    HEIGHT__H_ = 18045

    BOLT_DISTANCE_W2 = 18046

    INTERMEDIATE_TOP_HEIGHT__H3_ = 18047

    DEPTH = 18049

    WIDTH_BOTTOM = 18050

    WEB_HEIGHT_NEAR_FLANGE = 18051

    WEB_SLOPE = 18052

    TOTAL_WIDTH = 18053

    RADIUS_R5 = 18054

    RADIUS_AT_WEB_ROOT = 18055

    FLANGE_THICKNESS_TOP = 18056

    DIAMETER__D_ = 18057

    INTERMEDIATE_BOTTOM_HEIGHT_F3 = 18058

    LIP_BOTTOM = 18059

    FLANGE_WIDTH = 18060

    WEAR = 18061

    RADIUS_R4 = 18062

    RADIUS_AT_FLANGE_ROOT = 18063

    INTERMEDIATE_BOTTOM_HEIGHT_F1 = 18064

    NUMBER_OF_PRECAST_ELEMENTS = 18065
    """ Returns the number of precast elements including the piece factor, type=int"""

    X_DIMENSION = 18066

    Y_DIMENSION = 18067

    Z_DIMENSION = 18068

    STYLE_NAME = 18071
    """ Name of selected architectural style, type=string"""

    BENDING_DIMENSIONS_ACI_A_R = 18072

    BENDING_SHAPE_KEY_ACI = 18073

    FLAMMABILITY_RATING = 18074
    """ IFC flammability rating, type=string"""

    ENTRANCE_LEVEL = 18075
    """ IFC entrance level, type=int"""

    DURABILITY_RATING = 18076
    """ Durability rating, type=string"""

    HYGROTHERMAL_RATING = 18077
    """ Hygrothermal rating, type=string"""

    ABOVE_GROUND = 18078
    """ IFC above ground, type=int"""

    AUTOMATIC_SPRINKLER_PROTECTION = 18079
    """ IFC sprinkler protection, automatic, type=int"""

    PREAST_ELEMENT_ROTATION_DIRECTION = 18081

    LOAD_BEARING_CAPACITY = 18082
    """ IFC load-bearing capacity, type=float """

    BENDING_DIMENSIONS_ACI_A = 18091

    BENDING_DIMENSIONS_ACI_B = 18092

    BENDING_DIMENSIONS_ACI_C = 18093

    BENDING_DIMENSIONS_ACI_D = 18094

    BENDING_DIMENSIONS_ACI_E = 18095

    BENDING_DIMENSIONS_ACI_F = 18096

    BENDING_DIMENSIONS_ACI_G = 18097

    BENDING_DIMENSIONS_ACI_H = 18098

    BENDING_DIMENSIONS_ACI_J = 18099

    BENDING_DIMENSIONS_ACI_K = 18100

    BENDING_DIMENSIONS_ACI_O = 18101

    BENDING_DIMENSIONS_ACI_R = 18102

    BIM_OBJECT_ID = 18103
    """ For objects downloaded from BimObject, type=string"""

    SHAPE = 18104

    COATING = 18105

    NAME_OF_STRUCTURAL_CROSS_SECTION = 18106

    BELOW_TERRAIN = 18107
    """ Below terrain -&gt; for Switzerland, type=string"""

    LOAD = 18108
    """ Column load or point load, type=float """

    CONCRETE_OVERLAP = 18109
    """ Concrete overlap, type=int"""

    IMPACT_LOAD = 18110
    """ Impact load, type=float """

    EXPOSED_CONCRETE_CLASS = 18111
    """ Exposed concrete class, type=string"""

    SURFACE_NPK = 18112
    """ Surface NPK for Switzerland, type=string"""

    SPREADER_HEIGHT = 18113
    """ Spreader height for Switzerland, type=string"""

    OPERATION = 18114
    """ Operation, type=string"""

    RELEASE_ID = 18115

    RELEASE_DESCRIPTION = 18116

    BIDITEM = 18117

    SPECIAL_COMPONENT_FOR_REINFORCEMENT = 18118

    MARK_NO__WITH_INDEX_MESHESBARS_IN_ELEMENT_PLAN = 18119
    """ Mark no. with index (meshes/bars) in element plan, type=string"""

    MAXIMUM_DIAMETER_OF_OUTER_LAYER_OF_CROSS_BARS = 18120
    """ Maximum diameter of outer layer of cross bars, type=float """

    STANDARD_LATTICE_GIRDER_HEIGHT = 18121
    """ Standard lattice girder, height, type=float """

    STANDARD_LATTICE_GIRDER_DIAMETER_OF_BOTTOM_BOOM = 18122
    """ Standard lattice girder, diameter of bottom boom, type=float """

    STANDARD_LATTICE_GIRDER_DIAMETER_OF_TOP_BOOM = 18123
    """ Standard lattice girder, diameter of top boom, type=float """

    REBAR_MARK = 18124

    CO_CLASS = 18125
    """ Part of classification, type=string"""

    REBAR_PREFIX = 18126

    SUFFIX_CURRENT_LENGTH_UNIT = 18128

    SUFFIX_CURRENT_AREA_UNIT = 18129

    SUFFIX_CURRENT_VOLUME_UNIT = 18130

    SUFFIX_CURRENT_LENGTH_UNIT_MM = 18131

    SUFFIX_CURRENT_LENGTH_UNIT_CM = 18132

    SUFFIX_CURRENT_LENGTH_UNIT_DM = 18133

    SUFFIX_CURRENT_LENGTH_UNIT_M = 18134

    SUFFIX_CURRENT_AREA_UNIT_MM = 18135

    SUFFIX_CURRENT_AREA_UNIT_CM = 18136

    SUFFIX_CURRENT_AREA_UNIT_DM = 18137

    SUFFIX_CURRENT_AREA_UNIT_M = 18138

    SUFFIX_CURRENT_VOLUME_UNIT_MM = 18139

    SUFFIX_CURRENT_VOLUME_UNIT_CM = 18140

    SUFFIX_CURRENT_VOLUME_UNIT_DM = 18141

    SUFFIX_CURRENT_VOLUME_UNIT_M = 18142

    SUFFIX_CURRENT_WEIGHT_UNIT_KG = 18148

    SUFFIX_CURRENT_WEIGHT_UNIT_TO = 18149

    CURRENT_TYPE_OF_LENGTH_UNIT = 18150

    BENDING_DIMENSIONS_ACI_B1 = 18151

    BENDING_DIMENSIONS_ACI_B2 = 18152

    BENDING_DIMENSIONS_ACI_C1 = 18153

    BENDING_DIMENSIONS_ACI_C2 = 18154

    BENDING_DIMENSIONS_ACI_D1 = 18155

    BENDING_DIMENSIONS_ACI_D2 = 18156

    BENDING_DIMENSIONS_ACI_E1 = 18157

    BENDING_DIMENSIONS_ACI_E2 = 18158

    BENDING_DIMENSIONS_ACI_F1 = 18159

    BENDING_DIMENSIONS_ACI_F2 = 18160

    BENDING_DIMENSIONS_ACI_H1 = 18161

    BENDING_DIMENSIONS_ACI_H2 = 18162

    BENDING_DIMENSIONS_ACI_K1 = 18163

    BENDING_DIMENSIONS_ACI_K2 = 18164

    SUPERIMPOSED_LOAD = 18165
    """ Area load on slab, type=float """

    LENGTHDM_M = 18171
    """ Length[dm] (m) - string, type=string"""

    LENGTHMM_M = 18172
    """ Length[mm] (m) - string, type=string"""

    VARIED_GROUP = 18173

    AXIS_START_POINT_X = 18174

    AXIS_START_POINT_Y = 18175

    AXIS_START_POINT_Z = 18176

    AXIS_END_POINT_X = 18177

    AXIS_END_POINT_Y = 18178

    AXIS_END_POINT_Z = 18179

    OBJECT_ROTATION_ANGLE = 18180

    CUSTOM_CLASSIFICATION_CODE = 18181
    """ For additional classification, type=string"""

    CUSTOM_CLASSIFICATION_DESCRIPTION = 18182
    """ For additional classification, type=string"""

    CLASSIFICATION_SOURCE = 18183
    """ For additional classification, type=string"""

    CLASSIFICATION_EDITION = 18184
    """ For additional classification, type=string"""

    CLASSIFICATION_EDITION_DATE = 18185
    """ For additional classification, type=string"""

    CLASSIFICATION_NAME = 18186
    """ For additional classification, type=string"""

    CLASSIFICATION_DESCRIPTION = 18187
    """ For additional classification, type=string"""

    CLASSIFICATION_LOCATION = 18188
    """ For additional classification, type=string"""

    CLASSIFICATION_REFERENCE_TOKENS = 18189
    """ For additional classification, type=string"""

    DENSITY = 18192
    """ Density, type=float """

    MATERIAL_ID = 18193
    """ Material ID, type=string"""

    MARK_NR_ = 18196
    """ Mark number, type=string"""

    SCHEME = 18197
    """ Schema for mark number, type=string"""

    FIRST_NUMBER = 18198
    """ Starting number for mark number, type=int"""

    CODE = 18199
    """ Material code from Material Catalog, type=string"""

    CONTROL_CODE = 18200

    BENDING_TYPE = 18201

    CHANGE_ORDER_NO = 18202

    CHANGE_ORDER_DESCRIPTION = 18203

    RFI_NO = 18204

    RFI_DESCRIPTION = 18205

    REBAR_STATUS = 18206

    BENDING_DIMENSIONS_ACI_B3 = 18207

    BENDING_DIMENSIONS_ACI_B4 = 18208

    BENDING_DIMENSIONS_ACI_C3 = 18209

    BENDING_DIMENSIONS_ACI_C4 = 18210

    BENDING_DIMENSIONS_ACI_D3 = 18211

    BENDING_DIMENSIONS_ACI_D4 = 18212

    BENDING_DIMENSIONS_ACI_E3 = 18213

    BENDING_DIMENSIONS_ACI_E4 = 18214

    BENDING_DIMENSIONS_ACI_F3 = 18215

    BENDING_DIMENSIONS_ACI_F4 = 18216

    BENDING_DIMENSIONS_ACI_H3 = 18217

    BENDING_DIMENSIONS_ACI_K3 = 18218

    BENDING_DIMENSIONS_ACI_J1 = 18219

    BENDING_DIMENSIONS_ACI_J2 = 18220

    BENDING_DIMENSIONS_ACI_J3 = 18221

    REFERENCE = 18222
    """ IFC-Reference, type=string"""

    START_END_PREP = 18226

    END_END_PREP = 18227

    DEFINITION_BUILDING_SYSTEM = 18231
    """ Definition of group by which building elements are grouped according to a common function within the building., type=string"""

    DEFINITION_OF_BUILDING_SERVICES = 18232
    """ Definition of distribution system groups, designed to receive, store, maintain, distribute, or control the flow of a distribution media., type=string"""

    BUILDING_SYSTEM = 18233
    """ Assignments of group by which building elements are grouped according to a common function within the building., type=string"""

    BUILDING_SERVICES = 18234
    """ Distribution system group assignments, designed to receive, store, maintain, distribute, or control the flow of a distribution media., type=string"""

    DEFINITION_GROUP = 18235
    """ Definition of of any arbitrary group., type=string"""

    GROUP = 18236
    """ Assignments to any arbitrary group., type=string"""

    END_MACHINING_ABBREVIATION = 18237

    CLEAR_WIDTH = 18238
    """ Actual clear width measured as the clear space for accessibility and egress., type=float """

    COUNTER_SLOPE = 18239
    """ Sloping angle of the object, measured perpendicular to the slope - relative to horizontal., type=float """

    MECHANICAL = 18241
    """ dication whether the element is operated machanically or not., type=int"""

    RADIATION_TRANSMITTANCE = 18242
    """ The ratio of incident solar radiation that directly passes through a shading system., type=float """

    RADIATION_REFLECTANCE = 18243
    """ The ratio of incident solar radiation that is reflected by a shading system., type=float """

    TRANSMITTANCE_FOR_VISIBLE_LIGHT = 18244
    """ Fraction of the visible light that passes the shading system at normal incidence., type=float """

    REFLECTANCE_FOR_VISIBLE_LIGHT = 18245
    """ Fraction of the visible light that is reflected by the glazing at normal incidence., type=float """

    SURFACE_ROUGHNESS = 18246
    """ A measure of the vertical deviations of the surface., type=string"""

    SURFACE_COLOR = 18247
    """ The color of the surface., type=string"""

    SUNSHADE_TYPE = 18248

    BUILDING_IDENTIFIER_PERMANENT = 18249
    """ Indicates whether the identity assigned to a building is permanent or temporary., type=int"""

    TYPE_OF_EXECUTION = 18250

    BUILDING_CLASS_FIRE_PROTECTION = 18251
    """ Main fire protection class for the building which is assigned from the fire protection classification table as given by the relevant national building code., type=string"""

    LAST_YEAR_OF_RENOVATION = 18252
    """ Year of last major refurbishment, or reconstruction, of the building., type=string"""

    MONUMENT_PROTECTION = 18253
    """ This builing is listed as a historic building., type=int"""

    SITE_OCCUPANCY_INDEX = 18254
    """ The ratio of the utilization, TotalArea / BuildableArea, expressed as a maximum value., type=float """

    CONSTRUCTION_PHASE = 18256
    """ Construction phase., type=string"""

    DEPARTMENT = 18257
    """ Postal Address: An organization defined address for internal mail delivery., type=string"""

    ADDRESS_LINE_1 = 18258
    """ Postal Address: First line of address, mostly used for building number and street name., type=string"""

    ADDRESS_LINE_2 = 18259
    """ Postal Address: Second, optional line of address, mostly used for aditional specification., type=string"""

    POSTAL_BOX = 18260
    """ Postal Address: Postal box. An address that is implied by an identifiable mail drop., type=string"""

    TOWN = 18261
    """ Postal Address: The name of a town., type=string"""

    REGION = 18262
    """ Postal Address: The name of a region. The counties of the United Kingdom and the states of North America are examples of regions., type=string"""

    POSTAL_CODE = 18263
    """ Postal Address: Postal code. The code that is used by the country's postal service., type=string"""

    COORDINATE_REFERENCE_SYSTEM = 18264
    """ Name by which the coordinate reference system is identified., type=string"""

    SURVEY_POINT_RIGHT_VALUE = 18265
    """ Specifies the location along the easting of the coordinate system of the target map coordinate reference system. , type=string"""

    SURVEY_POINT_HEIGHT_VALUE = 18266
    """ Specifies the location along the northing of the coordinate system of the target map coordinate reference system. , type=string"""

    SURVEY_POINT_HEIGHT = 18267
    """ Orthogonal height relative to the vertical datum specified. , type=string"""

    SURVEY_POINT_ANGLE = 18268
    """ Specifies the rotation angle of the target map coordinate reference system. , type=string"""

    STYLE = 18269
    """ Furniture style description., type=string"""

    NOMINAL_HEIGHT = 18270
    """ Indication of the nominal height of the object. , type=float """

    NOMINAL_LENGTH = 18271
    """ Determines the nominal or specified length of the object. , type=float """

    NOMINAL_DEPTH = 18272
    """ Determines the nominal depth or specified depth of the object. , type=float """

    MAIN_COLOR = 18273
    """ Indication of the main color of this type of furniture. , type=string"""

    BUILT_IN = 18274
    """ Indication whether the furniture type is built-in (TRUE) or not (FALSE). , type=int"""

    USED = 18275
    """ Indication whether the element is integrated into a workstation (TRUE) or not (FALSE). , type=int"""

    GROUP_NUMBER = 18276
    """ Indication of the group number, e.g. for panels, work surfaces, storage, etc. , type=string"""

    NOMINAL_WIDTH = 18277
    """ Indication of the nominal width of the object. , type=float """

    SURFACE_TREATMENT = 18278
    """ Specifying the surface treatment of the system furniture elements of this type, such as 'walnut' or 'fabric'. , type=string"""

    SAFETY_STANDARD = 18279
    """ Safety standard (BG Bau), type=string"""

    LOAD_CLASS = 18280
    """ Load class (BG Bau), type=string"""

    WIDTH_CLASS = 18281
    """ Width class (BG Bau), type=string"""

    BRAND = 18283
    """ Brand name (Leviat, general), type=string"""

    HOMEPAGE_DEVELOPER = 18284
    """ Homepage developer (Leviat, general), type=string"""

    CERTIFICATES = 18285
    """ Certificates (Leviat, general), type=string"""

    STANDARDS = 18286
    """ Standards (Leviat, general), type=string"""

    COPYRIGHT = 18287
    """ Copyright (Leviat, general), type=string"""

    MANHOLE_INLET_4 = 18288
    """ Manhole inlet 4, type=float """

    MANHOLE_INLET_5 = 18289
    """ Manhole inlet 5, type=float """

    MANHOLE_INLET_6 = 18290
    """ Manhole inlet 6, type=float """

    MANHOLE_INLET_7 = 18291
    """ Manhole inlet 7, type=float """

    MANHOLE_INLET_8 = 18292
    """ Manhole inlet 8, type=float """

    MANHOLE_INLET_9 = 18293
    """ Manhole inlet 9, type=float """

    WINDOW_TYPE = 18294
    """ Window type, type=string"""

    SURFACE_WEATHERBOARD = 18295
    """ Surface weatherboard, type=string"""

    BASE_MATERIAL = 18296
    """ Specification about the material in which the window will be fixed, type=string"""

    WHEELCHAIR_RAMP = 18297
    """ Threshold wheelchair ramp available, type=string"""

    TG_INSIDE = 18298
    """ Specification tempered glass inside, type=int"""

    LSG_INSIDE = 18299
    """ Specification laminated safety glass inside, type=int"""

    LSG_OUTSIDE = 18300
    """ Specification laminated safety glass outside, type=int"""

    MAP_PROJECTION = 18301
    """ Name by which the map projection is identified, e.g. 'UTM', 'Gaus-Krueger'., type=string"""

    MAP_ZONE = 18302
    """ Name by which the map zone, relating to the MAP_PROJECTION, is identified, like '32' for UTM32., type=string"""

    MAP_UNIT = 18303
    """ Length unit of the coordinate axes composing the map coordinate system., type=string"""

    DATE__TIME_ORDERED = 18304

    DATE__TIME_SHEARED = 18305

    DATE__TIME_BENT = 18306

    DATE__TIME_THREADED = 18307

    DATE__TIME_LOADED = 18308

    DATE__TIME_SHIPPED = 18309

    DATE__TIME_PLACED = 18310

    LOADER_ID = 18311

    UNLOADER_ID = 18312

    ATTRIBUTE_SET_CATEGORY = 18313
    """ Attribute set category to link attribute set, type=string"""

    EMPTY_DRILLING = 18315
    """ Civil engineering/excavation pit, type=float """

    DRILLING_METHOD = 18316
    """ Civil engineering/excavation pit, type=string"""

    VIEW_AREA = 18317
    """ Civil engineering/excavation pit, type=float """

    REINFORCED = 18318
    """ Civil engineering/excavation pit, type=int"""

    VIEW_PLANE = 18319
    """ Civil engineering/excavation pit, type=float """

    MAXIMUM_GRAIN_SIZE = 18320
    """ Maximum grain concrete, type=string"""

    STEEL_GRADE = 18321
    """ Civil engineering/excavation pit, type=string"""

    BEAM_INSTALLATION = 18322
    """ Civil engineering/excavation pit, type=string"""

    AXIS_OFFSET = 18323
    """ Civil engineering/excavation pit, type=float """

    INSULATION_THICKNESS = 18324
    """ Insulation thickness/thickness, type=float """

    G_VALUE = 18325
    """ Total energy transmittance g value, type=float """

    UW_VALUE = 18326
    """ Thermal transmittance Uw [W/m2K], type=float """

    UG_VALUE = 18327
    """ Thermal transmittance Ug [W/m2K], type=float """

    UF_VALUE = 18328
    """ Thermal transmittance Uf [W/m2K], type=float """

    UCW_VALUE = 18329
    """ Ucw value [W/m2K], type=float """

    LIGHT_TRANSMITTANCE = 18330
    """ Light transmittance, type=float """

    SPECTRUM_MATCHING_VALUE_C = 18331
    """ Spectrum matching value C (sound absorption), type=int"""

    SPECTRUM_MATCHING_VALUE_CTR = 18332
    """ Spectrum matching value Ctr , type=int"""

    IMPOSED_LOAD = 18333
    """ Imposed load, type=float """

    AMOUNT_OF_WORK = 18334
    """ Amount of work, type=float """

    CONSISTENCY_CLASS = 18335
    """ Consistency class, type=string"""

    MASONRY_BEARING = 18336
    """ Masonry bearing, type=string"""

    E_MODULE = 18337
    """ E-module, type=float """

    SHRINKAGE_DIMENSION = 18338
    """ Shrinkage dimension, type=string"""

    EXPOSED_CONCRETE = 18339
    """ Exposed concrete yes/no, type=int"""

    FOOTSTEP_SOUND_LEVEL_REDUCTION = 18340
    """ Footstep sound level reduction, type=float """

    SD_VALUE = 18341
    """ Water vapor diffusion equivalent air layer thickness, type=float """

    PRACTICAL_DEGREE_OF_SOUND_ABSORPTION = 18342
    """ Rated building sound insulation index R'w, type=int"""

    RATED_SOUND_ABSORPTION_COEFFICIENT = 18343
    """ Rated building sound insulation index R'w, type=int"""

    CHLORIDE_CLASS = 18344
    """ Chloride class, type=string"""

    CHLORIDE_CONTENT = 18345
    """ Chloride content in percent, type=float """

    WALLING_TYPE = 18346
    """ Walling type/bond types, type=string"""

    MARK_NUMBER_TEXT = 18347
    """ Mark number in text format, type=string"""

    XPLAN_VERSION = 18352
    """ Project attribute: XPlan version (5.3, 4.1, ...), type=string"""

    XPLAN_CLASS = 18353
    """ Project attribute: XPlan class (BP_Plan, FP_Plan, RP_Plan, LP_Plan, SO_Plan), type=string"""

    XPLAN_ATTRIBUTES = 18354
    """ Project attribute: XPlan attributes, type=string"""

    XPLAN_OBJECT_VERSION = 18355
    """ XPlan version (5.3, 4.1, ...), type=string"""

    XPLAN_OBJECT = 18356
    """ XPlan object type (any BP_.., FP_.., ...), type=string"""

    XPLAN_OBJECT_ATTRIBUTES = 18357
    """ XPlan object attributes, type=string"""

    ATTRIBUTE_SET_OBJECT = 18358
    """ Attribute set objekt to link attribute set, type=string"""

    XPLAN_COORDINATE_SYSTEM = 18362
    """ Project attribute: XPlan coordination system (EPSG code), type=string"""

    GROUTING_LINE = 18363
    """ Civil engineering/excavation pit, type=float """

    FREE_LENGTH_SYSTEM = 18364
    """ Civil engineering/excavation pit, type=float """

    LIFE_CYCLE = 18365
    """ Civil engineering/excavation pit, type=int"""

    VERTICAL_INCLINATION = 18366
    """ Civil engineering/excavation pit, type=float """

    HORIZONTAL_INCLINATION = 18367
    """ Civil engineering/excavation pit, type=float """

    CHARACTERISTIC_ANCHORING_FORCE = 18368
    """ Civil engineering/excavation pit, type=float """

    TEST_FORCE = 18369
    """ Civil engineering/excavation pit, type=float """

    CLAMPING_FORCE = 18370
    """ Civil engineering/excavation pit, type=float """

    ULTIMATE_LOAD = 18371
    """ Civil engineering/excavation pit, type=float """

    LOAD_AT_YIELD_STRENGTH = 18372
    """ Civil engineering/excavation pit, type=float """

    NUMBER_OF_STRANDS = 18373
    """ Civil engineering/excavation pit, type=int"""

    STRAND_DIAMETER = 18374
    """ Civil engineering/excavation pit, type=float """

    BEAM_DIAMETER = 18375
    """ Civil engineering/excavation pit, type=float """

    REMOVABLE = 18376
    """ Civil engineering/excavation pit, type=int"""

    REGROUT = 18377
    """ Civil engineering/excavation pit, type=int"""

    PRESTRESSED = 18378
    """ Civil engineering/excavation pit, type=int"""

    ANCHOR_TYPE = 18379
    """ Civil engineering/excavation pit, type=string"""

    CORROSION_PROTECTION = 18380
    """ Civil engineering/excavation pit, type=string"""

    STEEL_GRADE_TENSION_MEMBER = 18381
    """ Civil engineering/excavation pit, type=string"""

    MATERIAL_GROUT_BODY = 18382
    """ Civil engineering/excavation pit, type=string"""

    ANCHOR_LOCATION = 18383
    """ Civil engineering/excavation pit, type=string"""

    SCOPE = 18384
    """ Civil engineering/excavation pit, type=string"""

    DRILLING_DIAMETER = 18385
    """ Civil engineering/excavation pit, type=float """

    DOUBLE_PROFILE_GAP = 18387
    """ Double profile gap, type=float """

    HEIGHT_IFC = 18392

    DIAMETER_IFC = 18393

    CLASH_FLAG = 18400

    CLASH_NUMBER = 18401

    CLASH_TYPE = 18402

    CLASH_DEPTH = 18403

    CLASH_PRIORITY = 18404

    CLASH_DATE_TIME = 18405

    CLASH_COMPONENT_A_GUID = 18406

    CLASH_COMPONENT_B_GUID = 18407

    CLASH_COMPONENT_A_DRAWING_FILE = 18408

    CLASH_COMPONENT_B_DRAWING_FILE = 18409

    CLASH_COMPONENT_A_OBJECT_NAME = 18410

    CLASH_COMPONENT_B_OBJECT_NAME = 18411

    CLASH_STATUS = 18412

    CLASH_DEPTH_TOLERANCE_HARD_CLASH = 18413

    CLASH_DEPTH_TOLERANCE_SOFT_CLASH = 18414

    CLASH_COMPONENTS = 18415

    CUT = 18417
    """ Civil engineering/excavation pit, type=float """

    FILL = 18418
    """ Civil engineering/excavation pit, type=float """

    CONSTRAINED_MODULUS = 18419
    """ Civil engineering/excavation pit, type=float """

    INNER_FRICTION_ANGLE = 18420
    """ Civil engineering/excavation pit, type=float """

    WET_UNIT_WEIGHT_OF_SOIL = 18421
    """ Civil engineering/excavation pit, type=float """

    UNIT_WEIGHT_OF_SOIL = 18422
    """ Civil engineering/excavation pit, type=float """

    UNDRAINED_COHESION = 18423
    """ Civil engineering/excavation pit, type=float """

    DRAINED_COHESION = 18424
    """ Civil engineering/excavation pit, type=float """

    DOUBLE_PROFILE_CONFIGURATION = 18425
    """ Double profile configuration, type=float """

    BOLT_FRICTION_BEARING_CONDITION = 18427

    FIELD_BOLTED = 18428
    """ Steel bolt is bolted on-construction-site, type=int"""

    TENSION_CONTROLLED_BOLT = 18429

    FIELD_WELDED = 18430
    """ Welding is done on-construction-site, type=int"""

    STITCHED_WELD = 18431

    WELD_ALL_AROUND = 18432

    PREQUALIFIED_WELD_TAIL_POSITION = 18433

    PREQUALIFIED_WELD_TAIL_PROCESS = 18434

    PREQUALIFIED_WELD_TAIL_TEXT = 18435

    WELD_ROOT_FACE = 18436

    WELD_ROOT_OPENING = 18437

    WELD_SETBACK_LEFT = 18438

    WELD_SETBACK_RIGHT = 18439

    WELD_CONTOUR = 18440

    USE_FILLET_BACKUP_WELD = 18441

    WELD_STITCH_LENGTH = 18442

    WELD_STITCH_SPACING = 18443

    WELD_STITCH_TERMINATION_LEFT = 18444

    WELD_STITCH_TERMINATION_RIGHT = 18445

    MATERIAL_USE = 18446

    AUSSCHREIBEN_DE = 18447
    """ Atttribute for connection to ausschreiben.de, type=string"""

    BENDING_DIMENSIONS_BS8666_A_R = 18461

    BENDING_DIMENSIONS_BS8666_A = 18462

    BENDING_DIMENSIONS_BS8666_B = 18463

    BENDING_DIMENSIONS_BS8666_C = 18464

    BENDING_DIMENSIONS_BS8666_D = 18465

    BENDING_DIMENSIONS_BS8666_E = 18466

    BENDING_DIMENSIONS_BS8666_F = 18467

    BENDING_DIMENSIONS_BS8666_R = 18468

    FORM_OF_DELIVERY = 18469
    """ Form of delivery, type=string"""

    MOMENT_OF_INERTIA = 18470
    """ Moment of inertia, type=float """

    ELASTIC_SECTION_MODULUS = 18471
    """ Elastic section modulus, type=float """

    PLASTIC_SECTION_MODULUS = 18472
    """ Plastic section modulus, type=float """

    STATIC_MOMENT = 18473
    """ Static moment, type=float """

    COATING_AREA = 18474
    """ Coating area, type=float """

    LCA_CLASS = 18476
    """ OneClick Life Cycle Assessment Class, type=string"""

    LCA_TRANSPORT_DISTANCE = 18477
    """ LCA transport distance in kilometers, type=float """

    SYSTEM = 18479

    COST_GROUP = 18490
    """ for example DIN 276 classification, type=string"""

    WELDED_LOCK = 18491
    """ Welded lock for Sheet pile wall, type=string"""

    NAME_OF_SCHEME = 18494
    """ Name of Schema for mark number, type=string"""


```

</details>