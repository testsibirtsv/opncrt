import pytest
from fixture.configuration import Configuration


fixture = None


@pytest.fixture()
def conf(request):
    global fixture
    if fixture is None:
        fixture = Configuration()
    else:
        if not fixture.is_valid():
            fixture = Configuration()
    fixture.session.check_login(email="taqc296@mail.com", password="root")
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def close():
        fixture.session.check_logout()
        fixture.exit_fixture()
    request.addfinalizer(close)
    return fixture
