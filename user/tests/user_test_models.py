from unittest import TestCase

from user.models import CustomUser


class UserAccountsTest(TestCase):
    def test_superuser(self):
        superuser = CustomUser.objects.create(
            email="email@gmail.com", username="test_name", password="password", role=1
        )
        self.assertEqual(superuser.email, "email@gmail.com")
        self.assertEqual(superuser.role, 1)
        self.assertTrue(superuser.is_staff)
        self.assertTrue(superuser.is_superuser)
        self.assertTrue(superuser.is_active)
        self.assertEqual(str(superuser), "tests@gmail.com")

    def test_user(self):
        user = CustomUser.objects.create_user(
            email="email@gmail.com", username="test_name", password="password", role=2
        )
        self.assertEqual(user.email, "email@gmail.com")
        self.assertEqual(user.role, 2)
        self.assertFalse(user.is_staff)
        self.assertFalse(user.is_superuser)
        self.assertFalse(user.is_active)

    def test_str_method(self):
        user = CustomUser.objects.create_user(
            email="email@gmail.com", username="test_name", password="password", role=2
        )
        self.assertEqual(user.__str__, "email@gmail.com")
