from django.db import models
from django.conf import settings

# Create your models here.
# 글종류 : PostType
class Posttype(models.Model) :
    name = models.CharField('구분', max_length = 200)
    def __str__(self):
        return self.name
# 글 : POST
class Post(models.Model):
    type = models.ForeignKey(Posttype, on_delete=models.CASCADE)
    headline = models.CharField('제목', max_length = 100)
    content = models.TextField('내용', blank=True, null=True)
    pub_date = models.DateField('날짜', auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    def __str__(self):
        return self.headline
    class Meta:
        ordering = ('-id', )
# 글에 들어있는 이미지 : Image
class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    image = models.ImageField('이미지 파일', upload_to = 'image/%y%m%d')
    def delete(self, *args, **kwargs):
        self.image.delete() #객체가 가지고 있는 이미지경로에 있는 파일을 삭제
        #Model 클래스의 delete 함수 호출
        super(Image.self).delete(*args, **kwargs)
    def __str__(self):
        return self.post.headline
# 글에 들어있는 파일 : File
class File(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    file = models.FileField('파일', upload_to='files/%y%m%d')
    def delete(self, *args, **kwargs):
        self.file.delete()
        super(File, self).delete(*args, **kwargs)
    def __str__(self):
        return self.post.headline