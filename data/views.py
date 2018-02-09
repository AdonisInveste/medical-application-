from data.models import Treatment, Symptom, Disease, Consultation, Patient
from django.shortcuts import get_object_or_404, render, redirect, render_to_response
from django.views.generic import View
from django.template import Template, Context, loader
from data.forms import IdentityForm
from formtools.wizard.views import SessionWizardView

import logging

logr = logging.getLogger(__name__)

def iivri(request):

    return render(request,'data/patient_list.html', {'patient_list':Patient.objects.all()})



# Class based view for patient list

class IdentityList(View):
    template_ = 'data/patient_list.html'
    def get(self, request):
        patient_list = Consultation.objects.all()
        return render(request, self.template_, {'patient_list':patient_list})

# Class based view for patient detail

class IdentitySpecific(View):
    model = Consultation
    template_ = 'data/patient_detail.html'
    def get(self, request, pk):
        patient_consult = Consultation.objects.filter(pk=pk)
        return render(request, self.template_, {'patient_consult':patient_consult})

# Function view for patient detail

# def patient_detail(request, pk):
#
#     patient_consult = Consultation.objects.filter(pk=pk)
#     template = loader.get_template('data/patient_detail.html')
#     context = {'patient_consult':patient_consult}
#
#     return render(request,'data/patient_detail.html', {'patient_consult':patient_consult})


# Class based view for patient creation

class IdentityCreate(View):
    # model form used to create patient object
    document_object = IdentityForm
    # Template object used to load and render the model form used to create the model object
    template_ = 'data/patient_form.html'

    def get(self, request):
        # output unbound document, instantiate unbound model form and render form to the template
        # if form keyword is changed to something else the form is not rendered. WHY?
        return render(request, self.template_, {'form':self.document_object()})

    def post(self, request):
        # instantiate bound form
        bound_document = self.document_object(request.POST)
        # if form is valid
        if bound_document.is_valid():
            # save form
            document_created = bound_document.save()
            # redirect to form's detail page
            return redirect(document_created)
        # if form is not valid, redisplay bound form with errors
        else:
            return render(request, self.template_, {'document':bound_document})


# Function view for patient creation

# def patient_create(request):
#     if request.method == 'POST':
#         form = IdentityForm(request.POST)
#
#
#         if form.is_valid():
#             patient_document = form.save()
#             return redirect(patient_document)
#         else:
#             return render(request,'data/patient_form.html', {'form':form})
#     else:
#         form = IdentityForm()
#
#     return render(request,'data/patient_form.html', {'form':form})


class MultiStep(SessionWizardView):
    template_ = 'data/multi_form.html'
    def done(self, form_list, **kwargs):
        form_data = process_form_data(form_list)

        return render_to_response('data/done.html', {'form_data':form_data})


def process_form_data(form_list):

    form_data = [form.cleaned_data for form in form_list]

    logr.debug(form_data[0]['NIS'])
    logr.debug(form_data[1]['identity'])
    logr.debug(form_data[2]['identity'])

    print(logr.debug(form_data[0]['NIS']))
    print(logr.debug(form_data[1]['identity']))
    print(logr.debug(form_data[2]['identity']))

    return form_data


class ConsultationCreate(SessionWizardView):
    instance = None

    def get_form_instance(self, step):
        if self.instance is None:
            self.instance = Patient
        return self.instance

    template_ = 'data/multi_form.html'

    def done(self, form_list, **kwargs):
        self.instance.save()


# def process_form_data(form_list):
#
#     form_data = [form.cleaned_data for form in form_list]
#
#     logr.debug(form_data[0]['NIS'])
#     logr.debug(form_data[1]['identity'])
#     logr.debug(form_data[2]['identity'])
#
#     return form_data
