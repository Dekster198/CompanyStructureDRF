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
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.employee = Employee.objects.create(fio='Test fio', post='Test post', salary=12345, age=18, department_id=self.test_department_id)


    def test_create_employee(self):
        url = reverse('structure:employee-list')
        data = {
            'fio': 'Testov Test Testovich',
            'post': 'Programmer',
            'salary': 500000,
            'age': 25,
            'department': self.test_department_id,
        }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Employee.objects.count(), 2)
        self.assertEqual(response.data['fio'], data['fio'])
        self.assertEqual(response.data['post'], data['post'])
        self.assertEqual(response.data['salary'], data['salary'])
        self.assertEqual(response.data['age'], data['age'])
        self.assertEqual(response.data['department'], data['department'])

        self.client.logout()

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_list_employee(self):
        url = reverse('structure:employee-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.logout()

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

        url = reverse('structure:employee-detail', kwargs={'pk': 4})
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.logout()

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_update_employee(self):
        url = reverse('structure:employee-list')
        data = {
            'fio': 'Testov Test Testovich',
            'post': 'Programmer',
            'salary': 500000,
            'age': 25,
            'department': self.test_department_id,
        }

        self.client.post(url, data)

        new_data = {
            'fio': 'New Test Testovich',
            'post': 'New programmer',
            # 'photo': 'http://testserver/photos/default_photo.jpg',
            'salary': 800000,
            'age': 28,
            'department': Department.objects.get(email='test_dep2@example.com').pk,
        }

        url = reverse('structure:employee-detail', kwargs={'pk': 5})
        response = self.client.put(url, data=new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['fio'], new_data['fio'])
        self.assertEqual(response.data['post'], new_data['post'])
        self.assertEqual(response.data['salary'], new_data['salary'])
        self.assertEqual(response.data['age'], new_data['age'])
        self.assertEqual(response.data['department'], new_data['department'])

        self.client.logout()

        response = self.client.put(url, data=new_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_delete_employee(self):
        url = reverse('structure:employee-detail', kwargs={'pk': 3})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)


class DepartmentTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create(username='tester')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        Department.objects.create(title='TestDepartment', email='test_dep@example.com')


    def test_create_department(self):
        url = reverse('structure:department-list')
        data = {
            'title': 'TestDepartment2',
            'email': 'test_dep2@example.com',
        }

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Department.objects.all().count(), 2)
        self.assertEqual(response.data['title'], data['title'])
        self.assertEqual(response.data['email'], data['email'])

        self.client.logout()

        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_list_department(self):
        url = reverse('structure:department-list')

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.logout()

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = reverse('structure:department-detail', kwargs={'pk': 4})
        self.client.force_authenticate(user=self.user)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        self.client.logout()

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)


    def test_update_department(self):
        url = reverse('structure:department-detail', kwargs={'pk': 5})
        new_data = {
            'title': 'NewTestTitleDepartment',
            'email': 'newtest_dep@example.com',
        }

        response = self.client.put(url, new_data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], new_data['title'])
        self.assertEqual(response.data['email'], new_data['email'])

        self.client.logout()

        response = self.client.put(url, new_data)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


    def test_delete_department(self):
        url = reverse('structure:department-detail', kwargs={'pk': 3})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.client.logout()

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)