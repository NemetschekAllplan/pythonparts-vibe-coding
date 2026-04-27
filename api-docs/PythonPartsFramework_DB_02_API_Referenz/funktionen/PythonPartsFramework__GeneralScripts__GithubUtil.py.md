---
title: "GithubUtil"
source: "PythonPartsFramework\GeneralScripts\GithubUtil.py"
type: "module"
category: "02_API_Referenz"
tags:
  - script
  - utility
related:
  -
last_updated: "2026-02-20"
---


# GithubUtil

> **Pfad:** `PythonPartsFramework\GeneralScripts\GithubUtil.py`  
> **Typ:** Modul  
> **Tags:** `script`, `utility`

## Übersicht

Keine Modul-Docstring vorhanden.

## Abhängigkeiten

- `NemAll_Python_AllplanSettings`
- `io`
- `os`
- `requests`
- `shutil`
- `zipfile`

## Klassen

Keine Klassen vorhanden.

## Funktionen

### `download_github_repo_as_zip(owner: str, repo: str, branch: str='main')`

Download github as a zip.

Args:
    owner  : Owner of the repo.
    repo   : Repo name.
    branch : Branch from which to download zip.

**Parameter:**
- `owner: str`
- `repo: str`
- `branch: str='main'`

**Rückgabe:** `None`

**Beispiel:**
```python
result = download_github_repo_as_zip(..., ..., ...)
```

### `check_github_branch_exists(owner: str, repo: str, branch: str)`

Check if github branch exists.

Args:
    owner  : Owner of the repo.
    repo   : Repo name.
    branch : Branch to check.

Returns:
    bool : Boolean to represent if branch exists.

**Parameter:**
- `owner: str`
- `repo: str`
- `branch: str`

**Rückgabe:** `bool`

**Beispiel:**
```python
result = check_github_branch_exists(..., ..., ...)
```

### `get_last_commit_info(owner, repo, branch)`

Get last commit of branch.
Args:
    owner  : Owner of the repo.
    repo   : Repo name.
    branch : Branch to check.

    Returns:
        dict : reponse from request as a python dict.

**Parameter:**
- `owner`
- `repo`
- `branch`

**Rückgabe:** `dict`

**Beispiel:**
```python
result = get_last_commit_info(..., ..., ...)
```

### `delete_folder()`

Keine Funktions-Docstring vorhanden.

**Parameter:**
- Keine

**Rückgabe:** `None`

**Beispiel:**
```python
result = delete_folder()
```

## Quellcode

<details>
<summary>Vollständiger Code anzeigen</summary>

```python
import requests
import zipfile
from io import BytesIO
import os
import shutil

import NemAll_Python_AllplanSettings as AllplanSettings

USR_PATH = AllplanSettings.AllplanPaths.GetUsrPath()

def download_github_repo_as_zip(owner: str, repo: str, branch: str ='main'):
    """ Download github as a zip.

    Args:
        owner  : Owner of the repo.
        repo   : Repo name.
        branch : Branch from which to download zip.
    """

    url = f'https://github.com/{owner}/{repo}/archive/refs/heads/{branch}.zip'

    response = requests.get(url)
    response.raise_for_status()

    zip_file = BytesIO(response.content)

    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        for x, info in zip_ref.NameToInfo.items():

            if (x.count("/") < 2 and x[-1] == "/") or x.endswith(".md") or x.startswith(".git"):
                continue

            info.filename  = "/".join(info.filename.split("/")[1:])
            zip_ref.extract(member = info, path = USR_PATH)

def check_github_branch_exists(owner: str, repo: str, branch: str) -> bool:
    """ Check if github branch exists.

    Args:
        owner  : Owner of the repo.
        repo   : Repo name.
        branch : Branch to check.

    Returns:
        bool : Boolean to represent if branch exists.
    """

    url = f'https://api.github.com/repos/{owner}/{repo}/branches/{branch}'


    response = requests.get(url)

    if response.status_code == 200:
        return True
    return False

def get_last_commit_info(owner, repo, branch) -> dict:
    """ Get last commit of branch.
    Args:
        owner  : Owner of the repo.
        repo   : Repo name.
        branch : Branch to check.

        Returns:
            dict : reponse from request as a python dict.
    """

    url = f'https://api.github.com/repos/{owner}/{repo}/commits/{branch}'

    response = requests.get(url)
    response.raise_for_status()

    return response.json()

def delete_folder():

    python_part = os.path.join(USR_PATH, "Library\\Examples\\PythonParts")
    example_script = os.path.join(USR_PATH, "PythonPartsExampleScripts")


    if os.path.exists(python_part):
        shutil.rmtree(python_part)
        print(f"Deleted folder at {python_part} successfully")

    if os.path.exists(example_script):
        shutil.rmtree(example_script)
        print(f"Deleted folder at {example_script} successfully")

```

</details>