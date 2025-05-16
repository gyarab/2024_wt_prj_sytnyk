from django.shortcuts import render
from main.models import Sight, Categorie
#from faker import Faker

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
    }

    #def random_person(request):
     #   context = {
        # use faker to generate random data
     #   "name": Faker().name(),
     #   "email": Faker().email(),
     #   "phone": Faker().phone_number(),
    #}

    return render(
        request, "main/random.html", context
    )
