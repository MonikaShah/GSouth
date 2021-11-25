from django.shortcuts import render
from django.core.serializers import serialize
from .models import GsouthBuildingPolygons

# Create your views here.
# def Map(request):
#     return render(request, "map/map.html")

def Map(req):
   #  obj = Ward61OsmBuildings.objects.all()
    obj=GsouthBuildingPolygons.objects.all()
    
    geojson=serialize('geojson',obj)
    context = {'geojson':geojson}
    return render(req,"map/map.html",context)