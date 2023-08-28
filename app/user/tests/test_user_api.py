"""
Test user endpoints
"""
from django.contrib.auth import get_user_model
from rest_framework.test import APIClient
from rest_framework import status
from django.test import TestCase
from django.urls import reverse


CREATER_USER_URL = reverse('user:create')


def create_user(**params):
    """test for creating new user"""
    return get_user_model().objects.create_user(**params)


class PublicUserApiTest(TestCase):
    """test the public user api"""

    def setUp(self):
        self.client = APIClient()

    def test_create_user_success(self):
        """Test create user success"""
        payload = {
            'email': 'user@example.com',
            'password': 'pass123',
            'name': 'user',
        }
        res = self.client.post(CREATER_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        user = get_user_model().objects.get(email=payload['email'])
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_user_email_already_exists(self):
        """Test email already exists"""
        payload = {
            'email': 'user@example.com',
            'password': 'pass123',
            'name': 'user',
        }
        create_user(**payload)
        res = self.client.post(CREATER_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short_error(self):
        """Password is too short error test"""
        payload = {
            'email': 'user@example.com',
            'password': 'pass',
            'name': 'user',
        }

        res = self.client.post(CREATER_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exists = get_user_model().objects.filter(
            email=payload['email']
        ).exists()
        self.assertFalse(user_exists)
