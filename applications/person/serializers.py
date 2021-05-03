from rest_framework import serializers, pagination

from .models import Person, Meeting, Hobby

# Serializer to Person

class PersonSerializer(serializers.ModelSerializer):
    class Meta:
        model = Person
        fields = ('__all__')

# Serializer to Person with specific fields

class PersonSerializer2(serializers.Serializer):
    id = serializers.IntegerField()
    full_name = serializers.CharField()
    job = serializers.CharField()
    email = serializers.EmailField()
    phone = serializers.CharField()
    active = serializers.BooleanField(required=False)

# Serializer to Person with an extra attribute 

class PersonSerializer3(serializers.ModelSerializer):

    active = serializers.BooleanField(default=False)

    class Meta:
        model = Person
        fields = ('__all__')

# Serializer to field ForeingKey

class MeetingSerializer(serializers.ModelSerializer):

    person = PersonSerializer()

    class Meta:
        model = Meeting
        fields = (
            'id',
            'date',
            'hour',
            'affair',
            'person',
            )

# Serializer to Hobby

class HobbySerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Hobby
        fields = ('__all__')

# Serializer to fields ManytoMany

class PersonSerializer4(serializers.ModelSerializer):
    
    hobbies = HobbySerializer(many=True)

    class Meta:
        model = Person
        fields = (
            'id',
            'full_name',
            'job',
            'email',
            'phone',
            'hobbies',
            'created',
            )

# Method to a serializer - MethodFieldSerializer
# Create a method that join date an hour to an attribute

class MeetingSerializer2(serializers.ModelSerializer):

    date_hour = serializers.SerializerMethodField()

    class Meta:
        model = Meeting
        fields = (
            'id',
            'date',
            'hour',
            'affair',
            'person',
            'date_hour',
            )
    
    def get_date_hour(self, obj):
        return str(obj.date) + ' - ' + str(obj.hour)

# HyperLinkedModelSerializer
# This method generate a URL an attribute that has a lot of values
# for avoid the overload from the memory

class MeetingSerializerLink(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = Meeting
        fields = (
            'id',
            'date',
            'hour',
            'affair',
            'person',
            )

        extra_kwargs = {
            'person': {'view_name': 'person_app:person-detail', 'lookup_field': 'pk'}
        }

# Pagination serializer 
# This method can use in any model serializers

class PersonPagination(pagination.PageNumberPagination):
    page_size = 5
    max_page_size = 100

class CountMeetingSerializer(serializers.Serializer):
    person__job = serializers.CharField()
    amount = serializers.IntegerField()