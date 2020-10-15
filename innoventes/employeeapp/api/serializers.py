from rest_framework import serializers
from employeeapp.models import Member_inno


class MemberSerializer(serializers.ModelSerializer):
    class Meta:
        model = Member_inno
        fields = ['id',
                  'first_name',
                  'last_name',
                  'date_of_birth',
                  'designation',
                  ]

