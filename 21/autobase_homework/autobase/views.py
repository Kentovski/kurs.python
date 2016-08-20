from django.shortcuts import render, HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_protect
from rest_framework import viewsets

from .forms import CreateAuto, CreateManufacturer, CreateBuyer, CreateOrders
from .models import Manufacturer, Auto, Warehouse, Buyer, Orders
from .serializers import (AutoSerializer, ManufacturerSerializer, 
                                        WarehouseSerializer, OrdersSerializer, BuyerSerializer)


def index(request):
    return render(request, 'models.html')


@require_GET
def auto(request):
    all_auto = Auto.objects.all()
    warehouse = Warehouse.objects.all()
    if 'searchby' in request.GET:
        searchby = request.GET.get('searchby', '')
        text = request.GET.get('text', '')
        if searchby in ['name', 'manufacturer', 'body', 'year']:
            if searchby == 'manufacturer':
                query = {"manufacturer__brand__icontains": text}
            else:
                query = {("%s__icontains" % searchby): text}
            all_auto = Auto.objects.filter(**query)
    if 'sortby' in request.GET:
        sortby = request.GET.get('sortby', '')
        text = request.GET.get('text', '')
        if sortby in ['name', '-name', 'manufacturer', '-manufacturer', 'body', '-body', 'year', '-year']:
            all_auto = Auto.objects.order_by(sortby)
    if 'id' in request.GET:
        id = request.GET.get('id', 0)
        auto = get_object_or_404(Auto, pk=id)
        return render(request, 'object_page_auto.html', {'auto': auto})
    if 'delete' in request.GET:
        delete = request.GET.get('delete', 0)
        result = Auto.objects.filter(pk=delete).delete()
        return render(request, 'objects_auto.html', {'all_auto': all_auto, 'result': result })

    return render(request, 'objects_auto.html', {'all_auto': all_auto, 'warehouse': warehouse})


@csrf_protect
def auto_create(request):
    if request.method == 'POST':
        form = CreateAuto(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('./')
        else:
            return render(request, 'create_object.html', {'form': form})
    return render(request, 'create_object.html', {'form': CreateAuto()})


@csrf_protect
def auto_edit(request):
    if 'id' in request.GET:
        id = request.GET.get('id', 0)
        auto = get_object_or_404(Auto, pk=id)
        init_dict = auto.__dict__
        m = init_dict.get('manufacturer_id')
        init_dict.update({'manufacturer': m})

    else:
        return HttpResponseRedirect('.')
    if request.method == 'POST':
        form = CreateAuto(request.POST, instance=auto)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('./')
        else:
            return render(request, 'create_object.html', {'form': form})
    return render(request, 'create_object.html', {'form': CreateAuto(initial=init_dict)})


@require_GET
def manufacturer(request):
    all_manufacturers = Manufacturer.objects.all()
    if 'searchby' in request.GET:
        searchby = request.GET.get('searchby', '')
        text = request.GET.get('text', '')
        if searchby == 'brand':
            all_manufacturers = Manufacturer.objects.filter(brand__icontains=text)
        if searchby == 'country':
            all_manufacturers = Manufacturer.objects.filter(country__icontains=text)
    if 'sortby' in request.GET:
        sortby = request.GET.get('sortby', '')
        text = request.GET.get('text', '')
        if sortby in ['brand', '-brand', 'country', '-country']:
            all_manufacturers = Manufacturer.objects.order_by(sortby)
    if 'id' in request.GET:
        id = request.GET.get('id', 0)
        manufacturer = get_object_or_404(Manufacturer, pk=id)
        return render(request, 'object_page_man.html', {'manufacturer': manufacturer})
    if 'delete' in request.GET:
        delete = request.GET.get('delete', 0)
        result = Manufacturer.objects.filter(pk=delete).delete()
        return render(request, 'objects_man.html', {'all_manufacturers': all_manufacturers, 'result': result })

    return render(request, 'objects_man.html', {'all_manufacturers': all_manufacturers})


@csrf_protect
def manufacturer_create(request):
    if request.method == 'POST':
        form = CreateManufacturer(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('./')
        else:
            return render(request, 'create_object.html', {'form': form})
    return render(request, 'create_object.html', {'form': CreateManufacturer()})


@csrf_protect
def manufacturer_edit(request):
    if 'id' in request.GET:
        id = request.GET.get('id', 0)
        manufacturer = get_object_or_404(Manufacturer, pk=id)
    else:
        return HttpResponseRedirect('.')
    if request.method == 'POST':
        form = CreateManufacturer(request.POST, instance=manufacturer)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('./')
        else:
            return render(request, 'create_object.html', {'form': form})
    return render(request, 'create_object.html', {'form': CreateManufacturer(initial=manufacturer.__dict__)})


@csrf_protect
def shopping_cart(request):
    warehouse = Warehouse.objects.all()
    goods = Auto.objects.all()
    cookies = []
    autos = []
    for c in request.COOKIES:
        if c.startswith('auto_') and request.COOKIES.get(c) != 'undefined':
            cookies.append(request.COOKIES.get(c))
    for item in goods:
        if str(item.id) in cookies:
            autos.append(item)
    if request.method == 'POST':
        buyer_form = CreateBuyer(request.POST)
        if buyer_form.is_valid():
            buyer = buyer_form.save()
        else:
            return render(request, 'shopping_cart.html', {'autos': autos, 'warehouse': warehouse, 'form': buyer_form})
        for i in request.POST:
            if i.startswith('quantity_'):
                goods = i.split('_')[1]
                amount = request.POST.get(i)
                order_form = CreateOrders({'goods': goods, 'amount': amount, 'buyer': buyer.id})
                if order_form.is_valid():
                    order_form.save()
        return render(request, 'thanks.html')
    return render(request, 'shopping_cart.html', {'autos': autos, 'warehouse': warehouse, 'form': CreateBuyer()})


class AutoViewSet(viewsets.ModelViewSet):
    queryset = Auto.objects.all()
    serializer_class = AutoSerializer


class ManufacturerViewSet(viewsets.ModelViewSet):
    queryset = Manufacturer.objects.all()
    serializer_class = ManufacturerSerializer


class WarehouseViewSet(viewsets.ModelViewSet):
    queryset = Warehouse.objects.all()
    serializer_class = WarehouseSerializer


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Orders.objects.all()
    serializer_class = OrdersSerializer


class BuyerViewSet(viewsets.ModelViewSet):
    queryset = Buyer.objects.all()
    serializer_class = BuyerSerializer
