from fastapi import FastAPI
from starlette.middleware.sessions import SessionMiddleware
import os
from routers.oauth import router
app = FastAPI()
secret_key = os.getenv('SESSION_SECRET_KEY', 'default-secret-key')
app.add_middleware(SessionMiddleware, secret_key=secret_key)
app.include_router(router)
