from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.template import RequestContext

from .models import DescriptionModel
from .forms import UploadFileForm
from .function import handle_uploaded_file

def upload_file(request):
    description = DescriptionModel.objects.first()
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            dict_final = handle_uploaded_file(request.FILES['docfile'])
            dict_final.update({'description': description})
            return render_to_response('success.html', dict_final)
    else:
        form = UploadFileForm()
    return render_to_response(
        'home.html', {'form': form, 'description': description}, context_instance=RequestContext(request)
        )
