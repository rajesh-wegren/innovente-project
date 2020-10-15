from django.urls import path
from employeeapp.employee_address.views import *

app = 'employeeapp'
urlpatterns = [

    path('list/<int:employeeid>', EmployeeAddressListAPIView.as_view(), name='employee_address_list'),
    path('create/<int:employeeid>', EmployeeAddressCreateAPIView.as_view(), name='employee_address_create'),
    path('details/<int:pk>', EmployeeAddressDetailView.as_view(), name='employee_address_details'),
    path('update/<int:employeeid>/<int:pk>', EmployeeAddressUpdateView.as_view(), name='employee_address_update'),
    path('delete/<int:pk>', EmployeeAddressDeleteView.as_view(), name='employee_address_delete'),

    path('employee_and_address_details/<int:employeeid>',EmployeeAddress2ListAPIView.as_view(), name='employee_and address_details_by_employeeid'),

]
