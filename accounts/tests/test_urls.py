# from django.test import SimpleTestCase
# from django.contrib.auth.views import LoginView, LogoutView
# from django.urls import resolve, reverse

# from ..views import SignUpView


# class UrlTest(SimpleTestCase):    

#     ### SIGN UP VIEW TEST ###
#     def test_signup_url_resolves_to_signup_view(self):
#         url = reverse('accounts:signup')
#         self.assertURLEqual(url, '/signup/')
#         self.assertEqual(resolve(url).func.view_class, SignUpView)

#     ### LOGIN VIEW TEST ###
#     def test_login_url_resolves_to_login_view(self):
#         url = reverse('accounts:login')
#         self.assertURLEqual(url, '/login/')
#         self.assertEqual(resolve(url).func.view_class, LoginView)

#      ### LOGOUT VIEW TEST ###
#     def test_logout_url_resolves_to_logout_view(self):
#         url = reverse('accounts:logout')
#         self.assertURLEqual(url, '/logout/')
#         self.assertEqual(resolve(url).func.view_class, LogoutView)
