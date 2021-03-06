from django.shortcuts import render,get_object_or_404,HttpResponse
from blog.models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .forms import EmailPostForm,CommentForm
from django.core.mail import send_mail
from taggit.models import Tag
import pyqrcode
# Create your views here.
def post_list(request,tag_slug=None):
    posts=Post.published.all()
    tag=None

    if tag_slug:
        tag=get_object_or_404(Tag,slug=tag_slug)
        posts=posts.filter(tag__in=[tag])

    paginator=Paginator(posts,3)
    page=request.GET.get('page')
    try:
        posts=paginator.page(page)
    except PageNotAnInteger:
        posts=paginator.page(1)
    except EmptyPage:
        posts=paginator.page(paginator.num_pages)

    return render(request,'post/list.html',{'page':page,'posts':posts,'tag':tag})

def post_detail(request,year,month,day,post):
    post=get_object_or_404(Post,slug=post,
                                status='published',
                                publish__year=year,
                                publish__month=month,
                                publish__day=day)

    comments = post.comments.filter(active=True)
    if request.method == 'POST':
        # A comment was posted
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment
            new_comment.post = post
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()
    return render(request, 'post/detail.html', {'post': post,
                                                     'comments': comments,
                                                     'comment_form': comment_form,
                                                     })



def post_share(request,post_id):
    post=get_object_or_404(Post,id=post_id,status='published')
    sent=False
    form=EmailPostForm(request.POST)
    if form.is_valid():
        cd=form.cleaned_data
        post_url=request.build_absolute_uri(post.get_absolute_url())
        subject='{}({}) reccomends you reading "{}"'.format(cd['name'],cd['email'],post.title)
        message='read "{}" at {}\n\n{}\'s comments:{}'.format(post.title,post_url,cd['name'],cd['comments'])
        send_mail(subject,message,'sharmachandan351@gmail.com',[cd['to']])
        sent=True
    else:
        form=EmailPostForm()
    return render(request,'post/share.html',{'post':post,
                                              'form':form,
                                              'sent':sent})


def profile(request):
    return render(request,'profile.html')



def qrcode(request):
    q=pyqrcode.create("http://127.0.0.1:8000/blog/profile")
    qrcode=q.png('myqr.png',scale=6)
    print("qrcode is generated")

    return render(request,'qrcode.html',{'qrcode':qrcode})



