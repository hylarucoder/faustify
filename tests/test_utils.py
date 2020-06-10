from unittest.mock import Mock


def mock_coro(return_value=None, **kwargs):
    """Create mock coroutine function."""

    async def wrapped(*args, **kwargs):
        return return_value

    return Mock(wraps=wrapped, **kwargs)