from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'homepage/index.html')


def contact(request):
    # ��ҳ
    return render(request, 'homepage/contact.html')


def AiSecurity(request):
    # ��ϵ����
    return render(request, 'homepage/AiSecurity.html')


def AiEducate(request):
    # �ǻ۽���
    return render(request, 'homepage/AiEducate.html')


def AiAgriculture(request):
    # �ǻ�ũҵ
    return render(request, 'homepage/AiAgriculture.html')


def AiFinance(request):
    # �ǻ۽���
    return render(request, 'homepage/AiFinance.html')


def AiMedical(request):
    # ����ҽ��
    return render(request, 'homepage/AiMedical.html')


def AiHousehold(request):
    # ���ܼҾ�
    return render(request, 'homepage/AiHousehold.html')
