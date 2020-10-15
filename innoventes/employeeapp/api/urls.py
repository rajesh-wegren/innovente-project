from django.urls import path, include

from employeeapp.api import views
from employeeapp.api.views import EmployeeListAPIView,EmployeeCreateAPIView,EmployeeDetailView,EmployeeUpdateView,EmployeeDeleteView


urlpatterns = [

    path('list/', EmployeeListAPIView.as_view(), name='employee-list'),
    path('create/', EmployeeCreateAPIView.as_view(), name='employee-create'),
    path('details/<int:pk>', EmployeeDetailView.as_view(), name='employee_details'),
    path('update/<int:pk>', EmployeeUpdateView.as_view(), name='employee_update'),
    path('delete/<int:pk>', EmployeeDeleteView.as_view(), name='employee_delete'),

    path('address/', include('employeeapp.employee_address.urls')),

]
