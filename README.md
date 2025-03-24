# Simple wrapper around matplotlib for render color scheme palette

The format of pictures for saving is the same as matplotlib

> [!WARNING]
> The library is under deep development.
> But it will be very useful to get feedback.

![palette](https://github.com/user-attachments/assets/576a0993-7a64-4e05-82eb-4c5a6101ca96)

## Usage

Install package

```bash
pip install draw_palette
```

Copy the lua file of a defined color.

Example usage:

```python
from draw_palette import utils, DrawPalette

# Use internal lua import function as dict of tuple (color_name, hex)
colors = utils.import_palette("./colors.lua")
# Sort colors by name
colors.sort(key=lambda x: x[0])

CONFIG = {
    "spacing": 0.05,  # spacing between cells
    "dpi": 300,  # dpi of output image
    "rounding": 0.05,  # rounding of cell
    "max_column_num": 6,  # max colomns
    "cell_size": 3.0,  # size of color cell
    "fontfamily": "monospace",  # font family for any text
    "color_name_size": 14,  # font size of label color name
    "color_hex_size": 8,  # font size of label color HEX value
}


# Create palette object
palette = DrawPalette(colors, config=CONFIG) # argument is a list of tuple
# Render it
palette.render()
# Save to the file
palette.save_image(image_name='palette.png')
```

### `colors.lua`

To render a palette, a color table must be fed to the input.
Example of lua file with scheme:

```lua
local M = {}

---@class Palette
---@type table
M.palette = {
  red = "#cc6666",
  -- color name = "# HEX RGB value",
}

return M.palette
```

## Development

Make Python virtual envelope and enable it

```bash
python -m venv .venv
make init
```
