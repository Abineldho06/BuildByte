from django.shortcuts import render

# Create your views here.
def calculation(request):
    if request.method=="POST":
        no1=int(request.POST.get('txt_num1'))
        no2=int(request.POST.get('txt_num2'))
        btn=request.POST.get('btn_submit')

        if btn=="+":
            result=no1+no2
        elif btn=="-":
            result=no1-no2
        elif btn=="*":
            result=no1*no2
        elif btn=="/":
            result=no1/no2

        return render(request,'Basics/Calculator.html',{'res':result})
    else:
        return render(request,'Basics/Calculator.html')
        
def largest(request):
    result=""
    if request.method=="POST":
        no1=int(request.POST.get('txt_num1'))
        no2=int(request.POST.get('txt_num2'))
        no3=int(request.POST.get('txt_num3'))

        if no1>no2 and no1>no3:
            result=no1
        elif no2>no1 and no2>no3:
            result=no2
        elif no3>no1 and no3>no2:
            result=no3
        
        return render(request,'Basics/Largest.html',{'res':result})
    else:
        return render(request,'Basics/Largest.html')
        
def add(request):
    if request.method=="POST":
        a=int(request.POST.get('txt_num1'))
        b=int(request.POST.get('txt_num2'))
        c=a+b

        return render(request,'Basics/Add.html',{'add':c})
    else:
        return render(request,'Basics/Add.html')
    