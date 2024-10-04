from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def hello(request):
    return HttpResponse("Hello World from Django!")




students =[
    {"id":1, "name":"Omar", "grade":100, 'image':"pic1.png"},
    {"id": 2, "name": "Ahmed", "grade": 100, 'image':"pic2.png"},
    {"id": 3, "name": "Mohamed", "grade": 100, 'image':"pic3.png"},
    {"id": 4, "name": "Noha", "grade": 100, 'image':"pic4.png"},
]
# return with templates
def liststds(request):
    return render(request, 'students/list.html', context={"students": students})



def profile(request, id ):
   stds = filter(lambda student : student['id'] == id, students)
   stds = list(stds)
   if stds:
       return render(request, 'students/profile.html', context={"student": stds[0]})
   return HttpResponse("<h1 style='color:red;'>Not Found</h1>")



