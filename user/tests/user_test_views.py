from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from user.models import CustomUser


class TestUserViews(APITestCase):
    def test_register_view(self):
        url = reverse("reg")
        user_data = {
            "username": "test_name",
            "email": "email@gmail.com",
            "password": "password",
            "role": 1,
        }
        response = self.client.post(url, user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_login_view(self):
        url = reverse("login")
        user = CustomUser.objects.create_user(
            email="email@gmail.com", username="test_name", password="password"
        )
        self.client.force_login(user)
        user_data = {
            "email": "email@gmail.com",
            "username": "test_name",
            "password": "password",
        }
        response = self.client.post(url, user_data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
