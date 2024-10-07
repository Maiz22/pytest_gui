from __future__ import annotations
from typing import TYPE_CHECKING
import os
from pytest_executer import run_tests_in_single_thread
from shared_state import shared_logger

if TYPE_CHECKING:
    from view import View
    from model import Model


class Controller:
    def __init__(self, view: View, model: Model) -> None:
        self.view = view
        self.model = model
        self.path = os.path.abspath(os.getcwd())
        self.update_textbox_with_logs()
        self.set_default_test_path()
        self.set_default_html_report_path()
        self.set_default_json_report_path()
        self.init_bindings()

    def init_bindings(self) -> None:
        self.view.select_path_btn_on_click(
            lambda event, fd: self.select_test_path(event, fd)
        )
        self.view.start_test_btn_on_click(self.run_tests)

    def set_default_test_path(self) -> None:
        self.view.cur_path.set(self.path)

    def set_default_html_report_path(self) -> None:
        path = os.path.normpath(f"{self.path}/html_reports")
        if not path:
            os.makedirs(path)
        self.view.html_report_path.set(path)

    def set_default_json_report_path(self) -> None:
        path = os.path.normpath(f"{self.path}/json_reports")
        if not path:
            os.makedirs(path)
        self.view.json_report_path.set(path)

    def select_test_path(self, event, fd) -> None:
        path = fd.askdirectory().strip()
        if path != "":
            self.view.cur_path.set(path)
            self.view.append_text_box_content(text=f"Set test directory to: {path}")
        return "break"

    def update_textbox_with_logs(self) -> None:
        """Check the shared logger and update the Text box with new messages."""
        while shared_logger.messages:
            message = shared_logger.messages.pop(0)
            self.view.append_text_box_content(text=message[0], tag_name=message[1])
        self.view.after(100, self.update_textbox_with_logs)

    def run_tests(self, event) -> None:
        if self.view.html_report_selected.get():
            pass
        if self.view.json_report_selected.get():
            pass
        print(
            self.view.html_report_selected.get(), self.view.json_report_selected.get()
        )
        run_tests_in_single_thread()

    def run(self) -> None:
        self.view.mainloop()
