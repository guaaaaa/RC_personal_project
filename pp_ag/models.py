from django.db import models
from django.urls import reverse
from .validators import validate_audio_size, validate_video_size


# Create your models here.

class User(models.Model):
    email = models.EmailField(blank=True)
    
    def __str__(self):
        return self.email

class Case(models.Model):
    project_name = models.CharField(max_length=256, blank=False)
    description = models.TextField(blank=False)
    goal = models.TextField(blank=False, null=True)
    cover_image = models.ImageField(null=True, blank=False, upload_to='covers')
    height_field=models.IntegerField(default=0)
    width_field=models.IntegerField(default=0)
    
    image1 = models.ImageField(null=True, blank=True, height_field='height_field', width_field='width_field', upload_to = 'pictures/')

    image2 = models.ImageField(null=True, blank=True, height_field='height_field', width_field='width_field', upload_to = 'pictures/')

    image3 = models.ImageField(null=True, blank=True, height_field='height_field', width_field='width_field', upload_to = 'pictures/')

    image4 = models.ImageField(null=True, blank=True, height_field='height_field', width_field='width_field', upload_to = 'pictures/')
    
    audio = models.FileField(blank=True, upload_to='audio', validators=[validate_audio_size])
    video = models.FileField(blank=True, upload_to='video', validators=[validate_video_size])
    document = models.FileField(blank=True, upload_to='document')

    def __str__(self):
        return self.project_name
    
    def get_absolute_url(self):
        return reverse("ag:case_detail", kwargs={"pk": self.pk})
