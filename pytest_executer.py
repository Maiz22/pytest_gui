from __future__ import annotations
import pytest
import threading
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import os


# def pytest_runtest_logreport(report):
#    """Hook to capture and handle test log reports."""
#    if report.when == "call":  # Only capture the "call" phase (test execution)
#        if report.passed:
#            print(f"Test {report.nodeid} passed")
#        elif report.failed:
#            print(f"Test {report.nodeid} failed")
#        elif report.skipped:
#            print(f"Test {report.nodeid} was skipped")


def run_tests_in_single_thread(
    args: list[str] | None = None, path: os.PathLike[str] | None = None
) -> None:
    # pytest_args = [args, path]
    pytest_args = ["-v", "--color=yes"]
    new_thread = threading.Thread(
        target=lambda pytest_args=pytest_args: pytest.main(pytest_args), daemon=True
    )
    new_thread.start()


if __name__ == "__main__":
    # run_tests_in_single_thread()
    pytest.main()
