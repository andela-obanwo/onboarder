from rest_framework import status

from api.services.messaging.messaging import Messaging


class Email(Messaging):
    SEND_URL = 'https://email_provider.com/send'
    STATUS_URL = 'https://email_provider.com/status'


    def parse_response(self, response):
        if response.status_code != status.HTTP_201_CREATED:
            self.message_id = self._get_message_id()
            return 'Message cannot be delivered'
        return 'Message delivered successfully'


    def _prepare_payload(self, message):
        payload = dict(email=message, recipient=self.user.email)
        return payload
