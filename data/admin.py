from django.contrib import admin
from . models import Patient, Symptom, Consultation, Disease, Treatment


class MedicalInline(admin.TabularInline):

    model = Consultation
    extra = 0

@admin.register(Patient)

class IdentityManage(admin.ModelAdmin):

    list_display = ('NIS', 'first_name', 'last_name', 'contact', 'email_address', 'location', 'born' )

    inlines = [MedicalInline]



class IdentityInline(admin.TabularInline):

    model = Consultation
    extra = 0

@admin.register(Symptom)

class MedicalManage(admin.ModelAdmin):

    list_display = ('id','identity', 'description')

    inlines = [IdentityInline]


@admin.register(Consultation)

class ConsultationManage(admin.ModelAdmin):

    list_display = ('patient_identity',)


@admin.register(Disease)

class DiseaseManage(admin.ModelAdmin):

    list_display = ('identity','description')

@admin.register(Treatment)

class TreatmentManage(admin.ModelAdmin):

    list_display = ('identity','description', )
    inlines = [IdentityInline]
