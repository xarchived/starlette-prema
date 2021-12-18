from starlette.schemas import SchemaGenerator

from starlette_prema.settings import PREMA_OPENAPI, PREMA_TITLE, PREMA_VERSION

schemas: SchemaGenerator = SchemaGenerator(
    {
        'openapi': PREMA_OPENAPI,
        'info': {
            'title': PREMA_TITLE,
            'version': PREMA_VERSION,
        },
    }
)
