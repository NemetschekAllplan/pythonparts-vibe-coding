# ALLPLAN PythonParts agent plugins

Agent plugins for developing ALLPLAN PythonParts with AI coding assistants. They work with Claude Code, Claude Desktop, GitHub Copilot (VS Code, CLI, and app), and OpenAI Codex.

The marketplace `allplan-pythonparts` provides one plugin per ALLPLAN major version:

| Plugin | ALLPLAN version |
|---|---|
| `pythonparts-2027` | 2027 |

Each plugin includes:

| Component | Type | Purpose |
|---|---|---|
| `pythonparts-planner` | Agent | Plans a PythonPart before any code is written. |
| `pythonparts-coder` | Agent | Implements PythonParts. |
| `pythonparts-local-mcp` | MCP server | Runs locally with your ALLPLAN installation. Type checks code, runs snippets, and inspects the PythonParts API. |
| `pythonparts-knowledge-mcp` | MCP server | Hosted PythonParts knowledge base. Requires sign-in with ALLPLAN Connect. |
| `pythonparts-mcp-setup` | Skill | Sets the ALLPLAN Std and Usr paths for `pythonparts-local-mcp`. |

## Quickstart

### 1. Install uv

`pythonparts-local-mcp` runs with `uvx`. Install [uv](https://docs.astral.sh/uv/getting-started/installation/). On Windows, you can use [winget](https://learn.microsoft.com/en-us/windows/package-manager/winget/):

```sh
winget install astral-sh.uv
```

Check that `uvx` is available in a new terminal:

```sh
uvx -V
```

### 2. Find your ALLPLAN Std and Usr paths

In ALLPLAN, open **Allmenu > Service > File Explorer**:

| Path | Allmenu entry | Example |
|---|---|---|
| Std | Office standard (STD) | `C:\Data\Allplan\Allplan 2027\Std` |
| Usr | My own CAD documents (USR) | `C:\Users\<you>\Documents\Nemetschek\Allplan\2027\Usr\Local` |

### 3. Install and configure the plugin

Claude Code asks for the Std and Usr paths during installation. Other clients can't, so you configure the paths with the `pythonparts-mcp-setup` skill after installation.

<details>
<summary>VS Code with GitHub Copilot</summary>

1. Click the button to install the plugin:

   [![Install in VS Code](https://img.shields.io/badge/VS_Code-Install_PythonParts_2027-0098FF?style=flat-square&logo=visualstudiocode&logoColor=white)](https://vscode.dev/redirect?url=vscode%3A%2F%2Fchat-plugin%2Finstall%3Fsource%3DTmVtZXRzY2hla0FsbHBsYW4vcHl0aG9ucGFydHMtdmliZS1jb2Rpbmc=%26plugin%3Dpythonparts-2027)

2. In the chat, run `/pythonparts-mcp-setup` and enter your Std and Usr paths.
3. Open the Command Palette, run **MCP: List Servers**, and restart `pythonparts-local-mcp`.

</details>

<details>
<summary>VS Code with Claude Code</summary>

1. Click the button to install the plugin:

   [![Install in Claude Code](https://img.shields.io/badge/Claude_Code-Install_PythonParts_2027-D97757?style=flat-square&logo=claude&logoColor=white)](https://vscode.dev/redirect?url=vscode%3A%2F%2Fanthropic.claude-code%2Finstall-plugin%3Fplugin%3Dpythonparts-2027%26marketplace%3DNemetschekAllplan%2Fpythonparts-vibe-coding)

2. In the chat, run `/pythonparts-2027:pythonparts-mcp-setup` and follow the instructions to enter your Std and Usr paths.

</details>

<details>
<summary>Claude Code CLI</summary>

1. In your terminal, run:

   ```sh
   claude plugin marketplace add NemetschekAllplan/pythonparts-vibe-coding
   claude plugin install pythonparts-2027@allplan-pythonparts
   ```

2. In Claude Code, run `/plugin configure pythonparts-2027@allplan-pythonparts` and enter your Std and Usr paths.

To skip step 2, pass the paths during installation:

```sh
claude plugin install pythonparts-2027@allplan-pythonparts --config "std_path=C:\Data\Allplan\Allplan 2027\Std" --config "usr_path=C:\Users\<you>\Documents\Nemetschek\Allplan\2027\Usr\Local"
```

</details>

<details>
<summary>Claude Desktop</summary>

Follow the steps for **Claude Code CLI** above.

</details>

<details>
<summary>GitHub Copilot CLI</summary>

1. In your terminal, run:

   ```sh
   copilot plugin marketplace add NemetschekAllplan/pythonparts-vibe-coding
   copilot plugin install pythonparts-2027@allplan-pythonparts
   ```

2. In a Copilot CLI session, run `/pythonparts-2027:pythonparts-mcp-setup` and enter your Std and Usr paths.
3. Restart the Copilot CLI session.

</details>

<details>
<summary>GitHub Copilot app</summary>

1. Click the button to add the marketplace:

   [![Add marketplace to the GitHub Copilot app](https://img.shields.io/badge/Copilot_app-Add_marketplace-24292F?style=flat-square&logo=github&logoColor=white)](ghapp://plugins/marketplace/add?source=NemetschekAllplan%2Fpythonparts-vibe-coding)

   Alternatively, go to **Customize > Plugins**, click the marketplace settings icon next to the marketplace dropdown, and add `NemetschekAllplan/pythonparts-vibe-coding`.

2. In **Customize > Plugins**, find `pythonparts-2027` and click **Install**.
3. In a session, run `/pythonparts-2027:pythonparts-mcp-setup` and enter your Std and Usr paths.
4. Start a new session.

</details>

<details>
<summary>OpenAI Codex</summary>

1. In your terminal, run:

   ```sh
   codex plugin marketplace add NemetschekAllplan/pythonparts-vibe-coding
   codex plugin add pythonparts-2027@allplan-pythonparts
   ```

2. Start a new Codex session, run `$pythonparts-mcp-setup`, and enter your Std and Usr paths.
3. Start a new Codex session.

</details>

### 4. Sign in to ALLPLAN Connect

`pythonparts-knowledge-mcp` requires sign-in with your ALLPLAN Connect account. Your client prompts you when it first connects to the server. In Claude Code, run `/mcp` and authenticate the server.

> [!NOTE]
> Updating or reinstalling the plugin resets paths configured with `pythonparts-mcp-setup`. Run the skill again afterwards. To change the paths later, repeat the configuration step for your client.
