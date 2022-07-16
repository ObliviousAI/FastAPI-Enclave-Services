from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from routes import hello, yao, psi, outbound, config

app = FastAPI()

# Adding routes for each example in the repo
app.include_router(hello.router, prefix='/hello')
app.include_router(config.router, prefix='/config')
app.include_router(outbound.router, prefix='/outbound')
app.include_router(yao.router, prefix='/yao')
app.include_router(psi.router, prefix='/psi')

# This is only here to customize the swagger :)
def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema
    openapi_schema = get_openapi(
        title="OBLV 💖 FastAPI",
        version="0.1.0",
        description="This is the Oblivious-FastAPI sample repo, intended to help you get started quickly with secure enclaves and Python-based APIs.",
        routes=app.routes,
    )
    openapi_schema["info"]["x-logo"] = {
        "url": "https://oblv.io/oblv-hearts-fastapi"
    }
    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi
