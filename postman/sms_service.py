import requests

from django.conf import settings
from .backends import BaseBackend


class SMSBackend(BaseBackend):
    def __init__(self, host=None, port=None, sms_route=None, auth_key=None, headers=None,
                 fail_silently=False, **kwargs):
        self.host = settings.POSTMAN_HOST
        self.route = settings.POSTMAN_SMS_ROUTE
        self.sms_route = '{host}{route}'.format(host=self.host, route=self.route)
        self.auth_key = settings.POSTMAN_AUTHKEY
        self.headers = {'application-key': self.auth_key}

    @property
    def connection(self):
        request = requests.head(self.sms_route, headers=self.headers)
        if request.status_code == 200:
            return True
        return False

    def _send_msg_to_postman(self, postman_body):
        request = requests.post(self.sms_route, json=postman_body, headers=self.headers)
        if request.status_code == 201:
            return True
        return False

    def send_messages(self, reciever, message, sender_id=None, route=None):
        postman_body = {
            "receiver": {
                "contact": reciever
            },
            "data": {
                "body": message
            },
            "extras": {
                "sender_id": sender_id if sender_id is not None else 'ENGDUN',
                "route": route if route is not None else 'clickhere'
            }
        }

        # send message to postman
        response = self._send_msg_to_postman(postman_body)
        print('SUCCESS' if response else 'FAILED')
