from .forms import ArticleForm
from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            t = open(r'nlp_project\text.txt', 'w')
            content = request.POST['content']
            content = str(content)
            t.write(content)
            t.close()
            return HttpResponse(content)
    else:
        return render(request, 'index.html')


def result(request):
    return render(request, 'result.html')
