from django.db import models

# if any changes are made to the models, run the following command:
# python manage.py makemigrations
# python manage.py migrate
class Todo(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title
