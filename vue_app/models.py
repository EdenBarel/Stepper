from django.db import models

class MyFiles(models.Model):
    my_image = models.ImageField(null='true', blank='true', upload_to='images/')
