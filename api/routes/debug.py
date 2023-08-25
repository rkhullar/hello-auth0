from ..depends import create_router, ReadAuthData

router = create_router()


@router.get('/auth-state', response_model=dict)
def debug_auth_state(auth_data: ReadAuthData):
    return {'auth_data': auth_data}
