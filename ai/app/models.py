from django.db import models


class UserInput(models.Model):
    user_message = models.TextField()
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    message = models.TextField(verbose_name="Message", null=True, blank=True)

    def __str__(self):
        return self.user_message


class UserInputGenai(models.Model):
    user_message = models.TextField()
    document = models.FileField(upload_to='documents/', null=True, blank=True)
    image = models.ImageField(upload_to='image/', null=True, blank=True)
    bot_message = models.TextField(verbose_name="Message", null=True, blank=True)

    def __str__(self):
        return self.user_message


class ChatGptModel(models.Model):
    user_message = models.TextField()
    bot_message = models.TextField(verbose_name="Message", null=True, blank=True)

    def __str__(self):
        return self.user_message