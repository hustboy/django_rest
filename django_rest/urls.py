from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from mysite import views
from rest_framework.urlpatterns import format_suffix_patterns
from mysite.views import SnippetViewSet, UserViewSet
from rest_framework import renderers



# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'is_staff')
#
# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

# Routers provide an easy way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)
# snippet_list = SnippetViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })
# snippet_detail = SnippetViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })
# snippet_highlight = SnippetViewSet.as_view({
#     'get': 'highlight'
# }, renderer_classes=[renderers.StaticHTMLRenderer])
# user_list = UserViewSet.as_view({
#     'get': 'list'
# })
# user_detail = UserViewSet.as_view({
#     'get': 'retrieve'
# })

# urlpatterns = [
#     # Examples:
#     # url(r'^$', 'django_rest.views.home', name='home'),
#     # url(r'^blog/', include('blog.urls')),
#     url(r'^$', views.api_root),
#     # url(r'^snippets/$', views.snippet_list),
#     # url(r'^snippets/(?P<pk>[0-9]+)/$', views.snippet_detail),
#     url(r'^users/$', views.UserList.as_view(),name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', views.UserDetail.as_view(), name='user-detail'),
#     url(r'^snippets/$', views.SnippetList.as_view(),name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', views.SnippetDetail.as_view(),name='snippet-detail'),
#     url(r'^admin/', include(admin.site.urls)),
#
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', views.SnippetHighlight.as_view(),name='snippet-highlight'),
#     # url(r'^', include(router.urls)),
#     url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]
# # urlpatterns += [
# #     url(r'^api-auth/', include('rest_framework.urls',
# #                                namespace='rest_framework')),
# # ]
# urlpatterns = format_suffix_patterns(urlpatterns)

# urlpatterns = format_suffix_patterns([
#     url(r'^$', views.api_root),
#     url(r'^snippets/$', snippet_list, name='snippet-list'),
#     url(r'^snippets/(?P<pk>[0-9]+)/$', snippet_detail, name='snippet-detail'),
#     url(r'^snippets/(?P<pk>[0-9]+)/highlight/$', snippet_highlight, name='snippet-highlight'),
#     url(r'^users/$', user_list, name='user-list'),
#     url(r'^users/(?P<pk>[0-9]+)/$', user_detail, name='user-detail')
# ])
#
# urlpatterns += [
#     url(r'^api-auth/', include('rest_framework.urls',
#                                namespace='rest_framework')),
# ]

from rest_framework.routers import DefaultRouter
# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'eutrancelltddpm', views.EutrancelltddpmViewSet)
router.register(r'eutrancelltdd', views.EutrancelltddViewSet)
router.register(r'zoneList', views.ZoneListViewSet)
router.register(r'alleutrancelltddpm', views.AllEutrancelltddpmViewSet)
router.register(r'getzoneid', views.GetZoneIdViewSet)
router.register(r'getcityname', views.GetCityNameViewSet)

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^csv_am/', views.csv_view_am, name='get_csv'),
    url(r'^csv_pm/', views.csv_view_pm, name='get_csv'),
    # url(r'^zonecsv/', views.zone_csv_view, name='get_zonecsv'),
    # url(r'^eutrancelltdd/$', views.EutrancelltddListView.as_view()),
    url(r'^auth/', include('djoser.urls.authtoken')),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^index/','mysite.views.index',name='index'),
    url(r'^busy/','mysite.views.busy',name='busy'),
]

