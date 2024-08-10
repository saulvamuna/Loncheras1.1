from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.shortcuts import get_object_or_404
from django.contrib.auth import login, authenticate
from .models import Roles, Users, Restaurants, Products, Diets, Students, Recognition
from django.http import HttpResponse

from django.core.files.storage import FileSystemStorage
from django.db import connection
from django.contrib import messages

# Create your views here.
def home(request):
    return render(request, 'home.html')

def login(request):
    if request.method == 'GET':
        return render(request, 'auth/login.html')
    else:
        user = authenticate(request, userName=request.POST['userName'], password=request.POST['userPassword'])
        if user is None:
            return HttpResponse('no es usuario')
        else:
            login(request, user)
            return redirect('students')

# def register(request):
#     if request.method == 'GET':
#         return render(request, 'auth/register.html')
#     else:
#         rol_acudiente = get_object_or_404(Roles, roleName="Acudiente")
#         try:
#             Users.objects.create(
#                 document=request.POST['document'],
#                 firstName=request.POST['firstName'],
#                 lastName=request.POST['lastName'],
#                 email=request.POST['email'],
#                 userName=request.POST['userName'],
#                 password=request.POST['userPassword'],
#                 rol= rol_acudiente,
#             )
#             return redirect('login')
#         except IntegrityError:
#             return HttpResponse('error')

def register(request):
    if request.method == "POST":
        if (request.POST.get("document") and request.POST.get("firstName") and request.POST.get("lastName") and request.POST.get("email")
            and request.POST.get("userName") and request.POST.get("userPassword") and request.FILES["userPhoto"] and request.POST.get("userRol")):
            
            User = Users()
            User.document = request.POST.get("document")
            User.firstName = request.POST.get("firstName")
            User.lastName = request.POST.get("lastName")
            User.email = request.POST.get("email")
            User.userName = request.POST.get("userName")
            User.password = request.POST.get("password")
            User.userPhoto = request.FILES["userPhoto"]
            User.rol = request.POST.get("userRol")
            
            image = FileSystemStorage()
            image.save(User.userPhoto.name, User.userPhoto)
            insertar = connection.cursor()
            insertar.execute(
                "call Registrarse('"
                + User.document
                + "','"
                + User.firstName
                + "','"
                + User.lastName
                + "','"
                + User.email
                + "','"
                + User.userName
                + "','"
                + User.password
                + "','"
                + User.userPhoto.name
                + "','"
                + User.rol
                + "')"
            )
        messages.success(
            request, "El usuario: " + User.userName + " fue guardado con exito "
        )
        return render(request, "auth/login.html")
    else:
        return render(request, "auth/register.html")

def students(request):
    students = Students.objects.all()
    return render(request, 'students.html', {"students": students})

def registerStudent(request):
    if request.method == "POST":
        if (request.POST.get("typeDocument") and request.POST.get("document") and request.POST.get("firstName") and request.POST.get("lastName")
            and request.POST.get("birthDate") and request.POST.get("course") and request.FILES["userPhoto"] and request.POST.get("accompanyingDocument")):
            
            student = Students()
            student.typeDocument = request.POST.get("typeDocument")
            student.document = request.POST.get("document")
            student.firstName = request.POST.get("firstName")
            student.lastName = request.POST.get("lastName")
            student.birthDate = request.POST.get("birthDate")
            student.course = request.POST.get("course")
            student.status = "activo"
            student.diet = request.POST.get("diet")
            student.user = request.POST.get("accompanyingDocument")
            student.userPhoto = request.FILES["userPhoto"]
            
            image = FileSystemStorage()
            image.save(student.userPhoto.name, student.userPhoto)
            insertar = connection.cursor()
            insertar.execute(
                "call Registrarse('"
                + student.typeDocument
                + "','"
                + student.document
                + "','"
                + student.firstName
                + "','"
                + student.lastName
                + "','"
                + student.birthDate
                + "','"
                + student.course
                + "','"
                + student.user
                + "','"
                + student.diet
                + "','"
                + student.userPhoto.name
                + "')"
            )
        messages.success(
            request, "El estudiante: " + student.firstName + " fue guardado con exito "
        )
        return render(request, "students.html")
    else:
        return render(request, "registerStudent.html")

def profile(request):
    return render(request, 'profile.html')