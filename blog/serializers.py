from blog.models import Post
from django.contrib.auth.models import User, Group
from rest_framework import serializers
from rest_framework.authtoken.models import Token


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ["id", "title", "author", "body", "category"]
        # fields = ' all '


class GroupSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['name', ]


class UserSerilizer(serializers.ModelSerializer):
    groups = GroupSerilizer(many=True, required=False)
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'groups']

        extra_kwargs = {'password': {
           'write_only': True,
           'required': True
        }}


    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        Token.objects.create(user=user)
        user.groups.add(1)
        return user


