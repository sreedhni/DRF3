from django.urls import path
from myapp.views import *
urlpatterns = [
  path('create/', CreateMyAppView.as_view(),name="create"),
  path('create/createapiview/', CreateMyAppapiView.as_view(),name="create"),
  path('createuser/', CreateUserView.as_view(),name="create"),
 
path('detail/<int:pk>/', MyAppDetailView.as_view(), name="snippet-detail"),
path('detail/retrieveapiview/<int:pk>/', MyAppDetailView.as_view(), name="snippet-detail"),

]
