from django.shortcuts import render
from .models import MeigennModel
from django.views.generic import ListView, DetailView, DeleteView, CreateView, UpdateView
from django.urls import reverse_lazy
from django.shortcuts import redirect



class Listfunc(ListView):
    template_name = 'list.html'
    model = MeigennModel

class Detailfunc(DetailView):
    template_name = 'detail.html'
    model = MeigennModel

class Deletefunc(DeleteView):
    template_name = 'delete.html'
    model = MeigennModel
    success_url = reverse_lazy('list')

class Createfunc(CreateView):
    template_name = 'create.html'
    model = MeigennModel
    fields = ('title', 'name', 'age', 'memo')
    success_url = reverse_lazy('list')


class Updatefunc(UpdateView):
    template_name = 'update.html'
    model = MeigennModel
    fields = ('title', 'name', 'age', 'memo')
    success_url = reverse_lazy('list')


