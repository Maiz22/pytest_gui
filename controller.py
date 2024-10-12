from __future__ import annotations
from typing import TYPE_CHECKING
import os
from pytest_executer import run_tests_in_single_thread
from shared_state import shared_logger
from datetime import datetime
from shutil import copy

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
        """
        Binds all the views buttons to controller methods.
        """
        # self.view.select_path_btn_on_click(
        #    lambda event, fd: self.select_test_path(event, fd)
        # )
        self.view.select_html_report_path_btn_on_click(
            lambda event, fd: self.select_html_report_path(event, fd)
        )
        self.view.select_json_report_path_btn_on_click(
            lambda event, fd: self.select_json_report_path(event, fd)
        )
        self.view.start_test_btn_on_click(self.run_tests)

    def set_default_test_path(self) -> None:
        """
        Creates a default directory for your tests inside your
        programs directory.
        """
        path = os.path.normpath(f"{self.path}/tests/")
        if not os.path.exists(path):
            os.makedirs(path)
        self.view.testcase_path_widget.path.set(path)
        # self.view.cur_path.set(path)

    def set_default_html_report_path(self) -> None:
        """
        Creates a default directory inside your main program
        for your html reports.
        """
        path = os.path.normpath(f"{self.path}/html_reports/")
        if not os.path.exists(path):
            os.makedirs(path)
        # self.view.html_report_path.set(path)
        self.view.html_report_widget.path.set(path)

    def set_default_json_report_path(self) -> None:
        """
        Creates a default directory inside your main program
        for your json reports.
        """
        path = os.path.normpath(f"{self.path}/json_reports/")
        if not os.path.exists(path):
            os.makedirs(path)
        # self.view.json_report_path.set(path)
        self.view.json_report_widget.path.set(path)

    def select_html_report_path(self, event, fd) -> None:
        """
        Lets the user select a directory for the html reports
        by calling the views askdirectory method.
        """
        path = fd.askdirectory().strip()
        if path != "":
            # self.view.html_report_path.set(path)
            self.view.html_report_widget.path.set(path)
            self.view.append_text_box_content(text=f"Set HTML report path to: {path}")

    def select_json_report_path(self, event, fd) -> None:
        """
        Lets the user select a directory for the json reports
        by calling the views askdirectory method.
        """
        path = fd.askdirectory().strip()
        if path != "":
            # self.view.json_report_path.set(path)
            self.view.json_report_widget.path.set(path)
            self.view.append_text_box_content(text=f"Set JSON report path to: {path}")

    # currently not used due to the conftest hook
    def select_test_path(self, event, fd) -> None:
        """
        Lets the user select a directory for the test cases
        by calling the views askdirectory method.
        """
        path = fd.askdirectory().strip()
        if path != "":
            # self.view.cur_path.set(path)
            self.view.testcase_path_widget.path.set(path)
            self.view.append_text_box_content(text=f"Set test directory to: {path}")

    def update_textbox_with_logs(self) -> None:
        """
        Check the shared logger and update the Text box with
        new messages.
        """
        while shared_logger.messages:
            message = shared_logger.messages.pop(0)
            self.view.append_text_box_content(text=message[0], tag_name=message[1])
        self.view.after(100, self.update_textbox_with_logs)

    def get_command_line_args(self) -> list[str]:
        """
        Extracts the command line args from the views entry field
        strips white, spaces and splits them at the ,.
        Returns the list of args or an empty list if no args have
        been entered.
        """
        args = self.view.command_line_args.get()
        if args.strip() != "":
            return [arg.strip() for arg in args.strip().split(",")]
        return []

    def add_html_report(self, args: list[str]) -> list[str]:
        """
        Adds the html report command line argument to the arguments
        if the option has been selected in the view.
        """
        if not self.view.html_report_widget.report_selected.get():
            return args
        args.append(
            f"--html={self.view.html_report_widget.path.get()}/report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.html"
        )
        args.append("--self-contained-html")
        return args

    def add_json_report(self, args: list[str]) -> list[str]:
        """
        Adds the json report command line argument to the arguments
        if the option has been selected in the view.
        """
        if not self.view.json_report_widget.report_selected.get():
            return args
        args.append("--json-report")
        args.append(
            f"--json-report-file={self.view.json_report_widget.path.get()}/report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.json"
        )
        args.append("--json-report-indent=4")
        return args

    def run_tests(self, event) -> None:
        """
        Configures the command line arguments and testpath
        and start the test.
        """
        args = self.get_command_line_args()
        args = self.add_html_report(args)
        args = self.add_json_report(args)
        path = self.view.testcase_path_widget.path.get()
        self.view.append_text_box_content(text=f"Start Test @ {path}")
        run_tests_in_single_thread(args=args, path=path)

    def run(self) -> None:
        """
        Calls the views mainloop to start the gui.
        """
        self.view.mainloop()
