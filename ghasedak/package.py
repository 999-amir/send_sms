import ghasedakpack

API_KEY = '***************************************'

sms = ghasedakpack.Ghasedak(API_KEY)
params = {
    'linenumber': f'*****',
    'receptor': f'*****',
    'message': 'امتحان میکنیم. لغو11'
}
sms.send(params)
