from django.contrib.auth.models import User
from django.db import models


class Question(models.Model):
    question = models.TextField(blank=False)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.question


class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    answer = models.CharField(max_length=100, blank=False)
    is_true = models.BooleanField(default=False)

    def __str__(self):
        return self.question.question


class Quiz(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    question = models.ForeignKey(Answer, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.email


class UserScore(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    score = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.quiz.user.email




