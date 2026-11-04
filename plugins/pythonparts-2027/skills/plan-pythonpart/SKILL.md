---
name: plan-pythonpart
description: Plans a new ALLPLAN 2027 PythonPart before any code is written. Clarifies the requirements (what it creates or modifies, interaction workflow, property palette UI, target location), researches the PythonParts framework, and produces a structured implementation plan. Use when the user asks to plan, design, scope, or specify a PythonPart, or asks to build a new PythonPart and no accepted plan exists yet. Not needed for small, clearly specified changes to an existing PythonPart.
---

# Plan a PythonPart

The result of this skill is an implementation plan that the user accepts. Implementing the plan is a separate step.

## Rules

- Do not create, edit, or modify any `.py` or `.pyp` files while planning, even if your tools allow it. Implementation starts only after the user accepts the plan.
- Do not write code beyond short illustrative pseudo-code in the plan.
- Produce the plan only after the requirements are clear.
- If the user already answered a question explicitly or implicitly, do not ask it again. Ask about missing requirements together in as few rounds as possible.
- For research, delegate only to the PythonParts researcher agent. Do not delegate planning or implementation to the PythonParts coder agent or to general-purpose agents.

## Asking questions

Whenever a requirement is missing or ambiguous:

- If a question tool is available (e.g. `ask_user`, `askQuestions`, or `AskUserQuestion`), ask with it and wait for the answers.
- If no question tool is available (e.g. you were started as a subagent), DO NOT produce a plan and DO NOT fill the gaps with assumptions. Return only a `## Questions` section and end your turn. Number the questions; for each, list the options you see and the one you recommend. The caller will forward them to the user and call you again with the answers.

## Tool use

- The PythonParts researcher agent is called `pythonparts-researcher` in Claude Code and **PythonParts Researcher** in GitHub Copilot. If it is not available, use the `list_resources` and `read_resource` tools of the `pythonparts-knowledge-mcp` server directly.
- MCP tools can be deferred: listed, but not callable until loaded. If a tool you need is not directly callable, load it with the tool-search tool (search for the server and tool name, e.g. `pythonparts-knowledge-mcp read_resource`). If the search does not return it, search again with the exact tool name before concluding it is unavailable.

## Workflow

### 1. Understand the "What"

Determine what the PythonPart should do. If not explicit or clearly implied, ask:

- Should it modify existing entities, or create new ones?
- If creating new elements:
  - Native ALLPLAN elements (walls, generic 3D solids, lines, ...), or
  - A custom, modifiable PythonPart element with its own "modification" logic (e.g. parametrics)?
- If a custom element: should the workflow be consistent between creation mode and modification mode?

### 2. Understand the workflow

Clarify the interaction steps the user performs when using the PythonPart, if not explicit or implied. Standard workflow for a parametric object:

1. Place the object by clicking a point in the viewport
2. Adjust parameters in the property palette
3. Confirm with ESC

Example of a custom workflow:

1. Select (pick) an existing element (e.g. a 2D profile)
2. Draw an axis
3. Adjust parameters in the property palette
4. Confirm with ESC

### 3. Understand the UI

Read the relevant PythonParts knowledge resource(s) on building UI/property palettes (native WPF controls) with the `read_resource` tool of the `pythonparts-knowledge-mcp` server. Then determine, implicitly or by asking, what UI controls are needed and whether the built-in property palette covers them, or a custom UI is required.

### 4. Decide where it should live

Determine, if not already clear:

- Directly in ALLPLAN (usable right away, good for small/personal projects), or
- In a dedicated directory (good for bigger projects with Git versioning)

If directly in ALLPLAN, clarify further:

- Office resources (Std directory) — available to the whole office, or
- User resources (Usr directory, recommended) — available only to this user

Take the Std and Usr paths from your environment information or from the `get_allplan_info` tool of the `pythonparts-local-mcp` server. Do not guess them. If `get_allplan_info` returns a path starting with `REPLACE-WITH-`, the local MCP server is not set up: ask the user to run `/pythonparts-mcp-setup` and do not rely on the paths.

### 5. Research

Once the requirements are reasonably clear, delegate the research to the PythonParts researcher agent in a single call. List every topic the plan depends on, for example: "Research: two-point input with preview, extrusion along a vector, boolean intersection for end cuts, PythonPart element with a placement matrix, closest examples, ALLPLAN paths." The briefing identifies:

- Relevant framework concepts, base classes, and examples that match the requested workflow
- Any constraints or ALLPLAN version details that affect the plan

Use the `pythonparts-knowledge-mcp` tools or `get_allplan_info` directly only for a single follow-up fact the briefing left open. Carry items marked "Not verified" into section 6 of the plan.

### 6. Produce the implementation plan

Output a single implementation plan using exactly this structure:

```markdown
## Implementation Plan: <PythonPart name>

### 1. Summary
<One paragraph: purpose of the PythonPart>

### 2. Requirements
- **Behavior**: modify existing / create new (native elements / custom PythonPart element)
- **Creation–modification consistency**: <yes/no/n-a, with reasoning>
- **Workflow steps**:
  1. ...
  2. ...
- **UI**:
  - Required controls: ...
  - Built-in property palette sufficient? yes/no — reasoning

### 3. Target location
- Placement: ALLPLAN (Std/Usr) or dedicated directory
- Path/naming convention

### 4. Framework findings
- Relevant resources/examples discovered (with source)
- Key base classes / APIs to use (e.g. BaseInteractor, AllplanGeometry, ...)

### 5. Proposed file structure
- Files to create (script(s), `.pyp` dialog, resource files) with brief purpose of each

### 6. Open questions / risks
- ...
```

## Output

Return exactly one of:

- **Questions**: if any requirement is still missing or ambiguous and you could not ask through a question tool, return only the `## Questions` section described in [Asking questions](#asking-questions), no plan.
- **Plan**: once all requirements are clear, return only the completed implementation plan in the structure above. Section 6 holds technical risks and unverified framework facts, not open requirements.

## After the plan

Ask the user to confirm or adjust the plan. Do not implement it as part of this skill. Once the user accepts it, the plan is the input for the PythonParts coder agent (`pythonparts-coder` in Claude Code, **PythonParts Coder** in GitHub Copilot).
