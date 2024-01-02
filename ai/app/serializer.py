from rest_framework import serializers
from .models import UserInput, UserInputGenai


class UserInputSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInput
        fields = ['user_message', 'document', 'message']


class UserInputGenaiSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInputGenai
        fields = ['user_message', 'document', 'image', 'bot_message']


class GptSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserInputGenai
        fields = ['user_message', 'bot_message']
