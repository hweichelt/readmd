"""Module containing TCSS style strings for the textual TUI"""

MAIN_CSS = """
$color-background: #0A0E0F;

Screen{
    layout: grid;
    grid-size: 2 1;
    background: $color-background;
}

MarkdownH1{
    text-align: left;
    border-bottom: wide rgba(255,255,255,0.2);
}
TextArea{
    background: transparent;
}
"""
