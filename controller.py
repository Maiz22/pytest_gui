from __future__ import annotations
from typing import TYPE_CHECKING
import os
from pytest_executer import run_tests_in_single_thread
from shared_state import shared_logger
from datetime import datetime

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
        #self.view.select_path_btn_on_click(
        #    lambda event, fd: self.select_test_path(event, fd)
        #)
        self.view.select_html_report_path_btn_on_click(
            lambda event, fd: self.select_html_report_path(event, fd)
        )
        self.view.select_json_report_path_btn_on_click(
            lambda event, fd: self.select_json_report_path(event, fd)
        )
        self.view.start_test_btn_on_click(self.run_tests)

    def set_default_test_path(self) -> None:
        path = os.path.normpath(f"{self.path}/tests/")
        if not os.path.exists(path):
            os.makedirs(path)
        self.view.cur_path.set(path)

    def set_default_html_report_path(self) -> None:
        path = os.path.normpath(f"{self.path}/html_reports/")
        if not os.path.exists(path):
            os.makedirs(path)
        self.view.html_report_path.set(path)

    def set_default_json_report_path(self) -> None:
        path = os.path.normpath(f"{self.path}/json_reports/")
        if not os.path.exists(path):
            os.makedirs(path)
        self.view.json_report_path.set(path)

    def select_html_report_path(self, event, fd) -> None:
        path = fd.askdirectory().strip()
        if path != "":
            self.view.html_report_path.set(path)
            self.view.append_text_box_content(text=f"Set HTML report path to: {path}")

    def select_json_report_path(self, event, fd) -> None:
        path = fd.askdirectory().strip()
        if path != "":
            self.view.json_report_path.set(path)
            self.view.append_text_box_content(text=f"Set JSON report path to: {path}")

    def select_test_path(self, event, fd) -> None:
        path = fd.askdirectory().strip()
        if path != "":
            self.view.cur_path.set(path)
            self.view.append_text_box_content(text=f"Set test directory to: {path}")
        # return "break"

    def update_textbox_with_logs(self) -> None:
        """Check the shared logger and update the Text box with new messages."""
        while shared_logger.messages:
            message = shared_logger.messages.pop(0)
            self.view.append_text_box_content(text=message[0], tag_name=message[1])
        self.view.after(100, self.update_textbox_with_logs)

    def get_command_line_args(self) -> list[str]:
        args = self.view.command_line_args.get()
        if args.strip() != "":
            return [arg.strip() for arg in args.strip().split(",")]
        return []

    def run_tests(self, event) -> None:
        args = self.get_command_line_args()
        if self.view.html_report_selected.get():
            args.append(f"--html={self.view.html_report_path.get()}/report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html")
            args.append("--self-contained-html")
        if self.view.json_report_selected.get():
            args.append("--json-report")
            args.append(f"--json-report-file={self.view.json_report_path.get()}/report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json")
            args.append("--json-report-indent=4")
        path = self.view.cur_path.get()
        self.view.append_text_box_content(text=f"Start Test @ {path}")
        run_tests_in_single_thread(args=args, path=path)

    def run(self) -> None:
        self.view.mainloop()
