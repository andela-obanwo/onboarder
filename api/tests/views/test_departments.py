import json

from django.test import TestCase, Client
from django.urls import reverse

from api.models import Departments


class DepartmentsViewsetTest(TestCase):

    def setUp(self):
        self.department_name = 'Test Department'
        self.department = Departments.objects.create(name=self.department_name)
        self.department.save()
        self.client = Client()

    def test_department_is_created_successfully(self):
        department_values = dict(name='New Department')
        response = self.client.post(reverse('api:departments-list'),
                                    data=department_values)
        data = json.loads(response.content)
        self.assertEqual(data['name'], department_values['name'])

        expected_items = Departments.objects.all()
        self.assertEqual(expected_items.count(), 2)
        self.assertEqual(expected_items.filter(name=department_values['name']).count(), 1)

    def test_departments_are_fetched_successfully(self):
        response = self.client.get(reverse('api:departments-list'))
        data = json.loads(response.content)

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], self.department_name)

    def test_department_is_fetched_successfully(self):
        pk = self.department.id
        response = self.client.get(reverse('api:departments-detail', kwargs={'pk': pk}))
        data = json.loads(response.content)

        self.assertEqual(data['name'], self.department.name)

    def test_department_is_updated_successfully(self):
        pk = self.department.id
        response = self.client.get(reverse('api:departments-detail', kwargs={'pk': pk}))
        old_data = json.loads(response.content)

        self.assertEqual(old_data['name'], self.department.name)

        new_name = 'People and Culture'
        payload = old_data
        payload.update(dict(name=new_name))
        payload = json.dumps(payload)
        response = self.client.put(reverse('api:departments-detail', kwargs={'pk': pk}), data=payload,
                                   content_type='application/json')

        new_data = json.loads(response.content)
        self.assertEqual(new_data['name'], new_name)

    def test_department_is_deleted_successfully(self):
        response = self.client.get(reverse('api:departments-list'))
        data = json.loads(response.content)

        self.assertEqual(len(data) , 1)

        pk = self.department.id
        self.client.delete(reverse('api:departments-detail', kwargs={'pk': pk}))

        response = self.client.get(reverse('api:departments-list'))
        data = json.loads(response.content)

        self.assertEqual(len(data), 0)
