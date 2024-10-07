# this conftest.py will outomatically be included by pytest

from shared_state import shared_logger


def pytest_runtest_logreport(report):
    """Capture test output and store it in the shared logger."""
    if report.when == "call":  # Only capture the "call" phase (test execution)
        if report.passed:
            shared_logger.log(
                f"======    Test passed     ======\n{report.nodeid} ",
                tag="success",
            )
        elif report.failed:
            shared_logger.log(
                f"======      Test failed      ======\n{report.nodeid}\nError: {report.longrepr}",
                tag="failure",
            )
        elif report.skipped:
            shared_logger.log(
                f"======    Test skipped    ======\n{report.nodeid}",
                tag="warning",
            )
