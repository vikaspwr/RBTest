from django.contrib import admin
from ApplicationTest.models import Question, Answer, Quiz, UserScore

admin.site.register(Question)
admin.site.register(Answer)
admin.site.register(Quiz)
admin.site.register(UserScore)

