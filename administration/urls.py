from django.conf.urls import url
from administration.views import UserList, UserLogin, UserInfo, \
    DocumentList

urlpatterns = [
    url(r'^userInfo/$', UserInfo.as_view(), name='userInfo'),
    url(r'^users/$', UserList.as_view(), name='users'),
    url(r'^users/(?P<pk>[0-9]+)', UserList.as_view(),
        name='user_byId'),
    url(r'^docs/$', DocumentList.as_view(), name='docs'),
    url(r'^docs/(?P<pk>[0-9]+)', DocumentList.as_view(),
        name='doc_byId'),

    url(r'^auth/login/$', UserLogin.as_view(),
        name='UserLogin'),
]
