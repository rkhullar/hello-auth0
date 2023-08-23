from .util import Auth0CodeBearer
import os
from fastapi import Security
from typing import Annotated

auth0_host = os.environ['AUTH0_HOST']
auth_scheme = Auth0CodeBearer(domain=auth0_host)

ReadAccessToken = Annotated[str, Security(auth_scheme)]
