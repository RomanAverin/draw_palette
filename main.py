import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch
import lupa.lua54 as lupa

# Initialize the Lua runtime
lua = lupa.LuaRuntime()
print(
    f"Using {lupa.LuaRuntime().lua_implementation} (compiled with {lupa.LUA_VERSION})"
)


with open("colors.lua", "r") as f:
    lua_code = f.read()

lua_palette = lua.execute(lua_code)["palette"]  # pyright: ignore
palette = {}
for color in lua_palette.items():
    palette.update({color[0]: color[1]})


def get_text_color(hex_color):
    """Get text colors"""
    hex_color = hex_color.lstrip("#")
    r = int(hex_color[0:2], 16)
    g = int(hex_color[2:4], 16)
    b = int(hex_color[4:6], 16)
    brightness = 0.299 * r + 0.587 * g + 0.114 * b
    return "white" if brightness < 128 else "black"


names = list(palette.keys())
colors = list(palette.values())
n = len(names)

# Grid settings
n_cols = 10  # max columm
SPACING = 0.05  # space between a cells
CELL_SIZE = 2.0
n_rows = (n + n_cols - 1) // n_cols


# Параметры стиля
RECT_PAD = 0.05
ROUNDING_SIZE = 0.05
RECT_WIDTH = CELL_SIZE - SPACING
HEX_FONTSIZE = 10
NAME_FONTSIZE = 12

fig, ax = plt.subplots(figsize=(n, 2.5 * n_rows * (CELL_SIZE + SPACING)))
ax.set_aspect("equal")
ax.axis("off")

for i in range(n):
    row = i // n_cols
    col = i % n_cols
    y_pos = (n_rows - 1 - row) * (CELL_SIZE + SPACING)
    x_pos = col * (CELL_SIZE + SPACING)

    # Создаем прямоугольник с закругленными краями
    rect = FancyBboxPatch(
        (x_pos + RECT_PAD, y_pos + RECT_PAD),
        RECT_WIDTH - 2 * RECT_PAD,
        RECT_WIDTH - 2 * RECT_PAD,
        boxstyle=f"round,pad={RECT_PAD},rounding_size={ROUNDING_SIZE}",
        facecolor=colors[i],
        edgecolor="none",
    )
    ax.add_patch(rect)

    text_color = get_text_color(colors[i])

    # Color name
    ax.text(
        x_pos + CELL_SIZE / 2,
        y_pos + CELL_SIZE / 2,
        names[i],
        ha="center",
        va="center",
        color=text_color,
        fontsize=NAME_FONTSIZE,
        wrap=True,
        linespacing=0.8,
    )

    # HEX-color
    ax.text(
        x_pos + CELL_SIZE - 0.1,
        y_pos + 0.1,
        colors[i].upper(),
        ha="right",
        va="bottom",
        color=text_color,
        fontsize=HEX_FONTSIZE,
        alpha=0.8,
        fontfamily="monospace",
    )

ax.set_xlim(0, n_cols * (CELL_SIZE + SPACING) - SPACING)
ax.set_ylim(0, n_rows * (CELL_SIZE + SPACING) - SPACING)

plt.savefig("color_palette.png", dpi=300, bbox_inches="tight", pad_inches=0.1)
plt.show()
