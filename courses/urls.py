
from freecourses.settings import MEDIA_ROOT, MEDIA_URL
from courses.views import home, coursePage
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from freecourses.settings import MEDIA_ROOT, MEDIA_URL

urlpatterns = [
    path('', home,name='home'),
    path('course/<slug:str>', coursePage,name='coursePage'),
]+ static(MEDIA_URL, document_root=MEDIA_ROOT)