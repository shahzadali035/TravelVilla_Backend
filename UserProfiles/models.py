from django.db import models

# Create your models here.

# User Profile


class UserProfile(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    eMail = models.EmailField(max_length=40, unique=True)
    passWord = models.CharField(max_length=20)

    def __str__(self):
        return self.firstName
        # This name is that which will show you when you create a form in django framework, Name of That will be this


# class Article(models.Model):
#     title = models.CharField(max_length=120)
#     content = models.TextField()
#
#     def __str__(self):
#         return self.title

