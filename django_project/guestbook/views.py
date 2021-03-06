from django.shortcuts import render, get_object_or_404, redirect

from .models import Feedback
from .forms import SearchForm


def index_view(request):
    form = SearchForm()
    if request.GET.get('author'):
        feedbacks = Feedback.objects.all().filter(
            name__startswith=request.GET.get('author'))
        return render(request, 'index.html', context={'feedbacks': feedbacks,
                                                      'form': form})
    feedbacks = Feedback.objects.all()
    return render(request, 'index.html', context={'feedbacks': feedbacks,
                                                  'form': form})