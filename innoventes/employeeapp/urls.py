from django.urls import path, include

app_name = 'employeeapp'
urlpatterns = [
    path('', include('employeeapp.api.urls')),
]
