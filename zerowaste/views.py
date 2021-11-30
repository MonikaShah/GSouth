from django.shortcuts import render,redirect,HttpResponse,HttpResponseRedirect
from .models import WasteSegregationDetails,UploadPictureModel#,OsmBuildings29Oct21
from map.models import  GsouthBuildingPolygons
from .forms import WasteSegregationDetailsForm,GsouthBuildingPolygonsForm,UploadPictureForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from django.utils.translation import gettext_lazy as _
from django.core.serializers import serialize
from map.models import GsouthBuildingPolygons


# Create your views here.
def HomePage(request):
    return render(request,"HomePage.html")

def user_login(request):
    # context = RequestContext(request)
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            if user.is_active: 
                login(request, user)
                messages.info(request,_(u"Logged in sucessfully."))
                # analytics = initialize_analyticsreporting()
                # response = get_report(analytics)
                # recd_response = print_response(response)
                # context = {
                #     'Visitor_count': recd_response
                # }

                # return render(request, "rating.html", context)
                return render(request,"HomePage.html")
            else:
                # Return a 'disabled account' error message
                messages.info(request,_(u"Your account is disabled"))
                return HttpResponseRedirect_(u"Your account is disabled.")
        else:
            # Return an 'invalid login' error message.
            print (_(u"invalid login details for " + username))
            # messages.info(request,"Invalid login details"+ username )
            messages.error(request, _(u"Invalid username or password."))
            return render(request,'adminlogin.html')
    else:
        return render(request,'adminlogin.html')

def logout_request(request):
    logout(request)
    messages.info(request, _(u"Logged out successfully!"))
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
    print(data.picture)
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
        form.errors.as_json()
        messages.error(request,"Sorry! Record not updated. Try Again")
    context = {
        'data':data,
        #'Visitor_count': recd_response
        } 
    print(GsouthBuildingPolygonsForm.errors)
    
    return render(request,'buildedit.html',context) 

def uploadimage(request,id):
    print(request.method)
    print(id)
    if request.method == 'POST':
        form = GsouthBuildingPolygons(request.POST, request.FILES)
        # date = request.POST.get('date')
        
        if form.is_valid():
            print("Form is valid")
            if  GsouthBuildingPolygons.objects.filter(osm_id=id).exists():
                messages.warning(request, _(u'Image for this building already exists'))
            else:
                # print("fail")
                # messages.error(request,"Sorry! Record not updated. Try Again")
                instance = form.save()
                instance.user = request.user
                instance.save()
                print("Image is saved.")
                messages.success(request,_(u'Image has been uploaded'))
                return redirect('/')
    else:
        form = UploadPictureForm()    
    
    context = {
        'form':form
    }

    # return render(request,'upload_image.html',{'form': form})
    return render(request,'upload_image.html',context)

#@csrf_exempt
# @require_http_methods(["GET"])
