from django.shortcuts import render





def index(request):
	return render(request,'index.html',)


def login(request):
    request.session['a']=request.POST.get('name')
    request.session['b']=request.POST.get('age')
    request.session['c']=request.POST.get('city')
    return render(request,'login.html')

def logout(request):
    return render(request,'logout.html')

def hello(request):
    return render(request, 'hello.html')

def hitman(request):
    return render(request, 'hitman.html')

def batman(request):
    return render(request, 'batman.html')	


















