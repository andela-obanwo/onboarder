from api.services.messaging.messaging import Messaging


class SMS(Messaging):
    SEND_URL = 'https://sms_provider.com/send'
    STATUS_URL = 'https://sms_provider.com/status'


    def _prepare_payload(self, message):
        payload = dict(sms=message, recipient=self.user.phone_number)
        return payload


    def _get_message_id(self, response):
        return response.json()['sms_id']
