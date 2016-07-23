from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import timezone
from django.views import generic

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User, Permission

from mysite import settings
from .forms import *
from .models import *

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

def signup(request):
    is_user = False

    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            firstname = form.cleaned_data['first_name']
            lastname = form.cleaned_data['last_name']
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
#            password1 = form.cleaned_data['Password']
            if firstname is None:
                return render(request, 'polls/signup.html/',
                {'error_message':'First name is required.'})
            elif username is None:
                return render(request, 'polls/signup.html/',
                {'error_message':'Username is required.'})
            elif email is None:
                return render(request, 'polls/signup.html/',
                {'error_message':'Email is required.'})
#            elif password is None or password1 is None:
 #               return render(request, 'polls/signup.html/',
  #              {'error_message':'Password is required.'})
   #         elif password != password1:
    #            return render(request, 'polls/signup.html/',
     #           {'error_message':'Passwords do not match.'})
            else:
                # Create a new user.
                user = form.save()
                user.set_password(user.password)
                user.save()
                is_user = True

                return render(request, 'polls/index.html',
                {'message':'Welcome to PollsApp!'})

#        else:
#           print 'The form is not valid!'
    else:
        form = SignUpForm()
    return render(request, 'polls/signup.html', {'form':form, 'is_user':is_user})


def log_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['Username']
            password = form.cleaned_data['Password']
            user = authenticate(username=username, password=password)

            if user is None:
                return render(request, 'polls/log_in.html/',
                {'error_message':"Incorrect username or password."})
            elif user.is_active:
                login(request, user)
                return HttpResponseRedirect(reverse('polls:index'),
                {'message':'Welcome to PollsApp!'})
            else:
                return render(request, 'polls/log_in.html/',
                {'error_message':"The account has been disabled."})
        else:
            return render(request, 'polls/log_in.html',
            {'error_message':'The form is not valid.'})
    else:
        form = LoginForm()

    return render(request, 'polls/log_in.html', {'form':form})

@login_required
def change_pw(request):
    if request.method == 'POST':
        form = Change_pwForm(request.POST)

        if form.is_valid():
            old_pw = form.cleaned_data['Old_pw']
            new_pw = form.cleaned_data['New_pw']
            new_pw1 = form.cleaned_data['New_pw1']

            if old_pw or new_pw or new_pw1 is None:
                return render(request, 'polls/change_pw.html/'),
                {'error_message':'Password is required.'}
            elif authenticate(username=user.username, password=old_pw) is None:
                return render(request, 'polls/change_pw.html',
                {'error_message':'Incorrect password.'})
            elif new_pw != new_pw1:
                return render(request, 'polls/change_pw.html',
                {'error_message':'The passwords do not match.'})
            elif old_pw == new_pw:
                return render(request, 'polls/change_pw.html',
                {'error_message':'The new password is same as the existing one.'})
            else:
                user.set_password(new_pw)
                user.save()
                return HttpResponseRedirect(reverse('polls:index'),
                {'message':'Password changed successfully!'})
    
    else:
        form = Change_pwForm()

    return render(request, 'polls/change_pw.html', {'form':form})

@login_required
def edit(request):
    if request.method == 'POST':
        form = EditForm(request.POST)

        if form.is_valid:
            password = form.cleaned_data['Password']
            firstname = form.cleaned_data['Firstname']
            lastname = form.cleaned_data['Lastname']
            email = form.cleaned_data['Email']
            user = request.user

            if authenticate(username=user.username, password=password) is None:
                return render(request, 'polls/edit.html',
                {'error_message':'Incorrect password.'})
            else:
                if firstname is not None:
                    user.firstname = firstname
                if lastname is not None:
                    user.lastname = lastname
                if email is not None:
                    user.email = email
        
                user.save()
                return HttpResponseRedirect(reverse('polls:index'),
                {'message':'Changes saved.'})

    else:
        form = EditForm()

    return render(request, 'polls/edit.html')

@login_required
def log_out(request):
    logout(request)
    return render(request, 'polls/log_in.html')


# Create your views here.
