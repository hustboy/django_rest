# -*-coding:utf-8 -*-
from datetime import datetime
from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *
import logging
logger = logging.getLogger('mylogger')


# class SnippetSerializer(serializers.Serializer):
#     pk = serializers.IntegerField(read_only=True)
#     title = serializers.CharField(required=False, allow_blank=True, max_length=100)
#     code = serializers.CharField(style={'base_template': 'textarea.html'})
#     linenos = serializers.BooleanField(required=False)
#     language = serializers.ChoiceField(choices=LANGUAGE_CHOICES, default='python')
#     style = serializers.ChoiceField(choices=STYLE_CHOICES, default='friendly')
#
#     def create(self, validated_data):
#         """
#         Create and return a new `Snippet` instance, given the validated data.
#         """
#         return Snippet.objects.create(**validated_data)
#
#     def update(self, instance, validated_data):
#         """
#         Update and return an existing `Snippet` instance, given the validated data.
#         """
#         instance.title = validated_data.get('title', instance.title)
#         instance.code = validated_data.get('code', instance.code)
#         instance.linenos = validated_data.get('linenos', instance.linenos)
#         instance.language = validated_data.get('language', instance.language)
#         instance.style = validated_data.get('style', instance.style)
#         instance.save()
#         return instance

# class SnippetSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Snippet
#         fields = ('id', 'title', 'code', 'linenos', 'language', 'style')

# class UserSerializer(serializers.ModelSerializer):
#     snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippet.objects.all())
#
#     class Meta:
#         model = User
#         fields = ('id', 'username', 'snippets')
#
# class SnippetSerializer(serializers.ModelSerializer):
#     owner = serializers.ReadOnlyField(source='owner.username')
#
#     class Meta:
#         model = Snippet
#         fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')

class SnippetSerializer(serializers.HyperlinkedModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    class Meta:
        model = Snippet
        fields = ('url', 'highlight', 'owner',
                  'title', 'code', 'linenos', 'language', 'style')


class UserSerializer(serializers.HyperlinkedModelSerializer):
    snippets = serializers.HyperlinkedRelatedField(many=True, view_name='snippet-detail', read_only=True)

    class Meta:
        model = User
        fields = ('url', 'username', 'snippets')
        
        
class EutrancelltddPmSerializer(serializers.HyperlinkedModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    # highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    # tdd_dn = serializers.ReadOnlyField(source='mysite.models.Eutrancelltdd')
    # def zone_list(self,obj):
    #     zone_id = self.context['request'].query_params.get('zone_id', None)
    #
    #
    #     return ZoneList.objects.filter(cgi__dn = obj.dn.dn,zone_id=zone_id).values()
    # zone_cgi = serializers.SerializerMethodField('zone_list')
    cgi=serializers.CharField(source='dn.cgi', read_only=True)


    class Meta:
        model = EutrancelltddPm
        fields = ('id','created','nid','dn','userlabel','rrc_attconnestab','rrc_succconnestab','erab_nbrattestab',
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
    'rrc_effectiveconnmean',
                  'cgi'

                  # 'zone_id',
                  # 'zone_cgi',
                  )


# class ZoneListSerializer(serializers.ModelSerializer):
#
#     # tdd_cgi = serializers.StringRelatedField(many=True)
#
#
#     class Meta:
#         model = ZoneList
#         fields = ('zone_id',
#     'zone_name',
#     'cgi',
#     'city_name',
#
#
#     )

class ZoneListSerializer(serializers.ModelSerializer):


    class Meta:
        model = ZoneList
        fields = ('zone_id',
                  'zone_name',
                  'cgi',
                  'city_name',

                  )


class ZoneIdSerializer(serializers.ModelSerializer):


    class Meta:
        model = ZoneList
        fields = ('zone_id',

                  )


class CityNameSerializer(serializers.ModelSerializer):


    class Meta:
        model = Eutrancelltdd
        fields = ('city_name',

                  )





class EutrancelltddSerializer(serializers.ModelSerializer):
    # owner = serializers.ReadOnlyField(source='owner.username')
    # highlight = serializers.HyperlinkedIdentityField(view_name='snippet-highlight', format='html')

    # zonelist_cgi = serializers.RelatedField(many=True)
    # zonelist_cgi = serializers.SlugRelatedField(
    #     many=True,
    #     read_only=True,
    #     slug_field='zone_id'
    #  )
    # def filter_zone(self, queryset):
    #     zone_id = self.context['request'].query_params.get('zone_id', None)
    #
    #     return ZoneList.objects.filter(zone_id=zone_id)



    # tdd_dn = EutrancelltddPmSerializer(many=True, read_only=True)
    # zone_cgi=serializers.CharField(source='zone_cgi.zone_id', read_only=True)

    # zone_cgi = serializers.SerializerMethodField('zone_list')

    # tdd_dn = serializers.SerializerMethodField('tdd_dn')


    # def zone_list(self,obj):
    #     zone_id = self.context['request'].query_params.get('zone_id', None)
    #
    #     logger.debug(obj.cgi)
    #     return ZoneList.objects.filter(cgi = obj.cgi,zone_id=zone_id).values()

    # def tdd_dn(self,obj):
    #
    #     begin=datetime.strptime(self.request.query_params.get('begin', None), "%Y-%m-%d %H:%M:%S")
    #
    #     end=datetime.strptime(self.request.query_params.get('end', None), "%Y-%m-%d %H:%M:%S")
    #
    #     logger.debug(obj.dn)
    #     return EutrancelltddPm.objects.filter(dn = obj.dn,created__gte=begin,created_lte=end).values()




    # zone_cgi = serializers.SlugRelatedField(
    #     many=True,
    #     queryset=zone_list,
    #     slug_field='zone_id'
    # )



    # pm_created=serializers.SlugRelatedField(
    #     many=True,
    #
    #     read_only=True,
    #     slug_field='created'
    #  )




    # def __init__(self, *args, **kwargs):
    #     zone_id = kwargs['context']['request'].query_params.get('zone_id', None)
    #
    #
    #     zone_cgi_f = self.fields['zone_id']
    #
    #     zone_cgi_f.queryset = zone_cgi_f.queryset.filter(zone_id=zone_id)
    #
    #     super(EutrancelltddSerializer, self).__init__(*args, **kwargs)




    class Meta:
        model = Eutrancelltdd

        fields = ('nid','dn',
                  'userlabel',
                  'cgi',
                  'city_name',

                  )




