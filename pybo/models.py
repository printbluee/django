from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Question(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_question')
    subject = models.CharField(max_length=200) # 제목,최대 200자 / CharField(글자수의 길이가 제한된 텍스트)
    content = models.TextField() # 내용 / TextField(글자수를 제한할 수 없는 텍스트)
    voter = models.ManyToManyField(User, related_name='voter_question')  # 추천인 추가
    create_date = models.DateTimeField() # 작성일시 / DateTimeField(날짜와 시간에 관계된 속성)
    modify_date = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return self.subject


class Answer(models.Model):
    # author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='author_answer')
    question = models.ForeignKey(Question, on_delete=models.CASCADE) # ForeignKey(기존 모델을 속성으로 연결)
    content = models.TextField()
    create_date = models.DateTimeField()
    modify_date = models.DateTimeField(null=True, blank=True)
    voter = models.ManyToManyField(User, related_name='voter_answer')
    # on_delete=models.CASCADE(답변과 연결된 질문(Question)이 삭제될 경우 답변(Answer)도 함께 삭제된다는 의미)
    
    