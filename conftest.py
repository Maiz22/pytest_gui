# this conftest.py will outomatically be included by pytest

from shared_state import shared_logger

test_results = {"passed": [], "failed": [], "skipped": []}


def pytest_runtest_logreport(report):
    """
    Capture test output and store it in the shared logger.
    This hook needs to be inside your test directory or
    in a parent directory of your tests in order to be
    executed.
    """
    if report.when == "call":
        if report.passed:
            shared_logger.log(
                f"======    Test passed     ======\n{report.nodeid} ",
                tag="success",
            )
            test_results["passed"].append(report.nodeid)
        elif report.failed:
            shared_logger.log(
                f"======      Test failed      ======\n{report.nodeid}\nError: {report.longrepr}",
                tag="failure",
            )
            test_results["failed"].append(report.nodeid)
        elif report.skipped:
            shared_logger.log(
                f"======    Test skipped    ======\n{report.nodeid}",
                tag="warning",
            )
            test_results["skipped"].append(report.nodeid)


def pytest_sessionfinish(session, exitstatus):
    """
    Uses captured test output and displays a final test report
    using the shared_logger function. This hook needs to be inside
    your test directory or in a parent directory of your tests in
    order to be executed.
    """
    shared_logger.log(f"\n======    Final Test Report     ======\n", tag="default")
    shared_logger.log(f"Passed tests: {len(test_results['passed'])}", tag="success")
    for result in test_results["passed"]:
        shared_logger.log(f"  - {result}", tag="success")
    shared_logger.log(f"Failed tests: {len(test_results['failed'])}", tag="failure")
    for result in test_results["failed"]:
        shared_logger.log(f"  - {result}", tag="failure")
    shared_logger.log(f"Skipped tests: {len(test_results['skipped'])}", tag="warning")
    for result in test_results["skipped"]:
        shared_logger.log(f"  - {result}", tag="warning")
    shared_logger.log(f"\nExit status: {exitstatus}", tag="default")
