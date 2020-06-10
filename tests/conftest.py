import pytest

from faustify.app import faustify_app


@pytest.mark.asyncio()
@pytest.fixture
def test_app(event_loop):
    faustify_app.finalize()
    faustify_app.conf.store = 'memory://'
    faustify_app.flow_control.resume()
    return faustify_app
