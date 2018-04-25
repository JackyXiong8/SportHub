from django.shortcuts import render, HttpResponse, redirect
from .models import *

def dashboard(request):
  return render(request, 'odin/index.html')
  request.session.clear()
  print (request.session['id'])

def register(request):
  errors = User.objects.nameValidator(request.POST)
  if len(errors):
    for key, value in errors.items():
      messages.error(request, value)
      request.session['first_name'] = request.POST['first_name']
      request.session['last_name'] = request.POST['last_name']
      request.session['email'] = request.POST['email']
      return redirect('/')
  else:
    request.session.clear()
    pwhash = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
    user = User.objects.create(first_name = request.POST['first_name'], last_name = request.POST['last_name'], email = request.POST['email'], password = pwhash)
    request.session['first_name'] = request.POST['first_name']
    request.session['last_name'] = request.POST['last_name']
    request.session['id'] = user.id
    return redirect('/')

def login(request):
  errors = User.objects.loginValidator(request.POST)
  if len(errors):
    for key, value in errors.items():
      messages.error(request, value)
    return redirect('/')
  else:
    request.session['first_name'] = User.objects.get(email=request.POST['email']).first_name
    request.session['last_name'] = User.objects.get(email=request.POST['email']).last_name
    request.session['id'] = User.objects.get(email=request.POST['email']).id
    print (request.session['id'])
    return redirect('/')

def nbaindex(request):

    return render(request, 'odin/nbaindex.html')

def mlbindex(request):

    return render(request, 'odin/mlbindex.html')

def nflindex(request):

    return render(request, 'odin/nflindex.html')

def about(request):

    return render(request, 'odin/about.html')

def music(request):

    return render(request, 'odin/music.html')

# Create your views here.
