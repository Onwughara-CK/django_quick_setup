from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model

from ..forms import SignUpForm


class IndexViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.response = cls.client.get('/')

        # create User instance
        cls.user = get_user_model().objects.create_user(
            email='test@test.com',username='tester', password='asdf7890')

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_returns_correct_template(self):
        self.assertTemplateUsed(self.response, "accounts/index.html")       


class SignUpViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.response = cls.client.get('/signup/')

    def test_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_returns_correct_template(self):
        self.assertTemplateUsed(self.response, "accounts/authenticate.html")

    def test_context_object(self):#         
        self.assertIsInstance(self.response.context.get('form'),SignUpForm)

    # POST
    def test_invalid_data(self):
        response = self.client.post('/signup/', {})
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "accounts/authenticate.html")

    def test_valid_data(self):
        response = self.client.post('/signup/', {
            'email': 'jamesbond@test.com',
            'username':'james',
            'password1': '1234asdf7890',
            'password2': '1234asdf7890',
        })
        user = get_user_model().objects.get(email='jamesbond@test.com')
        self.assertEqual(user.email, 'jamesbond@test.com')
        self.assertEqual(response.status_code, 302)
        self.assertRedirects(response, reverse('accounts:index'))


class LoginViewTest(TestCase):
    """
    Test Login View
    """

    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.response = cls.client.get(reverse('accounts:login'))

        cls.user = get_user_model().objects.create_user(
            email='test@test.com', 
            username = 'tester',
            password='asdf7890',
        )       

    def test_url_resolves_with_correct_status_code(self):
        self.assertEqual(self.response.status_code, 200)

    def test_returns_correct_template(self):
        self.assertTemplateUsed(self.response, "accounts/authenticate.html")

    def test_user_is_redirect_if_authenticated(self):        
        
        self.client.login(
            username='tester', password='asdf7890')
        response = self.client.get('/login/')
        self.assertEqual(response.status_code, 302)
        self.assertTrue(self.user.is_authenticated)


class LogoutViewTest(TestCase):
    """
    Test Logout View
    """
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()

        cls.user = get_user_model().objects.create_user(
            email='test@test.com', 
            username = 'tester',
            password='asdf7890',
        )

    def setUp(self):
        self.client.login(
            username = 'tester', password='asdf7890')

    def test_url_resolves_with_correct_status_code(self):        
        response = self.client.get('/logout/')
        self.assertEqual(response.status_code, 200)

    def test_returns_correct_template(self):
        response = self.client.get('/logout/')
        self.assertTemplateUsed(response, "accounts/logout.html")
        
