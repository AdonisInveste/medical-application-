from django.conf.urls import url
from data.views import IdentityList, IdentityCreate, IdentitySpecific, ConsultationCreate, MultiStep
from data.forms import  SymptomForm, DiseaseForm, IdentityForm

urlpatterns = [
        url(r'^patient/$', IdentityList.as_view(),  name = 'data_patient_list'),


        # url(r'^patient/create/$', patient_create, name = 'data_patient_create'),


         # url patterns representing the multi-step modelform creation
                # url(r'^patient/create$', MultiStep.as_view([IdentityForm, SymptomForm, DiseaseForm]),  name = 'data_patient_create'),
        url(r'^patient/create$', ConsultationCreate.as_view([IdentityForm, SymptomForm, DiseaseForm]),  name = 'data_patient_create'),


        # url(r'^patient/create/$', IdentityCreate.as_view(), name = 'data_patient_create'),
        # url(r'^patient/(?P<pk>[\w\-]+)/$', patient_detail, name = 'data_patient_detail'),
        url(r'^patient/(?P<pk>[\w\-]+)/$', IdentitySpecific.as_view(), name = 'data_patient_detail'),
]
