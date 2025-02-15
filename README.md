# Simple script for render color scheme palette

![Sample palette](./color_palette.png)

## Usage

Make Python virtual enveloplent and activate it

```bash
python -m venv .venv
source .venv/bin/activate
```

Install package

```bash
pip install -r requirements.txt
```

Run script(befor copy colors.lua to the root)

```bash
./plot_palette.py
```

## colors.lua format

To render a palette, a color table must be fed to the input.

```lua
local M = {}

---@class Palette
---@type table
M.palette = {
  red = "#cc6666",
  -- color name = "# HEX RGB value",
}

return M
```
