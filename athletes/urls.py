from django.conf.urls import url
from athletes.views import AthleteList, ParentList, \
    DocumentList, AthleteListFull, AthleteBirthdateList

urlpatterns = [
    url(r'^athletesFull/$', AthleteListFull.as_view(), name='athletesFull'),
    url(r'^athletes/$', AthleteList.as_view(), name='athletes'),
    url(r'^athletes/(?P<pk>[0-9]+)', AthleteList.as_view(),
        name='Athlete_byId'),
    url(r'^athletes-birthdate/$', AthleteBirthdateList.as_view(),
        name='athletes_birthdate'),

    url(r'^parents/$', ParentList.as_view(), name='parents'),
    url(r'^parents/(?P<pk>[0-9]+)',
        ParentList.as_view(), name='Parent_byId'),

    url(r'^documents/$', DocumentList.as_view(), name='documents'),
    url(r'^documents/(?P<pk>[0-9]+)',
        DocumentList.as_view(), name='Document_byId'),
]
