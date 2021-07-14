import pytest
from urlshort import create_app

@pytest.fixture
def app():
	app = create_app()
	yield app

# this will act as a browser/client and test out the app
@pytest.fixture
def client(app):
	return app.test_client()
