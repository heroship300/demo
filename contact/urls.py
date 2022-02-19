from django.urls import path
from .import views

from .views import send_gmail
from .views import contact

# Tao đường dẫn để show lên trang contact trên web ở views.contact
# tạo đường dẫn để thực hiện hàm send_mail khi click send_mail

urlpatterns = [path("contact", views.contact, name="contact"),
                path('send_mail/', send_gmail, name="send_mail"),
] 