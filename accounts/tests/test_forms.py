from django.test import TestCase
from django.contrib.auth import get_user_model

from accounts.forms import SignUpForm, SignInForm


class SignUpFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.form = SignUpForm()


    def test_signup_form_valid_data(self):
        form = SignUpForm(data={
            'email': 'test@test.com',
            'password1': 'nklsjiaskljnishujippaodjije2211m2k2m11',
            'password2': 'nklsjiaskljnishujippaodjije2211m2k2m11',
            'username': 'tester'

        })

        self.assertTrue(form.is_valid())

    def test_signup_form_no_data(self):
        self.assertFalse(self.form.is_valid())

    def test_correct_form_fields(self):
        self.assertIsNotNone(self.form.fields.get('email', None))
        self.assertIsNotNone(self.form.fields.get('username', None))
        self.assertIsNotNone(self.form.fields.get('password1', None))
        self.assertIsNotNone(self.form.fields.get('password2', None))

    def test_wrong_form_fields(self):
        self.assertIsNone(self.form.fields.get('bar', None))
        self.assertIsNone(self.form.fields.get('foo', None))
        self.assertIsNone(self.form.fields.get('foo_bar', None))

    def test_no_of_form_fields(self):
        self.assertEqual(len(self.form.fields), 4)

    def test_form_model(self):
        self.assertEqual(get_user_model(),self.form._meta.model)

        
class SignInFormTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        cls.form = SignInForm()

    def test_username_label(self):
        self.assertEqual(
            self.form.fields['username'].help_text,
            'Provide a registered Email or Username to Sign In'
        )
        self.assertEqual(
            self.form.fields['username'].label,
            'Username or Email'
        )
