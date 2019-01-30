from .forms import ArticleForm
from django.shortcuts import render
from preprocessing_prediction import prepr_pred


def index(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            t = open(r'nlp_project\text.txt', 'w')
            content = request.POST['content']
            content = str(content)
            t.write(content)
            t.close()
            cont = prepr_pred()
            context = {'polarity': cont[0], 'accuracy': cont[1], 'text': cont[2]}
            return render(request, 'result.html', context)

    else:
        return render(request, 'index.html')


def result(request):
    return render(request, 'result.html')

