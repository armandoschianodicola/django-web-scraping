from django.shortcuts import render
from .forms import InputForm
from .models import Item
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView
from django.shortcuts import get_object_or_404


class MarkersMapView(TemplateView):
    template_name = "map.html"
    form_class = InputForm


def ticket_system_view(request):

    if request.method == 'POST':
        print('ok')

    else:
        print('get')

    return render(request, 'map.html')


    # def get_context_data(self, *, object_list=None, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #
    #     return context
    #
    # def form_valid(self, form):
    #     # form.instance.author = self.request.user
    #     print('ok')
    #
    #     return super(MarkersMapView, self).form_valid(form)
