from django.urls import path,include
from django.conf.urls import url
from . import views
from django.conf import settings
from django.conf.urls.static import static

# from visits.models import Visits
urlpatterns = [
    path('',views.HomePage, name = 'homepage'),
    path('garbage_seg/', views.WasteSegregationDetailsView,name='garbage_seg'),
    path('buildedit/<int:id>',views.Buildedit, name ='buildedit'),
    path('buildupdate/<int:id>',views.Buildupdate, name ='buildupdate'),
    path('login/', views.user_login, name='login'),
    path("logout", views.logout_request, name="logout"),
    path('uploadimage/<int:id>',views.uploadimage, name = 'uploadimage'),
]
