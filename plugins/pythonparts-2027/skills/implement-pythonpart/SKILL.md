---
name: implement-pythonpart
description: Implements an ALLPLAN 2027 PythonPart from an accepted implementation plan, or applies a clearly specified change to PythonPart scripts (.py) and parameter dialog files (.pyp). Looks up the framework APIs and examples, writes the code, and type checks it until it is clean. Use when the user asks to implement a PythonPart plan, write or modify a PythonPart script or pyp file, or add a parameter to a PythonPart. Does not gather requirements or plan; use the plan-pythonpart skill for that.
---

# Implement a PythonPart

The result of this skill is working PythonParts code (`.py` scripts and `.pyp` parameter dialog files) that passes the type check. Gathering requirements and planning is a separate step.

## Rules

- Implement only from an accepted implementation plan or a self-explanatory request. If no plan exists and the request is not self-explanatory, do not write code. Reply with "Plan required:", list the missing information, and recommend creating a plan first with the `plan-pythonpart` skill or the PythonParts planner agent. This also applies when another agent delegated the task to you.
- Do not write PythonParts code from memory. Always verify APIs in the `pythonparts-knowledge-mcp` knowledge base first and follow the patterns and APIs described there exactly.
- Do not invent class names, method signatures, or module paths. Verify them with the `inspect_symbol` tool of the `pythonparts-local-mcp` server.
- Do not add unrequested features, refactors, or docstrings.
- For research, delegate only to the PythonParts researcher agent. Do not delegate to the PythonParts planner agent or to general-purpose agents, and never ask a subagent to edit files or run commands.

## Asking questions

If the plan leaves a decision open that affects the code (a missing value, conflicting plan details, several valid options):

- If a question tool is available (e.g. `ask_user`, `askQuestions`, or `AskUserQuestion`), ask with it and wait for the answers.
- If no question tool is available (e.g. you were started as a subagent), DO NOT guess and DO NOT create or edit files for the affected part. Return only a `## Questions` section and end your turn. Number the questions; for each, list the options you see and the one you recommend. The caller will forward them to the user and call you again with the answers.

## Tool use

- The PythonParts researcher agent is called `pythonparts-researcher` in Claude Code and **PythonParts Researcher** in GitHub Copilot. If it is not available, use the `list_resources` and `read_resource` tools of the `pythonparts-knowledge-mcp` server directly.
- The PythonParts planner agent is called `pythonparts-planner` in Claude Code and **PythonParts Planner** in GitHub Copilot.
- MCP tools can be deferred: listed, but not callable until loaded. If a tool you need is not directly callable, load it with the tool-search tool (search for the server and tool name, e.g. `pythonparts-local-mcp typecheck_file`). If the search does not return it, search again with the exact tool name before concluding it is unavailable.

## Workflow

1. **Understand the plan**: Read the implementation plan (or request) to identify the files, elements, and behavior to implement.
2. **Look up implementation details on demand**: If you need details on several plan elements at once (dialog controls, interactors, geometry, reinforcement, closest examples, ...), delegate them in one call to the PythonParts researcher agent and work from its briefing. For a single lookup, call the `list_resources` tool of the `pythonparts-knowledge-mcp` server to find the relevant resource, then its `read_resource` tool to load it.
3. **Verify environment assumptions**: Never assume paths, the Python version, or other environment facts. Call the `get_allplan_info` tool of the `pythonparts-local-mcp` server to confirm them before relying on them in code. If it returns `Not set. Use set_allplan_paths()` for the Std or Usr path, the local MCP server is not set up: follow the `pythonparts-mcp-setup` skill to set the paths, verify them with `get_allplan_info`, and then continue. If you cannot ask the user for the paths, return a `## Questions` section asking for the Std and Usr paths instead.
4. **Explore existing code**: Read and search the workspace to understand any existing scripts or pyp files involved.
5. **Explore examples**: Look for real-world examples similar to the plan element at hand. Check the workspace first (e.g. an `Examples/PythonParts` folder). If not present there, look under the Usr path from your environment information or from `get_allplan_info`:
   - `<Usr>\Library\Examples\PythonParts` — `.pyp` dialog examples
   - `<Usr>\Library\PythonPartsExamples` — `.py` script examples

   If neither location exists, ask the user to install the PythonParts SDK in ALLPLAN and use its "Download examples" feature.
6. **Implement**: Create or edit files following the framework conventions from the resources.
7. **Verify uncertain symbols**: If unsure how to use a class, method, or module, call the `inspect_symbol` tool of the `pythonparts-local-mcp` server instead of guessing.
8. **Validate**: Run the `typecheck_file` tool of the `pythonparts-local-mcp` server on every file you created or changed.
9. **Fix and repeat**: Address any reported errors and re-run the type check until the output is clean, applying the [type-check exception](#type-check-exception).

## Type-check exception

Symbols exposed from C++ (module/class names starting with `NemAll_Python_*`) are type-checked against imperfect stub files. If `typecheck_file` reports an error or warning on such a symbol and the usage matches the documented or inspected API, treat it as a known stub limitation, note it briefly to the user, and do not "fix" working code to silence it.

## Definition of done

The coding task is complete when `typecheck_file` reports the changed file(s) as error-free, apart from the `NemAll_Python_*` stub exception above.

## Output

Produce working, idiomatic PythonParts code that follows the conventions described in the framework resources. After completing a file, briefly summarize what was created or changed.
