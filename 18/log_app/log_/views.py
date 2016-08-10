from django.contrib.auth import authenticate
from django.http import HttpResponse, HttpResponseForbidden, HttpResponseBadRequest
from .models import Log
from django.forms import ModelForm
from django.views.decorators.csrf import csrf_exempt


class LogForm(ModelForm):
    class Meta:
        model = Log
        fields = ['time', 'level', 'message']


@csrf_exempt
def logger_view(request):
    username = request.POST.get('username', '')
    password = request.POST.get('password', '')
    user = authenticate(username=username, password=password)
    if user is not None:
        if user.is_active:
            log_form = LogForm(request.POST)
            if log_form.is_valid():
                before_save_to_db = log_form.save(commit=False)
                before_save_to_db.sender = user
                before_save_to_db.save()
                return HttpResponse()
            else:
                return HttpResponseBadRequest(content=log_form.errors)

        else:
            return HttpResponseForbidden('Your account has been disabled')
    else:
        return HttpResponse(status=401, content='Authorization needed')
