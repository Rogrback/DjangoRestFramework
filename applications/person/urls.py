#
from django.urls import path, re_path
from . import views

app_name = 'person_app'

urlpatterns = [
    # PersonSerializer
    path(
        'people/',
        views.ListPeople.as_view(),
        name='people'
        ), 
    path(
        'api/persona/lista',
        views.PersonListApiView.as_view(),
        ), 
    path(
        'list',
        views.PersonListView.as_view(),
        name='list'
        ),
    path(
        'api/persona/search/<kword>',
        views.PersonSearchApiView.as_view(),
        ),     
    path(
        'api/persona/create',
        views.PersonCreateView.as_view(),
        ), 
    path(
        'api/persona/detail/<pk>',
        views.PersonDetailView.as_view(),
        name='person-detail'
        ),  
    path(
        'api/persona/delete/<pk>',
        views.PersonDeleteView.as_view(),
        ), 
    path(
        'api/persona/update/<pk>/',
        views.PersonUpdateView.as_view(),
    ),
    path(
        'api/persona/modificate/<pk>/',
        views.PersonRetriveUpdateView.as_view(),
    ),
    # PersonSerializer2
    path(
        'api/personas/',
        views.PersonApiList.as_view(),
    ),
    path(
        'api/meeting/',
        views.MeetingApiList.as_view(),
    ),
    path(
        'api/meeting2/',
        views.MeetingApiList2.as_view(),
    ),
    path(
        'api/meeting-link/',
        views.MeetingApiListLink.as_view(),
    ),
    path(
        'api/people/pagination/',
        views.PersonPaginationList.as_view(),
    ),
    path(
        'api/meeting/forjob/',
        views.MeetingByPersonJob.as_view(),
    ),
]
