# from django.shortcuts import render
# from django.http import HttpResponse
# from django.http import HttpResponse
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import StudentForm

# def home(request):
#     return HttpResponse("Hello, Django")
# def check_age(request):
#     print("VIEW LOADED")
#     age = None
#     if request.method == "POST":
#         age = int(request.POST.get("age", 0))
#     return render(request, 'home.html', {'age': age})
# def loop(request):
#     data = "Hello World"
#     number_list = [1, 2, 3, 4, 5, 6,7 ,8, 9, 10]
#     context = {
#         "data": data,
#         "list": number_list,
#     }
#     return render(request, 'home.html', context)
# def ti(request):
#     return render(request, 'extendedgeeks.html')
# def home(request):
#     return render(request, 'home.html')

# def welcome(request):
#     return HttpResponse("Welcome to Django")
# def square(request, num):
#     return render(request, 'home.html', {"number" : num * num})

def details(request):
    context = {'name': 'Athif', 'age': 22}
    context2 = {'name': 'athif', 'price': 1500.567,
    'msg': '<b>Welcome</b>',
    'fruits': ['apple', 'banana', 'mango'],
    'age': 17 ,
    'nums': [1,2,3,4,5,6]
    }
    return render(request, 'home.html', context2)
def hello(request):
    return render(request, 'hello.html')

def set_session(request):
    request.session['name'] = 'Athif'
    return HttpResponse("session created")

# def forms(request):
#     request.session['name'] = 'Athif'
#     name = None

#         name = request.POST.get('name')
#     return render(request, 'forms.html', {'message': name})


def response(request):
    request.session['name'] = "Athif"
    session = request.session.get('name')
    # del request.session['name']
    



    
    # return HttpResponse(session)
    return HttpResponse(session)
    
def hello(request):
    return render(request, 'hello.html')

def link(request):
    return render(request, 'link.html')

def form(request):
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'hello.html',{'name':name})

    else:
        form = StudentForm
    name = request.POST.get('name')

    return render(request, 'forms.html', {'message': form, 'name': name})

    





