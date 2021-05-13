# creating the package of models folder so that easy to import in different files
from django.db import models
from courses.models.courses import Courses, Tag, Learning, Prerequisite
from courses.models.video import Video