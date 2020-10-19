# from django.shortcuts import render, get_object_or_404, redirect
# from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
# from django.contrib.messages.views import SuccessMessageMixin
# from django.core.paginator import Paginator
# from django.core.exceptions import PermissionDenied
# from django.views import generic, View
# from django.urls import reverse_lazy, reverse
# from django.contrib import messages
# from django.http import HttpResponse
# from django.forms import formset_factory



# #################################################
# ################# LIST ##########################
# #################################################

# class QuizListView(LoginRequiredMixin, UserPassesTestMixin, generic.ListView):
#     model = Quiz
#     template_name = "dashboard/quiz_list.html"
#     context_object_name = 'quizzes'

#     def test_func(self):
#         user = self.request.user
#         if not user.teacher:
#             raise PermissionDenied
#         return True

# class PostListView(ListView):
#     model = Post
#     context_object_name = 'posts'
#     ordering = ['-date_posted']
#     paginate_by = 4


# class UserPostListView(ListView):
#     model = Post
#     context_object_name = 'posts'
#     ordering = ['-date_posted']
#     paginate_by = 4

#     def get_queryset(self):
#         user = get_object_or_404(User, username=self.kwargs.get('username'))
#         return user.post_set.all()









# #################################################
# ################# CREATE ########################
# #################################################

# class PostCreateView(LoginRequiredMixin, CreateView):
#     model = Post
#     fields = ['title', 'content']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)














# #################################################
# ################# DETAIL ########################
# #################################################

# class PostDetailView(DetailView):
#     model = Post
#     context_object_name = 'post'


# class QuizDetailView(LoginRequiredMixin, UserPassesTestMixin, generic.DetailView):
#     model = Quiz
#     template_name = "dashboard/quiz_detail.html"
#     context_object_name = 'quiz'

#     def test_func(self):
#         user = self.request.user
#         if not user.teacher:
#             raise PermissionDenied
#         return True















# #######################################
# ############## DELETE #################
# #######################################

# class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
#     model = Post
#     context_object_name = 'obj'
#     success_url = '/'

#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False


# class QuizDeleteView(
#     LoginRequiredMixin,
#     UserPassesTestMixin,
#     generic.edit.DeleteView
# ):
#     model = Quiz
#     success_url = reverse_lazy('dash:quiz_list')
#     success_message = 'Successfully Deleted quiz'
#     context_object_name = 'object'
#     template_name = "dashboard/dash_confirm_delete.html"

#     def test_func(self):
#         user = self.request.user
#         if not user.teacher:
#             raise PermissionDenied
#         return True

#     def delete(self, request, *args, **kwargs):
#         messages.success(self.request, self.success_message)
#         return super().delete(request, *args, **kwargs)


# class QuestionDeleteView(
#     LoginRequiredMixin,
#     UserPassesTestMixin,
#     generic.edit.DeleteView
# ):
#     model = Question
#     success_message = 'Successfully Deleted Question'
#     context_object_name = 'object'
#     template_name = "dashboard/dash_confirm_delete.html"

#     def test_func(self):
#         user = self.request.user
#         if not user.teacher:
#             raise PermissionDenied
#         return True

#     def get_success_url(self):
#         return reverse('dash:quiz_questions', args=[self.object.quiz.pk])

#     def delete(self, request, *args, **kwargs):
#         self.object = self.get_object()
#         messages.success(self.request, self.success_message)
#         return super().delete(request, *args, **kwargs)



















# #################################################
# ################# UPDATE ########################
# #################################################

# class QuizUpdateView(
#     LoginRequiredMixin,
#     UserPassesTestMixin,
#     SuccessMessageMixin,
#     generic.edit.UpdateView
# ):
#     model = Quiz
#     fields = ('quiz_text', 'duration', 'quiz_title')
#     success_message = 'Successfully Updated quiz'
#     template_name = "dashboard/dash_form.html"

#     def test_func(self):
#         user = self.request.user
#         if not user.teacher:
#             raise PermissionDenied
#         return True

# class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
#     model = Post
#     fields = ['title', 'content']

#     def form_valid(self, form):
#         form.instance.author = self.request.user
#         return super().form_valid(form)

#     def test_func(self):
#         post = self.get_object()
#         if self.request.user == post.author:
#             return True
#         return False


        




