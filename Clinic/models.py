from django.db import models
import datetime
import os
# Create your models here.


def get_file_path(request, filename):
    original_filename = filename
    nowTime = datetime.datetime.now().strftime('%Y%m%d%H:%M:%S')
    filename = "%s%s" % (nowTime, original_filename)
    return os.path.join('uploads/', filename)


class Doctors(models.Model):
    DocId = models.TextField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    image = models.ImageField(upload_to=get_file_path, null=True, blank=True)
    description = models.TextField(max_length=500, null=False, blank=False)
    Slots = models.IntegerField(null=False, blank=False)
    status = models.BooleanField(
        default=False, help_text="0=default, 1=Hidden")
    trending = models.BooleanField(
        default=False, help_text="0=default, 1=Trending")
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.TextField(
        max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Patients(models.Model):
    doctors = models.ForeignKey(Doctors, on_delete=models.CASCADE)
    PatientId = models.TextField(max_length=50, null=False, blank=False)
    name = models.CharField(max_length=150, null=False, blank=False)
    patientimage = models.ImageField(
        upload_to=get_file_path, null=True, blank=True)
    small_description = models.CharField(
        max_length=250, null=False, blank=False)
    description = models.TextField(max_length=500, null=False, blank=False)
    Consulatation_fee = models.FloatField(null=False, blank=False)
    status = models.BooleanField(
        default=False, help_text="0=default, 1=Hidden")
    meta_title = models.CharField(max_length=150, null=False, blank=False)
    meta_keywords = models.CharField(max_length=150, null=False, blank=False)
    meta_description = models.TextField(
        max_length=500, null=False, blank=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
