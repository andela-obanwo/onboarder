from django.test import TestCase
from django_dynamic_fixture import G
from api.models import OnboardingItems, Departments


class OnboardingItemsTest(TestCase):

    def setUp(self):
        super(OnboardingItemsTest, self).setUp()
        self.department = G(Departments)
        self.onboarding_item_values = dict(name='Provide Laptop', type=OnboardingItems.POSTSTART, owner=self.department)

    def test_item_has_name_owner_and_type(self):
        item = OnboardingItems.objects.create(**self.onboarding_item_values)
        self.assertEqual(item.name, self.onboarding_item_values['name'])
        self.assertEqual(item.type, self.onboarding_item_values['type'])
        self.assertEqual(item.owner, self.onboarding_item_values['owner'])

    def test_items_string_representation(self):
        item = OnboardingItems.objects.create(**self.onboarding_item_values)
        self.assertEqual(str(item), "{}: {}".format(item.name, item.type))