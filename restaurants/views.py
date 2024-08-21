from django.shortcuts import render , get_object_or_404
from django.http import HttpResponse , HttpResponseRedirect
from django.views import View
import random
from django.db.models import Q
from django.views.generic import TemplateView , ListView , DetailView , CreateView , UpdateView
from django.template import loader
from .models import RestaurantLocation
from .forms import RestaurantCreateForm , RestaurantLocationCreateForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

class RestaurantListView(LoginRequiredMixin,ListView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner = self.request.user)


class RestaurantDetailView(LoginRequiredMixin,DetailView):
    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner=self.request.user)


class RestaurantCreateView(LoginRequiredMixin,CreateView):
    form_class = RestaurantLocationCreateForm
    login_url = '/login/'
    template_name = 'form.html'
    success_url = '/restaurants/'

    def form_valid(self,form):
            instance = form.save(commit=False)
            instance.owner = self.request.user
            #instance.save()
            return super(RestaurantCreateView,self).form_valid(form)

    def get_context_data(self, *args , **kwargs):
        context = super(RestaurantCreateView, self).get_context_data(*args,**kwargs)
        context['title'] = 'Add Restaurant'
        return context

class RestaurantUpdateView(LoginRequiredMixin,UpdateView):
    form_class = RestaurantLocationCreateForm
    login_url = '/login/'
    template_name = 'restaurants/detail-update.html'

    def get_context_data(self, *args , **kwargs):
        context = super(RestaurantUpdateView, self).get_context_data(*args,**kwargs)
        name = self.get_object().name
        context['title'] = f"Update Restaurant: {name}"
        return context

    def get_queryset(self):
        return RestaurantLocation.objects.filter(owner = self.request.user)