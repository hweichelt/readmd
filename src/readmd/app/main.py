"""The main readmd application"""

import asyncio
from copy import deepcopy
from datetime import datetime

from textual import on
from textual.app import App, ComposeResult
from textual.widgets import Footer, TextArea, MarkdownViewer, Static
from textual.reactive import reactive

from .style import MAIN_CSS
from . import EXAMPLE_TEXT


class ReadmdTextualApp(App[int]):
    """A textual app for editing markdown files"""

    CSS = MAIN_CSS

    def __init__(self) -> None:
        super().__init__()
        self.bind("ctrl+x", "exit", description="Exit", key_display="CTRL+X")
        self._last_text_change = datetime.now()

    def compose(self) -> ComposeResult:
        """
        Composes the `ReadmdTextualApp`'s components
        """
        editor = EditorWidget(self)
        viewer = ViewerWidget(self)
        editor.focus()
        yield editor
        yield viewer
        yield Footer()

    def action_exit(self):
        """Action to exit the textual application"""
        self.exit(0)

    def check_action(self, action: str, parameters: tuple[object, ...]) -> bool | None:
        """Check if an action may run."""
        return True


class EditorWidget(Static):

    def __init__(self, app: ReadmdTextualApp) -> None:
        super().__init__()
        self._app = app
        self._text = EXAMPLE_TEXT
        self._last_changed = datetime.now()

    def compose(self) -> ComposeResult:
        yield TextArea.code_editor(self._text, language="markdown")

    @on(TextArea.Changed)
    async def text_changed(self, event: TextArea.Changed) -> None:
        self._last_changed = datetime.now()
        self._text = event.text_area.text
        self.run_worker(self._update_viewer(), exclusive=True)

    async def _update_viewer(self):
        last_update_before = deepcopy(self._last_changed)
        await asyncio.sleep(0.5)
        if last_update_before == self._last_changed:
            self._app.query_one(ViewerWidget).text = self._text


class ViewerWidget(Static):

    text = reactive(EXAMPLE_TEXT, recompose=True)

    def __init__(self, app: ReadmdTextualApp) -> None:
        super().__init__()
        self._app = app

    def compose(self) -> ComposeResult:
        yield MarkdownViewer(self.text, show_table_of_contents=True)
