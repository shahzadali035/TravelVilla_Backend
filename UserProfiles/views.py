# from django.http import HttpResponse
# from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets

# from .api.serializers import FormSerializer, ArticleSerializer
# from .models import Form, Article

from .api.serializers import UserProfilesSerializer
from .models import UserProfile


class FormViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfilesSerializer


# class ArticleViewSet(viewsets.ModelViewSet):
#     queryset = Article.objects.all()
#     serializer_class = ArticleSerializer


