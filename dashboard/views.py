# Create your views here.
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import redirect, render
from django.views.decorators.http import require_POST

from courses.models import Course
from dashboard.forms import LoginForm, RegisterForm
from dashboard.models import Status, Profile


@require_POST
def enroll(request):
    course = Course.objects.get(pk=request.POST['course'])

    rel = Status(course=course, user=request.user.profile,
                 role="student")
    rel.save()

    return redirect("courses:lectures", (course.id))


def auth(request):
    # FIXME: notification about bad credentials is not show
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():

            user = authenticate(username=form.data['username'], password=form.data['password'])
            if user:
                login(request, user)
                return redirect("home")

    else:
        form = LoginForm()
    return render(request, 'login.html', {"form": form})


def register(request):
    if request.method == "POST":
        form = RegisterForm(data=request.POST)

        if form.is_valid():
            User.objects.create_user(
                username=form.data['username'],
                email=form.data['email'],
                password=form.data['password']
            )

            # Now we save the UserProfile model instance.
            user = authenticate(username=form.data['username'], password=form.data['password'])
            login(request, user)
            Profile.objects.create(user=user)

            return redirect("home")

    else:
        form = RegisterForm()

    return render(request, 'register.html', {'form': form})


def dashboard(request, username):
    enrolled = Course.objects.filter(profile=User.objects.get(username=username).profile).all()
    return render(request, 'dashboard.html', {"enrolled": enrolled})