from rest_framework import status, generics, mixins

from rest_framework.response import Response

from employeeapp.api.serializers import MemberSerializer
from employeeapp.employee_address.serializers import MemberAddressSerializer,MemberSerializer2
from employeeapp.models import Member_inno, Address
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import APIException


# this class is used the  list the records with Pagination and Insert the the record to the data base.
class EmployeeAddressListAPIView(mixins.ListModelMixin,
                           generics.GenericAPIView):
    queryset = Address.objects.all().order_by('id')
    serializer_class = MemberAddressSerializer

    def get(self, request, employeeid, *args, **kwargs):
        self.queryset = self.queryset.filter(member=employeeid)
        query = request.query_params.get("q")

        if query:
            self.queryset = self.queryset.filter(
                Q(city__icontains=query) |
                Q(country__icontains=query)
            )
        paginator = PageNumberPagination()
        # ONE page only 10 records show
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(self.queryset, request)
        serializer = MemberAddressSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class EmployeeAddressCreateAPIView(mixins.CreateModelMixin,generics.GenericAPIView):
    queryset = Address.objects.all().order_by('id')
    serializer_class = MemberAddressSerializer

    def post(self, request, employeeid):
        employee_address_serializer = MemberAddressSerializer(data=request.data)
        if employee_address_serializer.is_valid():
            post_data = request.data
            # member(Key)----Foreign key,
            member = employeeid
            # address  is the object of  Address table
            address = Address()

            # member is the Foreign key field .link the field Member_inno table
            address.member = Member_inno.objects.filter(id=member).first()

            address.address_type = post_data.get('address_type')
            address.address_line1 = post_data.get('address_line1')
            address.address_line2 = post_data.get('address_line2')
            address.city = post_data.get('city')
            address.pin = post_data.get('pin')
            address.country = post_data.get('country')
            address.save()
            return Response({"status": status.HTTP_201_CREATED, "message": " Employee Address created successfully"})
        return Response(employee_address_serializer.errors, status=status.HTTP_201_CREATED)


# this class show the details views .in this class define 3 function (GET,PUT,DELETE)
class EmployeeAddressDetailView(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                              generics.GenericAPIView):
    serializer_class = MemberAddressSerializer

    def get_object(self, pk):
        obj = Address.objects.filter(id=pk).first()
        if obj is None:
            raise APIException({"code": 404, "message": " Record  Does Not Exist"})
        else:
            return (obj)

    # used  pk to show the particular record.
    def get(self, request, pk=None):
        obj = self.get_object(pk)
        serialize = MemberAddressSerializer(obj)
        return Response(serialize.data)



class EmployeeAddressUpdateView(mixins.UpdateModelMixin,
                              generics.GenericAPIView):
    serializer_class = MemberAddressSerializer

    def get_object(self, employeeid, pk):
        obj = Address.objects.filter(id=pk, member=employeeid).first()
        if obj is None:
            raise APIException({"code": 404, "message": " Record  Does Not Exist"})
        else:
            return (obj)

    # update the particular record  through pk
    def put(self, request, employeeid, pk=None):
        obj = self.get_object(employeeid, pk)
        serializer = MemberAddressSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"code": 200, "message": " Update successfully"})
        return Response(serializer.erros, status=400)


class EmployeeAddressDeleteView(mixins.DestroyModelMixin,
                              generics.GenericAPIView):
    serializer_class = MemberAddressSerializer

    def get_object(self, pk):
        obj = Address.objects.filter(id=pk).first()
        if obj is None:
            raise APIException({"code": 404, "message": " Record  Does Not Exist"})
        else:
            return (obj)

    # delete the particular Record of  through pk
    def delete(self, request, pk=None):
        obj = self.get_object(pk)
        obj.delete()
        return Response({"status": status.HTTP_204_NO_CONTENT, "message": " Record deleted successfully"})

#____________________________________________________________________________________________________________________
# Get Employee (by employee ID) ALONG WITH Address details
class EmployeeAddress2ListAPIView(mixins.ListModelMixin,
                           generics.GenericAPIView):
    queryset = Address.objects.all().order_by('id')
    serializer_class = MemberSerializer2

    def get(self, request, employeeid, *args, **kwargs):
        self.queryset = self.queryset.filter(member=employeeid)
        query = request.query_params.get("q")

        if query:
            self.queryset = self.queryset.filter(
                Q(city__icontains=query) |
                Q(country__icontains=query)
            )
        paginator = PageNumberPagination()
        # ONE page only 10 records show
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(self.queryset, request)
        serializer = MemberSerializer2(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)
