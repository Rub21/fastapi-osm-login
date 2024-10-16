import os
from authlib.integrations.starlette_client import OAuth
oauth = OAuth()

client_id = os.getenv('OSM_CLIENT_ID')
client_secret = os.getenv('OSM_CLIENT_SECRET')

# Register OSM OAuth
oauth.register(
    name='osm',
    client_id=client_id,
    client_secret=client_secret,
    authorize_url='https://www.openstreetmap.org/oauth2/authorize',
    token_url='https://www.openstreetmap.org/oauth2/token',
    token_endpoint='https://www.openstreetmap.org/oauth2/token',
    redirect_uri=os.getenv('REDIRECT_URI', 'https://hud-tets.staging.geocompas.ai/auth'),
    client_kwargs={'scope': 'read_prefs'}
)