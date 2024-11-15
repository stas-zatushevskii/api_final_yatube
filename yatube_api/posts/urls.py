from api.views import (CommentViewSet, FollowerViewSet, GroupViewSet,
                       PostViewSet)
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet,
                basename='comments')
router.register('follow', FollowerViewSet, basename='follow')


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),

]
