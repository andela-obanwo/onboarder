import json

import requests
import requests_mock
from django.test import TestCase
from rest_framework import status

from api.fixtures.users import User
from api.services.messaging.sms import SMS
from api.tests.services.test_messaging import BaseMessagingServiceTest


@requests_mock.Mocker()
class SMSServiceTest(BaseMessagingServiceTest, TestCase):

    def setUp(self):
        super(SMSServiceTest, self).setUp()
        self.user = User()
        self.messaging_service = SMS(self.user)
        self.send_url = self.messaging_service.SEND_URL
        self.status_url = self.messaging_service.STATUS_URL
        self.MESSAGE_ID_KEY = 'sms_id'


    def test_messaging_prepare_payload(self, m):
        message = 'Task ZBA is overdue by 1 day'
        expected_payload = dict(sms=message, recipient=self.user.phone_number)
        payload = self.messaging_service._prepare_payload(message)
        self.assertEqual(payload, expected_payload)
