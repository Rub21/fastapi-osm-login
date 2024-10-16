from fastapi import APIRouter, Request
from starlette.responses import JSONResponse
import logging
from oauth import oauth
import os
router = APIRouter()
redirect_uri = os.getenv('REDIRECT_URI', 'http://localhost')

@router.get('/login')
async def login(request: Request):
    return await oauth.osm.authorize_redirect(request, redirect_uri)

@router.get("/auth")
async def auth(request: Request):
    try:
        # Fetch the access token using the OAuth client
        token = await oauth.osm.authorize_access_token(request)
        logging.info(f"OAuth token: {token}")
        if not token:
            return JSONResponse({"error": "Failed to retrieve access token"}, status_code=400)
        return {"token": token}
    except Exception as e:
        logging.error(f"OAuth Error: {e}")
        return JSONResponse({"error": str(e)}, status_code=500)