from django.db import models

# Create your models here.

# 새로운 단어를 만들고 싶은 외래어를 제시하는 리스트

class Presenting(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField()

    def __str__(self):
        return self.subject

# 제시된 안건에 제안하는 리스트

class Suggestion(models.Model):
    suggestion = models.ForeignKey(Presenting, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()

 