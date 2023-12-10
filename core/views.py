from django.shortcuts import render, redirect, HttpResponse
from django.views import View
from core.models import Brands, Clients
from core.forms import BrandEditForm, BrandAddForm, ClientEditForm, ClientAddForm
class HomeView(View):
    def get(self, request):
        return render(request, 'core/homepage.html')

def about(request):
        return HttpResponse('Найдите свой брэнд красоты и здоровья!')

def create_brand(request):
    context = {}

    if request.method == "POST":
        brand_form = BrandAddForm(request.POST)
        if brand_form.is_valid():
            brand_form.save()
            return HttpResponse("Готово!")

    brand_form = BrandAddForm()
    context["form"] = brand_form
    return render(request, 'brand/create_brand.html', context)

class BrandsView(View):
    def get(self, request):
        brands = Brands.objects.all()
        return render(request, 'brand/brands_list.html', {'brands': brands})

def brand_detail(request, pk):
    brand_object = Brands.objects.get(pk=pk)
    return render(
        request,
        'brand/brand_detail.html',
        {'brand_object': brand_object}
    )

def brand_edit(request, pk):
    brand_object = Brands.objects.get(pk=pk)

    if request.method == "GET":
        form = BrandEditForm(instance=brand_object)
        return render(request, "brand/brand_edit.html", {"form": form})

    elif request.method == "POST":
        form = BrandEditForm(data=request.POST, instance=brand_object)
        if form.is_valid():
            object = form.save()
            return redirect(brand_detail, pk=object.pk)
        else:
            return HttpResponse("Форма не валидна")


def create_client(request):
    context = {}

    if request.method == "POST":
        client_form = ClientAddForm(request.POST)
        if client_form.is_valid():
            client_form.save()
            return HttpResponse("Готово!")

    client_form = ClientAddForm()
    context["form"] = client_form
    return render(request, 'client/create_client.html', context)


class ClientsView(View):
    def get(self, request):
        clients = Clients.objects.all()
        return render(request, 'client/clients_list.html', {'clients': clients})


def client_detail(request, pk):
    client_object = Clients.objects.get(pk=pk)
    return render(
        request,
        'client/client_detail.html',
        {'client_object': client_object}
    )

def client_edit(request, pk):
    client_object = Clients.objects.get(pk=pk)

    if request.method == "GET":
        form = ClientEditForm(instance=client_object)
        return render(request, "client/client_edit.html", {"form": form})

    elif request.method == "POST":
        form = ClientEditForm(data=request.POST, instance=client_object)
        if form.is_valid():
            object = form.save()
            return redirect(client_detail, pk=object.pk)
        else:
            return HttpResponse("Форма не валидна")