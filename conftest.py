import pytest
from fixture.configuration import Configuration


@pytest.fixture(scope="session")
def conf(request):
    fixture = Configuration()
    fixture.session.login(email="taqc296@gmail.com", password="root")
    def close():
        fixture.session.logout()
        fixture.exit_fixture()
    request.addfinalizer(close)
    return fixture
