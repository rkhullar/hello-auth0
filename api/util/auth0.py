from functools import cached_property

import httpx
from fastapi.security import OAuth2AuthorizationCodeBearer


class Auth0CodeBearer(OAuth2AuthorizationCodeBearer):

    def __init__(self, domain: str, scopes: list[str]):
        self.domain = domain
        super().__init__(
            authorizationUrl=self.metadata['authorization_endpoint'],
            tokenUrl=self.metadata['token_endpoint'],
            scopes={scope: scope for scope in scopes}
        )

    @property
    def metadata_url(self) -> str:
        return f'https://{self.domain}/.well-known/openid-configuration'

    @cached_property
    def metadata(self) -> dict:
        response = httpx.get(self.metadata_url)
        response.raise_for_status()
        return response.json()
