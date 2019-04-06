import json

import requests
from rest_framework import status


class BaseMessagingServiceTest(object):

    def test_messaging_get_message_id(self, m):
        response_dict = {self.MESSAGE_ID_KEY: 'xxx3'}
        m.register_uri('GET', self.send_url, text=json.dumps(response_dict),
                       status_code=status.HTTP_200_OK)
        response = requests.get(self.send_url)
        id = self.messaging_service._get_message_id(response)
        self.assertEqual(id, response_dict[self.MESSAGE_ID_KEY])


    def test_messaging_parse_response_successful_request(self, m):
        response_dict = {self.MESSAGE_ID_KEY: 'xxx3', 'message': 'Message sent successfully'}
        m.register_uri('GET', self.send_url, text=json.dumps(response_dict),
                       status_code=status.HTTP_200_OK)
        response = requests.get(self.send_url)
        expected_response = dict(message='Message sent successfully', message_id=response_dict[self.MESSAGE_ID_KEY])
        parsed_response = self.messaging_service._parse_response(response)

        self.assertEqual(parsed_response, expected_response)

    def test_messaging_parse_response_failed_request(self, m):
        response_dict = {}
        m.register_uri('GET', self.send_url, text=json.dumps(response_dict),
                       status_code=status.HTTP_400_BAD_REQUEST)
        response = requests.get(self.send_url)
        expected_response = dict(message='Message Could not be sent')
        parsed_response = self.messaging_service._parse_response(response)

        self.assertEqual(parsed_response, expected_response)


    def test_messaging_delivery_status_successful_request(self, m):
        response_dict = {self.MESSAGE_ID_KEY: 'xxx3', 'message': 'Message Delivered'}
        m.register_uri('POST', self.status_url, text=json.dumps(response_dict),
                       status_code=status.HTTP_200_OK)
        expected_response = dict(message='Message Delivered', message_id=response_dict[self.MESSAGE_ID_KEY])
        delivery_status = self.messaging_service.delivery_status(response_dict[self.MESSAGE_ID_KEY])

        self.assertEqual(delivery_status, expected_response)

    def test_messaging_delivery_status_failed_request(self, m):
        response_dict = {self.MESSAGE_ID_KEY: 'xxx3', 'message': 'Request Failed'}
        m.register_uri('POST', self.status_url, text=json.dumps(response_dict),
                       status_code=status.HTTP_400_BAD_REQUEST)
        expected_response = dict(message='Request Failed')
        delivery_status = self.messaging_service.delivery_status(response_dict[self.MESSAGE_ID_KEY])

        self.assertEqual(delivery_status, expected_response)

    def test_messaging_send_successful_request(self, m):
        message = 'task completed'
        response_dict = {self.MESSAGE_ID_KEY: 'xxx3', 'message': 'Message sent successfully'}
        m.register_uri('POST', self.send_url, text=json.dumps(response_dict),
                       status_code=status.HTTP_200_OK)
        expected_response = dict(message='Message sent successfully', message_id=response_dict[self.MESSAGE_ID_KEY])
        parsed_response = self.messaging_service.send(message)

        self.assertEqual(parsed_response, expected_response)

    def test_messaging_send_failed_request(self, m):
        message = 'task completed'
        response_dict = {self.MESSAGE_ID_KEY: 'xxx3', 'message': 'Request Failed'}
        m.register_uri('POST', self.send_url, text=json.dumps(response_dict),
                       status_code=status.HTTP_400_BAD_REQUEST)
        expected_response = dict(message='Message Could not be sent')
        parsed_response = self.messaging_service.send(message)

        self.assertEqual(parsed_response, expected_response)
