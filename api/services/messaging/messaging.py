import requests
from rest_framework import status

from api.fixtures.users import User


class Messaging(object):
    SEND_URL = NotImplemented
    STATUS_URL = NotImplemented

    def __init__(self, user):
        self.user = user

    def send(self, message):
        data = self._prepare_payload(message)
        response = requests.post(url=self.SEND_URL, data=data)
        return self._parse_response(response)

    def _prepare_payload(self, message):
        raise NotImplementedError

    def _parse_response(self, response):
        if response.status_code != status.HTTP_200_OK:
            return dict(message='Message Could not be sent')
        self.message_id = self._get_message_id(response)
        return dict(message='Message sent successfully', message_id=self.message_id)

    def delivery_status(self, message_id):
        response = requests.post(url=self.STATUS_URL, data=dict(id=message_id))
        if response.status_code != status.HTTP_200_OK:
            return dict(message='Request Failed')
        return dict(message=response.json()['message'], message_id=message_id)

    def _get_message_id(self, response):
        return response.json()['message_id']
