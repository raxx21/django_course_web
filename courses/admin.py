from django.contrib import admin
from courses.models import Courses, Tag, Learning, Prerequisite, Video
# Register your models here.

#  Creating the table formate to add all the fields in courses to make it easy
class TagAdmin(admin.TabularInline):
    model = Tag

class LearningAdmin(admin.TabularInline):
    model = Learning

class PrerequisiteAdmin(admin.TabularInline):
    model = Prerequisite

class VideoAdmin(admin.TabularInline):
    model = Video

#  Adding all the Tables in one model Courses
class CoursesAdmin(admin.ModelAdmin):
    inlines = [
        TagAdmin,
        LearningAdmin,
        PrerequisiteAdmin,
        VideoAdmin
    ]

# registering the models to see in the admin section
admin.site.register(Courses,CoursesAdmin)
admin.site.register(Video)

