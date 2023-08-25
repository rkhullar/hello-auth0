import os

from pydantic_settings import BaseSettings


class ProjectSettings(BaseSettings):
    environment: str = os.environ['ENVIRONMENT']
    reload_fastapi: bool = 'RELOAD_FASTAPI' in os.environ


class NetworkSettings(BaseSettings):
    service_host: str = os.getenv('SERVICE_HOST', 'localhost')
    service_port: int = int(os.getenv('SERVICE_PORT', '8000'))


class Auth0Settings(BaseSettings):
    auth0_host: str = os.environ['AUTH0_HOST']
    auth0_client_id: str = os.environ['AUTH0_CLIENT_ID']
    auth0_scopes: list[str] = ['openid', 'email', 'profile', 'message:read', 'message:write']
    auth0_audience: str = os.environ['AUTH0_AUDIENCE']


class Settings(ProjectSettings, NetworkSettings, Auth0Settings):
    pass
