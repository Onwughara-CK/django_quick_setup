# from django.test import TestCase


# #################################################
# ################ TEST FORM ######################
# #################################################
# class ChoiceFormTest(SimpleTestCase):
#     def test_valid_data(self):
#         data = {
#             'choice_text': 'choice 1',
#             'mark': 'wrong',
#         }

#         form = forms.ChoiceForm(data)
#         self.assertTrue(form.is_valid())

#     def test_invalid_data(self):
#         data = {}
#         form = forms.ChoiceForm(data)
#         self.assertFalse(form.is_valid())

#     def test_correct_form_fields(self):
#         form = forms.ChoiceForm()
#         self.assertIsNotNone(form.fields.get('choice_text', None))
#         self.assertIsNotNone(form.fields.get('mark', None))

#     def test_wrong_form_fields(self):
#         form = forms.ChoiceForm()
#         self.assertIsNone(form.fields.get('bar', None))
#         self.assertIsNone(form.fields.get('foo', None))

#     def test_no_of_form_fields(self):
#         form = forms.ChoiceForm()
#         self.assertEqual(len(form.fields), 2)

#     def test_form_model(self):
#         self.assertEqual(get_user_model(),self.form._meta.model)

#     def test_username_label(self):
#         self.assertEqual(
#             self.form.fields['username'].help_text,
#             'Provide a registered Email or Username to Sign In'
#         )
#         self.assertEqual(
#             self.form.fields['username'].label,
#             'Username or Email'
#         )






















# #################################################
# ################ TEST MODELS ####################
# #################################################

# class ChoiceModelTest(TestCase):
#     @classmethod
#     def setUpTestData(cls):
#         # set up unmodifiable test data
#         cls.quiz = models.Quiz.objects.create(
#             quiz_title='title 1',
#             quiz_text='text 1',
#             duration=timedelta(minutes=25)
#         )

#         cls.question = models.Question.objects.create(
#             question_text='text 1',
#             quiz=cls.quiz,
#         )

#         cls.choice = models.Choice.objects.create(
#             choice_text='text 1',
#             question=cls.question,
#         )

#         cls.MARK = (
#             ('right', 'Right'),
#             ('wrong', 'Wrong'),
#         )

#     def test_choice_text_label(self):
#         field_label = self.choice._meta.get_field(
#             'choice_text').verbose_name
#         self.assertEqual(field_label, 'choice text')

#     def test_choice_text_max_length(self):
#         max_length = self.choice._meta.get_field('choice_text').max_length
#         self.assertEqual(max_length, 250)

#     def test_question_label(self):
#         field_label = self.choice._meta.get_field('question').verbose_name
#         self.assertEqual(field_label, 'question')

#     def test_mark_label(self):
#         field_label = self.choice._meta.get_field('mark').verbose_name
#         self.assertEqual(field_label, 'mark')

#     def test_mark_max_length(self):
#         max_length = self.choice._meta.get_field('mark').max_length
#         self.assertEqual(max_length, 5)

#     def test_mark_default(self):
#         default = self.choice._meta.get_field('mark').default
#         self.assertEqual(default, 'wrong')

#     def test_mark_choices(self):
#         choices = self.choice._meta.get_field('mark').choices
#         self.assertEqual(choices, self.MARK)

#     def test_get_update_url(self):
#         self.assertEqual(self.choice.get_update_url(),
#                          f'/dashboard/choice/{self.choice.pk}/update/')

#     def test_choice_foreign_key_relationship_with_question(self):
#         self.assertEqual(self.question.choices.count(), 1)
#         self.assertEqual(self.question.choices.first().pk, self.choice.pk)
#         self.assertEqual(str(self.choice.question), str(self.question))

#     def test_choice_foreign_key_related_model(self):
#         self.assertEqual(self.choice._meta.get_field(
#             'question').related_model, models.Question)

#     def test_str(self):
#         self.assertEqual(str(self.choice), self.choice.choice_text)




# #################################################
# ################ TEST URLS ######################
# #################################################


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

#     ### LOGOUT VIEW TEST ###
#     def test_logout_url_resolves_to_logout_view(self):
#         url = reverse('accounts:logout')
#         self.assertURLEqual(url, '/logout/')
#         self.assertEqual(resolve(url).func.view_class, LogoutView)

#     ### INDEX VIEW TEST ###
#     def test_index_url_resolves_to_index_view(self):
#         url = reverse('accounts:index')
#         self.assertURLEqual(url, '/')
#         self.assertEqual(resolve(url).func.view_class, IndexView)









# #################################################
# ################ TEST VIEWS #####################
# #################################################


# ################ INDEX VIEW ################
# class DashViewTest(TestCase):
#     """
#     Test Dash View
#     """

#     @classmethod
#     def setUpTestData(cls):
#         cls.client = Client()

#         ### create student ###
#         cls.student = get_user_model().objects.create_user(
#             email='student@test.com', password='asdf7890')

#         ### create teacher ###
#         cls.teacher = get_user_model().objects.create_user(
#             email='teacher@test.com', password='asdf7890',)
#         cls.teacher.teacher = True
#         cls.teacher.save()

#     def setUp(self):
#         self.client.login(
#             email='teacher@test.com', password='asdf7890')
#         self.response = self.client.get(reverse('dash:dashboard'))

#     def test_redirect_if_not_logged_in(self):
#         self.client.logout()
#         response = self.client.get(reverse('dash:dashboard'))
#         self.assertRedirects(response, '/login/?next=/dashboard/')
#         self.assertEqual(response.status_code, 302)

#     def test_logged_in_with_correct_permission(self):
#         self.assertEqual(self.response.status_code, 200)

#     def test_returns_correct_template(self):
#         self.assertTemplateUsed(self.response, 'dashboard/dash.html')


# ################ CREATE VIEW ################

# class CreateQuizViewTest(TestCase):
#     """
#     Test Create Quiz View
#     """
#     @classmethod
#     def setUpTestData(cls):
#         cls.client = Client()

#         ### create student ###
#         cls.student = get_user_model().objects.create_user(
#             email='student@test.com', password='asdf7890')

#         ### create teacher ###
#         cls.teacher = get_user_model().objects.create_user(
#             email='teacher@test.com', password='asdf7890',)
#         cls.teacher.teacher = True
#         cls.teacher.save()

#     def setUp(self):
#         self.client.login(
#             email='teacher@test.com', password='asdf7890')
#         self.response_get = self.client.get(
#             reverse('dash:create_quiz'))

#     def test_redirect_if_not_logged_in(self):
#         self.client.logout()
#         response_get = self.client.get(
#             reverse('dash:create_quiz'))
#         response_post = self.client.post(
#             reverse('dash:create_quiz'))
#         self.assertRedirects(
#             response_get, '/login/?next=/dashboard/create_quiz/')
#         self.assertRedirects(
#             response_post, '/login/?next=/dashboard/create_quiz/')
#         self.assertEqual(response_get.status_code, 302)
#         self.assertEqual(response_post.status_code, 302)

#     def test_logged_in_but_not_correct_permission(self):
#         self.client.login(
#             email='student@test.com', password='asdf7890')
#         response_get = self.client.get(
#             reverse('dash:create_quiz'))
#         response_post = self.client.post(
#             reverse('dash:create_quiz'))
#         self.assertEqual(response_post.status_code, 403)
#         self.assertEqual(response_get.status_code, 403)

#     def test_logged_in_with_correct_permission(self):
#         self.assertEqual(self.response_get.status_code, 200)
#         self.assertTemplateUsed(
#             self.response_get, 'dashboard/create_quiz.html')

#         ### test request.POST['finish'] ###
#         response_post = self.client.post(
#             path=reverse('dash:create_quiz'),
#             data={
#                 'quiz_text': 'quiz text finish',
#                 'quiz_title': 'quiz title',
#                 'duration': timedelta(minutes=25),
#                 'finish': True,
#             }
#         )
#         ### redirects after post ###
#         self.assertEqual(response_post.status_code, 302)
#         self.assertEqual(models.Quiz.objects.get(
#             quiz_text='quiz text finish').quiz_text, 'quiz text finish')

#         ### test request.POST['finish'] is None ###
#         response_post = self.client.post(
#             path=reverse('dash:create_quiz'),
#             data={
#                 'quiz_text': 'quiz text',
#                 'quiz_title': 'quiz title',
#                 'duration': timedelta(minutes=25),
#             }
#         )
#         self.assertEqual(response_post.status_code, 200)
#         self.assertTemplateUsed(response_post, 'dashboard/create_quiz.html')

#         ### test request.POST['continue'] ###
#         response_post = self.client.post(
#             path=reverse('dash:create_quiz'),
#             data={
#                 'quiz_text': 'quiz text continue',
#                 'quiz_title': 'quiz title',
#                 'duration': timedelta(minutes=25),
#                 'continue': True,
#             }
#         )
#         self.assertEqual(response_post.status_code, 302)
#         self.assertEqual(models.Quiz.objects.get(
#             quiz_text='quiz text continue').quiz_text, 'quiz text continue')
        
#     def test_invalid_data(self):
#         response_post = self.client.post(reverse('dash:create_quiz'), data={})
#         self.assertEqual(response_post.status_code, 200)
#         self.assertEqual(models.Quiz.objects.count(), 0)


# ################ DETAIL VIEW ################
# class QuestionDetailViewTest(TestCase):
#     """
#     Test Question Detail View
#     """
#     @classmethod
#     def setUpTestData(cls):
#         cls.client = Client()

#         ### create student ###
#         cls.student = get_user_model().objects.create_user(
#             email='student@test.com', password='asdf7890')

#         ### create teacher ###
#         cls.teacher = get_user_model().objects.create_user(
#             email='teacher@test.com', password='asdf7890',)
#         cls.teacher.teacher = True
#         cls.teacher.save()

#         ### create question ###
#         cls.quiz = models.Quiz.objects.create(
#             quiz_text='text', quiz_title='title')
#         cls.question = models.Question.objects.create(
#             question_text='text', quiz=cls.quiz)

#     def setUp(self):
#         self.client.login(
#             email='teacher@test.com', password='asdf7890')
#         self.response = self.client.get(
#             reverse('dash:question_detail', args=[self.question.pk]))

#     def test_redirect_if_not_logged_in(self):
#         self.client.logout()
#         response = self.client.get(reverse('dash:question_detail', args=[1]))
#         self.assertRedirects(response, '/login/?next=/dashboard/question/1/')
#         self.assertEqual(response.status_code, 302)

#     def test_logged_in_with_correct_permission(self):
#         self.assertEqual(self.response.status_code, 200)

#     def test_returns_correct_template(self):
#         self.assertEqual(self.response.status_code, 200)
#         self.assertTemplateUsed(
#             self.response, 'dashboard/question_detail.html')

#     def test_context_object_name(self):
#         self.assertTrue('question' in self.response.context)









# ################ LIST VIEW ################
# class QuestionListViewTest(TestCase):
#     """
#     Test Question List View
#     """
#     @classmethod
#     def setUpTestData(cls):
#         cls.client = Client()

#         ### create student ###
#         cls.student = get_user_model().objects.create_user(
#             email='student@test.com', password='asdf7890')

#         ### create teacher ###
#         cls.teacher = get_user_model().objects.create_user(
#             email='teacher@test.com', password='asdf7890',)
#         cls.teacher.teacher = True
#         cls.teacher.save()

#         ### create 10 questions ###
#         quiz = models.Quiz.objects.create(quiz_text='text', quiz_title='title')
#         for i in range(1, 11):
#             models.Question.objects.create(
#                 question_text=f'text {i}', quiz=quiz)

#     def setUp(self):
#         self.client.login(
#             email='teacher@test.com', password='asdf7890')
#         self.response = self.client.get(reverse('dash:question_list'))

#     def test_redirect_if_not_logged_in(self):
#         self.client.logout()
#         response = self.client.get(reverse('dash:question_list'))
#         self.assertRedirects(response, '/login/?next=/dashboard/questions/')
#         self.assertEqual(response.status_code, 302)

#     def test_logged_in_with_correct_permission(self):
#         self.assertEqual(self.response.status_code, 200)

#     def test_logged_in_but_not_correct_permission(self):
#         self.client.login(
#             email='student@test.com', password='asdf7890')
#         response = self.client.get(reverse('dash:question_list'))
#         self.assertEqual(response.status_code, 403)

#     def test_returns_correct_template(self):
#         self.assertEqual(self.response.status_code, 200)
#         self.assertTemplateUsed(self.response, 'dashboard/question_list.html')

#     def test_context_object(self):
#         self.assertTrue('questions' in self.response.context)
#         self.assertContains(self.response, 'text 10')
#         self.assertCountEqual(
#             self.response.context['questions'], models.Question.objects.all())



# ################ UPDATE VIEW ################
# class QuestionUpdateViewTest(TestCase):
#     """
#     Test Question Update View
#     """
#     @classmethod
#     def setUpTestData(cls):
#         cls.client = Client()

#         ### create student ###
#         cls.student = get_user_model().objects.create_user(
#             email='student@test.com', password='asdf7890')

#         ### create teacher ###
#         cls.teacher = get_user_model().objects.create_user(
#             email='teacher@test.com', password='asdf7890',)
#         cls.teacher.teacher = True
#         cls.teacher.save()

#     def setUp(self):
#         self.client.login(
#             email='teacher@test.com', password='asdf7890')
#         self.quiz = models.Quiz.objects.create(
#             quiz_text='text', quiz_title='title')
#         self.question = models.Question.objects.create(
#             question_text='text', quiz=self.quiz)
#         self.response_get = self.client.get(
#             reverse('dash:question_update', args=[self.question.pk]))
#         self.response_put = self.client.post(
#             path=reverse('dash:question_update', args=[self.question.pk]),
#             data={
#                 'question_text': 'text updated',
#             }
#         )

#     def test_redirect_if_not_logged_in(self):
#         self.client.logout()
#         response_get = self.client.get(
#             reverse('dash:question_update', args=[1]))
#         response_put = self.client.put(
#             reverse('dash:question_update', args=[1]))
#         self.assertRedirects(
#             response_get, '/login/?next=/dashboard/question/1/update/')
#         self.assertRedirects(
#             response_put, '/login/?next=/dashboard/question/1/update/')
#         self.assertEqual(response_get.status_code, 302)
#         self.assertEqual(response_put.status_code, 302)

#     def test_logged_in_but_not_correct_permission(self):
#         self.client.login(
#             email='student@test.com', password='asdf7890')
#         response_get = self.client.get(
#             reverse('dash:question_update', args=[1]))
#         response_put = self.client.put(
#             reverse('dash:question_update', args=[1]))
#         self.assertEqual(response_put.status_code, 403)
#         self.assertEqual(response_get.status_code, 403)

#     def test_logged_in_with_correct_permission(self):
#         self.assertEqual(self.response_put.status_code,
#                          302)  # redirects after update
#         self.question.refresh_from_db()
#         self.assertEqual(self.question.question_text, 'text updated')

#     def test_success_message(self):
#         # no context data as it redirects
#         messages = list(get_messages(self.response_put.wsgi_request))
#         self.assertEqual(str(messages[0]), 'Successfully Updated Question')

#     def test_invalid_data(self):
#         response_post = self.client.post(
#             path=reverse('dash:question_update', args=[self.question.pk]),
#             data={}
#         )
#         # should redirect with status code 302 not 200
#         self.assertEqual(response_post.status_code, 200)


# ################ DELETE VIEW ################
# class QuestionDeleteViewTest(TestCase):
#     """
#     Test Question Delete View
#     """
#     @classmethod
#     def setUpTestData(cls):
#         cls.client = Client()

#         ### create student ###
#         cls.student = get_user_model().objects.create_user(
#             email='student@test.com', password='asdf7890')

#         ### create teacher ###
#         cls.teacher = get_user_model().objects.create_user(
#             email='teacher@test.com', password='asdf7890',)
#         cls.teacher.teacher = True
#         cls.teacher.save()

#     def setUp(self):
#         ### create question ###
#         self.quiz = models.Quiz.objects.create(
#             quiz_text='text', quiz_title='title')

#         self.question = models.Question.objects.create(
#             question_text='text', quiz=self.quiz)

#         self.client.login(
#             email='teacher@test.com', password='asdf7890')

#         self.response_get = self.client.get(
#             reverse('dash:question_delete', args=[self.question.pk]))

#         self.response_delete = self.client.delete(
#             reverse('dash:question_delete', args=[self.question.pk]))

#     def test_redirect_if_not_logged_in(self):
#         self.client.logout()
#         response_get = self.client.get(
#             reverse('dash:question_delete', args=[1]))
#         response_delete = self.client.delete(
#             reverse('dash:question_delete', args=[1]))
#         self.assertRedirects(
#             response_get, '/login/?next=/dashboard/question/1/delete/')
#         self.assertRedirects(
#             response_delete, '/login/?next=/dashboard/question/1/delete/')
#         self.assertEqual(response_get.status_code, 302)
#         self.assertEqual(response_delete.status_code, 302)

#     def test_logged_in_but_not_correct_permission(self):
#         self.client.login(
#             email='student@test.com', password='asdf7890')
#         response_get = self.client.get(
#             reverse('dash:question_delete', args=[1]))
#         response_delete = self.client.delete(
#             reverse('dash:question_delete', args=[1]))
#         self.assertEqual(response_delete.status_code, 403)
#         self.assertEqual(response_get.status_code, 403)

#     def test_logged_in_with_correct_permission(self):
#         # redirects to confirm delete template
#         self.assertEqual(self.response_get.status_code, 200)
#         self.assertEqual(self.response_delete.status_code,
#                          302)  # redirects after delete
#         self.assertFalse(models.Question.objects.filter(
#             pk=self.question.pk).exists())  # check if the deleted item still exists

#     def test_returns_correct_confirm_delete_template(self):
#         self.assertEqual(self.response_get.status_code, 200)
#         self.assertTemplateUsed(
#             self.response_get, 'dashboard/dash_confirm_delete.html')

#     def test_context_object_name(self):
#         self.assertTrue('object' in self.response_get.context)

#     def test_success_message(self):
#         # no context data as it redirects
#         messages = list(get_messages(self.response_delete.wsgi_request))
#         self.assertEqual(str(messages[0]), 'Successfully Deleted Question')










