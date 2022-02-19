from email import message
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render

from django.urls import reverse
from django.views.generic import TemplateView
from django.core.mail import send_mail

# để render là file dữ liệu contact.html trong templates
# Create your views here.
def contact(request):
    return render(request, 'contact.html')

# Hàm nhận mail thông tin của khách hàng
# Đầu ra là print ra nội dung name, sub, mess và trả lại trang contact và 
# trả về câu : Thank you for submitting the form, We will be in touch soon

def send_gmail(request):
    if request.method == "POST":
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        print(name, subject, message)

        send_mail(
            subject,
            message,
            'khangnguyen013@gmail.com',
            ['khangnguyen014@gmail.com'],
            
            fail_silently = False,


        )

        # return HttpResponseRedirect(reverse('contact'))
        return HttpResponse('Thank you for submitting the form, We will be in touch soon')
    else:
        return HttpResponse('Invalid request')