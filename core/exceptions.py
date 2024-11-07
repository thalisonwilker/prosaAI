"""Exceptions for the core module."""

from fastapi import HTTPException

class NewsNotFoundException(HTTPException):
    """Exception raised when no news are found."""
    def __init__(self):
        super().__init__(status_code=404, detail="No news found.")

class NewsCollectionException(HTTPException):
    """Exception raised when there is an error collecting news."""
    def __init__(self):
        super().__init__(status_code=500, detail="Error collecting news.")

class NewsSummaryException(HTTPException):
    """Exception raised when there is an error generating a summary."""
    def __init__(self):
        super().__init__(status_code=500, detail="Error generating summary.")



class ParserError(Exception):
    """Exception raised when there is an error parsing the feed.
    Args:
        message (str): Error message.
    """
    def __init__(self, message):
        super().__init__(message)
        self.message = message
