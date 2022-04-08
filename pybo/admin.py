from django.contrib import admin
from .models import Question, Answer

# Register your models here.

class QuestionAdmin(admin.ModelAdmin): # 검색창 만들기
    search_fields = ['subject']

admin.site.register(Question,QuestionAdmin)
admin.site.register(Answer,QuestionAdmin)