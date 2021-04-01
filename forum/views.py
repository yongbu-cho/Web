from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from .models import Presenting
from django.utils import timezone
from .forms import PresentingForm, SuggestionForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages


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

@login_required(login_url='common:login')
def suggestion_create(request, presenting_id):
    """
    제시 안건에 제안 등록
    """
    presenting = get_object_or_404(Presenting, pk=presenting_id)

    if request.method == "POST":
        form = SuggestionForm(request.POST)
        if form.is_valid():
            suggestion = form.save(commit=False)
            suggestion.author = request.user
            suggestion.create_date = timezone.now()
            suggestion.suggestion = presenting
            suggestion.save()
            return redirect('forum:detail', presenting_id=presenting.id)
    else:
        form = SuggestionForm()
    context = {'presenting': presenting, 'form': form}
    return render(request, 'forum/presenting_detail.html', context)


@login_required(login_url='common:login')
def presenting_create(request):
    """
    새로운 안건  등록
    """
    if request.method == 'POST':
        form = PresentingForm(request.POST)
        if form.is_valid():
            presenting = form.save(commit=False)
            presenting.author = request.user
            presenting.create_date = timezone.now()
            presenting.save()
            return redirect('forum:index')
    else:
        form = PresentingForm()
    context = {'form': form}
    return render(request, 'forum/presenting_form.html', context)


@login_required(login_url='common:login')
def presenting_modify(request, presenting_id):
    """
    forum 제시문 수정
    """
    presenting = get_object_or_404(Presenting, pk=presenting_id)
    if request.user != presenting.author:
        messages.error(request, '수정권한이 없습니다')
        return redirect('forum:detail', presenting_id=presenting.id)

    if request.method == "POST":
        form = PresentingForm(request.POST, instance=presenting)
        if form.is_valid():
            presenting = form.save(commit=False)
            presenting.author = request.user
            presenting.modify_date = timezone.now()  # 수정일시 저장
            presenting.save()
            return redirect('forum:detail', presenting_id=presenting.id)
    else:
        form = PresentingForm(instance=presenting)
    context = {'form': form}
    return render(request, 'forum/presenting_form.html', context)    



@login_required(login_url='common:login')
def presenting_delete(request, presenting_id):
    """
    forum 질문삭제
    """
    presenting = get_object_or_404(Presenting, pk=presenting_id)
    if request.user != presenting.author:
        messages.error(request, '삭제권한이 없습니다')
        return redirect('forum:detail', presenting_id=presenting.id)
    presenting.delete()
    return redirect('forum:index')    