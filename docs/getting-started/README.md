---
title: Getting Started
summary: Quick installation and usage instructions.
authors:
    - hreikin
---
## Installation

To get a local copy up and running choose one of the below install instructions and follow the steps provided.

### Install With PIP

The simplest way to install `tkintermd` is to use `pip`:

```sh
pip install tkintermd
```

### Install From Source

Alternatively you can install from source by following the steps below:

1. Clone the repo:

   ```sh
   git clone https://github.com/hreikin/tkintermd.git
   cd tkintermd/
   ```

2. Create and source a Python virtual environment:

   ```sh
   python3 -m venv .venv
   source .venv/bin/activate
   ```

3. Install requirements with `pip`:

   ```sh
   pip install -r requirements.txt
   ```

<!-- USAGE EXAMPLES -->
## Usage

### Embedded

To use the `TkintermdFrame` in one of your own python scripts:

```python
from tkintermd.frame import TkintermdFrame

import tkinter as tk
from tkinter.constants import *

root = tk.Tk()
app = TkintermdFrame(root)
app.pack(fill="both", expand=1)
app.mainloop()
```
