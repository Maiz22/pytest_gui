import time
import threading


def test_background_task() -> None:
    # This simulates background tasks that print to stdout
    for i in range(10):
        # print(f"Logging info: Task running {i}")
        time.sleep(1)
    raise ValueError("Example error")  # Simulate an error


def start_test_task() -> None:
    task_thread = threading.Thread(target=test_background_task)
    task_thread.start()
