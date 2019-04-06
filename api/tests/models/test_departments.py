from django.test import TestCase

from api.models import Departments


class DepartmentsTest(TestCase):

    def setUp(self):
        super(DepartmentsTest, self).setUp()
        self.department_name = 'Human Resources'

    def test_department_has_name(self):
        item = Departments.objects.create(name=self.department_name)
        self.assertEqual(item.name, self.department_name)

    def test_departments_string_representation(self):
        item = Departments.objects.create(name=self.department_name)
        self.assertEqual(str(item), item.name)
