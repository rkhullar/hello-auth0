from fastapi import APIRouter
from .depends import ReadAccessToken

router = APIRouter()


@router.get('/test')
def hello_world(access_token: ReadAccessToken):
    print(access_token)
    return {'message': 'hello world'}
