from django.db import models
import datetime
import os


class Doctor(models.Model):
    doctor_id = models.BigAutoField(primary_key=True)
    doctor_name = models.CharField(max_length=50, blank=True, null=True)
    specialization = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'doctor'


class Patient(models.Model):
    patient_id = models.BigAutoField(primary_key=True)
    patient_pesel = models.CharField(max_length=50, blank=True, null=True)
    patient_name = models.CharField(max_length=50, blank=True, null=True)
    age = models.IntegerField(blank=True, null=True)
    gender = models.CharField(max_length=4, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'patient'

def get_filename(instance,filename):
    old_name = filename
    current_time = datetime.datetime.now().strftime('%Y%m%d%H;%M:%S')
    filename = "%s%s" % (current_time,old_name)
    return os.path.join('uploads/',filename)



class Study(models.Model):
    study_id = models.BigAutoField(primary_key=True)
    hospital = models.CharField(max_length=64, blank=True, null=True)
    study_date = models.DateField(blank=True, null=True)
    study_time = models.CharField(max_length=64, blank=True, null=True)
    modality = models.CharField(max_length=10, blank=True, null=True)
    note = models.CharField(max_length=500, blank=True, null=True)
    pathfile = models.CharField(db_column='pathFile', max_length=100, blank=True, null=True)
    patient = models.ForeignKey(Patient, models.DO_NOTHING, blank=True, null=True)
    doctor = models.ForeignKey(Doctor, models.DO_NOTHING, blank=True, null=True)
    image = models.ImageField(upload_to=get_filename, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'study'
        
class ChangesHistory(models.Model):
    his_change_id = models.BigAutoField(primary_key=True)
    his_study_id = models.IntegerField(blank=True, null=True)
    his_hospital = models.CharField(max_length=64, blank=True, null=True)
    his_study_date = models.DateField(blank=True, null=True)
    his_study_time = models.CharField(max_length=64, blank=True, null=True)
    his_modality = models.CharField(max_length=10, blank=True, null=True)
    his_note = models.CharField(max_length=500, blank=True, null=True)
    his_pathfile = models.CharField(db_column='pathFile', max_length=100, blank=True, null=True)
    his_patient = models.ForeignKey(Patient, models.DO_NOTHING, blank=True, null=True)
    his_doctor = models.ForeignKey(Doctor, models.DO_NOTHING, blank=True, null=True)
    his_image = models.CharField(db_column='pathToFile', max_length=500, blank=True, null=True)
    his_change_date = models.DateTimeField('date_published', auto_now=True)


    class Meta:
        managed = True
        db_table = 'changesHistory'
