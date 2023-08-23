from fastapi import FastAPI
from .config import Settings
from .router import router as api_router


def create_app(settings: Settings) -> FastAPI:
    app = FastAPI(
        settings=settings,
        swagger_ui_init_oauth={
            'clientId': settings.auth0_client_id,
            'usePkceWithAuthorizationCodeGrant': True,
            'scopes': ' '.join(['openid', 'profile', 'email'])
        }
    )
    app.include_router(api_router)
    return app
