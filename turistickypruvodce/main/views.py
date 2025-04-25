from django.shortcuts import render
from main.models import Sight

def get_homepage(request):
    context = {
        "svatek": "nika",
        # SELECT *from.Sights LIMIT 10
        "sights": Sight.objects.all().order_by('name')[:10]
    } 
    return render(
        request, "main/homepage.html", context
    )
