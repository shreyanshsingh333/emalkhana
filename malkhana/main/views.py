from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import TemplateView, View
from .forms import *
from django.views.generic import (
    CreateView,
    DeleteView,
    UpdateView,
    ListView,
    DetailView,
)


# Create your views here.
class HomePageView(TemplateView):
    template_name = 'index.html'


class AddVivechak(View):
    form_class = VivechakForm
    template_name = 'vivechak.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            vivechak = form.save(commit=False)

            # cleaned(normalized) data
            name = form.cleaned_data['name']
            address = form.cleaned_data['address']
            mobile = form.cleaned_data['mobile']
            adhar = form.cleaned_data['adharcard']
            pan = form.cleaned_data['pancard']

            # save cleaned data to form
            vivechak.name = name
            vivechak.mobile = mobile
            vivechak.address = address
            vivechak.adharcard = adhar
            vivechak.pancard = pan

            vivechak.save()

            if vivechak is not None:
                context = {
                    'form': VivechakForm,
                }
                if 'save' in request.POST:
                    return render(request, 'index.html', context)
                elif 'addanother' in request.POST:
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


class VivechakList(ListView):
    template_name = 'vivechaklist.html'
    queryset = Vivechak.objects.all()


def editvivechak(request, pk):
    item = get_object_or_404(Vivechak, pk=pk)

    if request.method == "POST":
        form = VivechakForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('vivechaklist')
    else:
        form = VivechakForm(instance=item)
        return render(request, 'editvivechak.html', {'form': form})


def deletevivechak(request, pk):
    item = get_object_or_404(Vivechak, pk=pk)
    item.delete()

    return redirect('vivechaklist')


class AddReport(View):
    form_class = ReportForm
    template_name = 'Report.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            report = form.save(commit=False)

            # cleaned(normalized) data


            # save cleaned data to form


            report.save()

            if report is not None:
                context = {
                    'form': ReportForm,
                }
                return render(request, 'index.html', context)
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


class ReportList(ListView):
    template_name = 'Reportlist.html'
    queryset = Report.objects.all()


class AddStock(View):
    form_class = StockInForm
    template_name = 'Stockin.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            report = form.save(commit=False)

            # cleaned(normalized) data

            # save cleaned data to form

            report.save()

            if report is not None:
                context = {
                    'form': ReportForm,
                }
                return render(request, 'index.html', context)
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


class RemoveStock(View):
    form_class = StockOutForm
    template_name = 'Stockout.html'

    # display blank form
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    # process form data
    def post(self, request):
        form = self.form_class(request.POST)

        if form.is_valid():
            report = form.save(commit=False)

            # cleaned(normalized) data

            # save cleaned data to form

            report.save()

            if report is not None:
                context = {
                    'form': ReportForm,
                }
                return render(request, 'index.html', context)
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


class StockInList(ListView):
    template_name = 'Stockinlist.html'
    queryset = StockIn.objects.all()


class StockOutList(ListView):
    template_name = 'Stockoutlist.html'
    queryset = StockOut.objects.all()
