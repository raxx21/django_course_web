from django.db import models

#  Courses model to add the courses available at the website
class Courses(models.Model):
    name = models.CharField(max_length= 30, null=False)
    description = models.CharField(max_length= 200, null=True)
    price = models.IntegerField(null=False)
    discount = models.IntegerField(null=False,default=0)
    active = models.BooleanField(default=False) # Is the courses is active to watch or not
    thumbnail = models.ImageField(upload_to= "files/thumbnail")
    date = models.DateTimeField(auto_now_add=True)
    resource = models.FileField(upload_to="files/resource")
    length = models.IntegerField(default=False)

    # To display the name of the course in the admin
    def __str__(self):
        return self.name

# Creating the base structure of the model so we can use in different models of the same structure
class CourseProperty(models.Model):
    description = models.CharField(max_length=100,null=False)
    course = models.ForeignKey(Courses, null=False,on_delete=models.CASCADE)
    # Not to create a models of this class bcz its only the structure
    class Meta:
        abstract = True

# By passing the class name of the structure we can access the fields of the structure of the class
class Tag(CourseProperty):
    pass

class Prerequisite(CourseProperty):
    pass

class Learning(CourseProperty):
    pass

