# pip install kavenegar
from kavenegar import *


API_KEY = '****'


def kave_negar_token_send(receptor):
    try:
        api = KavenegarAPI(API_KEY)
        params = {
            'sender': f'****',
            'receptor': receptor,
            'message': '****'
        }
        response = api.sms_send(params)
        print('message send')
    except APIException as e:
        print(e)
    except HTTPException as e:
        print(e)


kave_negar_token_send('****')
