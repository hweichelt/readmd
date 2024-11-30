from rich.style import Style
from textual.widgets.text_area import TextAreaTheme

monokai = TextAreaTheme.get_builtin_theme("monokai")
theme_readmd_dark = TextAreaTheme(
    name="readmd_dark",
    base_style=Style(color="#FFFFFF", bgcolor="#000000"),
    cursor_style=Style(color="white", bgcolor="blue"),
    cursor_line_style=Style(bgcolor="#111111"),
    syntax_styles=monokai.syntax_styles,
)
