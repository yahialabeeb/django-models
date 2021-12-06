from django.views.generic import ListView, DetailView
from .models import Snack


class SnacksListView(ListView):
    template_name = "home.html"
    model = Snack


class SnacksDetailView(DetailView):
    template_name = "snack_detail.html"
    model = Snack

