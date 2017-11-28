import requests

from django.conf import settings
from django.core.mail.backends.base import BaseEmailBackend


class EmailBackend(BaseEmailBackend):
    def __init__(self, host=None, port=None, username=None, password=None,
                 use_tls=None, fail_silently=False, use_ssl=None, timeout=None,
                 ssl_keyfile=None, ssl_certfile=None,
                 **kwargs):
        super(EmailBackend, self).__init__(fail_silently=fail_silently)
        self.host = settings.POSTMAN_HOST
        self.route = settings.POSTMAN_EMAIL_ROUTE
        self.email_route = '{host}{route}'.format(host=self.host, route=self.route)
        self.auth_key = settings.POSTMAN_AUTHKEY
        self.headers = {'application-key': self.auth_key}

    @property
    def connection(self):
        request = requests.head(self.email_route, headers=self.headers)
        if request.status_code == 200:
            return True
        return False

    def send_messages(self, email_messages):
        if not email_messages:
            return None

        if not self.connection:
            # failing if connection failed.
            return None

        for message in email_messages:
            sent = self._send(message)
            num_sent = 0
            if sent:
                num_sent += 1
        return num_sent

    def _send_email_to_postman(self, postman_body):
        request = requests.post(self.email_route, json=postman_body, headers=self.headers)
        if request.status_code == 201:
            return True
        return False

    def _send(self, email_message):
        ''' Helper method that does the actual email sending '''
        # check email contains recipients
        if not email_message.to:
            return False

        from_email = email_message.from_email
        recipients = email_message.to
        message = email_message.body
        subject = email_message.subject
        content_type = email_message.content_subtype

        try:
            # make request_body for postman
            for recipient in recipients:
                postman_body = {
                    "receiver": {
                        "contact": recipient
                    },
                    "sender": {
                        "contact": from_email
                    },
                    "data": {
                        "body": message,
                        "subject": subject,
                        "content_type": 'text/{ct}'.format(ct=content_type)
                    }
                }

            # PASS request to POSTMAN
            return self._send_email_to_postman(postman_body)
        except Exception as e:
            pass
