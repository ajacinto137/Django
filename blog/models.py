from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# go to terminal
# must rum make migrations after to update migrations file
# python manage.py sqlmigrate blog 0001 (name of app and file app)
#  then run python manage.py migrate

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title