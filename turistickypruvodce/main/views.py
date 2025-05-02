from django.shortcuts import render
from main.models import Sight

def get_homepage(request):
        # SELECT *from.Sights LIMIT 10
        "sight": Sight.objects.all().order_by('name')
    
    return render(
        request, "main/homepage.html", context
    )

    if request.GET.get("search"):
        sights = sights.filter(name__icontant=request.GET.get("search"))

    context = {
        "sights": sights,
    }

    return render(
        request, "main/homepage.html", context
    )
