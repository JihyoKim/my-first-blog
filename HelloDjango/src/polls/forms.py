#모델 클래스와 관련된 입력양식 클래스를 만드는 파일
from django.forms.models import ModelForm #모델클래스와 연관디ㅗㄴ 입력양식 클래스를 만들때 사용
from . import models #. : 현재 위치

class QuestionForm(ModelForm):
    class Meta: #어떤 모델클래스/속성을 사용하는지, 
        #model : 내가 연결한 모델 클래스
        #fields, exclude 중 택 1
        #fields : 모델 클래스의 속성 중 사용자가 작성해야하는 것을 명시
        #exclude : 모델 클래스에 명시한 속성을 제외한 속성들을 사용자가 작성
        model = models.Question #Question 클래스를 사용하는 것을 명시
        fields = ['question_text', 'image', ] #변수이름과 동일한 문자열 작성
        #exclude=['pub_data', 'customuser',]
        
class ChoiceForm(ModelForm):
    class Meta:
        model = models.Choice
        # fields = ['question', 'choice_text', ] 또는
        exclude = ['votes', 'question', ]
        
class CommentForm(ModelForm):
    class Meta:
        model = models.Comment
        fields=['text', 'image']