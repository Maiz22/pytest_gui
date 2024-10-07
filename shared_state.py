class SharedLogger:
    """A shared logger class to store log messages."""

    def __init__(self):
        self.messages = []

    def log(self, message):
        """Log a message to the shared logger."""
        self.messages.append(message)


# Create a single instance of the shared logger
shared_logger = SharedLogger()
