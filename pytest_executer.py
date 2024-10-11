from __future__ import annotations
import pytest
import threading
from typing import TYPE_CHECKING
import os


def run_tests_in_single_thread(
    args: list[str] | None = None, path: os.PathLike[str] | None = None
) -> None:
    """
    Takes the path of the test and the commandline arguments and calls
    pytest main function inside a single thread.
    """
    if not args:
        args = []
    if not path:
        raise Exception("No test directory selected")
    args.append(path)
    new_thread = threading.Thread(
        target=lambda pytest_args=args: pytest.main(pytest_args), daemon=True
    )
    new_thread.start()
