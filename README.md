# Nekoslife
**An unofficial wrapper for [nekos.life api](https://nekos.life/) with proxy support.**

![PyPI - Downloads](https://img.shields.io/pypi/dw/nekoslife?color=g&label=Downloads&logo=pypi&style=for-the-badge)
![PyPI - Version](https://img.shields.io/pypi/v/nekoslife?style=for-the-badge)
![GitHub Workflow Status (event)](https://img.shields.io/github/workflow/status/Blank-c/NekosLife/Upload%20Python%20Package?style=for-the-badge)

## Installation:
```
pip install nekoslife
```

## Usage:
```python
from nekoslife import Life

life = Life()

async def func():
    data = await life.img_neko()
    return data.get("url")
```

**To use proxy:**
```python
life = Life(proxy= True)
```

**List of available modules:**
```python
life = Life()
print(life._endpoints)
```
## Features:
- Fully Asynchronous.
- Proxy Support.
- Easy to use.
- Lightweight.
- Fast even with proxy.
