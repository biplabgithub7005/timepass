from django.shortcuts import render
from .models import Posts
from .forms import PostForm
from accounts.models import Signup
# Create your views here.
def all_posts(request):
    form =PostForm(request.POST or None, request.FILES or None)
    if form.is_valid():

        title=form.cleaned_data.get('title')
        image=form.cleaned_data.get('image')
        login_usr = request.session.get('email')
        usr = Signup.objects.get(email=login_usr)

        post = Posts(user=usr, title=title, image=image)
        post.save()



        print('New post Successfully')

    posts=Posts.objects.all()
    context={
        'form':form,
        'posts':posts,
    }
    return render(request, 'posts.html',context)