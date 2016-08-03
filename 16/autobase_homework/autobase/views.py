from django.shortcuts import render, HttpResponseRedirect
from django.views.decorators.http import require_GET
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_protect

from .forms import CreateAuto, CreateManufacturer
from .models import Manufacturer, Auto


def index(request):
    return render(request, 'models.html')


@require_GET
def auto(request):
    all_auto = Auto.objects.all()
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

    return render(request, 'objects_auto.html', {'all_auto': all_auto})


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
