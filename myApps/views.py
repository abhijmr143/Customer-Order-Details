from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import CustomerOrderDetails
from .forms import CustomerOrderDetailsForm
from . import utils
# Create your views here.


def list_view(request):
    data = CustomerOrderDetails.objects.all()
    context = {
        'data': data
    }
    return render(request, 'myApps/list.html', context=context)

def create_list(request):
    form = CustomerOrderDetailsForm()
    if request.method == 'POST':
        form = CustomerOrderDetailsForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    context = {
        'form': form,
    }
    return render(request, 'myApps/create.html', context=context)

def update_list(request, pk):
    obj = CustomerOrderDetails.objects.get(pk=pk)
    form = CustomerOrderDetailsForm(instance=obj)
    if request.method == 'POST':
        form = CustomerOrderDetailsForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    context = {
        'form': form,
    }
    return render(request, 'myApps/update.html', context=context)

def delete_list(request, pk):
    obj = CustomerOrderDetails.objects.get(pk=pk)
    obj.delete()
    return HttpResponseRedirect('/')

def visualization_view(request):
    obj = CustomerOrderDetails.objects.all()
    x = [x.order_sales for x in obj]
    y = [y.order_units for y in obj]
    chart = utils.get_plot(x, y)
    context = {
        'chart': chart,
    }
    return render(request, 'myApps/visualize.html', context=context)