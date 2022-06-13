# Nekoslife
**An unofficial wrapper for [nekos.life api](https://nekos.life/) with proxy support.**


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
- Lightweight
- Fast even with proxy
