from django.shortcuts import render
from .forms import *
from django.views.generic import TemplateView, View
from django.http import HttpResponse
from .resources import VivechakResource
from tablib import Dataset

# Create your views here.


class HomePageView(TemplateView):
    template_name = 'base.html'


class AddMaalView(View):
    template_name = 'AddMaal.html'
    form_class = AddMaalForm

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():

            maal = form.save()

            if maal is not None:
                context = {
                    'form': AddMaalForm,
                }
                return render(request, self.template_name, context)
            else:
                context = {
                    'form': form,
                    'error_message': 'something went wrong!',
                }
                return render(request, self.template_name, context)
        else:
            context = {
                'form': form,
                'error_message': 'Form validation failed!',
            }
            return render(request, self.template_name, context)


def export(request):
    vivechak_resource = VivechakResource()
    dataset = vivechak_resource.export()
    response = HttpResponse(dataset.xls, content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment; filename="vivechak.xls"'
    return response


def import_vivechak(request):
    if request.method == 'POST':
        vivechak_resource = VivechakResource()
        dataset = Dataset()
        new_vivechak = request.FILES['myfile']

        imorted_data = dataset.load(new_vivechak.read())
        result = vivechak_resource.import_data(dataset, dry_run=True)

        if not result.has_errors():
            vivechak_resource.import_data(dataset, dry_run=False)

    return render(request, 'vivechak_import.html')
