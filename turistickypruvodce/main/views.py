from django.shortcuts import render
from main.models import Sight, Categorie

def get_homepage(request):
    # SELECT *from.Sights LIMIT 10
    sights = Sight.objects.all().order_by('name')

    search = request.GET.get('search')
    if search:
        sights = sights.filter(name__icontains=search) | sights.filter(description__icontains=search)

    # filter by category if query parameter category is present
    categorie = request.GET.get('categorie')
    if categorie:
        sights = sights.filter(categories__name=categorie)
    
    context = {
        "sights": sights,
        "categories": Categorie.objects.all().order_by('name'),
        "categorie": categorie,
    }

    return render(
        request, "main/homepage.html", context
    )
