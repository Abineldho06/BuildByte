from django.shortcuts import render,redirect
from Admin.models import*
from Guest.models import*

# Create your views here.

#User Registration

def index(request):
    return render(request,"Guest/Index.html")
def Registration(request):
    districtdata=tbl_district.objects.all()
    if request.method=='POST':
        name=request.POST.get('txt_name')
        email=request.POST.get('txt_email')
        address=request.POST.get('txt_address')
        contact=request.POST.get('txt_contact')
        place=tbl_place.objects.get(id=request.POST.get('txt_place'))
        photo=request.FILES.get('file_photo')
        password=request.POST.get('txt_password')

        tbl_user.objects.create(user_name=name,user_email=email,user_address=address,user_contact=contact,place=place,user_photo=photo,user_password=password)
        return render(request,'Guest/USerReg.html',{'msg':"Inserted"})
    else:
        return render(request,'Guest/UserReg.html',{'dis':districtdata})

def ajaxplace(request):
    district=tbl_district.objects.get(id=request.GET.get('did'))
    place=tbl_place.objects.filter(district=district)
    return render(request,'Guest/AjaxPlace.html',{'plc':place})

#Login
def login(request):
    if request.method=='POST':
        email=request.POST.get('txt_email')
        password=request.POST.get('txt_pass')

        usercount=tbl_user.objects.filter(user_email=email,user_password=password).count()
        admincount=tbl_admin.objects.filter(admin_email=email,admin_password=password).count()

        if usercount>0:
            userdata=tbl_user.objects.get(user_email=email,user_password=password)
            request.session['uid']=userdata.id
            return redirect('User:homepage')
        
        elif admincount>0:
            admindata=tbl_admin.objects.get(admin_email=email,admin_password=password)
            request.session['aid']=admindata.id
            return redirect('Admin:homepage')
        else:
            return render(request,'Guest/login.html',{'msg':"Invalid Data"})
    return render(request,'Guest/login.html')