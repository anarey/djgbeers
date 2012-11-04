# Create your views here.
from django.shortcuts import render_to_response
from django.template import RequestContext

from .forms import GbeersForm


def gbeers(request):
    data = None
    if request.method == 'POST':
        data = request.POST
    form = GbeersForm(data=data)
    if form.is_valid():
        form.save()
        messages.add_message(request, messages.SUCCESS, 
                             'Cambios guardados correctamente')
    return render_to_response('gbeers.html', {'form': form},
                              context_instance=RequestContext(request))
