from typing import Annotated, Type

from fastapi import APIRouter, Depends, Request, Security

from .config import Auth0Settings
from .util import Auth0CodeBearer, decode_jwt

settings = Auth0Settings()
auth_scheme = Auth0CodeBearer(domain=settings.auth0_host)
ReadAccessToken = Annotated[str, Security(auth_scheme)]


def require_auth():
    def dependency(request: Request, access_token: ReadAccessToken) -> str:
        request.state.auth_data = decode_jwt(access_token)
        return access_token
    return Security(dependency)


def create_router() -> APIRouter:
    return APIRouter(dependencies=[require_auth()])


def read_request_state(key: str, _type: Type):
    def dependency(request: Request) -> _type:
        return getattr(request.state, key, None)
    return Annotated[_type, Depends(dependency)]


# ReadAuthType = read_request_state(key='auth_type', _type=AuthScheme)
ReadAuthData = read_request_state(key='auth_data', _type=dict)


''' NOTE: how to support multiple auth schemes:
- add auto_error=False to auth_scheme instance
- concern to map of auth schemes
- name schemes and annotations accordingly
- update require_auth
 - define type for auth schemes: i.e: `AuthScheme = Literal['access_token', 'api_key', 'custom_jwt']`
 - add parameter for allowed auth schemes: i.e: `allowed: Iterable[AuthScheme]`
 - add dependency params for other auth schemes
 - if more than one scheme uses JWT, add logic to decode the token and infer the auth type
 - inject the auth type into the request state along with the auth data
 - add logic to check that the given auth type is allowed
 - raise 401 if the auth type is not allowed
- update create_router
 - add optional param for auth: `with_auth: Iterable[AuthScheme] = None`
 - define dependencies as null; and update before passing to APIRouter
 - forward with_auth param values into require_auth: `require_auth(allowed=with_auth)`
'''
