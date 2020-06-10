from unittest.mock import patch

import pytest

from tests.test_utils import mock_coro


@pytest.mark.asyncio()
async def test_foo(test_app):
    with patch(__name__ + '.bar') as mocked_bar:
        mocked_bar.send = mock_coro()
        async with foo.test_context() as agent:
            await agent.put('hey')
            mocked_bar.send.assert_called_with('hey')


@pytest.mark.asyncio()
async def test_bar(test_app):
    async with bar.test_context() as agent:
        event = await agent.put('hey')
        assert agent.results[event.message.offset] == 'heyYOLO'