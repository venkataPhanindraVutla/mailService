"""
Module for custom exceptions and exception handling utilities.
"""
from fastapi import HTTPException
from starlette.status import HTTP_500_INTERNAL_SERVER_ERROR
import functools

def handle_exceptions(func):
    """
    Decorator to handle exceptions in asynchronous functions and raise HTTPException.

    Args:
        func: The asynchronous function to wrap.

    Returns:
        The wrapped asynchronous function.
    """
    @functools.wraps(func)
    async def wrapper(*args, **kwargs):
        try:
            await func(*args, **kwargs)
        except Exception as e:
            # Log the exception here if needed
            raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail=str(e))
    return wrapper