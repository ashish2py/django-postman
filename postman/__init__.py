__version__ = '0.1.0'


from .sms_service import SMSBackend

try:
    from django.conf import settings

    backend = settings.EMAIL_BACKEND
    host = settings.POSTMAN_HOST
    e_route = settings.POSTMAN_EMAIL_ROUTE
    s_route = settings.POSTMAN_SMS_ROUTE
    auth = settings.POSTMAN_AUTHKEY
except Exception as e:
    __RED = '\033[91m'
    raise NotImplementedError(__RED+'Make sure you have imported EMAIL_BACKEND and POSTMAN settings. Detailed ERROR, '+str(e) + __RED)

sms_backend = SMSBackend()
