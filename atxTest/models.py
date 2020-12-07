# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Case(models.Model):
    caseid = models.AutoField(db_column='caseId', primary_key=True)  # Field name made lowercase.
    casename = models.CharField(db_column='caseName', max_length=255)  # Field name made lowercase.
    casescripts = models.CharField(db_column='caseScripts', max_length=255)  # Field name made lowercase.
    # caseparameters = models.TextField(db_column='caseParameters')  # Field name made lowercase.
    caseowner = models.CharField(db_column='caseOwner', max_length=255)  # Field name made lowercase.
    casefr = models.CharField(db_column='caseFR', max_length=255)  # Field name made lowercase.
    casetime = models.DateTimeField(db_column='caseTime')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'case'


class Device(models.Model):
    id = models.IntegerField(primary_key=True)
    ip = models.CharField(max_length=255)
    mac = models.CharField(max_length=255)
    status = models.IntegerField()
    # objects = models.Manager()
    class Meta:
        managed = True
        db_table = 'device'


class Result(models.Model):
    jobid = models.IntegerField(db_column='jobId', primary_key=True)  # Field name made lowercase.
    suite = models.CharField(max_length=255, blank=True, null=True)
    device = models.CharField(max_length=255, blank=True, null=True)
    starttime = models.DateTimeField(db_column='startTime')  # Field name made lowercase.
    endtime = models.DateTimeField(db_column='endTime', blank=True, null=True)  # Field name made lowercase.
    jobowner = models.CharField(db_column='jobOwner', max_length=255)  # Field name made lowercase.
    bugid = models.CharField(db_column='bugId', max_length=255, blank=True, null=True)  # Field name made lowercase.
    result = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'result'


class Suite(models.Model):
    suiteid = models.AutoField(db_column='suiteId', primary_key=True)  # Field name made lowercase.
    suitename = models.CharField(db_column='suiteName', max_length=255)  # Field name made lowercase.
    suiteowner = models.CharField(db_column='suiteOwner', max_length=255)  # Field name made lowercase.
    createtime = models.DateTimeField(db_column='createTime')  # Field name made lowercase.
    suitecase = models.TextField(db_column='suiteCase')  # Field name made lowercase.

    class Meta:
        managed = True
        db_table = 'suite'

class Parameters(models.Model):
    Case = models.ForeignKey(Case, on_delete=models.CASCADE)
    key = models.CharField("key", max_length=255)
    value = models.CharField("value", max_length=255)

    class Meta:
        managed = True
        db_table = 'parameters'

class Execute(models.Model):
    suite = models.CharField("suite", max_length=255)
    device = models.CharField("device", max_length=255)
    flag = models.IntegerField("flag")

    class Meta:
        managed = True
        db_table = 'execute'