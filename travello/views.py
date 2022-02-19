from django.shortcuts import render

from .models import Destination


# Create your views here.

# Hàm index nhận giá trị là các tour du lịch(Destination) có trên database
# trả về trang index và toàn bộ các Destination trên database

def index(request):




    dests = Destination.objects.all()

    return render(request, "index.html", {'dests': dests})


