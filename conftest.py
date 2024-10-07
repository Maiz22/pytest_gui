# this conftest.py will outomatically be included by pytest

from shared_state import shared_logger


def pytest_runtest_logreport(report):
    """Capture test output and store it in the shared logger."""
    print("CONFTEST REPORT")
    if report.when == "call":  # Only capture the "call" phase (test execution)
        if report.passed:
            shared_logger.log(f"Test passed: {report.nodeid}")
        elif report.failed:
            shared_logger.log(f"Test failed: {report.nodeid}\nError: {report.longrepr}")
        elif report.skipped:
            shared_logger.log(f"Test skipped: {report.nodeid}")
