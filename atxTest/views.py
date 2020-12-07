from django.shortcuts import render
from atxTest.models import Case, Suite, Device
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.

def pageList(list,num,page=1):
    paginator = Paginator(list, num)

    try:
        List = paginator.page(page)#获取当前页码数的记录列表
    except PageNotAnInteger:
        List = paginator.page(1)#如果输入的页数不是整数则显示第1页的内容
    except EmptyPage:
        List = paginator.page(paginator.num_pages)

    return List

def caseview(request):
    case_list = Case.objects.all()
    page = request.GET.get('page', 1)

    case_list = pageList(case_list,5,page)

    return render(request,"caseview.html", {"cases": case_list})

def casesearch(request):
    search_casename = request.GET.get("casename", "")
    search_caseowner = request.GET.get("caseowner", "")
    search_casefr = request.GET.get("casefr", "")
    case_list=None
    if search_casename:
        case_list = Case.objects.filter(casename__icontains=search_casename)
    elif search_caseowner:
        case_list = Case.objects.filter(caseowner__icontains=search_caseowner)
    elif search_casefr:
        case_list = Case.objects.filter(casefr__icontains=search_casefr)

    case_list = pageList(case_list, 5, 1)

    return render(request,'caseview.html', {"cases":case_list})

def suiteview(request):
    suite_list = Suite.objects.all()
    page = request.GET.get('page', 1)

    suite_list = pageList(suite_list,5,page)

    return render(request,"suiteview.html", {"suites": suite_list})

def suitesearch(request):
    search_suitename = request.GET.get("suitename", "")
    search_suiteowner = request.GET.get("suiteowner", "")
    suite_list=None
    if search_suitename:
        suite_list = Suite.objects.filter(suitename__icontains=search_suitename)
    elif search_suiteowner:
        suite_list = Suite.objects.filter(suiteowner__icontains=search_suiteowner)

    suite_list = pageList(suite_list, 5, 1)

    return render(request, "suiteview.html", {"suites": suite_list})


def deviceview(request):
    device_list = Device.objects.all()
    page = request.GET.get('page', 1)

    device_list = pageList(device_list, 5, page)

    return render(request, "deviceview.html", {"devices": device_list})


def devicesearch(request):
    search_id = request.GET.get("id", "")
    search_ip = request.GET.get("ip", "")
    search_mac = request.GET.get("mac", "")
    search_status = request.GET.get("status", "")
    device_list = None
    if search_id:
        device_list = Device.objects.filter(id__icontains=search_id)
    elif search_ip:
        device_list = Device.objects.filter(ip__icontains=search_ip)
    elif search_mac:
        device_list = Device.objects.filter(mac__icontains=search_mac)
    elif search_status:
        device_list = Device.objects.filter(status__icontains=search_status)

    device_list = pageList(device_list, 5, 1)

    return render(request, "deviceview.html", {"devices": device_list})

def submitview(request):
    return render(request, "submitview.html")