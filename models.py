# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=80)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.BooleanField()
    username = models.CharField(unique=True, max_length=30)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.CharField(max_length=254)
    is_staff = models.BooleanField()
    is_active = models.BooleanField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class AuthtokenToken(models.Model):
    key = models.CharField(primary_key=True, max_length=40)
    created = models.DateTimeField()
    user = models.ForeignKey(AuthUser, models.DO_NOTHING, unique=True)

    class Meta:
        managed = False
        db_table = 'authtoken_token'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.SmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class EnbfunctionCmTemp(models.Model):
    datetime = models.DateField(blank=True, null=True)
    nid = models.IntegerField(blank=True, null=True)
    reldn = models.TextField(blank=True, null=True)
    dn = models.TextField(blank=True, null=True)
    userlabel = models.TextField(blank=True, null=True)
    enbid = models.TextField(blank=True, null=True)
    administrativestate = models.TextField(blank=True, null=True)
    operationalstate = models.TextField(blank=True, null=True)
    longitude = models.FloatField(blank=True, null=True)
    latitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'enbfunction_cm_temp'


class Eutrancelltdd(models.Model):
    nid = models.IntegerField(blank=True, null=True)
    dn = models.TextField(blank=True, null=True)
    userlabel = models.TextField(blank=True, null=True)
    enb_dn = models.TextField(blank=True, null=True)
    enb_userlabel = models.TextField(blank=True, null=True)
    cgi = models.TextField(blank=True, null=True)
    earfcn = models.IntegerField(blank=True, null=True)
    pci = models.IntegerField(blank=True, null=True)
    bandindicator = models.IntegerField(blank=True, null=True)
    tac = models.IntegerField(blank=True, null=True)
    operationalstate = models.TextField(blank=True, null=True)
    enb_administrativestate = models.TextField(blank=True, null=True)
    enb_operationalstate = models.TextField(blank=True, null=True)
    enb_longitude = models.FloatField(blank=True, null=True)
    enb_latitude = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'eutrancelltdd'


class EutrancelltddPm(models.Model):
    begintime = models.DateTimeField(blank=True, null=True)
    nid = models.IntegerField(blank=True, null=True)
    dn = models.TextField(blank=True, null=True)
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


class EutrancelltddPm20161027(models.Model):
    begintime = models.DateTimeField(blank=True, null=True)
    nid = models.IntegerField(blank=True, null=True)
    dn = models.TextField(blank=True, null=True)
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
    id = models.AutoField()

    class Meta:
        managed = False
        db_table = 'eutrancelltdd_pm_20161027'


class MysiteSnippet(models.Model):
    created = models.DateTimeField()
    title = models.CharField(max_length=100)
    code = models.TextField()
    linenos = models.BooleanField()
    language = models.CharField(max_length=100)
    style = models.CharField(max_length=100)
    highlighted = models.TextField()
    owner = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'mysite_snippet'


class Position(models.Model):
    groupname = models.CharField(max_length=-1, blank=True, null=True)
    position = models.CharField(max_length=-1, blank=True, null=True)
    positionratio = models.FloatField(blank=True, null=True)
    systime = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'position'


class Transaction(models.Model):
    exchangetime = models.DateTimeField(blank=True, null=True)
    groupname = models.CharField(max_length=-1, blank=True, null=True)
    stockname = models.CharField(max_length=-1, blank=True, null=True)
    beforeoperation = models.FloatField(blank=True, null=True)
    afteroperation = models.FloatField(blank=True, null=True)
    follow = models.CharField(max_length=-1, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'transaction'


class ZoneList(models.Model):
    zone_id = models.IntegerField(blank=True, null=True)
    zone_name = models.TextField(blank=True, null=True)
    cgi = models.TextField(blank=True, null=True)
    city_name = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'zone_list'
