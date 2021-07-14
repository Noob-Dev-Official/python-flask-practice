from urlshort import create_app

def test_shorten(client):
	response = client.get('/') # says to visit the homepage
	assert b'Shorten' in response.data
