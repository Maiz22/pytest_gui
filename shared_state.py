class SharedLogger:
    """
    A shared logger class to store log messages.
    """

    def __init__(self) -> None:
        self.messages = []

    def log(self, message: str, tag: str) -> None:
        """
        Adds a message and a tag to the messages list of
        the logger. The tag can be used inside the view
        displaying messages for colorcoding etc.
        """
        self.messages.append((message, tag))


# Create a single instance of the shared logger that shall be used by all parties
shared_logger = SharedLogger()
