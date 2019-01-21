from django.shortcuts import render
from .forms import *
from django.views.generic import TemplateView, View

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
