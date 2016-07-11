from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views import generic

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth. decorators import login_required
from django.contrib.auth.models import User, Permission

from mysite import settings
from .models import Question, Choice

class IndexView(generic.ListView):

    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five questions that have been published."""
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):

    model = Question
    template_name = 'polls/detail.html'

    def get_queryset(self):
        """Excludes the future questions."""
        return Question.objects.filter(pub_date__lte=timezone.now())

class ResultsView(generic.DetailView):

    model = Question
    template_name = 'polls/results.html'

@login_required
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', { 
            'question': question, 
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))

def create_user(request):
    firstname = request.POST['Firstname']
    lastname = request.POST['Lastname']
    username = request.POST['Username']
    email = request.POST['Email']
    password = request.POST['Password']
    # Create a new user.
    user = User.objects.create_user(username, email, password)
    user.firstname = firstname
    user.lastname = lastname
    user.save()
    return HttpResponseRedirect(reverse('polls:index'))

def user_auth(request):
    username = request.POST['Username']
    password = request.POST['Password']
    user = authenticate(username=username, password=password)

    if user is None:
        return HttpResponse("Incorrect username or password.")
    elif user.is_active:
        login(request, user)
        return HttpResponseRedirect(reverse('polls:index'))
    else:
        return HttpResponse("The account has been disabled.")

def login(request):
    return render(request, 'polls/login.html/')

def signup(request):
    return render(request, 'polls/signup.html/')

@login_required
def change_pw(request):
    return render(request, 'polls/change_pw.html/')

@login_required
def check_pw(request):
    old_pw = request.POST['Old_pw']
    new_pw = request.POST['New_pw']
    new_pw1 = request.POST['New_pw1']
    if old_pw != password:
        return render(request, 'polls/change_pw.html')
    elif new_pw != new_pw1:
        return render(request, 'polls/change_pw.html')
    elif old_pw == new_pw:
        return render(request, 'polls/change_pw.html')
    else:
        user.set_password(new_pw)
        user.save()
        return HttpResponseRedirect(reverse('polls:index'))

def log_out(request):
    logout(request)
    return HttpResponseRedirect(reverse('polls:login'))


# Create your views here.
