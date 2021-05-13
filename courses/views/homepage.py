from django.shortcuts import HttpResponse, render
from courses.models import Courses
def home(request):
    courses = Courses.objects.all()
    context = {
        "courses" : courses
    }
    return render(request, template_name="courses/home.html",context=context)