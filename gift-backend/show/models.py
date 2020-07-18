from django.db import models


# Create your models here.
class Questions(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    questions_text = models.CharField(max_length=200, unique=True)
    answers = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.questions_text

    class Meta:
        verbose_name = '问题'
        verbose_name_plural = '问题'


class Score(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    total_score = models.IntegerField()

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = '积分'
        verbose_name_plural = '积分'
