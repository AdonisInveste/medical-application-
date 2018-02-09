from django.db import models
from django.utils import timezone
from django.shortcuts import reverse

import datetime

class Patient(models.Model):

    NIS =models.CharField(max_length = 200, primary_key = True)
    timestamp = models.DateTimeField(auto_now = True)
    first_name = models.CharField(max_length = 80, null = True)
    last_name = models.CharField(max_length = 80, null = True )
    contact = models.CharField(max_length = 15, null = True)
    location  = models.CharField(max_length = 100, blank = True)
    email_address = models.EmailField()

    CHOOSE = 'The patient is'
    MALE = 'M'
    FEMALE = 'F'
    personGender = ((CHOOSE,'The patient is'),(MALE, 'Male'),(FEMALE,'Female'),)
    gender = models.CharField(max_length=2,choices=personGender,default=CHOOSE)

    born = models.DateField(auto_now = False, auto_now_add = False, blank = True, null = True)




    def __str__(self):
        return '%s, %s' % ( self.first_name ,self.last_name)

    class Meta:
        ordering = ['last_name']


class Symptom(models.Model):

    identity = models.CharField('Name of symptom', max_length = 80, default = '')
    description = models.TextField(max_length = 1000, default = '')
    patient = models.ManyToManyField(Patient,  through = 'Consultation')

    def __str__(self):
        return '%s' % ( self.identity )

class Disease(models.Model):

    identity = models.CharField('Name of disease', max_length = 80, default = '')
    description = models.TextField(max_length = 5000, default = '')
    symptom = models.ManyToManyField(Symptom)

    def __str__(self):
        return '%s' % ( self.identity )

class Treatment(models.Model):

    identity = models.CharField('Name of treatment', max_length = 80, default = '' )
    disease = models.ManyToManyField(Disease, through = 'Consultation')
    description = description = models.TextField(max_length = 5000, default = '')


    def __str__(self):
        return '%s' % ( self.identity )


# Consultation model is the intermediate model
class Consultation(models.Model):


    patient_identity = models.ForeignKey(Patient)
    patient_condition = models.ForeignKey(Symptom)
    patient_disease = models.ForeignKey(Disease)
    patient_treatment = models.ForeignKey(Treatment)
    consultation_date_and_time = models.DateTimeField('visitation date and time', auto_now = False, auto_now_add = False, blank = True, null = True)

    # Use get_absolute_url to access single page model objects that possess a Canonical Uniform resource locator
    def get_absolute_url(self):
        return reverse('data_patient_detail', kwargs={'pk':self.pk})


"""
 Get all symptoms who patient_key has a first name that begins with 'Issa'
Unusual_state.objects.filter(patient_key__first_name__startswith = 'Issa')

Find all the patients with the Test Sickness, Test Heath condition
that consulted the doctor on 12-03-2017.

Identity.objects.filter(unusual_state__nomenclature = 'Test Sickness, Test Health',
consultation___date_seen = '2017-03-12' )
"""
