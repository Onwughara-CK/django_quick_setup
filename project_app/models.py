# from datetime import timedelta

# from django.db import models
# from django.contrib.auth import get_user_model
# from django.urls import reverse


# class Quiz(models.Model):
#     title = models.CharField(max_length=100)
#     text = models.TextField()
#     date_posted = models.DateTimeField(default=timezone.now)
#     author = models.ForeignKey(User, on_delete=models.CASCADE)
    
#     class Meta:
#         verbose_name_plural = 'books'
#         verbose_name = 'book'
#         get_latest_by = 'date_posted'
#         ordering = 'date_posted'


#     def get_absolute_url(self):
#         return reverse('dash:quiz_detail', args=[self.pk, ])

#     def get_delete_url(self):
#         return reverse('dash:quiz_delete', args=[self.pk, ])

#     def get_update_url(self):
#         return reverse('dash:quiz_update', args=[self.pk, ])

#     def __str__(self):
#         return self.title
