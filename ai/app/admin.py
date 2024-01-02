from django.contrib import admin
from .models import UserInput, UserInputGenai, ChatGptModel

# Register your models here.
admin.site.register(UserInput)
admin.site.register(UserInputGenai)
admin.site.register(ChatGptModel)
