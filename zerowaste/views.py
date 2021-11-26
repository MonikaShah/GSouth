from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from .models import WasteSegregationDetails#,OsmBuildings29Oct21
from map.models import  GsouthBuildingPolygons
from .forms import WasteSegregationDetailsForm,GsouthBuildingPolygonsForm
from django.contrib import messages
from django.utils.translation import gettext_lazy as _
from django.core.serializers import serialize
from map.models import GsouthBuildingPolygons


# Create your views here.
def HomePage(request):
    return render(request,"HomePage.html")

def WasteSegregationDetailsView(request):
        form = WasteSegregationDetailsForm()
        building = request.POST.get('building_cluster')
        # form.fields['building_cluster'].choices = [building.building]
        # print(request.method)
        if request.method == 'POST':
            form = WasteSegregationDetailsForm(request.POST)
            # region = form.cleaned_data['region']
            # print(region)
            # regionName = form.cleaned_data['region']
            # print(form['region'].value())
            # print(form['building_cluster'].value())
            if form.is_valid():
                regionName = form.cleaned_data['region']
                bldgcluster = form.cleaned_data['building_cluster']
                bldgname = form.cleaned_data['building_name']
                print(regionName)
                print(bldgcluster)
                print(bldgname)
                collDate = form.cleaned_data['coll_date']
                if regionName =="none":
                    messages.warning(request, _(u'Please select Region'))
                if  WasteSegregationDetails.objects.filter(coll_date=collDate, region=regionName, building_name=bldgname, building_cluster=bldgcluster).exists():
                    messages.warning(request, _(u'Data already exists for this {} -{} and Date{}.').format(regionName,bldgname,collDate))
                else:  
                    instance = form.save(commit=False)
                    instance.save()
                    messages.success(request, _(u'Your data is saved for {} - {} - {} dated {}').format(regionName,bldgcluster,bldgname,collDate))
                    # print(form)
                #   messages.success(request,'Form is valid')
                return HttpResponseRedirect(request.path_info)
            else:
                # print(form['region'].value())
                # print(form['building_cluster'].value())
                form.errors.as_json()
                messages.warning(request, _(u'Please check your form'))
                messages.warning(request,form.errors.as_json)
        else:
                form = WasteSegregationDetailsForm()
                # print(form)
                form.errors.as_json()
        return render(request, 'GarbageSeg.html', {'form': form})

def Buildedit(request, id):  
    data = GsouthBuildingPolygons.objects.get(osm_id=id)
    # docdata  = doctor.objects.get(id=id)  
    # print(data.coll_date)
    print(data.building_name)
    context = {
        'data':data,
        #'Visitor_count': recd_response
    }
    # return render(request,'edit.html', {'data':data}) 
    return render(request,'buildedit.html',context) 
def Buildupdate(request, id):
    # print(id)
    data = GsouthBuildingPolygons.objects.get(osm_id=id) 
    # print(data) 
    form = GsouthBuildingPolygonsForm(request.POST, instance=data)  
    print(form)
    
    if form.is_valid(): 
        print("success") 
        messages.success(request,"Record Updated")          
        form.save()          
    else:
        print("fail")
        messages.error(request,"Sorry! Record not updated. Try Again")
    context = {
        'data':data,
        #'Visitor_count': recd_response
        } 
    print(GsouthBuildingPolygonsForm.errors)
    
    return render(request,'buildedit.html',context) 