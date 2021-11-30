# from django.db import models
from django.contrib.gis.db import models
from django.core.serializers import serialize
# from .models import GsouthBuildingPolygons

# Create your models
class GsouthBuildingPolygons(models.Model):
    geom = models.MultiPolygonField(blank=True, null=True)
    fid = models.DecimalField(max_digits=100, decimal_places=5, blank=True, null=True)
    osm_id = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)
    building_name = models.CharField(max_length=97, blank=True, null=True)
    building_category = models.CharField(max_length=80, blank=True, null=True)
    ward = models.CharField(max_length=60, blank=True, null=True)
    region = models.CharField(max_length=50, blank=True, null=True)
    building_cluster = models.CharField(max_length=60, blank=True, null=True)
    wing_name = models.CharField(max_length=50, blank=True, null=True)
    num_wings_buildingcluster = models.IntegerField(blank=True, null=True)
    num_flats_building = models.IntegerField(blank=True, null=True)
    num_shops_buildings = models.IntegerField(blank=True, null=True)
    picture = models.ImageField(upload_to='Images/', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gsouth_building_polygons'