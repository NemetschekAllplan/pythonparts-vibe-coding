# Changelog

All notable changes to the `pythonparts-2027` plugin are documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/).

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
