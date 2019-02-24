from django.shortcuts import render
from mn_sl import sem_analyze


def index(request):
    if request.method == 'POST':
        content: str = request.POST['content']
        result = sem_analyze(content)
        context = {'result': result[1], 'arguments': result[0], 'text': content}
        return render(request, 'result.html', context)

    else:
        return render(request, 'index.html')



