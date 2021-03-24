from django.shortcuts import render

# Create your views here.
from .models import Presenting



def index(request):
    """
    포럼의 제시된 안건 목록을 보여줍니다.
    """
    presenting_list = Presenting.objects.order_by('-create_date')
    context = {'presenting_list': presenting_list}
    return render(request, 'forum/presenting_list.html', context)



def detail(request, presenting_id):
    """
    제시한 내용 출력
    """
    presenting = Presenting.objects.get(id=presenting_id)
    context = {'presenting': presenting}
    return render(request, 'forum/presenting_detail.html', context)