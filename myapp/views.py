from django.shortcuts import render
from .models import Posst
from django.utils import timezone
from django.http import HttpResponse



def post_list(request):
    posts = Posst.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    # Aquí se está mandando a post a la plantilla para poder usar sus valores "{'postsss': posts}"
    return render(request, 'blog/post_list.html', {'postsss': posts}) 
