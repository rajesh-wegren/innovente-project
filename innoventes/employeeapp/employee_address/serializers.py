from rest_framework import serializers
from employeeapp.models import Address,Member_inno


class MemberAddressSerializer(serializers.ModelSerializer):
    class Meta:

        model = Address

        fields = ['id',
                  'address_type',
                  'address_line1',
                  'address_line2',
                  'city',
                  'pin',
                  'country',
                  'member']

class MemberSerializer2(serializers.ModelSerializer):
    class Meta:
        model = Address

        fields = [
                  'address_type',
                  'address_line1',
                  'address_line2',
                  'city',
                  'pin',
                  'country',
                  'member']
        depth = 1