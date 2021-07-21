from django.shortcuts import render
from .models import Expirement


def index(request):
    table_experiment = Expirement.objects.all()
    return render(request, 'DB/homepage.html',{'table_experiment':table_experiment})
