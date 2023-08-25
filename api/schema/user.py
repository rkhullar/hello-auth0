from typing import Self

from pydantic import BaseModel


class User(BaseModel):
    id: str
    name: str
    email: str


class Auth0IdentityToken(BaseModel):
    sub: str  # google-oauth2|int
    given_name: str
    family_name: str
    nickname: str
    name: str
    picture: str
    locale: str
    updated_at: str  # datetime
    email: str
    email_verified: bool


class Auth0User(User):

    @classmethod
    def from_token(cls, token: Auth0IdentityToken) -> Self:
        return cls(id=token.sub, name=token.name, email=token.email)
