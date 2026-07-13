# PythonParts Vibe Coding

A collection of **AI agent skills** that turn GitHub Copilot or Claude Code into an expert **PythonParts developer** — so you can build parametric ALLPLAN extensions by describing what you want, rather than writing everything from scratch.

## What's in this repo

```
agents/
    pythonpart-coder.agent.md   ← A specialized AI agent for PythonParts development
skills/
    create-new-pythonpart/      ← Step-by-step workflow for creating a new PythonPart
    allplan-environment/        ← ALLPLAN version, framework paths, and file locations
    ui-design/                  ← How to design the PYP file and its property palette
    pythonpart-script/          ← How to structure and write the PY file
    allplan-elements/           ← How to create native ALLPLAN elements from geometry
    geometry/                   ← How to create and manipulate ALLPLAN geometry
```

The **agent** orchestrates the whole process. The **skills** are focused building blocks it calls when needed — and you can invoke them directly too.

> **This is a living project.** New skills covering more ALLPLAN features and use cases will be added over time. Watch or star the repo to stay updated.

## How to use it

### With GitHub Copilot (VS Code)

Copy the `agents/` and `skills/` folders into a `.github/` directory inside your project:

```
your-project/
└── .github/
    ├── agents/
    └── skills/
```

Then open GitHub Copilot Chat, switch to **Agent mode**, and select the **PythonPart Coder** agent. Describe what you want to build and let it guide you.

### With Claude Code

Copy the `agents/` and `skills/` folders into a `.claude/` directory inside your project:

```
your-project/
└── .claude/
    ├── agents/
    └── skills/
```

### With Codex

Copy the `agents/` and `skills/` folders into a `.codex/` directory inside your project:

```
your-project/
└── .codex/
    ├── agents/
    └── skills/
```

Then start a Codex task in your ALLPLAN project and describe the PythonPart you want to build. Codex can use the PythonPart Coder agent and the installed skills directly, such as `create-new-pythonpart`, `ui-design`, and `pythonpart-script`.
Claude Code will automatically pick up the skills (invoke them with `/coding-pythonpart`, `/property-palette`, etc.) and the subagent definition.

## Typical workflow

1. Open your ALLPLAN project in VS Code
2. Start the PythonPart Coder agent and describe your PythonPart (e.g. *"Create a parametric rectangular column with configurable width, depth, and height"*)
3. The agent will ask clarifying questions, then generate both the PYP and PY files
4. Copy the generated files to the correct ALLPLAN directories (the agent tells you where)
5. Open ALLPLAN and test your PythonPart

You don't need to understand every line of code to get started — but the generated code is clean and well-structured, so it's a good starting point if you want to learn.

## Requirements

- **ALLPLAN** (2026 or newer recommended)
- **VS Code** with the GitHub Copilot extension, or **Claude Code**
- No Python installation required to get started — ALLPLAN ships its own Python runtime
