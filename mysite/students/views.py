from django.shortcuts import render, redirect, reverse

from django.http import HttpResponse
from students.models import Student

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



def index(request):
    # get objects from db ??
    # use models
    # model provide functions --> get objects from db .
    # select * from students;
    # in django
    students= Student.objects.all()
    return  render(request, 'students/index.html',
                   context={"students":students})


# get specific student ??
def show(request, id):
    # get student --> with given Id
    student = Student.objects.filter(id=id) # list --> contains one object
    if student:
        return render(request, 'students/show.html', context={"student": student[0]})

    return HttpResponse("<h1 style='color:red;'>Not Found</h1>")


def delete(request, id):
    student = Student.objects.get(id=id) # get the object
    # model provide function --> delete ??
    # delete from students where id=id;
    student.delete()
    url  = reverse("students.index") # return with url ---> name --> students.index --> /students/
    return  redirect(url)
    # return HttpResponse("<h1 style='color:red;'>Deleted </h1>")




def create(request):
    # print(request)
    if request.method == 'POST':
        print("params", request.POST)
        student = Student()
        student.name = request.POST['name']
        student.grade = request.POST['grade']
        student.email = request.POST['email']

        # when you use enctype to allow uploading files
        # you will find the file details in request.FILES
        # student.image = request.POST['image']
        student.image= request.FILES['image']

        # insert into students_student
        student.save() # save object in db.

        print(student.id) # object created
        # return HttpResponse("<h1 style='color:green;'>Request post recevied</h1>")
        return redirect(student.show_url)

    return  render(request, 'students/create.html')

