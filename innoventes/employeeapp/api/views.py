from rest_framework import status, mixins, generics
from rest_framework.response import Response
from employeeapp.api.serializers import MemberSerializer
from employeeapp.models import Member_inno
from django.db.models import Q
from rest_framework.pagination import PageNumberPagination
from rest_framework.exceptions import APIException


class EmployeeListAPIView(mixins.ListModelMixin, generics.GenericAPIView):
    queryset = Member_inno.objects.all().order_by('id')
    serializer_class = MemberSerializer

    def get(self, request, *args, **kwargs):
        query = request.query_params.get("q")

        if query:
            self.queryset = self.queryset.filter(
                Q(first_name__icontains=query) |
                Q(designation__icontains=query)
            )
        paginator = PageNumberPagination()
        # ONE page only 2 records show
        paginator.page_size = 10
        result_page = paginator.paginate_queryset(self.queryset, request)
        serializer = MemberSerializer(result_page, many=True)
        return paginator.get_paginated_response(serializer.data)


class EmployeeCreateAPIView(mixins.CreateModelMixin,
                            generics.GenericAPIView):
    queryset = Member_inno.objects.all().order_by('id')
    serializer_class = MemberSerializer

    def post(self, request):
        member_serializer = MemberSerializer(data=request.data)
        if member_serializer.is_valid():
            post_data = request.data

            member_obj = Member_inno()

            member_obj.first_name = post_data.get('first_name')
            member_obj.last_name = post_data.get('last_name')
            member_obj.date_of_birth = post_data.get('date_of_birth')
            member_obj.designation = post_data.get('designation')
            member_obj.save()
            return Response({"status": status.HTTP_201_CREATED, "message": " employee  created successfully"})
        return Response(member_serializer.errors, status=status.HTTP_201_CREATED)


# this class show the details views .in this class define 3 function (GET,PUT,DELETE)
class EmployeeDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin,mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    serializer_class = MemberSerializer

    def get_object(self, pk):
        try:
            obj = Member_inno.objects.filter(id=pk).first()
            return (obj)
        except Member_inno.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # used  pk to show the particular record.
    def get(self, request, pk=None):
        obj = self.get_object(pk)
        serializer = MemberSerializer(obj)
        return Response(serializer.data)


# Update the Record
class EmployeeUpdateView(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    serializer_class = MemberSerializer

    def get_object(self, pk):
        try:
            obj = Member_inno.objects.filter(id=pk).first()
            return (obj)
        except Member_inno.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # update the particular record  through pk
    def put(self, request, pk=None):
        obj = self.get_object(pk)
        serializer = MemberSerializer(obj, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.erros, status=400)


class EmployeeDeleteView(mixins.RetrieveModelMixin,
                         mixins.UpdateModelMixin,
                         mixins.DestroyModelMixin,
                         generics.GenericAPIView):
    serializer_class = MemberSerializer

    def get_object(self, pk):
        try:
            obj = Member_inno.objects.filter(id=pk).first()
            return (obj)
        except Member_inno.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    # delete the particular Record of  through pk
    def delete(self, request, pk=None):
        obj = self.get_object(pk)
        obj.delete()
        # return Response(status=status.HTTP_204_NO_CONTENT)
        return Response({"status": status.HTTP_204_NO_CONTENT, "message": " Record deleted successfully"})
