from django.db import models

AGE = (('令和', '令和'), ('平成', '平成'), ('昭和', '昭和'),('大正', '大正'),('明治', '明治'))
class MeigennModel(models.Model):
    title = models.CharField(max_length=50)

    name = models.CharField(max_length=50)

    age = models.CharField(
        max_length=50,
        choices = AGE
    )

    memo = models.TextField(max_length=200)

def __str__(self):
    return self.title
