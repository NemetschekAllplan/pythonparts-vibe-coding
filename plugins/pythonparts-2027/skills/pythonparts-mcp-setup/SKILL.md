---
name: pythonparts-mcp-setup
description: Sets up or reconfigures the `pythonparts-local-mcp` server with the ALLPLAN 2027 Std and Usr paths. Use when the user runs /pythonparts-mcp-setup, wants to set or change their ALLPLAN Std or Usr path, or when `get_allplan_info` of `pythonparts-local-mcp` returns a Std or Usr path starting with `REPLACE-WITH-`. You MUST run this skill before any PythonParts work that relies on `pythonparts-local-mcp` (type checks, snippets, symbol inspection, ALLPLAN paths) if the server is not set up.
---

# PythonParts local MCP setup

The `pythonparts-local-mcp` server needs the user's ALLPLAN 2027 **Std** (office standard) and **Usr** (user) directories. Claude Code asks for them when the plugin is installed. GitHub Copilot (VS Code and CLI) cannot, so the plugin ships with placeholders and this skill writes the real paths into the plugin's MCP configuration.

## Determine the server state

Call `get_allplan_info` of `pythonparts-local-mcp` and look at `paths.std` and `paths.usr`:

| Result | State |
|---|---|
| A path starts with `REPLACE-WITH-` | **not-setup** |
| Both paths are set | **working** |
| The tool is not available or the call fails | Read `<plugin-root>/mcp.json`. If it contains `REPLACE-WITH-`, the state is **not-setup**, otherwise **not-working**. |

Then act on the state:

- **working**: if the user explicitly asked to change the paths, follow [Configure the paths](#configure-the-paths). Otherwise, continue with the user's original request without mentioning this check.
- **not-setup**: tell the user the local PythonParts MCP server is not configured yet and follow [Configure the paths](#configure-the-paths).
- **not-working**: follow [Troubleshooting](#troubleshooting).

Do not suggest workarounds that bypass the MCP server, such as hard-coding paths in the code or skipping the type check. Set up the server first unless the user explicitly asks otherwise.

## Configure the paths

Pick the section that matches the client you are running in.

### GitHub Copilot (VS Code or CLI)

1. **Ask for the paths.** Ask the user for their ALLPLAN 2027 Std and Usr paths. Do not try to detect them on the user's machine, and do not pre-fill them. Show the typical locations only as examples:

   | Path | Example |
   |---|---|
   | Std | `C:\Data\Allplan\Allplan 2027\Std` |
   | Usr | `C:\Users\<you>\Documents\Nemetschek\Allplan\2027\Usr\Local` |

   If the user is unsure, tell them that ALLPLAN shows both paths in **Allmenu > Service > Windows Explorer**. Use the paths exactly as the user enters them.

2. **Write the configuration.** Edit `<plugin-root>/mcp.json` as described in [Edit rule](#edit-rule).

3. **Ask the user to reload.** Tell the user:

   > The local PythonParts MCP server has been configured. To activate it:
   >
   > - **VS Code**: open the Command Palette, run **MCP: List Servers**, and restart `pythonparts-local-mcp`.
   > - **Copilot CLI**: restart the session.
   >
   > Updating or reinstalling the plugin resets this configuration. Run `/pythonparts-mcp-setup` again afterwards.

   Then stop. Do not call `pythonparts-local-mcp` tools until the user has reloaded.

### Claude Code

Claude Code stores the paths as plugin options, not in `mcp.json`. Do not edit any plugin file. Tell the user:

> To set or change the ALLPLAN paths, run `/plugin configure pythonparts-2027@allplan-pythonparts`, enter the Std and Usr paths, and then run `/mcp` to reconnect `pythonparts-local-mcp`.

Then stop.

## Edit rule

`<plugin-root>` is the directory that contains this skill's `skills` folder. Derive it by removing `skills/pythonparts-mcp-setup/SKILL.md` from this file's path. Edit `<plugin-root>/mcp.json` only. Never edit `<plugin-root>/.mcp.json`, which belongs to Claude Code.

In the `pythonparts-local-mcp` entry, replace only the argument that follows `--std-path` and the argument that follows `--usr-path`. Leave everything else untouched, including `--allplan-version` and the `pythonparts-knowledge-mcp` entry.

Escape each backslash as `\\` in JSON. Before and after (example):

```json
"--std-path", "REPLACE-WITH-ALLPLAN-STD-PATH",
"--usr-path", "REPLACE-WITH-ALLPLAN-USR-PATH"
```

```json
"--std-path", "C:\\Data\\Allplan\\Allplan 2027\\Std",
"--usr-path", "C:\\Users\\jdoe\\Documents\\Nemetschek\\Allplan\\2027\\Usr\\Local"
```

After editing, parse the file as JSON (for example, with `ConvertFrom-Json`) to confirm it is still valid.

## Troubleshooting

If the paths are configured but `pythonparts-local-mcp` does not respond, tell the user:

> The local PythonParts MCP server is configured but not running. Check the following:
>
> 1. `uv` is installed and `uvx` is on `PATH`. To install it, run `winget install astral-sh.uv`, then restart VS Code or the terminal.
> 2. ALLPLAN 2027 is installed on this machine.
> 3. The server is started. In VS Code, run **MCP: List Servers** and start or restart `pythonparts-local-mcp`. In Copilot CLI, restart the session.
>
> To enter different paths, run `/pythonparts-mcp-setup` again.

Then stop.
