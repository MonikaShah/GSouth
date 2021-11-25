from django.db import models

# Create your models here.
class WasteSegregationDetails(models.Model):
    track_id = models.AutoField(primary_key=True)
    coll_date  = models.DateField(default = 10/10/21)
    ward = models.CharField(max_length=50,blank=False, null=False, default='193')
    region = models.CharField(max_length=100, blank=True, null=True)
    building_cluster = models.CharField(max_length=100, blank=True, null=True)
    building_name = models.CharField(max_length=100, blank=True, null=True)
    num_wings = models.IntegerField(blank=True, null=True)
    wing_name = models.CharField(max_length=100, blank=True, null=True)
    building_type = models.CharField(max_length=100, blank=True, null=True)
    population = models.IntegerField(blank=True, null=True)
    num_households_premises = models.IntegerField(blank=True, null=True)
    num_shops_premises = models.IntegerField(blank=True, null=True)
    type_waste_generator = models.CharField(max_length=100, blank=True, null=True)
    waste_segregation = models.CharField(max_length=100, blank=True, null=True)
    wet_waste_before_segregation = models.IntegerField(blank=True, null=True)
    dry_waste_before_segregation = models.IntegerField(blank=True, null=True)
    hazardous_waste = models.IntegerField(blank=True, null=True)
    compostable_waste = models.IntegerField(blank=True, null=True)
    recyclable_waste = models.IntegerField(blank=True, null=True)
    rejected_waste = models.IntegerField(blank=True, null=True)
    # composting_type = models.CharField(max_length=100, blank=True, null=True)
    # compost_bin_by_mcgm = models.CharField(max_length=100, blank=True, null=True)
    # date_notice_issued = models.DateField(null=True,blank=True)
    # name_number = models.CharField(max_length=100, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'waste_segregation_details'
    def __str__(self):
        return self.coll_date