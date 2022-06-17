
import os
from django.http.response import Http404
from django.shortcuts import render
from .models import FileAdmin
from django.http import HttpResponse
from .models import FileAdmin
from django.conf import settings
from .filters import FileFilter


def home(request):
    file = FileAdmin.objects.all()
    myFilter = FileFilter(request.GET, queryset=file)
    file = myFilter.qs
    context = {'file': file, 'myFilter': myFilter}
    return render(request, 'downloads/home.html', context)


def download(request, path):
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path):
        with open(file_path, 'rb') as fh:
            response = HttpResponse(
                fh.read(), content_type="application/adminUpload")
            response['Content-Disposition'] = 'inline;filename=' + \
                os.path.basename(file_path)
            return response
    raise Http404
