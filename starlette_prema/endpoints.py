from starlette.requests import Request
from starlette.responses import Response, JSONResponse

from starlette_prema import schemas


async def openapi_yaml(request: Request) -> Response:
    return schemas.OpenAPIResponse(request=request)


async def openapi_json(request: Request) -> Response:
    schema_dict: dict = schemas.get_schema(routes=request.app.routes)

    return JSONResponse(schema_dict)
