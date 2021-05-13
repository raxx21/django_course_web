from django.db import models
from courses.models import Courses

# Video model to add the videos of the courses
class Video(models.Model):
    title = models.CharField(max_length=100,null=False)
    course = models.ForeignKey(Courses, null=False,on_delete=models.CASCADE)
    serial_number = models.IntegerField(null= False) # Unique id to the video 
    video_id = models.CharField(max_length=20,null=False) # the url of the video to be displayed
    is_preview = models.BooleanField(default=False) # Is video is available for preview before the payment

    # To display the name of the course in the admin
    def __str__(self):
        return self.title
