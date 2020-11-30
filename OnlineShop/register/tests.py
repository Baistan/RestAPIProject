from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, force_authenticate, APIRequestFactory
from django.urls import reverse
from .models import *

# Create your tests here.

class AccountTestCase(APITestCase):

    def setUp(self):
        self.create_url = reverse('create')
        Account.objects.create(name='Baistan',
                                last_name='Almazbekov',
                                username='baistan',
                                password='123456abc',
                                email='almazbekovbaistan@gmail.com',
        )

    def test_account_create(self):
        data = {
            "name":"Baistan",
            "last_name":"Almazbekov",
            "email":"almazbekovbaistan1@gmail.com",
            "username":"baistan1",
            "password":"123456abc",
            "password2":"123456abc",
        }
        self.response = self.client.post(self.create_url,data)
        print(self.response.data)
        self.assertEqual(self.response.status_code,status.HTTP_201_CREATED)



    def test_account_create_empty_username(self):
        data = {
            "name": "Baistan",
            "last_name": "Almazbekov",
            "email": "almazbekovbaistan@gmail.com",
            "username": "",
            "password": "123456abc",
            "password2": "123456abc",
        }
        self.response = self.client.post(self.create_url, data)
        print(self.response.data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_account_create_empty_email(self):
        data = {
            "name": "Baistan",
            "last_name": "Almazbekov",
            "email": "",
            "username": "baistan",
            "password": "123456abc",
            "password2": "123456abc",
        }
        self.response = self.client.post(self.create_url, data)
        print(self.response.data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_account_create_empty_last_name(self):
        data = {
            "name": "Baistan",
            "last_name": "",
            "email": "almazbekovbaistan@gmail.com",
            "username": "baistan",
            "password": "123456abc",
            "password2": "123456abc",
        }
        self.response = self.client.post(self.create_url, data)
        print(self.response.data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_passwords_dont_match(self):
        data = {
            "name": "Baistan",
            "last_name": "Almazbekov",
            "email": "almazbekovbaistan@gmail.com",
            "username": "baistan",
            "password": "123456abc",
            "password2": "123456abcd",
        }
        self.response = self.client.post(self.create_url, data)
        print(self.response.data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_account_create_username_duplicate(self):
        data = {
            "name": "Baistan",
            "last_name": "Almazbekov",
            "email": "almazbekovbaistan@gmail.com",
            "username": "baistan",
            "password": "123456abc",
            "password2": "123456abc",
        }
        self.response = self.client.post(self.create_url, data)
        print(self.response.data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_account_create_email_duplicate(self):
        data = {
            "name": "Baistan",
            "last_name": "Almazbekov",
            "email": "almazbekovbaistan@gmail.com",
            "username": "baistan",
            "password": "123456abc",
            "password2": "123456abc",
        }
        self.response = self.client.post(self.create_url, data)
        print(self.response.data)
        self.assertEqual(self.response.status_code, status.HTTP_400_BAD_REQUEST)


class loginTestCase(APITestCase):

    def setUp(self):
        self.login_url = reverse('login')
        self.factory = APIRequestFactory()
        self.request = self.factory.get(self.login_url)
        Account.objects.create(name='Baistan',
                               last_name='Almazbekov',
                               username='baistan',
                               password='123456abc',
                               email='almazbekovbaistan@gmail.com',
                               )



    def test_login(self):
        user = Account.objects.get(username='baistan')
        force_authenticate(request=self.request,user=user)
        print(self.request.body)



    def test_login_empty(self):
        user = Account.objects.get(username="",password="")
        force_authenticate(request=self.request, user=user)
        print(self.request.body)


