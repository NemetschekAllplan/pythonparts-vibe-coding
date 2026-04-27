---
name: allplan-pythonparts
description: >
  Generates production-ready Allplan 2026 PythonParts (.py + .pyp pairs).
  Use for any Allplan, PythonPart, parametric CAD, BIM scripting,
  reinforcement, or NemAll_Python_* task. Always read
  references/anti_hallucination.md before writing code.
---

# Allplan PythonParts 2026 - Code Generation Skill

## CRITICAL: Read First
-> references/anti_hallucination.md (MANDATORY before any code)

## Workflow
1. Read references/anti_hallucination.md
2. Read `../../../../brain.md` for accumulated project knowledge
3. Choose contract type -> references/contracts.md
4. Copy matching template from templates/
5. Load relevant domain references (geometry, palette, elements, etc.)
6. Check examples/ for similar patterns
7. Implement, then run scripts/validate_pythonpart.py
8. Verify against references/output_checklist.md
9. Deliver `.py + .pyp` pair to projects/
10. If learning occurred -> update brain.md

## Contract Type Decision
| Need | Contract | PYP <Interactor> |
|------|----------|-------------------|
| Parametric geometry from palette | Standard | False |
| Element selection, multi-step workflow, state | Script Object | False |
| Real-time mouse input, interactive placement | Interactor | True |

## Domain References (load as needed)
| Topic | File |
|-------|------|
| Anti-Hallucination | references/anti_hallucination.md |
| Contract Types & Skeletons | references/contracts.md |
| Geometry | references/geometry.md |
| Palette & PYP | references/palette.md |
| Elements & Properties | references/elements.md |
| Reinforcement | references/reinforcement.md |
| Input & Selection | references/input_selection.md |
| Debugging | references/debugging.md |
| Output Checklist | references/output_checklist.md |

## Extended API Docs
For full API signatures search `api-docs/`.

## Example PythonParts
Working implementations are in `../../../../examples/`.
