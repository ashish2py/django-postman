
class BaseBackend(object):
    '''
    Base Class for email and sms backend
    '''

    def __init__(self, fail_silently=False, **kwargs):
        self.fail_silently = fail_silently

    @property
    def connection(self):
        raise NotImplementedError('subclasses of BaseBackend must override connection() method')

    def send_messages(self):
        raise NotImplementedError('subclasses of BaseBackend must override connection() method')
