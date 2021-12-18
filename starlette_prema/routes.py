from starlette.routing import Route

from starlette_prema.endpoints import openapi_yaml, openapi_json

routes = [
    Route(path='/openapi.yaml', endpoint=openapi_yaml, include_in_schema=False),
    Route(path='/openapi.json', endpoint=openapi_json, include_in_schema=False),
]
