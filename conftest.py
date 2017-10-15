import pytest
from app.application import Application


@pytest.fixture
def app(request):
    _app = Application()
    request.addfinalizer(_app.quit)
    return _app
