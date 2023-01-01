from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView

from .models import BlogPost


class BlogHome(ListView):
    model = BlogPost  # Le model à utiliser
    context_object_name = 'posts'  # Variable à utiliser dans le fichier de template (par défaut: blogpost_list)

    def get_queryset(self):
        queryset = super().get_queryset()
        if self.request.user.is_authenticated:
            return queryset
        return queryset.filter(published=True)


@method_decorator(login_required, name='dispatch')
class BlogPostCreate(CreateView):
    model = BlogPost
    template_name = "blog/blogpost_create.html"  # On définit le template à utiliser pour la création d'article
    fields = ['title', 'content']  # On définit les champs qu'on souhaite afficher


@method_decorator(login_required, name='dispatch')
class BlogPostUpdate(UpdateView):
    model = BlogPost
    template_name = 'blog/blogpost_update.html'
    fields = ['title', 'content', 'published', ]


class BlogPostDetail(DetailView):
    model = BlogPost
    context_object_name = 'post'


class BlogPostDelete(DeleteView):
    model = BlogPost
    context_object_name = 'post'
    success_url = reverse_lazy('blog:home')  # L'url de redirection après suppression d'un article


# Create your views here.
def blog(request):
    return render(request, 'blog/blog.html')


def article(request, num_art):
    if num_art in ['01', '02', '03']:
        return render(request, f'blog/article-{num_art}.html')
    return render(request, 'blog/aticle-not-found.html')
