from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, APIClient

from .models import *

class EmployeeTests(APITestCase):
    def setUp(self):
        self.test_department = Department.objects.create(title='TestDepartment', email='test_dep@example.com')
        Department.objects.create(title='TestDepartment2', email='test_dep2@example.com')
        self.test_department_id = self.test_department.id
        self.user = User.objects.create(username='tester')
        self.employee = Employee.objects.create(fio='Test fio', post='Test post', salary=12345, age=18, department_id=self.test_department_id)


    def test_create_employee(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        url = reverse('structure:employee-list')
        data = {
            'fio': 'Testov Test Testovich',
            'post': 'Programmer',
            'salary': 500000,
            'age': 25,
            'department': self.test_department_id,
        }

        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 2)
        self.assertEqual(Employee.objects.get(pk=2).fio, 'Testov Test Testovich')
        self.assertEqual(Employee.objects.get(pk=2).post, 'Programmer')
        self.assertEqual(Employee.objects.get(pk=2).salary, 500000)
        self.assertEqual(Employee.objects.get(pk=2).age, 25)
        self.assertEqual(Employee.objects.get(pk=2).department_id, self.test_department_id)

        client.logout()

        response = client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_list_employee(self):
        client = APIClient()
        client.force_authenticate(user=self.user)
        url = reverse('structure:employee-list')

        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        client.logout()

        response = client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_update_employee(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        url = reverse('structure:employee-list')
        data = {
            'fio': 'Testov Test Testovich',
            'post': 'Programmer',
            'salary': 500000,
            'age': 25,
            'department': self.test_department_id,
        }

        client.post(url, data)

        new_data = {
            'fio': 'New Test Testovich',
            'post': 'New programmer',
            # 'photo': 'http://testserver/photos/default_photo.jpg',
            'salary': 800000,
            'age': 28,
            'department': Department.objects.get(email='test_dep2@example.com').pk,
        }

        response = client.put('/api/v1/employee/5/', data=new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        del response.data['id']
        del response.data['photo']

        client.logout()

        response = client.put('/api/v1/employee/5/', data=new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_delete_employee(self):
        client = APIClient()
        client.force_authenticate(user=self.user)

        response = client.delete('/api/v1/employee/3/')

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
