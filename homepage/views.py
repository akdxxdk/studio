from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'homepage/index.html')


def contact(request):
    # 主页
    return render(request, 'homepage/contact.html')


def AiSecurity(request):
    # 联系我们
    return render(request, 'homepage/AiSecurity.html')


def AiEducate(request):
    # 智慧教育
    return render(request, 'homepage/AiEducate.html')


def AiAgriculture(request):
    # 智慧农业
    return render(request, 'homepage/AiAgriculture.html')


def AiFinance(request):
    # 智慧金融
    return render(request, 'homepage/AiFinance.html')


def AiMedical(request):
    # 智能医疗
    return render(request, 'homepage/AiMedical.html')


def AiHousehold(request):
    # 智能家居
    return render(request, 'homepage/AiHousehold.html')
