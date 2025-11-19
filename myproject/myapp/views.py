from django.shortcuts import render
from django.http import HttpResponse

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
def home(request):
    return render(request, 'home.html')
