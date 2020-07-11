from django.db import models


# Create your models here.
class Questions(models.Model):
    questions_text = models.CharField(max_length=200, primary_key=True, unique=True)
    answers = models.CharField(max_length=200, unique=True, default='0')
    
    def __str__(self):
        return self.questions_text

    class Meta:
        verbose_name = '问题'
        verbose_name_plural = '问题'
