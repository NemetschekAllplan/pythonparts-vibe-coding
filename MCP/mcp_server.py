import os
from pathlib import Path
from typing import Optional

import git
from fastmcp import FastMCP
from fastmcp.server.transforms import ResourcesAsTools

# Create the server instance
mcp = FastMCP("my-local-server", instructions="My custom tools for VS Code / local development.")

# Configuration
REPO_URL = "https://github.com/NemetschekAllplan/pythonparts-vibe-coding/tree/MCP"  # Change this
LOCAL_PATH = Path("./cloned_repos/my-knowledge-repo")  # Local clone destination

def ensure_repo_up_to_date():
    """Clone if missing, otherwise pull latest."""
    if not LOCAL_PATH.exists():
        print(f"Cloning {REPO_URL}...")
        git.Repo.clone_from(REPO_URL, str(LOCAL_PATH))
    else:
        try:
            repo = git.Repo(str(LOCAL_PATH))
            print("Pulling latest changes...")
            repo.remotes.origin.pull()
        except Exception as e:
            print(f"Pull failed: {e}. Consider removing {LOCAL_PATH} and retrying.")


@mcp.tool
def add(a: int, b: int) -> int:
    """Add two numbers together."""
    return a + b


@mcp.tool
def greet(name: str) -> str:
    """Greet a user by name."""
    return f"Hello, {name}!"


@mcp.tool
def place_python_parts_to_allplan_file_system() -> str:
    """Simulate placing Python parts to Allplan.
    
    Palette, visual, representation (*.pyp) files should be placed in the Allplan library under the Private folder.
    Allplan -> Library -> Private
    
    C:\\Users\\lmajerik\\Documents\\Nemetschek\\MAIN_Construction\\99\\Usr\\Local\\Library\\
        
    Script, logical files (*.py) should be placed in the Allplan python folder:
    
    C:\\P4V\\MainConstruction\\DeliveryData\\etc\\PythonPartsExampleScripts\\VibeCoding
    
    Pyp files will than have the following pointing to the the script file, it should run:
    
    F.e.: new python part created with name new_python_part will have the following structure:
    
    <Script>
        <Title>new_python_part</Title>
        <Name>VibeCoding\\new_python_part.py</Name> 
    
    """

    return "Python parts have been placed to Allplan successfully."


# 2. Resource Template - Read any file while preserving path
@mcp.resource("knowledge://{path*}")
def get_file(path: str) -> str:
    """
    Read any file from the folder while preserving the full path structure.
    
    Examples:
    - folder://README.md
    - folder://docs/architecture.md
    - folder://src/utils/helper.py
    """
    
    ensure_repo_up_to_date()

    if not LOCAL_PATH.exists():
        raise FileNotFoundError(f"File not found: {path}")


    # Return as text (for .md, .txt, .py, .json, etc.)
    if LOCAL_PATH.suffix.lower() in {'.md', '.txt', '.py', '.json', '.yaml', '.yml', '.html', '.css', '.js'}:
        return LOCAL_PATH.read_text(encoding="utf-8")
    else:
        # For binary files, you can return a note or use BinaryResource
        return f"[Binary file: {path}] Size: {LOCAL_PATH.stat().st_size} bytes"

# 3. Optional: Root index / summary
@mcp.resource("knowledge://index")
def folder_index() -> str:
    """Summary of the folder structure."""
    
    ensure_repo_up_to_date()
    
    files = list(LOCAL_PATH.rglob("*"))
    tree = []
    for item in sorted(files):
        rel = item.relative_to(LOCAL_PATH)
        prefix = "  " * (len(rel.parts) - 1)
        tree.append(f"{prefix}• {rel}")
    
    return f"""Folder: {LOCAL_PATH.name}
        Total items: {len(files)}
        Structure:
        """ + "\n".join(tree)

@mcp.resource("knowledge://index")
def resource_dummy_1() -> str:
    
    """This is a dummy resource to demonstrate multiple resources under the same template."""
    return "This is a dummy resource response."
    

mcp.add_transform(ResourcesAsTools(mcp))



if __name__ == "__main__":
    # For local use with VS Code: default is STDIO (recommended)
    mcp.run()

    # For HTTP (if you want a remote-accessible server):
    # mcp.run(transport="http", host="127.0.0.1", port=8000)
