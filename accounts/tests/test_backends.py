from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate

class EmailAuthBackendTest(TestCase):
    """
    Test EmailAuthBackend 
    """
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

        cls.user = get_user_model().objects.create_user(
            email='test@test.com', 
            username = 'tester',
            password='asdf7890',
        )

    def test_user_authenticates_with_email(self):
        # authenticate(**credentials) returns the user if exist
        self.assertEqual(authenticate(
                email='test@test.com',
                password='asdf7890', 
        ),self.user)

    def test_invalid_email(self):
        #authenticate returns none if invalid credentials
        self.assertIsNone(authenticate(
                email='invalid-email@test.com',
                password='asdf7890', 
            )
        )

    def test_invalid_password(self):
        #authenticate returns none if invalid password
        self.assertIsNone(authenticate(
                email='test@test.com',
                password='invalid-password', 
            )
        )

