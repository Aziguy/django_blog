from django.shortcuts import render


# Create your views here.
def blog(request):
    return render(request, 'blog/blog.html')


def article(request, num_art):
    if num_art in ['01', '02', '03']:
        return render(request, f'blog/article-{num_art}.html')
    return render(request, 'blog/aticle-not-found.html')
