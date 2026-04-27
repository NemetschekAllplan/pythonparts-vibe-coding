# Brain - Accumulated Project Knowledge

> Auto-growing. Insert new learnings at the top.
> Categories: [API], [Geometry], [Palette], [Reinforcement], [Workflow], [Debugging]
> Never delete - only add or refine.

---
### [2026-04-14] Pergola: Lamellenhoehe-Default 20 mm und stabiler Setzpfad
- **Kontext:** Nach Korrekturen zeigte die Vorschau korrekt, beim Absetzen traten teils wieder U-Profile auf.
- **Problem:** Geometrieaufbau ueber `append_geometry_3d`-Pfad war in diesem Profilfall nicht durchgaengig reproduzierbar.
- **Lösung:** Lamellengeometrie direkt als `AllplanBasisEle.ModelElement3D`-Liste aufbauen und dennoch als editierbares PythonPart via `PythonPartUtil.create_pythonpart(...)` erzeugen; Default `LamellenHoehe` auf `20 mm` gesetzt.
- **Regel:** Bei Profilabweichungen zwischen Preview und Setzen den Geometrieaufbau auf direkte `ModelElement3D`-Objekte vereinfachen und Editierbarkeit ueber `PythonPartUtil` beibehalten.

### [2026-04-14] Pergola-Interlock: gleiche Endfuge an markierten Spitzen
- **Kontext:** Im geschlossenen Zustand beruehrten sich die gegeneinander laufenden Profilenden lokal trotz korrekter Grundkontur.
- **Problem:** Gleiche Profilhoehe an beiden Gegenstegen fuehrte an den markierten Spitzen zu Kontakt statt Luftfuge.
- **Lösung:** Effektive Steghoehe fuer beide Endstege um eine gemeinsame `tip_clearance` reduziert (`lip_height = LamellenHoehe - tip_clearance`), mit `tip_clearance = interlock_gap`.
- **Regel:** Bei ineinandergreifenden Lamellen Endfuge explizit als eigener Geometriewert fuehren und symmetrisch auf beide Gegenspitzen anwenden.

### [2026-04-14] Pergola-Lamellen: Geschlossen-Zustand mit Schliesswinkel + Mehrbreite
- **Kontext:** Profilform war korrekt, aber im Zustand `Geschlossen` griffen Lamellen noch zu flach ineinander.
- **Problem:** Bei exakt 0-Grad-Schliesslage und ohne zusaetzliche Profilbreite entsteht zu geringe Ueberdeckung im Endbereich.
- **Lösung:** `Geschlossen` auf kleinen Schliesswinkel (`5 Grad`) gesetzt, Profilspanne um `8 mm` vergroessert und Luftfuge bei `2.5 mm` gehalten.
- **Regel:** Fuer regensichere Lamellen den geschlossenen Zustand nicht zwingend als 0 Grad modellieren; kleine Schliessneigung plus kontrollierte Mehrbreite verbessert Interlock ohne Kontakt.

### [2026-04-14] Pergola-Lamellenprofil per Nutzerfeedback bestaetigt
- **Kontext:** Nach mehreren Iterationen zur Pergola-Lamelle wurde die Zielkontur durch Nutzerfeedback als korrekt bestaetigt.
- **Loesung:** Lamelle als `└────┐`-Profil (links Upstand, horizontaler Steg, rechts Downstand) mit Pitch + Ueberdeckung umgesetzt und als editierbares PythonPart ueber `PythonPartUtil.create_pythonpart(...)` ausgegeben.
- **Regel:** Bei bioklimatischen Lamellen zuerst die geschlossene Verzahnungslogik am Querschnitt sichern und danach zwingend Editierbarkeit des gesetzten PythonParts pruefen.

### [2026-04-14] Pergola-Zprofil: Editierbarkeit hat Vorrang beim Ausgabeweg
- **Kontext:** Nach Umstellung auf direkte `ModelEleList`-Rueckgabe war die Lamellenkontur sichtbar stabil, aber das gesetzte Objekt nicht mehr als editierbares PythonPart nutzbar.
- **Problem:** Direkte Geometrieausgabe (`CreateElementResult(elements=model_list)`) erzeugt kein vollwertiges, parametereditierbares PythonPart-Containerobjekt.
- **Lösung:** Fuer editierbare Ergebnisse wieder `PythonPartUtil.add_pythonpart_view_2d3d(...)` + `create_pythonpart(build_ele)` verwenden.
- **Regel:** Wenn ein Bauteil nach dem Setzen nicht editierbar ist, zuerst den Ausgabeweg auf `PythonPartUtil.create_pythonpart(...)` zurueckstellen.

### [2026-04-14] Pergola-Lamellen: Preview-vs-Setzen mit direktem ModelEleList stabilisiert
- **Kontext:** `Pergola_ZProfil` zeigte in der Vorschau die korrigierte Kontur, nach dem Absetzen wirkte das Profil erneut wie U.
- **Problem:** Ausgabe über `PythonPartUtil.add_pythonpart_view_2d3d(...)` kann je Darstellungs-/Ableitungspfad zu abweichender Konturwirkung zwischen Preview und erzeugtem Element führen.
- **Lösung:** Geometrie direkt als `ModelEleList` mit `append_geometry_3d(...)` zurückgeben (`CreateElementResult(elements=model_list, handles=...)`), ohne zusätzlichen View-Wrapper.
- **Regel:** Wenn Profilkonturen zwischen Vorschau und gesetztem Element differieren, zuerst auf direkten `ModelEleList`-Ausgabeweg umstellen und Verhalten erneut prüfen.

### [2026-04-14] Pergola-Lamellen: echtes Z-Profil statt U/C-Anmutung
- **Kontext:** `Pergola_ZProfil` zeigte im Querschnitt eine U/C-Anmutung; Nutzer forderte regensicheres Z-Profil.
- **Problem:** Oberer und unterer Flansch lagen auf derselben Seite der Stegachse; dadurch wirkte das Profil nicht wie ein Z.
- **Lösung:** Lamellenquerschnitt auf gegensinnig versetzte Flansche umgestellt (oben und unten entgegengesetzt), Steg auf Innenhoehe begrenzt.
- **Regel:** Bei Z-Lamellenprofilen Flansche immer spiegelversetzt zur Stegmitte modellieren; gleichseitige Flansche erzeugen eine C/U-Wirkung.

# Allplan 2026 PythonParts API Knowledge Base

## Purpose
This document captures reusable API patterns, stability rules, and debug heuristics for Allplan 2026 PythonParts.
The focus is generic implementation knowledge that can be applied to new tools without depending on existing project scripts.

## 1) Interactor Boot and Lifecycle

### 1.1 Robust `create_interactor` handling
- Use `create_interactor(*args)` and support multiple call signatures.
- In practice, signatures can differ by context (for example 1 arg, 7 args, 8 args).
- Do not hard-fail when argument shape changes.
- Prefer guarded extraction and type checks over fixed index assumptions.

### 1.2 Abstract method completeness
- Ensure all abstract methods required by `BaseInteractor` are implemented.
- Missing one required method can block instantiation at startup.

### 1.3 Palette visibility
- Interactor execution does not guarantee visible palette controls.
- Initialize palette service explicitly and call its show method.
- Add guards for empty or mismatched `build_ele_list` and `control_props_list`.

## 2) Selection and Adapter Handling

### 2.1 Stable selection processing
- Treat selection order as unstable unless explicitly guaranteed.
- Derive anchors and order by geometry/logic, not by raw API return order.

### 2.2 Parent-child safety
- When transforming architectural objects, include hierarchy awareness.
- Normalize to root where needed and handle child adapters in delete sets.
- Ausnahme (RoomArrange/Architektur-Raeume): Child-Delete nur gezielt einsetzen; pauschales Tree-Delete kann Architekturfuellungen/Elementzustand beschaedigen.

### 2.3 No-op filtering
- Exclude elements with effectively zero shift from delete/create batches.
- This avoids side effects and unnecessary element recreation.

## 3) Attributes and Metadata

### 3.1 Safe attribute reads
- Prefer attribute reads with explicit read state where required by API.
- Use service fallback when direct adapter call fails.

### 3.2 Classification strategy
- Build classification from robust metadata sources (function/use/type).
- Keep mapping tables configurable in palette parameters.
- Provide deterministic fallback category when metadata is missing.

## 4) Geometry and Bounding Boxes

### 4.1 Geometry source fallback chain
- Query multiple geometry entry points in a guarded sequence.
- Build 2D bounds from extracted XY points.
- Log geometry source used for each element to simplify debugging.

### 4.2 String-based fallback parsing
- If parsing geometry from strings, guard against class-name digits.
- Validate parsed coordinates with plausibility checks.

### 4.3 Coordinate utilities
- Maintain consistent helpers for:
- bbox center
- bbox size
- overlap and gap checks
- axis span and axis shift

## 5) Transformation and Write-Back

### 5.1 Reliable move pattern
- Read model from adapter.
- Apply matrix translation.
- Delete originals.
- Create transformed models.

### 5.2 Operation order
- Delete before create in recreate workflows where identity conflicts can occur.

### 5.3 Batch behavior
- Plan all target vectors first, then execute write-back in batch.
- Avoid sequential mutation based on stale adapter references.

## 6) Layout and Collision Patterns

### 6.1 Deterministic layout over free scoring
- For reproducible results, prefer deterministic row/band placement.
- Use sorting keys with explicit priority and tie-breakers.

### 6.2 Gap-correct placement
- Gap constraints must be enforced on final bounding boxes, not only candidate positions.
- Post-placement compact passes can reduce leftover voids while preserving minimum gap.

### 6.3 Collision scopes
- Keep collision scopes intentional.
- If two logical groups should align to the same reference line, do not let one group push the other along the same axis.

### 6.4 Anchor-aware reference lines
- If layout references an anchor edge, define clearly:
- which anchor edge per axis
- whether first element starts with or without edge gap
- which objects are allowed to influence that reference during collision resolution

## 7) Logging Standard

### 7.1 Required context per run
- timestamp
- script build/version
- log path
- selection count
- parameter snapshot

### 7.2 Required context per element
- classification result
- bbox source and bbox values
- planned dx/dy and move decision

### 7.3 End-of-run summary
- moved count
- total count
- overlap count after resolution
- create/delete counts for write-back

## 8) Stability Checklist for New PythonParts
- Implement robust interactor signature handling.
- Implement all required abstract interactor methods.
- Ensure palette service opens reliably.
- Use guarded geometry fallback chain.
- Validate bbox extraction.
- Separate planning from write-back.
- Filter no-op moves.
- Keep logs actionable and complete.
- Run at least one manual smoke pass and inspect logs.

## 9) Debug Workflow
- Reproduce with minimal deterministic input set.
- Confirm script build in log first.
- Verify parameter snapshot.
- Verify anchor/reference decisions.
- Verify per-element planned shifts.
- Verify overlap result and batch recreate counts.
- Apply one small fix at a time and retest.

## 10) Validated UX Patterns (TicTacToe Demo)

### 10.1 Keep core mechanics stable
- Preserve proven gameplay core once accepted by user.
- Prefer additive options (mode, difficulty, palette organization) over logic rewrites.

### 10.2 Difficulty as move selection policy
- Keep Minimax unchanged as ground truth evaluator.
- Implement difficulty by probabilistic choice among scored legal moves.
- Keep `Unbeatable` as strict best-move mode.

### 10.3 Mode switch without branching complexity
- Support `Player/AI Assistant` and `Player/Player` with one shared click pipeline.
- In PvP, alternate the active marker by state, not by duplicated handlers.
- Reuse existing winner/draw checks in both modes.

### 10.4 Palette usability improvements
- Separate gameplay controls from tuning options.
- Use a main page for active gameplay (`Game`) and a settings page (`Einstellungen`).
- Hide non-essential status fields when they do not add value for users.
- Use role-neutral scoreboard labels that work for both PvP and AI mode.

## 11) Color Index Reference (Line Color)

### 11.1 Observed mapping from user screenshot (Allplan line color list)
- Index `1`: blue
- Index `2`: yellow
- Index `3`: cyan / turquoise
- Index `4`: green
- Index `5`: magenta
- Index `6`: red
- Index `7`: deep blue
- Index `8`: orange
- Index `9`: very light gray / off-white
- Index `10`: pale yellow-green
- Index `11`: light green
- Index `12`: brown
- Index `13`: warm gray / brown-orange
- Index `14`: neutral gray
- Index `15`: purple
- Indices `16..30`: grayscale ramp (dark to light tones)

### 11.2 Usage note
- Treat this as project-local baseline from the provided screenshot.
- Allplan office/color-table settings can override visual appearance.
- For stable visuals in previews, avoid assumptions that index names are globally identical across offices.

## 12) Color Index Reference (Filling)

### 12.1 Observed mapping from user screenshot (Allplan filling color list)
- Index `0`: black
- Index `1`: near-black / very dark gray
- Index `2`: yellow
- Index `3`: cyan / turquoise
- Index `4`: green
- Index `5`: magenta
- Index `6`: red
- Index `7`: deep blue
- Index `8`: orange
- Index `9`: very light gray / off-white
- Index `10`: pale yellow-green
- Index `11`: light green
- Index `12`: ochre / mustard brown
- Index `13`: brown-orange
- Index `14`: medium brown
- Index `15`: purple
- Indices `16..31`: grayscale ramp (dark to light tones)

### 12.2 Usage note
- This mapping is derived from the provided filling-color screenshot.
- Keep in mind that office color-table settings can still shift appearance per workstation.

## 13) Chessboard Pattern Rendering (Validated in Chess)

### 13.1 Stable approach for checkerboard background
- Do not rely on line/pattern hatch for checkerboard preview rendering.
- Use `FillingElement` with `FillingProperties` (`TransitionType.eNoTransition`) for solid field fill.
- In preview, rectangular fill polygons can appear as half-filled triangles in some modes.
- Stable fix: draw each board square as **two filled triangles** (same color) instead of one rectangle polygon.

### 13.2 Recommended rendering settings
- Use `DrawElementPreview(..., bDirectDraw=False)` for more reliable filled area preview behavior.
- Keep a guarded fallback path to plain polygon rectangles if filling creation fails.
- Log fallback activation so preview issues can be diagnosed quickly.

### 13.3 Color control for later changes
- Define two dedicated color indices for board squares and use only these values in board rendering:
- `light_square_fill_index` (currently `29`)
- `dark_square_fill_index` (currently `26`)
- To change board look later, only change these two indices, not drawing logic.

## 14) Chess UX and Preview Learnings (Validated)

### 14.1 Player naming and UX wording
- If player 1 uses red piece color (index `6`), align text labels with user language:
- Use `Rot` instead of `Weiss` in status and win/check messages.
- Keep naming consistent across palette status and dialog line text.

### 14.2 Hover preview color behavior
- Use distinct hover states for clear interaction feedback:
- Empty cell hover: green outline (`4`).
- Own piece hover: blue outline (`7`) to avoid office tables where `1` can appear near-black.
- Keep hover as double-outline (outer + inner rectangle) for visibility over filled backgrounds.

### 14.3 Legal move preview (selected piece)
- Keep legal destination cells highlighted in yellow (`2`).
- Add line-based move preview for better readability:
- `R/B/Q`: draw directional rays to farthest legal cell per direction.
- `N`: draw jump markers (small X) on legal target cells.
- `K/P`: draw direct line from source to each legal target.
- This gives a "maximal path" feeling without changing chess rules.

### 14.4 Targeting enemy pieces while aiming
- If a piece is selected and hovered field contains an enemy piece:
- Show special target outline only when `(hovered_field in legal_moves)`.
- Use current player color for target outline (player 1 red `6`, player 2 black `1` in this project).
- This avoids false attack indicators and keeps rule correctness.

### 14.5 Stability guards for previews

## 15) BetonStuetze Learnings (Allplan 2026)

### 15.1 Start-Checkliste fuer Standard-PythonParts (kritisch)
- Erste lauffaehige Version immer minimal halten: `check_allplan_version`, `create_element`, `create_preview`.
- Imports strikt auf benoetigte Module begrenzen und Import-Fehler frueh loggen.
- In `create_element` immer top-level `try/except` mit `CreateElementResult()` als Fallback verwenden.
- Bereits beim Modulladen eine Build-Kennung loggen (`Script build`) und bei jedem Aufruf `create_element called`.
- Parameter robust lesen (`getattr(..., None)` + default), damit fehlende/alte Palette-Felder den Start nicht blockieren.
- `.py` und `.pyp` Parameternamen muessen 1:1 passen. Bei Umbenennung Legacy-Fallback im Code behalten.
- Vor erstem Allplan-Test lokal mindestens `python -m py_compile <script>.py` ausfuehren.

### 15.2 NOI-Fehler ohne Python-Traceback richtig einordnen
- Wenn im Log nur `module loading`, `check_allplan_version`, `create_element` erscheint und kein Traceback folgt,
  liegt die Ursache meist in nativer API-Geometrie/Bewehrung, nicht in einer normalen Python-Exception.
- In diesem Fall letzte komplexe Geometrieaenderung isolieren und auf stabile Builder-Varianten zurueckgehen.
- Aenderungen in kleinen Schritten: erst wieder stabil starten lassen, dann Geometrie fachlich verfeinern.

### 15.3 Bewehrungs-Formen: stabile Reihenfolge der Umsetzung
- Zuerst stabile Standardformen (`create_longitudinal_shape_with_hooks`, `create_stirrup_with_user_hooks`) verwenden.
- Freiform/Kroepfung erst danach und kontrolliert ueber `GeneralReinfShapeBuilder.create_freeform_shape_with_hooks`.
- Keine riskanten Low-Level-Formpfade als erste Version einsetzen, wenn bekannt ist, dass sie zu NOI-Abstuerzen fuehren koennen.

### 15.4 Fachlogik Kroepfung und Richtung
- Kroepfung der Anschlussbewehrung als durchgehender Stab ausbilden, nicht als separater versetzter Zusatzstab.
- Kroepfung immer zur Stuetzenmitte orientieren; Richtungsvektor je Stab aus aktueller Stabposition zur Querschnittsmitte bilden.
- Rotationsabbildung sauber pruefen (Vorzeichenfehler fuehren zu scheinbar zufaelliger Drehrichtung in Quadranten).

### 15.5 Einheiten-Regel (Projektkonvention)
- Bewehrungsdurchmesser und geometrische Detailmasse in mm.
- Anschlussbewehrungslaenge in der Palette in m anbieten (`ConnectionRebarLengthM`, Standard `1.0`) und intern in mm umrechnen.
- Beschriftung in der Palette muss die Einheit explizit zeigen, um Fehleingaben zu vermeiden.
- Keep rendering paths inside guarded blocks and avoid silent failures.
- Prefer small additive visual features (extra outlines/lines) over replacing core draw logic.
- After each visual iteration, run at least a compile smoke check and quick in-Allplan hover/click validation.

### [2026-02-23] Anchor-Referenz bei Band-Layout
- **Kontext:** RoomArrangeByRules (Interactor), Reihenstart im Band-Layout auf Szenenkante umgestellt.
- **Problem:** Anchor-Raum blieb technisch fix, lag im Gesamtlayout aber relativ falsch; zudem traten Ueberlagerungen bei leerem Corridor-Set auf.
- **Lösung:** Reihenstart wieder an Anchor-Kante (`_compute_row_start_from_anchor_edge`) und Anchor explizit in POS/NEG-Kollisions-Scope aufnehmen.
- **Regel:** Bei anchor-gefuehrten Layouts keine globale Szenenkante als Startreferenz verwenden, wenn die Anchor-Lage fachlich stabil bleiben muss.

### [2026-02-23] Gap-Offset ohne Flurraeume
- **Kontext:** RoomArrangeByRules, Fall mit `corridor_count=0`.
- **Problem:** `Gap` wurde in der Band-Referenz so angewendet, dass die anchor-nahe Reihenkante um `gap` versetzt war.
- **Lösung:** Bei leerem Flur-Set `band_center` um genau `gap_mm` verschieben, damit Anchor-Kante und Reihenkante fluchten.
- **Regel:** Ohne dedizierte Flurraeume den Gap-Offset in der Band-Referenz explizit behandeln, sonst entstehen scheinbar falsche 0.25-m-Versaetze.

### [2026-02-23] Leere Anforderungsdatei als MVP-Fallback
- **Kontext:** Aufgabe verwies auf `stefansstütze.md`, Datei war leer.
- **Problem:** Keine fachlichen Sonderregeln fuer Geometrie-/Bewehrungsableitung verfuegbar.
- **Lösung:** MVP mit klaren Annahmen umgesetzt (rechteckige, achsparallele Stuetze; 2D-Fallbackhoehe).
- **Regel:** Wenn Spezifikationsdatei leer ist, Annahmen explizit dokumentieren und als `[UNSICHER]` kennzeichnen.

### [2026-02-23] Script-Object-Vorgabe strikt umsetzen
- **Kontext:** Neue Spezifikation fuer AutoBewehrung verlangte `BaseScriptObject` + `SingleElementSelectInteractor`.
- **Problem:** Interactor-Variante funktional moeglich, aber nicht konform zur geforderten Workflow-Architektur.
- **Lösung:** Umsetzung auf `create_script_object`, `start_input`, `start_next_input`, `execute`, `on_cancel_function` umgestellt.
- **Regel:** Wenn die Aufgabenbeschreibung ein konkretes PythonPart-Pattern nennt, dieses Muster vorrangig und vollstaendig anwenden.

### [2026-02-23] Script-Object Startfehler durch Interactor-Tag
- **Kontext:** Script-Object PythonPart startete mit Meldung `create_interactor not implemented`.
- **Problem:** In der `.pyp` stand `<Interactor>True</Interactor>`, dadurch erwartete Allplan einen Interactor-Einstieg.
- **Lösung:** Fuer Script-Object `<Interactor>False</Interactor>` setzen (oder Tag weglassen), `create_script_object` beibehalten.
- **Regel:** Bei Script-Object-Implementierungen den Interactor-Tag immer gegen die Framework-Doku validieren.

### [2026-02-23] PythonPart-Koerper nicht selektierbar durch strikten Vorfilter
- **Kontext:** AutoBeStuetze Script-Object startete, aber vorhandene von PythonPart erzeugte 3D-Koerper waren nicht auswaehlbar.
- **Problem:** Der `SingleElementSelectInteractor` nutzte einen Vorfilter mit `GetMinPoint/GetMaxPoint`; einige Container/Adapter liefern das in der Selektion nicht zuverlaessig.
- **Lösung:** Vorfilter entfernt (`ele_filter=None`) und 3D-/Geometrievalidierung erst in `execute()` durchgefuehrt.
- **Regel:** Bei heterogenen Adaptertypen Selektion zuerst breit zulassen und fachliche Pruefung nach der Auswahl ausfuehren.

### [2026-02-23] Ausgangspunkt/Winkel-Prompt bei Script-Object unterdruecken
- **Kontext:** Nach Elementselektion fragte AutoBeStuetze zusaetzlich nach Ausgangspunkt/Winkel.
- **Problem:** Framework wechselte in den allgemeinen Platzierungsmodus fuer das `CreateElementResult`.
- **Lösung:** In `execute()` festen `placement_point` setzen (`Point3D(0,0,0)`) und `multi_placement=False`.
- **Regel:** Wenn Ergebnisse bereits in globalen Koordinaten vorliegen, Platzierungsdialog explizit durch gesetzten Placement-Point neutralisieren.

### [2026-02-23] Placement-Dialog robust vermeiden via Direkt-Writeback
- **Kontext:** Placement-Prompt blieb trotz gesetztem `placement_point` in Script-Object bestehen.
- **Problem:** Framework kann weiterhin in den Platzierungsmodus wechseln, wenn `execute()` Elemente zur Platzierung zurueckgibt.
- **Lösung:** Bewehrung in `execute()` direkt per `AllplanBaseElements.CreateElements(...)` schreiben und anschliessend `CreateElementResult()` leer zurueckgeben.
- **Regel:** Wenn keine interaktive Platzierung gewuenscht ist, Ergebnis nicht als zu platzierendes Element zurueckgeben, sondern direkt ins Dokument schreiben.

### [2026-02-23] BoundingBox-Fallback fuer PythonPart-Container
- **Kontext:** AutoBeStuetze konnte selektierte, bereits vorhandene PythonPart-Koerper nicht bewehren.
- **Problem:** `GetMinPoint/GetMaxPoint` und direkte Punktlisten waren am selektierten Adapter unvollstaendig, dadurch `BoundingBox konnte nicht ermittelt werden`.
- **Lösung:** Fallback-Kette erweitert: `CalcMinMax(geo)`, Modellobjekt via `GetElement(...)`, Child-Elemente via `GetChildModelElementsFromTree(...)` und Box-Merge.
- **Regel:** Bei selektierten PythonPart-/Container-Elementen BoundingBox nie nur aus einem Adapterzugriff ableiten.

### [2026-02-23] Text-Parsing als letzter Geometrie-Fallback
- **Kontext:** Selbst erweiterte API-Zugriffe konnten bei bestimmten selektierten Containern keine BoundingBox liefern.
- **Problem:** Geometrieobjekte sind je Adaptertyp heterogen; nicht jeder Typ bietet punktbasierten Zugriff.
- **Lösung:** Als letzte Stufe `repr(...)` von Adapter/Geometrie/Modellobjekt auf Koordinatentupel parsen und daraus Min/Max bilden.
- **Regel:** Bei gemischten Allplan-Objekttypen immer einen robusten String-Fallback vorsehen, um Interaktionsschleifen ohne Ergebnis zu vermeiden.

### [2026-02-23] QRCode2D mit externer Library robust absichern
- **Kontext:** Standard-PythonPart `QRCode2D` erzeugt 2D-Flaechen aus einer `qrcode`-Matrix.
- **Problem:** In Allplan-Umgebungen kann `qrcode` fehlen, was sonst zu stillen Funktionsausfaellen fuehrt.
- **Lösung:** `import qrcode` guarden, im Fehlerfall klare Trace-Meldung inkl. `pip install qrcode[pil]` und leeres `CreateElementResult` zurueckgeben.
- **Regel:** Bei optionalen Drittbibliotheken immer frueh und explizit failen, inkl. Installationshinweis fuer Consultants.

### [2026-02-23] QRCode2D Fallback muss weiterhin Geometrie liefern
- **Kontext:** `QRCode2D` lieferte bei fehlender `qrcode`-Library kein platzierbares PythonPart.
- **Problem:** Leeres `CreateElementResult()` fuehrte zu "nichts wird erstellt", obwohl Script startete.
- **Lösung:** Interne QR-Matrix-Generierung (EC-M, V1..V6) als Fallback integriert und 2D-Module wie im `QRCodeCube`-2D-Pfad aufgebaut.
- **Regel:** Bei nicht-kritischen Drittlibs fuer Kernfunktion immer lauffaehigen algorithmischen Fallback vorsehen, nicht nur Fehlermeldung.

### [2026-02-24] Discovery-Skripte immer mit fixem Workdir ausfuehren
- **Kontext:** Workspace-Discovery fuer automatische master.md-Erstellung mit mehreren Shell-Kommandos.
- **Problem:** Parallel gestartete Kommandos ohne expliziten workdir erzeugten fehlende/unerwartete Ausgabedateien.
- **Lösung:** Alle Datei-schreibenden Discovery-Schritte mit festem Arbeitsverzeichnis ausfuehren und Ausgabe direkt verifizieren.
- **Regel:** Bei Multi-Step-Automation nach jedem Schreibschritt Existenz/Zeilenzahl pruefen, bevor Folgeschritte starten.

### [2026-02-24] Master-Generator robust fuer PowerShell 5 und leere Dateien
- **Kontext:** Rekursiver Workspace-Crawl zur Erstellung einer einzigen `master.md` mit vollstaendig eingebetteten Dateiinhalten.
- **Problem:** `System.IO.Path.GetRelativePath` ist in aelterer PowerShell nicht verfuegbar; `Get-Content -Raw` kann bei leeren Dateien `null` liefern.
- **Lösung:** Relative Pfade per Prefix/Regex ermitteln und `null`-Inhalte vor dem Schreiben auf leeren String setzen.
- **Regel:** Discovery-/Generator-Skripte immer PS5-kompatibel bauen und bei Textaggregation `null`-Guards fuer Dateiinhalte setzen.

### [2026-02-24] PowerShell-Teilarithmetik explizit als Integer halten
- **Kontext:** Aufteilung einer grossen Markdown-Datei in drei gleich grosse Textteile.
- **Problem:** Array-Literal mit eingebettetem `if` fuehrte zu `op_Addition`-/Typkoerzionsfehlern in aelterer PowerShell.
- **Lösung:** Teilgroessen mit expliziten Integer-Variablen (`l1/l2/l3`) berechnen und danach `Substring` anwenden.
- **Regel:** Bei PS5-kompatiblen Skripten Groessenberechnung schrittweise und typstabil statt in kompakten Array-Ausdruecken schreiben.

### [2026-02-24] API-Recherche ohne aggregierte master-Dateien
- **Kontext:** Umsetzung eines neuen Script-Object PythonParts im Workspace ohne `master*.md`.
- **Problem:** Geplante Referenzsuche auf aggregierten Dateien scheiterte trotz korrektem Projektpfad.
- **Lösung:** API-Quellen direkt aus `features/`, `key_components/` und `PythonPartsFramework_DB/` lesen.
- **Regel:** Discovery immer gegen den real vorhandenen Dateibestand starten; aggregierte Masterdateien nicht voraussetzen.

### [2026-02-24] Diagnose bei ausbleibendem PythonPart-Log
- **Kontext:** Nutzer meldet unveraenderten UI-Flow und fehlende Debug-Ausgaben trotz Script-Anpassungen.
- **Problem:** Unklar, ob Allplan die aktuelle Script-Datei ueberhaupt laedt.
- **Lösung:** Debug-Build mit eindeutigem Dateinamen/Titel/Version und Modul-Load-Log auf mehrere Pfade erstellen.
- **Regel:** Bei Verdacht auf falsches Script-Mapping zuerst eindeutige Build-Identitaet erzwingen, dann funktional debuggen.

### [2026-02-24] Raumfunktion ueber Attribut-Tupel auslesen
- **Kontext:** RoomArrange-Raumbeschriftung lieferte trotz aktiver Checkbox keine Funktionsnamen.
- **Problem:** Bei selektierten Raumadaptern kamen Attribute als Tupel `(attribute_id, value)`; Objekt-basierte Attributlese lieferte dadurch leere Strings.
- **Lösung:** Zuerst `adapter.GetAttributes(ReadAll)` auswerten, ID-basierte Prioritaet nutzen (`506/236/327/994`) und Enum-Werte in Text aufloesen.
- **Regel:** Bei Allplan-Raumattributen immer Tupel- und Objekt-Format parallel unterstuetzen, sonst faellt die Funktionsklassifikation/Beschriftung aus.

### [2026-02-24] Raumfunktion-Fallback ueber RoomProperties
- **Kontext:** RoomArrange-Beschriftung blieb leer trotz aktiver Label-Option und mehrfacher Attribut-Fallbacks.
- **Problem:** Einige Raumadapter liefern Funktion nicht verlässlich ueber Attributlisten (tuple/objekt), dadurch bleibt `function_raw` leer.
- **Lösung:** Nach Attributpfaden zusaetzlich `RoomElement.GetProperties().GetFunction()` bzw. `Properties.Function` als Fallback nutzen.
- **Regel:** Bei Raum-Funktionslogik immer Attributpfad UND RoomProperties-Pfad implementieren und im Log ein kurzes Attribut-Sample ausgeben.

### [2026-02-25] Windows-Limit bei grossen Einmal-Patches
- **Kontext:** Erstellung einer grossen neuen PythonPart-Datei (`out/SVGPlacer.py`) per Single-Command/Patch.
- **Problem:** PowerShell/Tooling schlug mit `Der Dateiname oder die Erweiterung ist zu lang` fehl, obwohl Zielpfad gueltig war.
- **Lösung:** Datei in mehrere kleinere Schreibbloecke aufteilen (`Set-Content` + `Add-Content`) statt Monolith-Patch.
- **Regel:** Bei grossen Neu-Dateien unter Windows keine extrem langen Single-Command-Strings verwenden; blockweise schreiben.

### [2026-02-25] PYP-Tag-Namen fuer Startstabilitaet
- **Kontext:** Script-Object PythonPart startete nicht, initiale PYP nutzte Kurz-Tags wie `<n>`.
- **Problem:** Workspace-Beispiele/Framework nutzen konsistent `<Name>`; Kurz-Tags sind nicht in jedem Setup robust.
- **Lösung:** Auf explizite XML-Tags (`<Name>`) umstellen und bei Script-Object `<Interactor>False</Interactor>` setzen.
- **Regel:** Fuer produktive PYPs im Projektstil keine Kurz-Tags verwenden, sondern vollstaendige Tag-Namen.

### [2026-02-25] Script-Name in PYP ohne Ordnerprefix
- **Kontext:** PythonPart startete mit Meldung `Script SVGPlacer.SVGPlacer not found`.
- **Problem:** `<Script><Name>` enthielt `SVGPlacer\SVGPlacer.py`; Loader aufloesung passte nicht zur erwarteten Script-Referenz.
- **Lösung:** `<Name>` auf reinen Dateinamen (`SVGPlacer.py`) setzen und PYP-Struktur wie Beispiele (`<Parameters>`-Container) ausrichten.
- **Regel:** In diesem Workspace Script-Referenzen in `.pyp` wie in `example/` halten: Dateiname statt Ordnerpfad.

### [2026-02-25] Script-Name muss zur PythonPartsScripts-Struktur passen
- **Kontext:** SVGPlacer startete nicht trotz vorhandener `.py`.
- **Problem:** `<Script><Name>` ohne Unterordner referenziert nur `PythonPartsScripts\SVGPlacer.py`; bei Ablage unter `PythonPartsScripts\SVGPlacer\SVGPlacer.py` wird Script nicht gefunden.
- **Lösung:** `<Name>` als relativen Unterordnerpfad setzen (`SVGPlacer\SVGPlacer.py`).
- **Regel:** PYP-Scriptpfad immer 1:1 zur realen Struktur unter `PythonPartsScripts` halten.

### [2026-02-25] Startfehler `Script X.Y not found` per Flattening umgehen
- **Kontext:** Allplan meldete wiederholt `Script SVGPlacer.SVGPlacer not found`.
- **Problem:** Unterordner-Referenz in `<Script><Name>` fuehrte zu Package-Import (`X.Y`), der in der Zielumgebung nicht aufgeloest wurde.
- **Lösung:** Scriptname auf flache Referenz (`SVGPlacer.py`) umstellen und Datei direkt unter `...\PythonPartsScripts\` deployen.
- **Regel:** Bei hartnaeckigem Script-Load-Fehler zuerst Flat-Layout ohne Unterordner verwenden.

### [2026-02-25] Embedded-SVG als Start-robuster Fallback
- **Kontext:** SVGPlacer sollte ohne externe Ordnersuche direkt nutzbar sein.
- **Problem:** Abhaengigkeit von Folder-Scan/Dateipfaden erschwert Startdiagnose und Nutzung.
- **Lösung:** SVG-Inhalt als Embedded-Text im Script hinterlegt, Dropdown aus fixen Embedded-Namen aufgebaut.
- **Regel:** Bei instabilen Datei-/Pfadumgebungen zuerst eine eingebettete Minimalauswahl bereitstellen.

### [2026-02-25] Loader-robust via Paketpfad + __init__.py
- **Kontext:** Wiederholter Startfehler `Script SVGPlacer.SVGPlacer not found` trotz variierender `<Name>`-Pfade.
- **Problem:** Zielumgebung loest Script als Paketmodul (`Ordner.Modul`) auf.
- **Lösung:** Script parallel als Paketstruktur bereitstellen (`PythonPartsScripts\SVGPlacer\SVGPlacer.py` + `__init__.py`) und PYP auf diesen Pfad setzen.
- **Regel:** Bei hartnaeckigen Loader-Fehlern beide Aufloesungen absichern (Standalone und Paketpfad).

### [2026-02-25] Startrobustheit: keine ScriptObject-Imports fuer Standard-PYP
- **Kontext:** PythonPart startete nicht und schrieb keinen Log, obwohl PYP/PY vorhanden waren.
- **Problem:** Top-level Imports aus ScriptObject-Framework koennen Modulladen frueh abbrechen, bevor eigene Logs laufen.
- **Lösung:** Standard-PythonPart mit minimalen, robusten Imports und fruehem stdlib-Log vor Allplan-Imports umstellen.
- **Regel:** Bei Startproblemen zuerst minimalen Standard-Contract (`check_allplan_version`, `create_element`) ohne ScriptObject-Abhaengigkeiten sicherstellen.

### [2026-02-25] Start/Preview-Hook muss gleiche Converter-Signatur nutzen
- **Kontext:** SVGPlacer startete, brach aber im Preview mit TypeError ab.
- **Problem:** `create_element/create_preview` riefen `shapes_to_allplan_elements` mit falscher Argumentanzahl auf.
- **Lösung:** Robuste Standard-Hooks ergänzt und Converter-Aufruf auf volle Signatur (`..., placement, create_fill, create_outline`) korrigiert.
- **Regel:** Bei gemischten Framework-Aufrufen (ScriptObject + Preview) Hook-Signaturen und internen Funktionsaufruf strikt konsistent halten.

### [2026-02-25] Deploy-Stand gegen Log-Pfad verifizieren
- **Kontext:** Fehler blieb bestehen, obwohl `out/SVGPlacer.py` bereits korrigiert war.
- **Problem:** Allplan lud weiterhin eine alte Datei aus `...\PythonPartsScripts\SVGPlacer.py`; Workspace-`out/` war nicht deployt.
- **Lösung:** Eindeutige `BUILD_ID` im Log ausgeben und absoluten Pfad aus Stacktrace gegen Deploy-Ziel vergleichen.
- **Regel:** Bei wiederholten Startfehlern zuerst pruefen, ob wirklich die aktuelle Datei am von Allplan gelesenen Pfad liegt.

### [2026-02-25] SVG-Polygon braucht echtes FillingElement
- **Kontext:** Generiertes SVG-PythonPart zeigte nur Konturen, keine sichtbare Flaechenfuellung.
- **Problem:** `ModelEleList.append_geometry_2d(Polygon2D, common_props)` liefert nicht zwingend eine echte Fuellung.
- **Lösung:** Fuer Flaechen explizit `FillingElement` (mit robusten Konstruktor-Fallbacks) erzeugen und optional Kontur separat anhaengen.
- **Regel:** Bei Fill-Anforderung nie nur auf Polygon+CommonProperties verlassen, sondern `FillingElement` explizit verwenden.

### [2026-02-25] FillingElement ohne Farbzuweisung wird schwarz
- **Kontext:** SVG-Symbol mit roten/weissen Flaechen wurde nach Fill-Fix vollflaechig schwarz dargestellt.
- **Problem:** `FillingProperties` ohne gesetzte `FirstColor/SecondColor` nutzt Defaultfarbe (schwarz), unabhaengig vom SVG-`fill`.
- **Lösung:** SVG-`fill`-Hex nach Allplan-Farb-ID mappen (`GetIdByColor` + Fallback) und in `FillingProperties` setzen.
- **Regel:** Bei SVG-Konvertierung fuer jede Flaeche die Fuellfarbe explizit in `FillingProperties` setzen, nie implizit lassen.

### [2026-02-25] Projektvorgabe: Rot als fester Farbindex 6
- **Kontext:** Nutzer forderte fuer das ISO-Brandzeichen roten Hintergrund exakt als Allplan-Fuellfarbe `6`.
- **Problem:** Dynamische RGB->ID-Aufloesung (`GetIdByColor`) lieferte in der Umgebung abweichende ID (`216`).
- **Lösung:** Fuer rote SVG-Hexwerte im Mapping zuerst festen Index `6` anwenden; dynamische Aufloesung nur als nachgelagerter Fallback.
- **Regel:** Bei farbverbindlichen Symbolen projektseitig feste Farbindizes priorisieren, keine rein dynamische Farb-ID-Ermittlung.

### [2026-02-25] Projektvorgabe: Weiss als fester Farbindex 0
- **Kontext:** Nutzer wollte bei SVG-Symbolen Weiss nicht als `9`, sondern als festen Fuellindex `0`.
- **Problem:** Vorheriges Mapping setzte helle/ungueltige Farben auf `9`, was in der Zielumgebung nicht gewuenscht war.
- **Lösung:** Weiss-/Fallback-Mapping in `_svg_hex_to_allplan_color_id` auf `0` umgestellt.
- **Regel:** Bei diesem Symbolprojekt feste Vorgaben verwenden: Rot `6`, Weiss `0`.

### [2026-02-25] Palette nur mit Allplan-Farbdropdowns
- **Kontext:** Nutzer wollte in der Symbol-Palette ausschliesslich zwei Farbwaehler mit sichtbarer Allplan-Farbliste.
- **Problem:** Zusaetzliche Parameter (Scale/Rotation/CommonProperties) machten die Palette unnoetig komplex.
- **Lösung:** Palette auf `BackgroundColor` und `SymbolColor` reduziert und beide als `<ValueType>Color</ValueType>` modelliert.
- **Regel:** Wenn Nutzer explizit nur Farbauswahl verlangt, Allplan-Resource-Control `Color` nutzen und restliche Parameter entfernen.

### [2026-02-25] Interactor ohne Palette-Service wirkt wie Startabbruch
- **Kontext:** `RoomArrange_V2` lud ohne Traceback, wurde aber sofort wieder beendet (`on_cancel_function`).
- **Problem:** Interactor initialisierte `BuildingElementPaletteService` nicht; dadurch kein stabiler Palette-Workflow.
- **Lösung:** Palette-Init inkl. `show_palette(...)`, `on_control_event(...)`, `modify_element_property(...)` und `close_palette()` aus stabiler Ausgangsversion uebernehmen.
- **Regel:** Bei Interactor-PythonParts Palette-Service explizit und robust initialisieren, sonst erscheint es fuer Nutzer wie „startet nicht“.

### [2026-02-25] Symbolauswahl per Dateikuerzel im Dropdown
- **Kontext:** PythonPart sollte als `SymbolPlacer` mehrere Symbole ueber Palette waehlbar machen.
- **Problem:** Vorversion war fest auf ein einzelnes Symbolskript ohne Symbolparameter gebunden.
- **Lösung:** Paletteparameter `SymbolChoice` als `StringComboBox` eingefuehrt und Symbol-Dispatch im Script ueber Kuerzel (`F001`) umgesetzt.
- **Regel:** Bei erweiterbaren Symbol-PythonParts immer Symbolschluessel als Dropdown-Parameter modellieren und Geometrie per Dispatch-Funktion trennen.

### [2026-02-25] Neue SVG-Symbole als eigene Dispatcher-Funktionen integrieren
- **Kontext:** Nachtraeglich hinzugefuegte `ISO_7010_F002.svg` und `ISO_7010_F003.svg` sollten im bestehenden `SymbolPlacer` waehlbar sein.
- **Problem:** Ohne Funktions-Dispatch und Dropdown-Update bleiben neue Dateien wirkungslos.
- **Lösung:** Geometrie pro Symbol in eigene Funktionen (`_add_symbol_f002/_f003`) uebernommen, Dispatch erweitert und `ValueList` auf `F001|F002|F003` gesetzt.
- **Regel:** Bei Mehrsymbol-PythonParts immer Palette-`ValueList`, Symbol-Dispatch und Geometriefunktionen synchron aktualisieren.
### [2026-02-25] Raummapping: Ankerraum aus Zuordnung ausschliessen
- **Kontext:** RoomArrangeV2 SVG/Raummapping zeigte trotz korrekter Zielpunkte unplausible Raum-Zuordnungen.
- **Problem:** Der fixe Ankerraum wurde in der 1:1-Matching-Menge mitgefuehrt und blockierte damit einen SVG-Slot.
- **Lösung:** Matching nur fuer Nicht-Anker-Raeume berechnen und Anker strikt mit Shift `(0,0)` fixieren.
- **Regel:** Bei anchor-basierten Layout-Mappings den Anker nie in die Assignment-Matrix aufnehmen.
### [2026-02-25] Raummapping: Positionskosten koennen Zuordnung verfälschen
- **Kontext:** RoomArrangeV2 mappt Raum-Rechtecke auf SVG-Referenzraeume.
- **Problem:** Kostenanteil aus aktueller Raumposition (`pos_cost`) zog Matches in falsche SVG-Slots, obwohl Maße besser passten.
- **Lösung:** Matching auf globale Minimalzuordnung nur über Dimension+Flaeche umgestellt; Anchor danach per Shift-Kompensation fixiert.
- **Regel:** Bei referenzplanbasiertem Mapping aktuelle Szenenlage nicht als Primärkriterium für Matching verwenden.
### [2026-02-25] Raummapping braucht eigenen Mindestabstands-Pass
- **Kontext:** RoomArrangeV2 mit korrekter SVG-Topologie, aber uneinheitlichen Abstaenden zwischen gemappten Raeumen.
- **Problem:** Reines Mittelpunkt-Mapping beruecksichtigt `Gap` nicht; dadurch bleiben zu kleine Kantenabstaende bestehen.
- **Lösung:** Nach dem Mapping einen iterativen BBox-Nachlauf einbauen, der bei Orthogonal-Ueberlappung mindestens `gap_mm` erzwingt (Anchor fix).
- **Regel:** Im Floorplan-Mapping `Gap` immer explizit als separaten Post-Constraint behandeln.
### [2026-02-25] Gap-Constraint im Mapping mit Naehe statt nur Ueberlappung
- **Kontext:** RoomArrangeV2 Floorplan-Mapping mit Post-Gap-Pass.
- **Problem:** Bei leicht versetzten Reihen/Spalten griff die Gap-Pruefung nicht, weil sie strikte Orthogonal-Ueberlappung (`>0`) verlangte.
- **Lösung:** Konfliktbedingung auf `overlap > -gap_mm` erweitert, damit auch nahezu ausgerichtete Nachbarn auf Mindestabstand korrigiert werden.
- **Regel:** Mindestabstaende in Layout-Loesern nicht nur bei echter Ueberlappung, sondern bei Nachbarschaft innerhalb der Gap-Toleranz pruefen.
### [2026-02-25] Floorplan-Mapping: zentrische Gesamt-BBox-Skalierung verzerrt Abstaende
- **Kontext:** RoomArrangeV2 nutzte normalisierte SVG-Positionen auf die aktuelle Gesamt-BBox der Selektion.
- **Problem:** Relative Raumtopologie blieb erkennbar, aber Kantenabstaende (Gap) wurden durch globale Re-Skalierung unzuverlaessig.
- **Lösung:** Zielpunkte anchor-relativ aus gematchten SVG-Zentren ableiten und Skalierung ueber mediane Breiten-/Hoehenverhaeltnisse bestimmen.
- **Regel:** Bei referenzbasiertem Mapping keine zentrale Re-Skalierung auf die Selektions-BBox verwenden, wenn Abstaende fachlich stabil bleiben muessen.
### [2026-02-25] Raummapping stabil mit Anchor-Referenz statt Zentral-Skalierung
- **Kontext:** RoomArrangeV2 (Raummapping) war topologisch nah am SVG, aber Abstaende/Lagen waren inkonsistent.
- **Problem:** Zentrische Einpassung auf die Gesamt-BBox verzerrte relative Abstaende trotz korrekter Zuordnung.
- **Lösung:** Anchor-relativen Transform mit gematchtem SVG-Anker und medianer X/Y-Skalierung verwenden; danach Gap-Pass anwenden.
- **Regel:** Bei Referenzplan-Mapping zuerst anchor-relativ abbilden, erst danach Mindestabstaende erzwingen.
### [2026-02-26] CoordinateInput-Prompt muss InputStringConvert nutzen
- **Kontext:** RoomArrangeV3 Zielrechteck-Button `Auswaehlen` startete die Punktaufnahme nicht.
- **Problem:** `InitFirstPointInput` wurde mit `str` statt `InputStringConvert` aufgerufen (Boost.Python.ArgumentError).
- **Lösung:** Prompt vor dem Aufruf mit `AllplanIFW.InputStringConvert(...)` erzeugen und dann `InitFirstPointInput(prompt)` verwenden.
- **Regel:** Bei CoordinateInput-Startmethoden keine Raw-Strings uebergeben, sondern immer den erwarteten Input-Wrapper nutzen.

### [2026-02-26] RoomArrangeV3 Writeback: Raumbewegung nur mit Root-Delete stabil
- **Kontext:** RoomArrangeV3 Anordnung/Mapping funktionierte, erzeugte aber fehlerhafte Bauteilmarkierung und Architekturfuellung-Artefakte.
- **Problem:** Child-Tree-Delete beim Recreate (`delete_set` deutlich groesser als Raumanzahl) griff zu tief in Architektur-Unterelemente ein.
- **Lösung:** Recreate-Mechanik beibehalten, aber Delete-Scope auf selektierte Raum-Root-Adapter begrenzen.
- **Regel:** Bei Architektur-Raummoves kein pauschales Child-Delete verwenden; zuerst Root-only loeschen und Verhalten pruefen.
### [2026-02-27] RoomFloorplan: Zielmittelpunkt robust per CoordinateInputResult
- **Kontext:** Debug-Modus fuer Raumverschiebung wurde erfolgreich genutzt, um selektierte Raeume als Gruppe zu bewegen.
- **Problem:** Punktaufnahme lieferte `CoordinateInputResult` statt Objekt mit direktem `.X/.Y`; dadurch brach der Platzierungsschritt ab.
- **Lösung:** Punkt-Extraktion als robusten Helper mit mehreren Zugriffspfaden (`X/Y`, Getter, Punkt-Attribute) umgesetzt und danach Workflow auf Zielmittelpunkt-vor-Selektion umgestellt.
- **Regel:** Bei Allplan-CoordinateInput niemals festen Punkttyp annehmen; Ergebnisobjekte defensiv in `Point2D` normalisieren.

### [2026-02-27] RoomFloorplan: Punktklick stabil mit GetInputPoint/GetPoint
- **Kontext:** 2-Punkt-Mittelpunkt (Punkt 1 + Punkt 2) fuer Raumverschiebung im Interactor.
- **Problem:** Maus-Klicks wurden in der Punktphase nicht zuverlaessig als Referenzpunkte uebernommen.
- **Lösung:** Punktaufnahme pro Event ueber `GetInputPoint(...)` und Weltpunkt ueber `CoordinateInputResult.GetPoint()` lesen; zweiten Punkt mit `InitNextPointInput(...)` starten.
- **Regel:** Bei CoordinateInput-Workflows Punkt-Snapping immer ueber `GetInputPoint` treiben und Eingabe nach jedem Klick explizit neu initialisieren.

### [2026-02-27] RoomFloorplan: Mapping stabil durch Root-Normalisierung
- **Kontext:** `UseRoomMapping` erzeugte fehlerhafte Bauteile/Symbole und konnte Allplan in 3D-Update-Schleifen bringen.
- **Problem:** Gemischte Adapter (Root/Child) wurden inkonsistent bewegt; Recreate erzeugte dadurch Zusatzobjekte (`created` deutlich > Raumanzahl).
- **Lösung:** Selektion zuerst auf eindeutige Raum-Root-Adapter normalisieren und Delete/Create pro verschobenem Raum konsistent auf denselben Root-Objektbaum anwenden.
- **Regel:** Bei Mapping-Recreate nie mit gemischten Raumadaptern arbeiten; immer erst Root-normalisieren und dann batchweise konsistent schreiben.
### [2026-02-27] RoomFloorplanV2: Beschriftung nur ueber Raumfunktion
- **Kontext:** Neue Beschriftungsfunktion in V2 nach erfolgreicher Stabilisierung des Label-Workflows.
- **Problem:** Labels zeigten teils Bezeichnung/Qualitaet statt der gewuenschten Raumfunktion.
- **Lösung:** Labeltext strikt auf `function` umgestellt und Attribut-Prioritaet auf Funktions-IDs begrenzt (`506/236/327/994`).
- **Regel:** Bei Raumbeschriftung den Labeltext immer aus dem Funktionsfeld ableiten, nicht aus Name/Qualitaetsattributen.
### [2026-03-09] Interactor-Preview nur bei Palette-Fokus
- **Kontext:** MokshaPatam-Interactor renderte Board, zeigte es aber nur stabil bei Palette-Hover; Feldtext war ueberdimensioniert.
- **Problem:** Kein stabiler CoordinateInput-Loop und textgroessen relativ zur Zellgroesse (z.B. 500 mm) skaliert.
- **Lösung:** Dialog-Input via `InitFirstPointInput(InputStringConvert(...))` aktiv halten, Redraw in `process_mouse_msg` ausfuehren und Spielfeld-Text auf feste mm-Werte setzen (1.5 mm).
- **Regel:** Bei Interactor-Previews immer Input-Loop explizit initialisieren und Textgroessen nicht direkt an grosse Geometrieparameter koppeln.

### [2026-03-11] ShowCube ohne Schnittkanten bei Null-Explosion
- **Kontext:** ShowCube zeigte im Ruhezustand sichtbare Kanten, weil nur getrennte Flaechenplatten dargestellt wurden.
- **Problem:** Reine Slab-Darstellung erzeugte unruhige Schnittkanten trotz korrekter Geometrie.
- **Lösung:** Einen durchgehenden Kernwuerfel wie in `QRCodeCube` als Basis verwenden und Explosions-Slabs nur bei `ExplosionFactor > 0` addieren.
- **Regel:** Fuer geschlossene Demo-Koerper zuerst einen Vollkoerper modellieren; Explosions-/Demoelemente nur additiv darueberlegen.

### [2026-03-11] ShowCube Palette mit nativen Farb-Dropdowns
- **Kontext:** Nutzer bestaetigte die Farbumsetzung in ShowCube als korrekt.
- **Problem:** Integer-Farbfelder und zusaetzliche Statusanzeige im TicTacToe waren unpassend fuer die gewuenschte Palette.
- **Lösung:** Farbparameter auf `ValueType=Color` umgestellt (`CubeColor/QRColor/TextColor/ReinfColor`) und TicTacToe-Statuszeile entfernt.
- **Regel:** Bei gewuenschter Allplan-Farbliste immer native `Color`-Controls nutzen und nicht-noetige Statusfelder ausblenden/entfernen.

### [2026-03-11] ShowCube Transparenz nur mit Surface-Texture stabil sichtbar
- **Kontext:** Parameter `CubeTransparency` wurde eingefuehrt, zeigte aber zunaechst keine sichtbare Wirkung.
- **Problem:** Transparenz griff im Wuerfel-Rendering nicht zuverlaessig mit dem ersten Texture-Append-Ansatz.
- **Lösung:** Wuerfelgeometrie mit `SurfaceDefinition.Transparency` + `TextureDefinition` als explizites `ModelElement3D(common, texture, geometry)` erzeugen; stabiler Surface-Name/Pfad.
- **Regel:** Fuer sichtbare 3D-Transparenz in Allplan Oberflaechen-Transparenz ueber Surface-Ressource setzen und per `ModelElement3D` mit TextureDefinition zuweisen.

### [2026-03-11] ShowCube Längseisen über Abstand mit fixen Eckstäben
- **Kontext:** Nutzer wollte Durchmesser als Dropdown und vertikale Eisen über Abstand (z.B. alle 100 mm) bei festen Eckstäben.
- **Problem:** Bisherige Count-Verteilung war unflexibel für gleichmäßige Abstandsvorgaben entlang des Umfangs.
- **Lösung:** `LongBarCount` durch `LongBarSpacing` ersetzt, Durchmesser als `IntegerComboBox` modelliert und Umfangsverteilung mit immer gesetzten Ecken implementiert.
- **Regel:** Für vertikale Stabverteilung bei Stützen-/Würfelquerschnitten Abstandsparameter nutzen und Ecken explizit fixieren statt reine Stückzahlsteuerung.

### [2026-03-11] ShowCube Textdefaults gegen ReadLastInput absichern
- **Kontext:** Palette sollte standardmäßig `Promt to Part` und `Digital Bau` anzeigen, zeigte aber teils nur `Promt`/`Digital`.
- **Problem:** Mit `ReadLastInput=True` wurden alte Kurzwerte aus gespeicherten Inputs geladen und übernahmen die neuen PYP-Defaults.
- **Lösung:** In `ShowCube.py` eine gezielte Restore-Logik eingebaut, die bekannte Altwerte auf vollständige Palettetexte korrigiert.
- **Regel:** Bei geänderten Default-Texten und aktivem `ReadLastInput` immer Legacy-Werte beim Laden normalisieren, sonst greifen PYP-Defaults nicht sichtbar.

### [2026-03-17] Chess Save/Close: Persistenz nur via Transaction stabil
- **Kontext:** Chess-Interactor verlor nach `Speichern + Schließen` teils das PythonPart oder erzeugte Duplikate.
- **Problem:** `no CreateElements` im Modification-Mode ließ das Element verschwinden; reines `CreateElements` erzeugte Mehrfach-Instanzen.
- **Lösung:** Speichern auf `PythonPartTransaction.execute(..., modification_element_list)` umgestellt, mit Fallback auf `CreateElements`.
- **Regel:** Bei Interactor-Änderung bestehender PythonParts zuerst Transaction-Writeback mit Modify-Liste nutzen, nicht manuell skippen oder blind neu erzeugen.
### [2026-03-26] Winkelstuetzwand Startstabilitaet mit verifizierten Basismustern
- **Kontext:** Neues Standard-PythonPart fuer Winkelstuetzwand mit Geometrie und Bewehrung aus Prompt umgesetzt.
- **Problem:** Bei Erstimplementierung besteht hohes Risiko fuer Start-/Importfehler und inkonsistente Parameterkopplung.
- **Lösung:** Contract strikt wie `BetonStuetze` aufgebaut, nur verifizierte Reinf-Builder genutzt und Parameternamen `.py/.pyp` automatisiert abgeglichen.
- **Regel:** Neue bewehrte Standard-PythonParts immer mit verifiziertem Referenzgeruest starten und vor Allplan-Test per `py_compile` + Parameternamen-Check absichern.
### [2026-03-27] Wandanfaenger-Hakenrichtung lagebezogen spiegeln
- **Kontext:** Winkelstuetzwand; Wandanfaenger-Haken waren lage- und richtungsseitig fast korrekt, aber eine Lage zeigte in die falsche Richtung.
- **Problem:** Einheitliche Rotationslogik erzeugte trotz korrekter Geometrie eine seitenverkehrte Hakenorientierung in einer Lage.
- **Lösung:** Hakendrehung lagebezogen geschaltet (`rot_z=180` nur fuer die betroffene Lage), restliche Logik unveraendert belassen.
- **Regel:** Bei spiegelbildlichen Bewehrungslagen die Hakenausrichtung pro Lage explizit steuern statt global gleich behandeln.
### [2026-03-27] Wand-Vertikale und Wandanfaenger 1:1 koppeln
- **Kontext:** Winkelstuetzwand; Anzahl/Position der Wand-Vertikale musste exakt zu den Wandanfaengern im Fundament passen.
- **Problem:** Gemischte Verlegearten (`by_count` vs. andere Serien) fuehrten zu unterschiedlichen Stabanzahlen und versetzten X-Positionen.
- **Lösung:** Beide Serien auf identische Verlegebasis umgestellt (`create_linear_bar_placement_from_to_by_dist` mit gleicher Achse, Abdeckung und Abstand).
- **Regel:** Zugehoerige Anschlussbewehrung immer mit derselben Verteilregel wie die Zielserie erzeugen, sonst entstehen Lageversatz und Stabdifferenzen.
### [2026-03-27] Wand-Steckbuegel: U-Form lagegebunden statt global rotiert
- **Kontext:** Winkelstuetzwand; Wand-Steckbuegel sollten zwei vertikale Wandlagen verbinden, Oeffnung nach unten, Stirnseite oben.
- **Problem:** Rotations-/Bezugspunktfehler erzeugten Steckbuegel ausserhalb der Wand bzw. nur mit einem korrekt liegenden Schenkel.
- **Lösung:** Wand-Steckbuegel als freie U-Form mit lagegebundenem Bezug auf `y_outer/y_inner` und oberer Stirnseite erzeugt; Schenkelrichtung per `span`-Vorzeichen gespiegelt.
- **Regel:** Bei lagekritischen Buegeln nie nur ueber globale Rotation arbeiten, sondern Schenkel explizit an Zielbewehrungslagen anbinden und Richtung separat pruefen.
### [2026-03-27] Stirnseiten-Steckbuegel horizontal: Oeffnung nach innen
- **Kontext:** Winkelstuetzwand; Steckbuegel fuer horizontale Wandeisen an linker/rechter Stirnseite.
- **Problem:** Buegel waren verdreht (Oeffnung nach aussen) und Stirnseitenbezug mit Deckung/Schenkellaenge war nicht fachgerecht.
- **Lösung:** Linke/rechte Serie gespiegelt ausgerichtet (Oeffnung jeweils nach innen), geschlossene Seite an Stirnflaeche mit Deckung; Schenkellaenge ueber `AnchorageLength` begrenzt.
- **Regel:** Bei spiegelbildlichen Stirnseiten stets zwei explizit gespiegelte Serien modellieren, statt nur eine global rotierte Form zu verwenden.

### [2026-04-07] Baumasse-Beschriftung lesbar mit Zweispalten-Layout
- **Kontext:** Baumasse-PythonPart sollte Kennwerte per Button "Beschriften" als Textblock platzieren.
- **Problem:** Ein einzelner Textblock bzw. ungeordnete Einzeltexte fuehrten zu ueberlagertem, unlesbarem "Texthaufen".
- **Lösung:** Beschriftung als getrennte TextElemente in zwei festen Spalten (Label/Wert) mit vorherigem Cleanup alter Labeltexte umgesetzt.
- **Regel:** Fuer dichte Kennwerte in Allplan nie einen langen Textblock nutzen, sondern tabellarische Einzeltexte mit definierter Spaltenausrichtung und Cleanup-Tagging.
### [2026-04-08] Hochregallager als editierbares PythonPart statt nackter 3D-Koerper
- **Kontext:** Neues Hochregallager startete erst nach Stabilitaetsfix wieder und erzeugte sichtbare Geometrie.
- **Problem:** Rueckgabe als reine `ModelElement3D`-Liste erzeugt zwar 3D-Koerper, aber kein nachtraeglich editierbares PythonPart-Containerobjekt.
- **Lösung:** Geometrie in `PythonPartUtil`-View kapseln und `create_pythonpart(build_ele)` als `CreateElementResult(elements=...)` zurueckgeben.
- **Regel:** Fuer nachtraeglich anpassbare Standard-PythonParts nie nur nackte ModelElemente zurueckgeben, sondern immer PythonPart-Container erzeugen.
### [2026-04-09] Hochregallager: Verbände ohne Block/Flaechenartefakte
- **Kontext:** Nach mehreren Korrekturen zeigten Verbände in der Vorschau korrekt, wurden final aber als Block/Flaeche erzeugt; Rammschutz war instabil.
- **Problem:** Ersatz-/Fallback-Geometrie fuer Diagonalen fuehrte zu falscher Darstellung; gleichzeitige Rammschutzanpassungen erhoehten die Fehlerlast.
- **Lösung:** Rammschutz komplett entfernt und Verbaende als orientierte `BRep3D.CreateCuboid`-Diagonalstaebe (Quadratrohr-Charakter) umgesetzt.
- **Regel:** Bei Preview-vs-Erzeugung-Abweichungen keine flaechigen/volumigen Ersatz-Fallbacks fuer Aussteifungen verwenden; direkt die endgueltige Stabgeometrie bauen.
### [2026-04-09] Hochregallager: Paletten-Parameter semantisch korrekt, Platzierung separat
- **Kontext:** Paletten sollten wie im Regalschema stehen (800 auf Traverse), ohne die Bedeutung von Laenge/Breite zu verbiegen.
- **Problem:** Durch Tausch der Defaultwerte (`PalletLength`/`PalletWidth`) blieb die Geometrie zwar aehnlich, aber die Parametersemantik war fachlich falsch.
- **Lösung:** Parameter auf fachliche Defaults belassen (`Laenge=1200`, `Breite=800`) und nur die Platzierungszuordnung setzen (`X=Breite`, `Y=Laenge`), Feldbreite-Default 2700mm.
- **Regel:** Bei Lagekorrekturen zuerst die Achszuordnung in der Geometrie anpassen; Parameternamen/-bedeutung und Einheiten nicht "durch Tausch" umdefinieren.
### [2026-04-09] Hochregallager: Paletten-Labels nur 3D und lesbar
- **Kontext:** Matrix-Beschriftung sollte auf jeder Palette im 3D-Modell sichtbar sein (`A3.1`, `A3.2`, ...).
- **Problem:** Im Preview war es korrekt, nach dem Setzen erschienen wieder 2D-Labels; zudem war die Schrift zu grob und die Feldrichtung fuer `A/B/C` invertiert.
- **Lösung:** Labels als 3D-Reliefgeometrie bauen und in `PythonPartUtil.add_pythonpart_view_3d(...)` ausgeben; Pixel-Font auf feinere 7x5-Glyphen umstellen.
- **Regel:** Bei Preview-vs-Setzen-Unterschieden fuer Beschriftung View-Trennung nutzen (2D/3D) und Feldlogik explizit am Nullpunkt definieren (`A` bei X=0, in X+ hochzaehlen).
### [2026-04-09] Hochregallager: Einzelgewichte nur sichtbar mit robuster Palette-Logik
- **Kontext:** `UseIndividualWeights` und `PalletWeights` wurden fuer Einzelgewichte je Palette eingefuehrt.
- **Problem:** Die Tabelle erschien nicht, weil `PalletsPerField` im Individualmodus durch Sichtbarkeit/Enable indirekt blockiert war und teils eine alte `input`-PYP geladen wurde.
- **Lösung:** `PalletsPerField` im Individualmodus explizit sichtbar/aktiv halten, `PalletWeights` auf `ShowPallets == True and UseIndividualWeights == True` binden und PYP-Version erhoehen.
- **Regel:** Bei 2D-Listen mit abhängigen Dimensionen immer die steuernden Parameter im Zielmodus sichtbar/editierbar halten und sicherstellen, dass die `out`-PYP-Version geladen wird.

### [2026-04-09] ExcelTest: Event-Buttons robust und Excel-Sync stabil
- **Kontext:** Standard-PythonPart `ExcelTest` mit 2D-Wertmatrix, Dateidialog und Excel-Buttons wurde neu umgesetzt.
- **Problem:** Bei Button-Events koennen Signaturvarianten auftreten; zusaetzlich muss TwoDimList-Import/Export robust gegen unvollstaendige oder ungueltige Zellwerte sein.
- **Loesung:** `on_control_event` robust mit optionalen Zusatzargumenten umgesetzt und Excel-Create/Export/Import inkl. Matrix-Normalisierung, Statusmeldungen und `openpyxl`-Guard implementiert.
- **Regel:** Bei Standard-PythonParts mit Palette-Buttons Event-Handling signaturtolerant implementieren und Listenimporte immer defensiv normalisieren statt Rohwerte direkt zu uebernehmen.

### [2026-04-09] Hochregallager v4.2: Feld-Ebenenlast steuert Farbe und Label
- **Kontext:** Hochregallager um 3-Zustands-Farblogik, zweizeilige Palettenlabels und Excel-Sync erweitert.
- **Problem:** Einzelgewichtsbasierte Farbzuordnung war fachlich missverstaendlich; Label zeigte Gewicht nicht direkt; Gewichtsdaten waren schwer extern zu pflegen.
- **Loesung:** Farbentscheidung auf Feld-Ebenen-Summe umgestellt (leer/orange, ok/gruen, ueberlast/rot), Label auf Code+Tonnen erweitert und Excel-Create/Export/Import per Button integriert.
- **Regel:** Bei lagerfachlichen Lastanzeigen die Auslastung immer auf relevante Tragebene aggregieren und Visualisierung + Datenschnittstelle gemeinsam aktualisieren.

### [2026-04-10] Hochregallager v4.5 Grundumbau bestaetigt
- **Kontext:** Einzelregal-Umstellung mit Regalname, Bodenlabel und Excel-Namenslogik.
- **Problem:** Nach dem Umbau war offen, ob Kernmechanik (Palette/Excel/Sub-PythonParts) stabil bleibt.
- **Lösung:** User-Feedback „ok sehrgut“ bestaetigte die Basis; noetig waren nur kleine Folgeanpassungen.
- **Regel:** Nach groesserem Strukturupdate erst Kernfreigabe sichern und Detailwuensche in kleinen Iterationen nachziehen.

### [2026-04-13] Terrassenueberdachung Rotation braucht Angle-Objekt
- **Kontext:** Standard-PythonPart Terrassenueberdachung startete, erzeugte aber keine Vorschau/kein Element.
- **Problem:** `Matrix3D.Rotation(...)` wurde mit `Angle.DegToRad(...)` (float) aufgerufen; die API erwartet `AllplanGeo.Angle`.
- **Lösung:** Rotationswinkel auf `AllplanGeo.Angle.FromDeg(-Neigung)` umgestellt und Build hochgezogen (`...-v2`).
- **Regel:** Bei `Matrix3D.Rotation` immer ein `Angle`-Objekt übergeben, nicht Rad-`float`.
### [2026-04-13] Terrassenueberdachung Glasleisten ohne Regression
- **Kontext:** Prompt2 verlangte Glasleisten (Rand/Mitte) zusaetzlich zur bestehenden Dachgeometrie.
- **Problem:** Erweiterung durfte bestehende Geometrie/Validierung nicht veraendern und musste parametrisierbar bleiben.
- **Lösung:** Zwei neue Profilparameter plus eigene Glasleisten-Schleife nach Eindeckung mit gleicher Rotation und Rand/Mitte-X-Logik umgesetzt.
- **Regel:** Bei Folgefeatures stabile PythonParts chirurgisch erweitern (eigene Schleife + Logging), Kerngeometrie unangetastet lassen.

