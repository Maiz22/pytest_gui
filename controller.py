from __future__ import annotations
from typing import TYPE_CHECKING

# import sys
# import redirect_logger
import os
from random_background_task import start_test_task
from pytest_executer import run_tests_in_single_thread
from shared_state import shared_logger

if TYPE_CHECKING:
    from view import View
    from model import Model


class Controller:
    def __init__(self, view: View, model: Model) -> None:
        self.view = view
        self.model = model
        # sys.stdout and sys.stderr are both overwritten/redirected to instances of RedirectLogger
        # sys.stdout = redirect_logger.RedirectLogger(self.view.text_box)
        # sys.stderr = redirect_logger.RedirectLogger(self.view.text_box)
        self.update_textbox_with_logs()
        self.set_default_path()
        self.init_bindings()

    def init_bindings(self) -> None:
        self.view.select_path_btn_on_click(
            lambda event, fd: self.select_test_path(event, fd)
        )
        self.view.start_test_btn_on_click(self.run_tests)

    def set_default_path(self) -> None:
        path = os.path.abspath(os.getcwd())
        self.view.cur_path.set(path)

    def select_test_path(self, event, fd) -> None:
        path = fd.askdirectory()
        print(path)
        return "break"

    def update_textbox_with_logs(self):
        """Check the shared logger and update the Text box with new messages."""
        while shared_logger.messages:
            message = shared_logger.messages.pop(0)
            self.view.append_text_box_content(text=message[0], tag_name=message[1])

        # Call this method again after 100 milliseconds
        self.view.after(100, self.update_textbox_with_logs)

    def run_tests(self, event) -> None:
        # start_test_task()
        run_tests_in_single_thread()

    def run(self) -> None:
        self.view.mainloop()
