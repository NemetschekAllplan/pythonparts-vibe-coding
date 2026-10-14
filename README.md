# ALLPLAN PythonParts agent plugins

Plugin marketplace `allplan-pythonparts` with one plugin per ALLPLAN major version.

| Plugin | ALLPLAN | Clients |
|---|---|---|
| `pythonparts-2027` | 2027 | Claude Code (CLI and VS Code extension) |

Each plugin adds the **pythonparts-planner** and **pythonparts-coder** agents and the
`pythonparts-local-mcp` and `pythonparts-knowledge-mcp` MCP servers.

## Prerequisites

- [`uv`](https://docs.astral.sh/uv/) on `PATH` (provides `uvx`)
  
  To install it using winget, run:

  ```sh
  winget install astral-sh.uv
  ```

- ALLPLAN 2027

## Installation

### Claude Code

```sh
claude plugin marketplace add NemetschekAllplan/pythonparts-vibe-coding
claude plugin install pythonparts-2027@allplan-pythonparts
```

When the plugin is enabled, Claude Code asks for **your** Allplan's Std and Usr paths:

| Option | Example |
|---|---|
| `std_path` | `C:\Data\Allplan\Allplan 2027\Std` |
| `usr_path` | `C:\Users\<you>\Documents\Nemetschek\Allplan\2027\Usr\Local` |

To change them later, run `/plugin configure pythonparts-2027@allplan-pythonparts` in Claude Code.
Alternatively, pass them with `--config` during the installation:

```sh
claude plugin install pythonparts-2027@allplan-pythonparts --config "std_path=C:\Data\Allplan\Allplan 2027\Std" --config "usr_path=C:\Users\<you>\Documents\Nemetschek\Allplan\2027\Usr\Local"
```

`pythonparts-knowledge-mcp` requires sign-in. Run `/mcp` in Claude Code and authenticate the server.

The agents appear as `pythonparts-2027:pythonparts-planner` and `pythonparts-2027:pythonparts-coder`.

## Repository layout

```text
.claude-plugin/marketplace.json        # Claude Code marketplace catalog
plugins/pythonparts-2027/
├── .claude-plugin/plugin.json         # Claude Code manifest, incl. userConfig for Std/Usr paths
├── .mcp.json                          # Claude Code MCP config
├── agents/                            # Claude Code agents
```
