from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from board.models import Boards,Comment
from django.core.urlresolvers import reverse
from django.shortcuts import get_object_or_404
from board.form import CommentForm
# Create your views here.
def index(request):
    boards = Boards.objects.all().order_by('-id')

    return render(request, 'index.html',{'boards':boards})

def new(request):
    return render(request, 'new.html',{})

def create(request):
    if request.POST['title'] != "" and request.POST['content']!="":
        title = request.POST['title']
        content = request.POST['content']
        bd = Boards(title=title,content=content)
        bd.save()

        return HttpResponseRedirect(reverse('board:index',args=()))
    else:
        return render(request, 'new.html',{
            'error_message':'제목이랑 내용 다 입력행'
        })

def show(request, board_id):
    bd = get_object_or_404(Boards, pk=board_id)
    form = CommentForm()
    comments = Comment.objects.filter(board=board_id).order_by('-id')
    return render(request,'show.html',{'board':bd,'comments':comments})

def edit(request, board_id):
    bd = get_object_or_404(Boards, pk=board_id)
    return render(request, 'edit.html',{'board':bd})

def update(request, board_id):
    bd = get_object_or_404(Boards, pk=board_id)

    bd2 = Boards.objects.filter(id=board_id)[0]
    bd2.title = request.POST['title']
    bd2.content = request.POST['content']
    bd2.save()

    return HttpResponseRedirect(reverse('board:show', args=(bd2.id,)))

def delete(request,board_id):
    bd = get_object_or_404(Boards, pk=board_id)
    bd2 = Boards.objects.filter(id=board_id)[0]
    bd2.delete()
    return HttpResponseRedirect(reverse('board:index', args=()))


def comment_create(request,board_id):
    b = get_object_or_404(Boards,pk=board_id)
    if request.method == "POST":
        comment = Comment()
        comment.content = request.POST['content']
        comment.board = b
        comment.save()
    else:
        form = PostForm()


    return HttpResponseRedirect(reverse('board:show',args=(board_id,)))


def comment_delete(request):
    pass
