from django.shortcuts import render
from preprocessing_prediction import prepr_pred


def index(request):
    if request.method == 'POST':
        content: str = request.POST['content']
        cont = prepr_pred(content)
        context = {'polarity': cont[0], 'accuracy': cont[1], 'text': content}
        return render(request, 'result.html', context)

    else:
        return render(request, 'index.html')



