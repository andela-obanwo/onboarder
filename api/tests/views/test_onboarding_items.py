import json

from django.test import TestCase, Client
from django.urls import reverse

from api.models import OnboardingItems, Departments


class OnboardingItemsViewsetTest(TestCase):

    def setUp(self):
        department_name = 'Test Department'
        self.department = Departments.objects.create(name=department_name)
        self.department.save()
        self.onboarding_item_values = dict(name='OnboardingItem10',
                                      type='prestart',
                                      owner=self.department)
        self.onboarding_item = OnboardingItems.objects.create(**self.onboarding_item_values)
        self.onboarding_item.save()
        self.client = Client()

    def test_onboarding_item_is_created_successfully(self):
        onboarding_item_values = dict(name='OnboardingItem11',
                                      type='prestart',
                                      owner=self.department.id)
        response = self.client.post(reverse('api:onboarding_items-list'),
                                    data=onboarding_item_values)
        data = json.loads(response.content)
        self.assertEqual(data['name'], onboarding_item_values['name'])
        self.assertEqual(data['owner'], onboarding_item_values['owner'])

        expected_items = OnboardingItems.objects.all()
        self.assertEqual(expected_items.count(), 2)
        self.assertEqual(expected_items.filter(name=onboarding_item_values['name']).count(), 1)

    def test_onboarding_items_are_fetched_successfully(self):
        response = self.client.get(reverse('api:onboarding_items-list'))
        data = json.loads(response.content)

        self.assertEqual(len(data), 1)
        self.assertEqual(data[0]['name'], self.onboarding_item_values['name'])

    def test_onboarding_item_is_fetched_successfully(self):
        pk = self.onboarding_item.id
        response = self.client.get(reverse('api:onboarding_items-detail', kwargs={'pk': pk}))
        data = json.loads(response.content)

        self.assertEqual(data['name'], self.onboarding_item.name)
        self.assertEqual(data['owner'], self.onboarding_item.owner.id)

    def test_onboarding_item_is_updated_successfully(self):
        pk = self.onboarding_item.id
        response = self.client.get(reverse('api:onboarding_items-detail', kwargs={'pk': pk}))
        old_data = json.loads(response.content)

        self.assertEqual(old_data['name'], self.onboarding_item.name)

        new_name = 'Wipe Hard Drive'
        payload = old_data
        payload.update(dict(name=new_name))
        payload = json.dumps(payload)
        response = self.client.put(reverse('api:onboarding_items-detail', kwargs={'pk': pk}), data=payload,
                                   content_type='application/json')

        new_data = json.loads(response.content)
        self.assertEqual(new_data['name'], new_name)

    def test_onboarding_item_is_deleted_successfully(self):
        response = self.client.get(reverse('api:onboarding_items-list'))
        data = json.loads(response.content)

        self.assertEqual(len(data) , 1)

        pk = self.onboarding_item.id
        self.client.delete(reverse('api:onboarding_items-detail', kwargs={'pk': pk}))

        response = self.client.get(reverse('api:onboarding_items-list'))
        data = json.loads(response.content)

        self.assertEqual(len(data), 0)