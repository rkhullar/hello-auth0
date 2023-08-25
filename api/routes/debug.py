from ..depends import GetUser, ReadAuthData, create_router
from ..schema.user import User

router = create_router()


@router.get('/auth-state', response_model=dict)
def debug_auth_state(auth_data: ReadAuthData):
    return {'auth_data': auth_data}


@router.get('/user-info', response_model=User)
def debug_user_info(user: GetUser):
    return user
