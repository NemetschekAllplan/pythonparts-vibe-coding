# Changelog

All notable changes to the `pythonparts-2027` plugin are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

## [Unreleased]

### Changed

- The ALLPLAN Std and Usr paths are saved once with the new `set_allplan_paths` tool of `pythonparts-local-mcp` and survive plugin updates. You no longer need to run `pythonparts-mcp-setup` again after an update.
- `pythonparts-mcp-setup` asks for the paths and calls `set_allplan_paths` instead of editing `mcp.json`. The paths are active immediately, without a reload. If the host provides no plugin data directory, the skill falls back to writing the paths into the `args` of `pythonparts-local-mcp`.
- `mcp.json` no longer contains the `REPLACE-WITH-` placeholders and the `--std-path` and `--usr-path` arguments.
- The Copilot agents detect a missing setup by the `Not set. Use set_allplan_paths()` value returned by `get_allplan_info`.
- The Copilot `pythonparts-planner` and `pythonparts-coder` agents run the `pythonparts-mcp-setup` skill themselves when the Std or Usr path is not set, instead of asking the user to run it. `pythonparts-researcher` reports the missing setup to its caller.
- Requires `pythonparts-mcp` 0.3.0 or later, which `uvx pythonparts-mcp@latest` installs.

## [2027.0.1-beta.2]

### Added

- `pythonparts-researcher` agent that answers framework questions with source-cited briefings for the planner and coder. It does not edit files.
- `ask_user` tool support in the Copilot agents for compatibility with the Copilot SDK.

### Changed

- `pythonparts-planner` and `pythonparts-coder` delegate research to `pythonparts-researcher`.
- Improved compatibility of the agents with the Copilot SDK and the local VS Code harness.

## [2027.0.1-beta.1]

### Added

- Initial beta release of the `pythonparts-2027` plugin for ALLPLAN 2027. The plugin is under active development, and its behavior may change between releases.
- `pythonparts-planner` agent for planning a PythonPart before any code is written.
- `pythonparts-coder` agent for implementing PythonParts.
- `pythonparts-local-mcp` MCP server for type checking, running snippets, and inspecting the PythonParts API.
- `pythonparts-knowledge-mcp` MCP server providing the hosted PythonParts knowledge base.
- `pythonparts-mcp-setup` skill for setting the ALLPLAN Std and Usr paths.
