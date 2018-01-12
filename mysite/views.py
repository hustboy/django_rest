# -*-coding:utf-8 -*-
# from django.http import HttpResponse
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.renderers import JSONRenderer
# from rest_framework.parsers import JSONParser
# from .models import Snippet
# from .serializers import SnippetSerializer
#
# class JSONResponse(HttpResponse):
#     """
#     An HttpResponse that renders its content into JSON.
#     """
#     def __init__(self, data, **kwargs):
#         content = JSONRenderer().render(data)
#         kwargs['content_type'] = 'application/json'
#         super(JSONResponse, self).__init__(content, **kwargs)
#
#
# @csrf_exempt
# def snippet_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'POST':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data, status=201)
#         return JSONResponse(serializer.errors, status=400)
#
# @csrf_exempt
# def snippet_detail(request, pk):
#     """
#     Retrieve, update or delete a code snippet.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return HttpResponse(status=404)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return JSONResponse(serializer.data)
#
#     elif request.method == 'PUT':
#         data = JSONParser().parse(request)
#         serializer = SnippetSerializer(snippet, data=data)
#         if serializer.is_valid():
#             serializer.save()
#             return JSONResponse(serializer.data)
#         return JSONResponse(serializer.errors, status=400)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return HttpResponse(status=204)


# from rest_framework import status,permissions
# from rest_framework.decorators import api_view,permission_classes
# from rest_framework.response import Response
# from .models import Snippet
# from .serializers import SnippetSerializer
#
#
# @api_view(['GET', 'POST'])
# @permission_classes((permissions.AllowAny,))
# # def snippet_list(request):
# def snippet_list(request, format=None):
#     """
#     List all snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
# @api_view(['GET', 'PUT', 'DELETE'])
# @permission_classes((permissions.AllowAny,))
# # def snippet_detail(request, pk):
# def snippet_detail(request, pk, format=None):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     try:
#         snippet = Snippet.objects.get(pk=pk)
#     except Snippet.DoesNotExist:
#         return Response(status=status.HTTP_404_NOT_FOUND)
#
#     if request.method == 'GET':
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     elif request.method == 'PUT':
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     elif request.method == 'DELETE':
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# from .models import Snippet
# from .serializers import SnippetSerializer
# from django.http import Http404
# from rest_framework.views import APIView
# from rest_framework.response import Response
# from rest_framework import status,permissions
# from rest_framework.decorators import permission_classes
#
# @permission_classes((permissions.AllowAny,))
# class SnippetList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, format=None):
#         serializer = SnippetSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#
# @permission_classes((permissions.AllowAny,))
# class SnippetDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404
#
#     def get(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet)
#         return Response(serializer.data)
#
#     def put(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         serializer = SnippetSerializer(snippet, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, pk, format=None):
#         snippet = self.get_object(pk)
#         snippet.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)




from rest_framework import status
from rest_framework.decorators import list_route

from rest_framework.settings import api_settings
from rest_framework_csv.parsers import CSVParser
from rest_framework_csv.renderers import CSVRenderer,CSVStreamingRenderer
import rest_framework_filters as filters
import django_filters
from .serializers import *
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework import generics,permissions,renderers,viewsets
from rest_framework.decorators import permission_classes,api_view
from django.contrib.auth.models import User
from djqscsv import render_to_csv_response
from .permissions import IsOwnerOrReadOnly
# @permission_classes((permissions.AllowAny,))
# class SnippetList(mixins.ListModelMixin,
#                   mixins.CreateModelMixin,
#                   generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)
#
#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)
#
# @permission_classes((permissions.AllowAny,))
# class SnippetDetail(mixins.RetrieveModelMixin,
#                     mixins.UpdateModelMixin,
#                     mixins.DestroyModelMixin,
#                     generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#
#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)
#
#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)
#
#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)


# @permission_classes((permissions.AllowAny,))
# class SnippetList(generics.ListCreateAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
#     def perform_create(self, serializer):
#             serializer.save(owner=self.request.user)
#     def pre_save(self, obj):
#             obj.owner = self.request.user
#     permission_classes = (permissions.IsAuthenticatedOrReadOnly,
#                       IsOwnerOrReadOnly,)
#
# @permission_classes((permissions.IsAuthenticatedOrReadOnly,IsOwnerOrReadOnly,))
# class SnippetDetail(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Snippet.objects.all()
#     serializer_class = SnippetSerializer
    # def pre_save(self, obj):
    #         obj.owner = self.request.user
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                   IsOwnerOrReadOnly,)


from rest_framework.decorators import detail_route
import datetime
from djqscsv import render_to_csv_response

from django.shortcuts import render


def index(request):
    return render(request, 'index.html')
def busy(request):
    return render(request, 'busy.html')

class PaginatedCSVRenderer (CSVStreamingRenderer):
    results_field = 'results'

    def render(self, data, *args, **kwargs):
        if not isinstance(data, list):
            data = data.get(self.results_field, [])
        return super(PaginatedCSVRenderer, self).render(data, *args, **kwargs)






class SnippetViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list`, `create`, `retrieve`,
    `update` and `destroy` actions.

    Additionally we also provide an extra `highlight` action.
    """
    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    # permission_classes = (permissions.IsAuthenticatedOrReadOnly,
    #                       IsOwnerOrReadOnly,)

    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)

# class UserList(generics.ListAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# class UserDetail(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)



# class SnippetHighlight(generics.GenericAPIView):
#     queryset = Snippet.objects.all()
#     renderer_classes = (renderers.StaticHTMLRenderer,)
#
#     def get(self, request, *args, **kwargs):
#         snippet = self.get_object()
#         return Response(snippet.highlighted)

# @api_view(['GET'])
# def api_root(request, format=None):
#     return Response({
#         'users': reverse('user-list', request=request, format=format),
#         'snippets': reverse('snippet-list', request=request, format=format)
#     })


# class EutrancelltddPmFilter(django_filters.rest_framework.FilterSet):
#     begin_time = django_filters.DateTimeFilter(name="created", lookup_expr='gte')
#     end_time = django_filters.DateTimeFilter(name="created", lookup_expr='lte')
#     class Meta:
#         model = EutrancelltddPm
#         fields = ('dn','begin_time', 'end_time')
#
#
# class EutrancelltddFilter(django_filters.rest_framework.FilterSet):
#     begin_time = django_filters.DateTimeFilter(name="pm_created__created", lookup_expr='gte')
#     end_time = django_filters.DateTimeFilter(name="pm_created__created", lookup_expr='lte')
#     class Meta:
#         model = Eutrancelltdd
#         # fields = ['dn','begin_time', 'end_time']
#         fields = ('zone_id__zone_id', 'city_name','dn','begin_time', 'end_time')
#
# class ZoneListFilter(django_filters.rest_framework.FilterSet):
#
#
#     class Meta:
#         model = ZoneList
#         fields = ['zone_id', 'zone_name']

# class EutrancelltddFilter(filters.FilterSet):
#     # dn = filters.CharFilter(name='dn')
#     # ZoneList = filters.RelatedFilter(ZoneListFilter,name='zone_cgi',queryset=ZoneList.objects.all())
#
#
#     class Meta:
#         model = Eutrancelltdd
#         fields = {'dn','cgi'}
#
#
# def zonelist(request):
#     zone_id = request.query_params.get('zone_id', None)
#     queryset = Eutrancelltdd.objects.filter (zone_cgi__zone_id=zone_id).all()
#     return queryset
#
# class EutrancelltddPmFilter(filters.FilterSet):
class EutrancelltddPmFilter(django_filters.rest_framework.FilterSet):
    created = django_filters.DateTimeFromToRangeFilter()
    # end_time = django_filters.DateTimeFilter(name="created", lookup_expr='lt')
    # date = django_filters.DateFilter(name="created", lookup_expr='contains')




    class Meta:
        model = EutrancelltddPm
        fields = {'created','dn__city_name'}
#
# class ZoneListFilter(filters.FilterSet):
#     Eutrancelltdd = filters.RelatedFilter(EutrancelltddFilter,name='zone_cgi',queryset=Eutrancelltdd.objects.all())
#     class Meta:
#         model = ZoneList
#         fields = {'zone_id'}






class EutrancelltddpmViewSet(viewsets.ReadOnlyModelViewSet):
# class EutrancelltddListView(generics.ListAPIView):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    # queryset = EutrancelltddPm.objects.filter(begintime='2016-10-27 00:00:00')

    # ordering_fields = ('created')

    queryset = EutrancelltddPm.objects.all()

    # filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    # filter_backends = (filters.backends.DjangoFilterBackend,)
    #
    # filter_class = EutrancelltddPmFilter
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = EutrancelltddPmSerializer
    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES)+(PaginatedCSVRenderer,)



    # parser_classes = (CSVParser,) + tuple(api_settings.DEFAULT_PARSER_CLASSES)

    #
    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """
        # queryset = Eutrancelltdd.objects.all()

        zone_id = self.request.query_params.get('zone_id', None)
        begin=self.request.query_params.get('begin', None)
        end=self.request.query_params.get('end', None)
        # cityname=self.request.query_params.get('cityname', None)


        # date=datetime.datetime.strptime(self.request.query_params.get('date', None), "%Y-%m-%d")

        # start_date_range = (
        #     datetime.datetime.combine(date, datetime.datetime.min.time()),
        #     datetime.datetime.combine(date, datetime.datetime.max.time())
        # )
        if zone_id is not None:
            # zonedn=Eutrancelltdd.objects.filter(zone_cgi__zone_id=zone_id)
            # queryset = EutrancelltddPm.objects.filter (created__lte=end,created__gte=begin,dn__dn__in=zonedn.values('dn'))
            # logger.debug(queryset.count())
            queryset=EutrancelltddPm.objects.raw('SELECT c.*  FROM zone_list a,eutrancelltdd b,eutrancelltdd_pm c WHERE c.created Between %s And %s and a.zone_id=%s and a.cgi=b.cgi and b.dn=c.dn ORDER BY c.created ', [begin,end,zone_id])
            return list(queryset)
        # else:
        #     queryset=EutrancelltddPm.objects.filter(created__range=start_date_range,dn__city_name=cityname)
        #     return queryset




    def get_renderer_context(self):
        context = super(EutrancelltddpmViewSet, self).get_renderer_context()
        context['header'] = (
            self.request.GET['fields'].split(',')
            if 'fields' in self.request.GET else None)
        return context





class AllEutrancelltddpmViewSet(viewsets.ReadOnlyModelViewSet):


    queryset = EutrancelltddPm.objects.all()

    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)

    # filter_backends = (filters.backends.DjangoFilterBackend,)

    filter_class = EutrancelltddPmFilter


    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    serializer_class = EutrancelltddPmSerializer

    ordering = 'dn'
    renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES











class ZoneListViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """

    queryset = ZoneList.objects.all()
    serializer_class = ZoneListSerializer

    # filter_backends = (filters.backends.DjangoFilterBackend,)
    # filter_class = ZoneListFilter

    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES)+(PaginatedCSVRenderer,)

    # def get_queryset(self):
    #     """
    #     Optionally restricts the returned purchases to a given user,
    #     by filtering against a `username` query parameter in the URL.
    #     """
    #     # queryset = Eutrancelltdd.objects.all()
    #     zone_id = self.request.query_params.get('zone_id', None)
    #     if zone_id is not None:
    #
    #         queryset = ZoneList.objects.filter (zone_id=zone_id)
    #     return queryset







    def get_renderer_context(self):
        context = super(ZoneListViewSet, self).get_renderer_context()
        context['header'] = (
            self.request.GET['results'].split(',')
            if 'fields' in self.request.GET else None)
        return context


class GetZoneIdViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """

    queryset = ZoneList.objects.distinct('zone_id')
    serializer_class = ZoneIdSerializer



    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES)


class GetCityNameViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides `list` and `detail` actions.
    """

    queryset = Eutrancelltdd.objects.distinct('city_name')
    serializer_class = CityNameSerializer



    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES)



class EutrancelltddViewSet(viewsets.ReadOnlyModelViewSet):
# class EutrancelltddListView(generics.ListAPIView):
    """
    This viewset automatically provides `list` and `detail` actions.
    """
    # queryset = EutrancelltddPm.objects.filter(begintime='2016-10-27 00:00:00')



    queryset = Eutrancelltdd.objects.all()





    serializer_class = EutrancelltddSerializer

    # filter_backends = (filters.backends.DjangoFilterBackend,)
    #
    # filter_class = EutrancelltddFilter

    # filter_fields = ('city_name','dn')

    # parser_classes = (CSVParser,) + tuple(api_settings.DEFAULT_PARSER_CLASSES)
    renderer_classes = tuple(api_settings.DEFAULT_RENDERER_CLASSES)+(PaginatedCSVRenderer,)

    def get_queryset(self):
        """
        Optionally restricts the returned purchases to a given user,
        by filtering against a `username` query parameter in the URL.
        """

        queryset = Eutrancelltdd.objects.all()
        begin=self.request.query_params.get('begin', None)

        end=self.request.query_params.get('end', None)
        zone_id = self.request.query_params.get('zone_id', None)
        if zone_id is not None:

            queryset = Eutrancelltdd.objects.filter (zone_cgi__zone_id=zone_id,tdd_dn__created__lte=end,tdd_dn__created__gte=begin)
            logger.debug(queryset.count())
        return queryset




    def get_renderer_context(self):
        context = super(EutrancelltddViewSet, self).get_renderer_context()
        context['header'] = (
            self.request.GET['fields'].split(',')
            if 'fields' in self.request.GET else None)
        return context









def csv_view_am(request):
    date= request.GET.get('created')
    city=request.GET.get('cityname')


    strattime= datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=8)
    endtime= datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=11)
    qs = EutrancelltddPm.objects.filter(created__gte=strattime,created__lte=endtime,dn__city_name=city).values('id','created','nid','dn','userlabel','rrc_attconnestab','rrc_succconnestab','erab_nbrattestab',
    'erab_nbrsuccestab',
    'context_attrelenb',
    'context_attrelenb_normal',
    'context_succinitalsetup',
    'context_nbrleft',
    'erab_nbrreqrelenb',
    'erab_nbrreqrelenb_normal',
    'erab_hofail',
    'erab_nbrleft',
    'erab_nbrhoinc',
    'rrc_attconnreestab',
    'ho_attoutinterenbs1',
    'ho_succoutinterenbs1',
    'ho_attoutinterenbx2',
    'ho_succoutinterenbx2',
    'ho_attoutintraenb',
    'ho_succoutintraenb',
    'iratho_attoutgeran',
    'iratho_succoutgeran',
    'iratho_attoututran',
    'iratho_succoututran',
    'pdcp_uppktdelaydl',
    'pdcp_upoctul',
    'pdcp_upoctdl',
    'rru_puschprbtotmeanul',
    'rru_puschprbmeantot',
    'rru_pdschprbtotmeandl',
    'rru_pdschprbmeantot',
    'rru_puschprbassn',
    'rru_pdschprbassn',
    'rru_puschprbtot',
    'rru_pdschprbtot',
    'pag_pagreceived',
    'pag_pagdiscarded',
    'rru_dtchprbassnul',
    'rru_dtchprbassndl',
    'rru_borrowfromscellprbtotdl',
    'rru_lendtopcellprbtotdl',
    'rrc_effectiveconnmean')
    # qs = EutrancelltddPm.objects.filter(created=created.date).values('id','created','nid','dn','userlabel','rrc_attconnestab','rrc_succconnestab','erab_nbrattestab',
    # 'erab_nbrsuccestab',
    # 'context_attrelenb',
    # 'context_attrelenb_normal',
    # 'context_succinitalsetup',
    # 'context_nbrleft',
    # 'erab_nbrreqrelenb',
    # 'erab_nbrreqrelenb_normal')
    return render_to_csv_response(qs)




def csv_view_pm(request):
    date= request.GET.get('created')
    city=request.GET.get('cityname')


    strattime= datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=18)
    endtime= datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S") + datetime.timedelta(hours=21)
    qs = EutrancelltddPm.objects.filter(created__gte=strattime,created__lte=endtime,dn__city_name=city).values('id','created','nid','dn','userlabel','rrc_attconnestab','rrc_succconnestab','erab_nbrattestab',
    'erab_nbrsuccestab',
    'context_attrelenb',
    'context_attrelenb_normal',
    'context_succinitalsetup',
    'context_nbrleft',
    'erab_nbrreqrelenb',
    'erab_nbrreqrelenb_normal',
    'erab_hofail',
    'erab_nbrleft',
    'erab_nbrhoinc',
    'rrc_attconnreestab',
    'ho_attoutinterenbs1',
    'ho_succoutinterenbs1',
    'ho_attoutinterenbx2',
    'ho_succoutinterenbx2',
    'ho_attoutintraenb',
    'ho_succoutintraenb',
    'iratho_attoutgeran',
    'iratho_succoutgeran',
    'iratho_attoututran',
    'iratho_succoututran',
    'pdcp_uppktdelaydl',
    'pdcp_upoctul',
    'pdcp_upoctdl',
    'rru_puschprbtotmeanul',
    'rru_puschprbmeantot',
    'rru_pdschprbtotmeandl',
    'rru_pdschprbmeantot',
    'rru_puschprbassn',
    'rru_pdschprbassn',
    'rru_puschprbtot',
    'rru_pdschprbtot',
    'pag_pagreceived',
    'pag_pagdiscarded',
    'rru_dtchprbassnul',
    'rru_dtchprbassndl',
    'rru_borrowfromscellprbtotdl',
    'rru_lendtopcellprbtotdl',
    'rrc_effectiveconnmean')
    # qs = EutrancelltddPm.objects.filter(created=created.date).values('id','created','nid','dn','userlabel','rrc_attconnestab','rrc_succconnestab','erab_nbrattestab',
    # 'erab_nbrsuccestab',
    # 'context_attrelenb',
    # 'context_attrelenb_normal',
    # 'context_succinitalsetup',
    # 'context_nbrleft',
    # 'erab_nbrreqrelenb',
    # 'erab_nbrreqrelenb_normal')
    return render_to_csv_response(qs)









