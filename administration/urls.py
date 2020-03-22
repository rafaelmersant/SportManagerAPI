from django.conf.urls import url
from administration.views import UserList, UserLogin

urlpatterns = [
    url(r'^users/$', UserList.as_view(), name='users'),
    url(r'^users/(?P<pk>[0-9]+)', UserList.as_view(),
        name='user_byId'),

    url(r'^auth/login/$', UserLogin.as_view(),
        name='UserLogin'),
]
