from django.db import models
from customuser.models import CustomUser
import customuser

# Create your models here.
class Question(models.Model):
    #id는 생략해도 자동으로 장고에서 만들어 준다.
    question_text = models.CharField('질문 제목', max_length=200)
    pub_date = models.DateTimeField('date published')
    #글쓴이
    customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    #이미지 경로 저장
    image = models.ImageField('이미지 파일', upload_to='uploadfile/%y/%m/%d/content', blank=True, null=True)
    def __str__(self):
        return self.question_text

class Choice(models.Model):
    choice_text = models.CharField('답변 항목', max_length=100)
    votes = models.IntegerField(default=0)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.choice_text

#질문에 대한 댓글 모델 클래스
class Comment(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    customuser = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    text = models.TextField('댓글') #댓글을 저장할 수 있는 공간
    image = models.ImageField('이미지', upload_to='comment/%y/%m/%d/', blank=True, null=True) #이미지를 저장할 수 있는 공간