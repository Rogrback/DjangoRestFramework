from django.shortcuts import render

from django.views.generic import ListView, TemplateView

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView, # Same to DetailView
    DestroyAPIView, # Same to DeleteView
    UpdateAPIView,
    RetrieveUpdateAPIView,
)

from .models import Person, Meeting, Hobby

from .serializers import (
    PersonSerializer,
    PersonSerializer2,
    PersonSerializer3,
    PersonSerializer4,
    MeetingSerializer,
    MeetingSerializer2,
    MeetingSerializerLink,
    PersonPagination,
    CountMeetingSerializer,
)

class ListPeople(ListView):
    template_name = "person/people.html"
    context_object_name = 'people'

    def get_queryset(self):
        return Person.objects.all()

class PersonListApiView(ListAPIView):
    serializer_class = PersonSerializer4
    
    def get_queryset(self):
        return Person.objects.all()

class PersonListView(TemplateView):
    template_name = 'person/list.html'

    def get_queryset(self):
        return Person.objects.all()

class PersonSearchApiView(ListAPIView):
    serializer_class = PersonSerializer

    def get_queryset(self):
        # filtramos datos
        kword = self.kwargs['kword']
        return Person.objects.filter(
            full_name__icontains=kword
        )

class PersonCreateView(CreateAPIView):
    serializer_class = PersonSerializer

class PersonDetailView(RetrieveAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonDeleteView(DestroyAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonUpdateView(UpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

class PersonRetriveUpdateView(RetrieveUpdateAPIView):
    serializer_class = PersonSerializer
    queryset = Person.objects.all()

#####################################################################

class PersonApiList(ListAPIView):
    serializer_class = PersonSerializer3

    def get_queryset(self):
        return Person.objects.all()

class MeetingApiList(ListAPIView):
    serializer_class = MeetingSerializer

    def get_queryset(self):
        return Meeting.objects.all()

class MeetingApiList2(ListAPIView):
    serializer_class = MeetingSerializer2

    def get_queryset(self):
        return Meeting.objects.all()

class MeetingApiListLink(ListAPIView):
    serializer_class = MeetingSerializerLink

    def get_queryset(self):
        return Meeting.objects.all()

# List people with pagination

class PersonPaginationList(ListAPIView):
    serializer_class = PersonSerializer
    pagination_class = PersonPagination

    def get_queryset(self):
        return Person.objects.all()

class MeetingByPersonJob(ListAPIView):
    serializer_class = CountMeetingSerializer

    def get_queryset(self):
        return Meeting.objects.amount_meetings_job()