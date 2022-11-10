from django.shortcuts import render
from .models import Posst
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
from django.http import HttpResponse



def post_list(request):
    posts = Posst.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # Aquí se está mandando a post a la plantilla para poder usar sus valores -> "{'postsss': posts}"
    return render(request, 'blog/post_list.html', {'postsss': posts}) 

def post_detail(request, pk):
#    Posst.objects.get(pk=pk)
    post = get_object_or_404(Posst, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})

def post_new(request):
    # Formulario cuando generamos un POST, Todos los campos del formulario estan en request.POST
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
        
    else:
        # Formulario vacio, mostrado por primera vez.
        form = PostForm()
        return render(request, 'blog/post_edit.html', {'form': form})

def post_edit(request, pk):
    post = get_object_or_404(Posst, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})