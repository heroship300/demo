from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth

# Create your views here.
# Hàm login sử dụng method post để đưa dư liệu lên gồm username và password
# kết quả nhận được nếu user none thì load ra trang mác định còn lại thì show ra lỗi Tên đăng nhập hoặc password không hợp lệ !!!


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'Tên đăng nhập hoặc password không hợp lệ !!!')
            return redirect('login')
    else:
        return render(request,'login.html')

# hàm register để đăng ký đầu vào vẫn nhận các method post do người dùng nhập vào
# và tiến hành kiểm tra các thông tin nhập vào xem có tồn tại email, username 
# Kêt quả nhận được ra redirect ra trang register nếu nhập pass ko trùng còn nếu đúng hết các giá trị thì 
# return lại trang chính mặc định là index 

def register(request):

    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        email = request.POST['email']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Tên đăng nhập đã tồn tại !!!')
                return redirect('register')

            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email đã tồn tại !!!')
                return redirect('register')

            else:   
                user = User.objects.create_user(username=username, password=password1, email=email,first_name=first_name,last_name=last_name)
                user.save()
                print('Tài khoản được tạo thành công')
                return redirect('login')

        else:
            messages.info(request,'password không chính xác...')    
            return redirect('register')
        return redirect('/')
        
    else:
        return render(request,'register.html')
   

# Hàm logout khi người dùng nhận được request thì điều hướng đến logout
## kết quả trả lại trang chính mặc định

def logout(request):
    auth.logout(request)
    return redirect('/')