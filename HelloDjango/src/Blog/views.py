from django.shortcuts import render, get_object_or_404
from .models import *
#함수기반의 뷰에 로그인을 한 상태에서만 접슨할 수 있도ㅗ록 설정하는 이노테이션(@)
#비로그인 상태일 때 해당 뷰를 접슨하면 LOGIN_URL에 적힌 페이지로 이도
from django.contrib.auth.decorators import login_required
from Blog.forms import PostForm
from django.http.response import HttpResponseRedirect
from django.urls import reverse
from django.template.context_processors import request
# Create your views here.
# 자유게시판 메인 페이지
# Post 객체를 10개씩 보여줌
# 다음 페이지 > 다음 객체 10개를 보여줌
# 이전 페이지 > 이전 객체 10개를 보여줌
def index(request):
    if request.method == "GET":
        index = int(request.GET.get('index', 0))
        # Post 객체 가져오기
        objs = Post.objects.all()
        max = len(objs) #전체 객체 개수
        # 현재 요청한 페이지의 첫번째 객체의 순서가 Post 객체 개수보다 작은가?
        data = None
        if index*10 < max :
            if index*10 + 9 < max:
                data = objs[index*10 : index*10+10]
                nextPage = index + 1
            else:
                data = objs[index*10 : ]
                nextPage = -1
                previousPage = index - 1 
                return render(request, 'blog/index.html', 
                              {'data':data, 'nextPage':nextPage, 
                               'previousPage':previousPage})
        else :
            return render(request, 'polls/error.html', 
                          {'error':'요청한 페이지가 없습니다.'})
            
def detail(request, post_id):
    obj = get_object_or_404(Post, pk = post_id)
    return render(request, 'blog/detail.html', 
                      {'obj': obj})
@login_required
def posting(request):  
    if request.method == "POST" :
        form = PostForm(request.POST)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            #request.FILES : 클라이언트가 보낸 파일들에 대한 데이터
            for f in request.FILES.getlist('images'):
                image = Image(post = obj, image = f)
                image.save()
            for f in request.FILES.getlist('files'):
                file = File(post = obj, file = f)
                file.save()
            return HttpResponseRedirect( reverse('blog:detail', args=(obj.id, )) )
        else:
            #입력값이 유효하지 않을 때 처리
            return render(request, 'blog/posting.html', {'form':form, 'error':'유효하지 않은 데이터입니다.'})
    if request.method == "GET":
        form = PostForm()
        return render(request, 'blog/posting.html', {'form':form})
    
@login_required
def post_delete(request, post_id):
    obj = get_object_or_404(Post, pk=post_id)
    if request.user == obj.author:
        obj.delete()
        return HttpResponseRedirect(reverse('blog:index'))
    else:
        return render(request, 'polls/error.html', 
                      {'error':'본인이 작선한 글만 삭제할 수 있습니다.', 
                       'mainurl':reverse('blog:index')})
    
#데코레이터
@login_required
def post_update(request, post_id):
    obj = get_object_or_404(Post, pk=post_id)
    if obj.author != request.user:
        return render(request, 'polls/error.html', 
                      {'error':'자신이 작성한 글만 수정할 수 있습니다.', 
                       'mainurl':reverse('blog:index')})
    if request.method == "POST" :
        form = PostForm(request.POST, instance = obj)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return HttpResponseRedirect(reverse('blog:detail', args = (post.id, )))
        else:
            return render(request, 'blog/update.html', {'form':form, 'error':'유효하지 않습니다.'})
    elif request.method == "GET" :
        form = PostForm(instance = obj)
        return render(request, 'blog/update.html', {'form':form})
    
    
    
    
    