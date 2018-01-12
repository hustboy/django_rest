# -*-coding:utf-8 -*-
# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin sqlcustom [app_label]'
# into your database.
from __future__ import unicode_literals

from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles

LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted((item, item) for item in get_all_styles())




class Eutrancelltdd(models.Model):
    nid = models.IntegerField(blank=True, null=True)
    dn = models.TextField(blank=True, null=True,unique=True)
    userlabel = models.TextField(blank=True, null=True)
    enb_dn = models.TextField(blank=True, null=True)
    enb_userlabel = models.TextField(blank=True, null=True)
    cgi = models.TextField(blank=True, null=True,unique=True)
    # cgi = models.ForeignKey(ZoneList, db_column='cgi',to_field='cgi',related_name='tdd_cgi')
    earfcn = models.IntegerField(blank=True, null=True)
    pci = models.IntegerField(blank=True, null=True)
    bandindicator = models.IntegerField(blank=True, null=True)
    tac = models.IntegerField(blank=True, null=True)
    operationalstate = models.TextField(blank=True, null=True)
    enb_administrativestate = models.TextField(blank=True, null=True)
    enb_operationalstate = models.TextField(blank=True, null=True)
    enb_longitude = models.FloatField(blank=True, null=True)
    enb_latitude = models.FloatField(blank=True, null=True)
    city_name = models.TextField(blank=True, null=True)


    class Meta:
        managed = False
        db_table = 'eutrancelltdd'

    # def __unicode__(self):
    #     return '%s' % self.dn





class EutrancelltddPm(models.Model):
    created = models.DateTimeField(blank=True, null=True)
    nid = models.IntegerField(blank=True, null=True)
    # dn = models.TextField(blank=True, null=True)
    dn=models.ForeignKey(Eutrancelltdd, db_column='dn',to_field='dn',related_name='tdd_dn')
    userlabel = models.TextField(blank=True, null=True)
    rrc_attconnestab = models.FloatField(blank=True, null=True)
    rrc_succconnestab = models.FloatField(blank=True, null=True)
    erab_nbrattestab = models.FloatField(blank=True, null=True)
    erab_nbrsuccestab = models.FloatField(blank=True, null=True)
    context_attrelenb = models.FloatField(blank=True, null=True)
    context_attrelenb_normal = models.FloatField(blank=True, null=True)
    context_succinitalsetup = models.FloatField(blank=True, null=True)
    context_nbrleft = models.FloatField(blank=True, null=True)
    erab_nbrreqrelenb = models.FloatField(blank=True, null=True)
    erab_nbrreqrelenb_normal = models.FloatField(blank=True, null=True)
    erab_hofail = models.FloatField(blank=True, null=True)
    erab_nbrleft = models.FloatField(blank=True, null=True)
    erab_nbrhoinc = models.FloatField(blank=True, null=True)
    rrc_attconnreestab = models.FloatField(blank=True, null=True)
    ho_attoutinterenbs1 = models.FloatField(blank=True, null=True)
    ho_succoutinterenbs1 = models.FloatField(blank=True, null=True)
    ho_attoutinterenbx2 = models.FloatField(blank=True, null=True)
    ho_succoutinterenbx2 = models.FloatField(blank=True, null=True)
    ho_attoutintraenb = models.FloatField(blank=True, null=True)
    ho_succoutintraenb = models.FloatField(blank=True, null=True)
    iratho_attoutgeran = models.FloatField(blank=True, null=True)
    iratho_succoutgeran = models.FloatField(blank=True, null=True)
    iratho_attoututran = models.FloatField(blank=True, null=True)
    iratho_succoututran = models.FloatField(blank=True, null=True)
    pdcp_uppktdelaydl = models.FloatField(blank=True, null=True)
    pdcp_upoctul = models.FloatField(blank=True, null=True)
    pdcp_upoctdl = models.FloatField(blank=True, null=True)
    rru_puschprbtotmeanul = models.FloatField(blank=True, null=True)
    rru_puschprbmeantot = models.FloatField(blank=True, null=True)
    rru_pdschprbtotmeandl = models.FloatField(blank=True, null=True)
    rru_pdschprbmeantot = models.FloatField(blank=True, null=True)
    rru_puschprbassn = models.FloatField(blank=True, null=True)
    rru_pdschprbassn = models.FloatField(blank=True, null=True)
    rru_puschprbtot = models.FloatField(blank=True, null=True)
    rru_pdschprbtot = models.FloatField(blank=True, null=True)
    pag_pagreceived = models.FloatField(blank=True, null=True)
    pag_pagdiscarded = models.FloatField(blank=True, null=True)
    rru_dtchprbassnul = models.FloatField(blank=True, null=True)
    rru_dtchprbassndl = models.FloatField(blank=True, null=True)
    rru_borrowfromscellprbtotdl = models.FloatField(blank=True, null=True)
    rru_lendtopcellprbtotdl = models.FloatField(blank=True, null=True)
    rrc_effectiveconnmean = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eutrancelltdd_pm'


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default='')
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(choices=LANGUAGE_CHOICES,
                                default='python',
                                max_length=100)
    style = models.CharField(choices=STYLE_CHOICES,
                             default='friendly',
                             max_length=100)
    owner = models.ForeignKey('auth.User', related_name='snippets')
    highlighted = models.TextField()

    class Meta:
        ordering = ('created',)







class ZoneList(models.Model):
    zone_id = models.IntegerField(blank=True, null=True)
    zone_name = models.TextField(blank=True, null=True)
    # cgi = models.TextField(blank=True, null=True)
    cgi = models.ForeignKey(Eutrancelltdd, db_column='cgi',to_field='cgi',related_name='zone_cgi')
    city_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zone_list'
        # unique_together = ('cgi', 'zone_name')
        # ordering = ['cgi']
