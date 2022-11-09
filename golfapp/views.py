from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView
from .models import Golfclub

# Create your views here.
class ClubListView(ListView):
    model = Golfclub
    template_name = 'club_list.html'
    context_object_name = 'all_clubs_list'

class ClubDetailView(DetailView):
    model = Golfclub
    template_name = 'club_detail.html'

class ClubCreateView(CreateView):
    model = Golfclub
    template_name = 'club_create.html'
    fields = ['name', 'location']

class ClubUpdateView(UpdateView):
    model = Golfclub
    template_name = 'club_edit.html'
    fields = ['name']

class ClubTListView(ListView):
    model = Golfclub
    template_name = 't_list.html'
    context_object_name = 'all_clubs_list'