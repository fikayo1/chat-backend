# friendships/urls.py
from django.conf.urls import url

from .views import ReceivedFriendRequests, SentFriendRequests, FriendsList


urlpatterns = [
    # {% url 'me:receivedfriendrequests' %}
    url(
        regex=r'^receivedfriendrequests/$',
        view=ReceivedFriendRequests.as_view(),
        name='receivedfriendrequests-list'
    ),

    # {% url 'me:sentfriendrequests' %}
    url(
        regex=r'^sentfriendrequests/$',
        view=SentFriendRequests.as_view(),
        name='sentfriendrequests-list'
    ),

    # {% url 'me:friends' %}
    url(
        regex=r'^friends/$',
        view=FriendsList.as_view(),
        name='friends-list'
    ),
]