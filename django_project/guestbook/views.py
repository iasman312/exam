from django.shortcuts import render, get_object_or_404, redirect

from .models import Feedback
from .forms import FeedbackForm, SearchForm


def index_view(request):
    form = SearchForm()
    if request.GET.get('author'):
        feedbacks = Feedback.objects.all().filter(
            author__startswith=request.GET.get('author'), status='active')
        return render(request, 'index.html', context={'feedbacks': feedbacks,
                                                      'form': form})
    feedbacks = Feedback.objects.all().filter(status='active')
    return render(request, 'index.html', context={'feedbacks': feedbacks,
                                                  'form': form})


def feedback_create_view(request):
    feedback = Feedback()
    if request.method == "GET":
        form = FeedbackForm()
        return render(request, 'feedback_create.html', context={'form': form})
    elif request.method == "POST":
        form = FeedbackForm(data=request.POST)
        if form.is_valid():
            feedback.author = form.cleaned_data.get('author')
            feedback.email = form.cleaned_data.get('email')
            feedback.text = form.cleaned_data.get('text')
            feedback.save()
            return redirect('feedback-list')
        return render(request, 'feedback_create.html', context={'form': form})


def feedback_update_view(request, pk):
    feedback = get_object_or_404(Feedback, id=pk)

    if request.method == 'GET':
        form = FeedbackForm(initial={
            'author': feedback.author,
            'email': feedback.email,
            'text': feedback.email
        })
        return render(request, 'feedback_update.html', context={'form': form,
                                                                'feedback':
                                                                    feedback})
    elif request.method == 'POST':
        form = FeedbackForm(data=request.POST)
        if form.is_valid():
            feedback.author = form.cleaned_data.get('author')
            feedback.email = form.cleaned_data.get('email')
            feedback.text = form.cleaned_data.get('text')
            feedback.save()
            return redirect('feedback-list')

        return render(request, 'feedback_create.html',
                      context={'form': form, 'feedback': feedback})
