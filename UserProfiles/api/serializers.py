from rest_framework import serializers

# from ..models import Article, Form
from ..models import UserProfile


class UserProfilesSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ('firstName', 'lastName', 'eMail', 'passWord')


# class ArticleSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Article
#         fields = ('title', 'content')


