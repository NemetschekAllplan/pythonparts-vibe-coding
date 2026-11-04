---
name: pythonparts-mcp-setup
description: Sets up or reconfigures the `pythonparts-local-mcp` server with the ALLPLAN 2027 Std and Usr paths. Use when the user runs /pythonparts-mcp-setup, wants to set or change their ALLPLAN Std or Usr path, or when `get_allplan_info` of `pythonparts-local-mcp` returns `Not set. Use set_allplan_paths()` for the Std or Usr path. You MUST run this skill before any PythonParts work that relies on `pythonparts-local-mcp` (type checks, snippets, symbol inspection, ALLPLAN paths) if the server is not set up.
---

# PythonParts local MCP setup

The `pythonparts-local-mcp` server needs the user's ALLPLAN 2027 **Std** (office standard) and **Usr** (user) directories. Claude Code asks for them when the plugin is installed. In the other clients, this skill asks for them and saves them with the `set_allplan_paths` tool of the server. The server stores them in the plugin data directory (`PLUGIN_DATA/config.json`), so they survive plugin updates.

## Determine the server state

Call `get_allplan_info` of `pythonparts-local-mcp` and look at `paths.std` and `paths.usr`:

| Result | State |
|---|---|
| A path is `Not set. Use set_allplan_paths()` | **not-setup** |
| Both paths are set | **working** |
| The tool is not available or the call fails | **not-working** |

Then act on the state:

- **working**: if the user explicitly asked to change the paths, follow [Configure the paths](#configure-the-paths). Otherwise, continue with the user's original request without mentioning this check.
- **not-setup**: tell the user the local PythonParts MCP server is not configured yet and follow [Configure the paths](#configure-the-paths).
- **not-working**: follow [Troubleshooting](#troubleshooting).

Do not suggest workarounds that bypass the MCP server, such as hard-coding paths in the code or skipping the type check. Set up the server first unless the user explicitly asks otherwise.

## Configure the paths

Pick the section that matches the client you are running in.

### GitHub Copilot and OpenAI Codex

1. **Ask for the paths.** Ask the user for their ALLPLAN 2027 Std and Usr paths. Do not try to detect them on the user's machine, and do not pre-fill them. Show the typical locations only as examples:

   | Path | Example |
   |---|---|
   | Std | `C:\Data\Allplan\Allplan 2027\Std` |
   | Usr | `C:\Users\<you>\Documents\Nemetschek\Allplan\2027\Usr\Local` |

   If the user is unsure, tell them that ALLPLAN shows both paths in **Allmenu > Service > File Explorer**. If the user wants to change only one path, ask only for that one. Use the paths exactly as the user enters them.

2. **Save the paths.** Call `set_allplan_paths` of `pythonparts-local-mcp` with `std_path` and `usr_path`. After the tool is called, the paths are active immediately.

   - If the tool rejects a path (it is not an existing directory), tell the user which one and ask again. Nothing was saved in that case.
   - If the response has `data.warnings`, relay them to the user.

3. **Check the result.**

   - `data.persisted` is `true`: tell the user that this was a one-time setup and it will survive plugin updates.
   - `data.persisted` is `false`: the paths are active only for the current session. Follow [Fallback without persistence](#fallback-without-persistence).

   Then call `get_allplan_info` to confirm and continue with the user's original request.

### Claude Code

Claude Code stores the paths as plugin options, not in `mcp.json`. Do not edit any plugin file. Tell the user:

> To set or change the ALLPLAN paths, run `/plugin configure pythonparts-2027@allplan-pythonparts`, enter the Std and Usr paths, and then run `/mcp` to reconnect `pythonparts-local-mcp`.

Then stop.

## Fallback without persistence

Use this only when `set_allplan_paths` reports `data.persisted` as `false`, which means the host does not provide a plugin data directory.

`<plugin-root>` is the directory that contains this skill's `skills` folder. Derive it by removing `skills/pythonparts-mcp-setup/SKILL.md` from this file's path. Edit `<plugin-root>/mcp.json` only. Never edit `<plugin-root>/.mcp.json`, which belongs to Claude Code.

In the `pythonparts-local-mcp` entry, add `--std-path` and `--usr-path` with the paths to `args`, after `--allplan-version`. Leave everything else untouched, including the `pythonparts-knowledge-mcp` entry. If the arguments already exist, replace only their values.

Escape each backslash as `\\` in JSON. Example:

```json
"args": [
  "pythonparts-mcp@latest",
  "--allplan-version", "2027",
  "--std-path", "C:\\Data\\Allplan\\Allplan 2027\\Std",
  "--usr-path", "C:\\Users\\jdoe\\Documents\\Nemetschek\\Allplan\\2027\\Usr\\Local"
]
```

After editing, parse the file as JSON (for example, with `ConvertFrom-Json`) to confirm it is still valid. Then tell the user:

> The paths could not be saved in a plugin data directory, so I wrote them into the `args` of `pythonparts-local-mcp` in `<plugin-root>/mcp.json`. Arguments take precedence over `config.json`. To activate them, restart the server (**VS Code**: **MCP: List Servers** > restart `pythonparts-local-mcp`; **Copilot CLI** and **Codex**: start a new session). Updating or reinstalling the plugin resets this change. Run `/pythonparts-mcp-setup` again afterwards.

The current session already uses the paths set by `set_allplan_paths`, so you can continue working without waiting for the restart.

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
