from django.test import TestCase

# Create your tests here.

from atxTest.models import Device, Suite, Execute
from django.http import HttpResponse

import pymysql

def testdb(request):
    # db = pymysql.connect("localhost", "root", "123456", "autotest")
    # cursor = db.cursor()
    # sql = "select ip,mac from device where id=1"
    # cursor.execute(sql)
    # data = cursor.fetchall()

    response=""
    data = Device.objects.all()
    print (data)

    for var in data:
        response += var.ip + " "

    return HttpResponse("<p>" + response+ "</p>")

def submitJob(request):
    suitename = request.POST.get('suitename')
    device = request.POST.get('ip')

    # suites = Suite.objects.filter(suitename=suitename).first()
    # print (suites.suitename)
    device_exists = False
    suite_exists = Suite.objects.filter(suitename=suitename).exists()
    device = Device.objects.filter(ip=device).first()
    if device.status == 0:
        device_exists = True
    if suite_exists and device_exists:
        Execute.objects.filter(device=device.ip).update(suite=suitename,flag=1)
        return HttpResponse("<p>submit job success</p>")
    else:
        return HttpResponse("<p>incorrect ip or suite</p>")
