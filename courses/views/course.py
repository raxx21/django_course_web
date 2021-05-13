from django.shortcuts import HttpResponse, render
from courses.models import Courses

def coursePage(request):
    context = {
    }
    return render(request, template_name="courses/home.html",context=context)