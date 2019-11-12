from django.test import TestCase
from users.models import UserProfile


class UserTestCase(TestCase):

    def setUp(self):
        self.value = 4
        self.user_profile = UserProfile.objects.create(
            bio="This is my Bio"
        )

    def test_math_add(self):
        self.assertEqual(2 + 2, 4)

    def test_value(self):
        self.assertEqual(self.value, 4)
