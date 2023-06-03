# youtube/urls.py
from django.urls import path
from .views import (logout_view, index, create_broadcast,
                    # authorize, oauth2callback, revoke, clear_credentials, test_api_request,
                    CreateBroadcastView, TransitionBroadcastView, PlaylistItemsInsertView,
                    FetchPlaylistsView, CreatePlaylistView # , FetchPlaylistsViewV2, FetchChannels
                    )
from .views_w import UserChannelsView, DeleteVideoView, LoadVideoView

urlpatterns = [
    path('', index, name='index'),
#     path('authorize/', authorize, name='authorize'),
#     path('test/', test_api_request, name='test_api_request'),
    path('createbroadcast/', create_broadcast, name='createbroadcast'),
    path('createbroadcast/api/', CreateBroadcastView.as_view(),
         name='create-broadcast-api'),
    path('transitionbroadcast/api/', TransitionBroadcastView.as_view(),
         name='transition-broadcast-api'),
#     path('authorize/', authorize, name='authorize'),
#     path('oauth2callback/', oauth2callback, name='oauth2callback'),
#     path('revoke/', revoke, name='revoke'),
#     path('clear/', clear_credentials, name='clear'),
    path('playlistitemsinsert/api/', PlaylistItemsInsertView.as_view(),
         name='playlist-items-insert-api'),
    path('fetchplaylists/api/', FetchPlaylistsView.as_view(), name='fetch-playlists'),
    path('createplaylist/api/', CreatePlaylistView.as_view(), name='create-playlist'),
#     path('fetchplaylists/api/v2', FetchPlaylistsViewV2.as_view(),
     #     name='fetch-playlists-v2'),
#     path('fetchchannels/api/', FetchChannels.as_view(), name='fetch-channels'),
    path('logout/', logout_view, name='logout'),
    path('channels/api/', UserChannelsView.as_view(), name='user_channel'),
    path('delete-video/', DeleteVideoView.as_view(), name='delete-video'),
    path('videos/api/',  LoadVideoView.as_view(), name='videos'),
]
