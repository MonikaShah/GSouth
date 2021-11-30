from django import forms
from .models import WasteSegregationDetails,UploadPictureModel
from map.models import GsouthBuildingPolygons
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, ButtonHolder
import datetime
# from phonenumber_field.formfields import PhoneNumberField
from django.contrib.gis import forms
from django.utils.translation import ugettext_lazy as _
from django.core.exceptions import ValidationError
from datetime import timedelta

wards_value = [('192', 'Ward 192'), ('193', 'Ward 193'), ('194', 'Ward 194'),('195', 'Ward 195'), ('196', 'Ward 196'), ('197', 'Ward 197'), ('198', 'Ward 198'),('199', 'Ward 199') ]  
buildingType_value = [('chs-res', 'CHS-Residentail'), ('chs-res-com', 'CHS-Residential-Cum-Commercial'), ('SRA', 'SRA'),('SMPA', 'SMPA'), ('Schools', 'Schools'), ('hotels_resta', 'Hotels/Restaurants'), ('198', 'Ward 198'),('govt_office', 'Government Offices') ]  

class WasteSegregationDetailsForm(forms.ModelForm): 
    coll_date  = forms.DateField(label = _(u'Date'),widget=forms.TextInput(attrs={'type': 'date'}),initial=datetime.date.today)
    ward = forms.ChoiceField(choices=wards_value)  
    # region = forms.ModelChoiceField(queryset = WasteSegregationDetails.objects.filter(region__isnull=False).values_list('region', flat=True).distinct('region'),empty_label="(Nothing)")
    # region = forms.ModelChoiceField(label = _(u'Region Name'),queryset = WasteSegregationDetails.objects.all(),empty_label="(Choose Region)", to_field_name="region")
    # region = forms.ModelChoiceField(label = _(u'Region Name'),queryset =WasteSegregationDetails.objects.all(),to_field_name='region', required=False)
    region = forms.CharField(label = _(u'Region Name'))
    # building_cluster = forms.CharField(label = _(u'Building Name'),building_choices,widget=forms.Select())
    # building_cluster = forms.ModelChoiceField(label = _(u'Building Name'),queryset = WasteSegregationDetails.objects.all(),widget=forms.Select(attrs={'class': 'form-control'}))
    building_cluster = forms.CharField(label = _(u'Building Cluster Name'))
    building_name = forms.CharField(label = _(u'Building Name'))
    # category = forms.ModelChoiceField(label = _(u'Building Category'),max_length=100)
    num_wings = forms.IntegerField(label=_(u'Number of Wings'))
    wing_name = forms.CharField(max_length=100, label=_(u'Wings Name'))
    building_type = forms.ChoiceField(choices=buildingType_value ,label = _(u'Building Type'))
    # building_type = forms.CharField(label = _(u'Building Type'))
    population = forms.IntegerField(label=_(u'Building Population'))
    num_households_premises = forms.IntegerField(label=_(u'Number of households in Building'))
    num_shops_premises = forms.IntegerField(label=_(u'Number of Shops in Building'))
    # type_waste_generator = forms.CharField(label = _(u'Type of waste generator'),max_length=100)
    waste_segregation = forms.CharField(label = _(u'Is segregation done'),max_length=100)
    wet_waste_before_segregation = forms.IntegerField(label=_(u'Wet Waste before Segregation (in Kgs)'))
    dry_waste_before_segregation = forms.IntegerField(label=_(u'Dry Waste before Segregation (in Kgs)'))
    hazardous_waste = forms.IntegerField(label=_(u'Hazardous Waste before Segregation (in Kgs)'))
    compostable_waste = forms.IntegerField(label=_(u'Compostable Waste before Segregation (in Kgs)'))
    recyclable_waste = forms.IntegerField(label=_(u'Recyclable Waste before Segregation (in Kgs)'))
    rejected_waste = forms.IntegerField(label=_(u'Rejected Waste before Segregation (in Kgs)'))
    # composting_type = forms.CharField(label = _(u'Composting Type'),max_length=100)
    # compost_bin_by_mcgm = forms.CharField(label = _(u'Bin provided by MCGM'),max_length=100)
    # date_notice_issued = forms.DateField(label=_(u'Date of Notice Issued'),widget=forms.TextInput(attrs={'type': 'date'}),initial=datetime.date.today)
    # name_number = forms.CharField(label=_(u'Name and Mobile number of Building Secretaty/Incharge'),max_length=100)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        
    class Meta:
        model = WasteSegregationDetails
        fields = '__all__'
        # fields = ['region','building_cluster']
        # exclude = ['category']

class GsouthBuildingPolygonsForm(forms.ModelForm): 
    # geom = forms.CharField(label = _(u'Geometry'))  # This field type is a guess.
    # fid = forms.IntegerField(label = _(u'FId'))
    # osm_id = forms.DecimalField(label = _(u'OSM ID'))
    # addrstreet = forms.CharField(label = _(u'Address'))
    ward = forms.CharField(label = _(u'Ward*'))
    region = forms.CharField(label = _(u'Region*'))
    building_cluster = forms.CharField(label = _(u'Building Cluster'),required=False)
    building_category = forms.CharField(label = _(u'Building Type'))
    building_name = forms.CharField(label = _(u'Building Name'))
    wing_name = forms.CharField(label = _(u'Wing Name'),required=False)
    num_wings_buildingcluster = forms.IntegerField(label=_(u'Number of Wings in cluster'),required=False)
    num_flats_building = forms.IntegerField(label = _(u'Number of Flats in Building'),required=False)
    num_shops_building = forms.IntegerField(label = _(u'Number of Shops in Building'),required=False)
    building_population = forms.IntegerField(label = _(u'Building Population'),required=False)
    picture = forms.CharField(widget=forms.Textarea(attrs={"rows":10, "cols":10}))
    
    
    def clean(self):
        cleaned_data = self.cleaned_data
        num_flat = cleaned_data.get('num_flats_building')
        wing = cleaned_data.get('wing_name')
        if not any([num_flat, wing]):
            raise forms.ValidationError(u'Please enter a value')
            # raise forms.ValidationError('Future Dates are not allowed.!!')
        
    class Meta:
        model = GsouthBuildingPolygons
        fields = '__all__'
        exclude = ['geom']


class UploadPictureForm(forms.ModelForm):
    class Meta:
        model = UploadPictureModel
        fields = ('picture','date')