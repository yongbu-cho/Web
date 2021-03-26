from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Presenting
from django.utils import timezone


def index(request):
    """
    포럼의 제시된 안건 목록을 보여줍니다.
    """
    presenting_list = Presenting.objects.order_by('-create_date')
    context = {'제시목록': presenting_list}
    return render(request, 'forum/presenting_list.html', context)



def detail(request, presenting_id):
    """
    제시한 내용 출력
    """
    presenting = Presenting.objects.get(id=presenting_id)
    context = {'presenting': presenting}
    return render(request, 'forum/presenting_detail.html', context)


def suggestion_create(request, presenting_id):
    """
    제시 안건에 제안 등록
    """
    presenting = get_object_or_404(Presenting, pk=presenting_id)
    presenting.suggestion_set.create(content=request.POST.get('content'), create_date=timezone.now())    
    return redirect('forum:detail', presenting_id=presenting.id)


def presenting_create(request):
    """
    새로운 안건  등록
    """
    form = PresentingForm()
    return render(request, 'forum/presenting_form.html', {'form': form})    