from django.shortcuts import render,redirect
from Guest.models import*
from Admin.models import*
from User.models import*
from django.db.models import Sum
from django.db.models import Q
from datetime import datetime

# Create your views here.

#User Homepage.
def Homepage(request):   
    return render(request,'User/Homepage.html')

def logout(request):
    del request.session['uid']
    return redirect('Guest:index')

#MyProfile.
def myprofile(request):
    userdata=tbl_user.objects.get(id=request.session['uid'])
    return render(request,'User/Myprofile.html',{'data':userdata})

#Edit Profile.
def editprofile(request):
    edituser=tbl_user.objects.get(id=request.session['uid'])
    if request.method=="POST":
        edituser.user_name=request.POST.get('txt_name')
        edituser.user_email=request.POST.get('txt_email')
        edituser.user_address=request.POST.get('txt_address')
        edituser.user_contact=request.POST.get('txt_contact')
        edituser.save()

        return render(request,'User/EditProfile.html',{'msg':"Updated"})
    else:
        return render(request,'User/EditProfile.html',{'edit':edituser})
    
#Change Password.
def changepassword(request):
    data=tbl_user.objects.get(id=request.session['uid'])
    dbpass=data.user_password
    if request.method=='POST':
        oldpass=request.POST.get('txt_oldpass')
        newpass=request.POST.get('txt_newpass')
        repass=request.POST.get('txt_repass')
        if dbpass==oldpass:
            if newpass==repass:
                if newpass!=dbpass:
                    data.user_password=newpass
                    data.save()
                    return render(request,'User/ChangePassword.html',{'msg':"Updated"})
                else:
                    return render(request,'User/ChangePassword.html',{'msg1':"The password is already exist"})
            else:
                return render(request,'User/ChangePassword.html',{'msg1':"New password & Confirm password not same"})
        else:
            return render(request,'User/ChangePassword.html',{'msg1':"Old password is incorrect"})
    else:
        return render(request,'User/ChangePassword.html')


#VIEW PRODUCTS
def viewproducts(request):
    categorydata=tbl_category.objects.all()
    product=tbl_product.objects.all()
    for i in product:
        total_stock = tbl_stock.objects.filter(product=i.id).aggregate(total=Sum('stock_qty'))['total']
        total_cart = tbl_cart.objects.filter(product=i.id, cart_status=1).aggregate(total=Sum('cart_qty'))['total']
        # print(total_stock)
        # print(total_cart)
        if total_stock is None:
            total_stock = 0
        if total_cart is None:
            total_cart = 0
        total =  total_stock - total_cart
        i.total_stock = total
    return render(request,'User/ViewProducts.html',{'cat':categorydata,'pro':product})

#SEARCH PRODUCT
def ajaxsearch(request):
    name=request.GET.get("name")
    product=tbl_product.objects.filter(product_name__icontains=name) | tbl_product.objects.filter(brand__brand_name__istartswith=name) | tbl_product.objects.filter(brand__category__category_name__istartswith=name)
    return render(request,"User/AjaxSearch.html",{"pro":product})



#ADD CART
def Addcart(request,pid):
    productdata=tbl_product.objects.get(id=pid)
    userdata=tbl_user.objects.get(id=request.session["uid"])
    bookingcount=tbl_booking.objects.filter(user=userdata,booking_status=0).count()
    if bookingcount>0:
        bookingdata=tbl_booking.objects.get(user=userdata,booking_status=0)
        cartcount=tbl_cart.objects.filter(booking=bookingdata,product=productdata).count()
        if cartcount>0:
            msg="Already added"
            return render(request,"User/ViewProducts.html",{'msg':msg})
        else:
            tbl_cart.objects.create(booking=bookingdata,product=productdata)
            msg="Added To cart"
            return render(request,"User/ViewProducts.html",{'msg':msg})
    else:
        bookingdata = tbl_booking.objects.create(user=userdata)
        tbl_cart.objects.create(booking=tbl_booking.objects.get(id=bookingdata.id),product=productdata)
        msg="Added To cart"
        return render(request,"User/ViewProducts.html",{'msg':msg})
    
    
#MY CART
def Mycart(request):
        if request.method=="POST":
            bookingdata=tbl_booking.objects.get(id=request.session["bookingid"])
            bookingdata.booking_amount=request.POST.get("carttotalamt")
            bookingdata.booking_status=1
            bookingdata.save()
            cart = tbl_cart.objects.filter(booking=bookingdata)
            for i in cart:
                i.cart_status = 1
                i.save()
            return redirect("User:productpayment")
        else:
            bookcount = tbl_booking.objects.filter(user=request.session["uid"],booking_status=0).count()
            if bookcount > 0:
                book = tbl_booking.objects.get(user=request.session["uid"],booking_status=0)
                request.session["bookingid"] = book.id
                cart = tbl_cart.objects.filter(booking=book)
                for i in cart:
                    total_stock = tbl_stock.objects.filter(product=i.product.id).aggregate(total=Sum('stock_qty'))['total']
                    total_cart = tbl_cart.objects.filter(product=i.product.id, cart_status=0).aggregate(total=Sum('cart_qty'))['total']
                    # print(total_stock)
                    # print(total_cart)
                    if total_stock is None:
                        total_stock = 0
                    if total_cart is None:
                        total_cart = 0
                    total =  total_stock - total_cart
                    i.total_stock = total
                return render(request,"User/MyCart.html",{'cartdata':cart})
            else:
                return render(request,"User/MyCart.html")

def DelCart(request,did):
   tbl_cart.objects.get(id=did).delete()
   return redirect("User:Mycart")


def CartQty(request):
   qty=request.GET.get('QTY')
   cartid=request.GET.get('ALT')
   cartdata=tbl_cart.objects.get(id=cartid)
   cartdata.cart_qty=qty
   cartdata.save()
   return redirect("User:Mycart")   

#PAYMENT
def loader(request):
    return render(request,"User/Loader.html")

def paymentsuc(request):
    return render(request,"User/Payment_suc.html")


def productpayment(request):
    bookingdata = tbl_booking.objects.get(id=request.session["bookingid"])
    amt = bookingdata.booking_amount
    if request.method == "POST":
        bookingdata.booking_status = 2
        bookingdata.save()
        return redirect("User:loader")
    else:
        return render(request,"User/Payment.html",{"total":amt})
    
#VIEW MY BOOKINGS
def viewmybookings(request):
    bookingdata=tbl_booking.objects.filter(user=request.session['uid'],booking_status__gt=1)

    return render(request,"User/MyBookings.html",{'bkg':bookingdata})


#VIEW MY PRODUCT
def viewmyproduct(request,pid):
    myproduct=tbl_cart.objects.filter(booking=pid,cart_status__gt=0)
    return render(request,"User/ViewMyProducts.html",{'product':myproduct})

#COMPLAINT
def complaint(request):
    complaintdata=tbl_complaint.objects.filter(user=request.session['uid'])

    if request.method=="POST":
        title=request.POST.get('txt_title')
        content=request.POST.get('txt_content')
        userid=tbl_user.objects.get(id=request.session['uid'])

        tbl_complaint.objects.create(complaint_title=title,complaint_content=content,user=userid)

        return render(request, 'User/Complaint.html',{'msg':"Inserted"})
    else:
        return render(request, 'User/complaint.html',{'com':complaintdata})
    
#Delete.
def deletecomplaint(request,did):
    tbl_complaint.objects.get(id=did).delete()
    return render(request,'User/Complaint.html',{'msgd':"Deleted"})


#FEEDBACK
def feedback(request):
    feedbackdata=tbl_feedback.objects.filter(user=request.session['uid'])

    if request.method=="POST":
        content=request.POST.get('txt_content')
        userid=tbl_user.objects.get(id=request.session['uid'])
        tbl_feedback.objects.create(feedback_content=content,user=userid)

        return render(request, 'User/Feedback.html' ,{'msg':"Feedback Uploaded"})
    else:
        return render(request, 'User/Feedback.html',{'feed':feedbackdata})

#Delete.
def deletefeedback(request,did):
    tbl_feedback.objects.get(id=did).delete()
    return render(request,'User/Feedback.html',{'msgd':"Deleted"})



#CUSTOMISE CPU.
def customcpu(request):
    user=tbl_user.objects.get(id=request.session['uid'])
    customc=tbl_customise.objects.filter(user=user, custome_status=0).count()
    if customc > 0:
        custom=tbl_customise.objects.get(user=user, custome_status=0)
        cid=custom.id
        request.session['cid']=cid
    else:
        custom=tbl_customise.objects.create(user=user)
        cid = custom.id
        request.session['cid']=cid
    return render(request, 'User/CustomCPU.html')

#SELECT MOTHERBOARD.
def selectmotherboard(request):
    motherboarddata=tbl_motherboard.objects.all()

    return render(request,'User/SelectMotherboard.html',{'mother':motherboarddata})

def addmotherboard(request,mid):
    add=tbl_customise.objects.get(id=request.session['cid'])
    mb=tbl_motherboard.objects.get(id=mid)
    add.motherboard=mb
    add.save()

    return render(request,'User/SelectMotherboard.html',{'msg':"Motherboard Added"})

#search bar
def ajaxsearchmotherboard(request):
    name=request.GET.get("name")
    motherboard=tbl_motherboard.objects.filter(motherboard_name__icontains=name) | tbl_motherboard.objects.filter(motherboard_details__icontains=name) | tbl_motherboard.objects.filter(brand__brand_name__istartswith=name)
    return render(request,"User/AjaxSearchMotherboard.html",{"mother":motherboard})


#SELECT PROCESSOR.
def selectprocessor(reqeust):
    processordata=tbl_processor.objects.all()
    
    return render(reqeust,'User/SelectProcessor.html',{'pro':processordata})

def addprocessor(request,pid):
    add=tbl_customise.objects.get(id=request.session['cid'])
    pro=tbl_processor.objects.get(id=pid)
    add.processor=pro
    add.save()

    return render(request,'User/SelectProcessor.html',{'msg':"Processor Added"})

#search Bar
def ajaxsearchprocessor(request):
    name=request.GET.get("name")
    processor=tbl_processor.objects.filter(processor_name__icontains=name) | tbl_processor.objects.filter(processor_details__icontains=name) | tbl_processor.objects.filter(brand__brand_name__istartswith=name)
    return render(request,"User/AjaxSearchprocessor.html",{"pro":processor})


#SELECT CASE.
def selectcase(reqeust):
    casedata=tbl_case.objects.all()
    
    return render(reqeust,'User/SelectCase.html',{'case':casedata})

def addcase(request,caseid):
    add=tbl_customise.objects.get(id=request.session['cid'])
    case=tbl_case.objects.get(id=caseid)
    add.case=case
    add.save()

    return render(request,'User/SelectCase.html',{'msg':"Case Added"})

#search Bar
def ajaxsearchcase(request):
    name=request.GET.get("name")
    case=tbl_case.objects.filter(case_name__icontains=name) | tbl_case.objects.filter(case_details__icontains=name) | tbl_case.objects.filter(brand__brand_name__istartswith=name)
    return render(request,"User/AjaxSearchCase.html",{"case":case})


#SELECT CASE COOLER.
def selectcasecooler(reqeust):
    casecoolerdata=tbl_casecooler.objects.all()
    
    return render(reqeust,'User/SelectCaseCooler.html',{'casec':casecoolerdata})

def addcasecooler(request,ccid):
    add=tbl_customise.objects.get(id=request.session['cid'])
    casec=tbl_casecooler.objects.get(id=ccid)
    add.casecooler=casec
    add.save()

    return render(request,'User/SelectCaseCooler.html',{'msg':"Case Cooler Added"})

#search Bar
def ajaxsearchcasecooler(request):
    name=request.GET.get("name")
    casecooler=tbl_casecooler.objects.filter(casecooler_name__icontains=name) | tbl_casecooler.objects.filter(casecooler_details__icontains=name) | tbl_casecooler.objects.filter(brand__brand_name__istartswith=name)
    return render(request,"User/AjaxSearchCaseCooler.html",{"casec":casecooler})


#SELECT CPU COOLER.
def selectcpucooler(reqeust):
    cpucoolerdata=tbl_cpucooler.objects.all()
    
    return render(reqeust,'User/SelectCPUCooler.html',{'cpuc':cpucoolerdata})

def addcpucooler(request,cpucid):
    add=tbl_customise.objects.get(id=request.session['cid'])
    cpuc=tbl_cpucooler.objects.get(id=cpucid)
    add.cpucooler=cpuc
    add.save()

    return render(request,'User/SelectCPUCooler.html',{'msg':"CPU Cooler Added"})

#search Bar
def ajaxsearchcpucooler(request):
    name=request.GET.get("name")
    cpucooler=tbl_cpucooler.objects.filter(cpucooler_name__icontains=name) | tbl_cpucooler.objects.filter(cpucooler_details__icontains=name) | tbl_cpucooler.objects.filter(brand__brand_name__istartswith=name)
    return render(request,"User/AjaxSearchCPUCooler.html",{"cpuc":cpucooler})


#SELECT GRAPHICS CARD.
def selectgraphicscard(reqeust):
    graphicscarddata=tbl_graphicscard.objects.all()
    
    return render(reqeust,'User/SelectGraphicsCard.html',{'gc':graphicscarddata})

def addgraphicscard(request,gid):
    add=tbl_customise.objects.get(id=request.session['cid'])
    graphics=tbl_graphicscard.objects.get(id=gid)
    add.graphicscard=graphics
    add.save()

    return render(request,'User/SelectGraphicsCard.html',{'msg':"Graphics Card Added"})

#search Bar
def ajaxsearchgraphicscard(request):
    name=request.GET.get("name")
    graphicscard=tbl_graphicscard.objects.filter(graphicscard_name__icontains=name) | tbl_graphicscard.objects.filter(graphicscard_details__icontains=name) | tbl_graphicscard.objects.filter(brand__brand_name__istartswith=name)
    return render(request,"User/AjaxSearchGraphicsCard.html",{"gc":graphicscard})


#SELECT POWER SUPPLY.
def selectpowersupply(reqeust):
    powersupplydata=tbl_powersupply.objects.all()
    
    return render(reqeust,'User/SelectPowerSupply.html',{'ps':powersupplydata})

def addpowersupply(request,psid):
    add=tbl_customise.objects.get(id=request.session['cid'])
    power=tbl_powersupply.objects.get(id=psid)
    add.powersupply=power
    add.save()

    return render(request,'User/SelectPowerSupply.html',{'msg':"Power Supply Added"})

#search Bar
def ajaxsearchpowersupply(request):
    name=request.GET.get("name")
    powersupply=tbl_powersupply.objects.filter(powersupply_name__icontains=name) | tbl_powersupply.objects.filter(powersupply_details__icontains=name) | tbl_powersupply.objects.filter(brand__brand_name__istartswith=name)
    return render(request,"User/AjaxSearchPowerSupply.html",{"ps":powersupply})


#SELECT RAM.
def selectram(request):
    ramdata=tbl_ram.objects.all()
    
    return render(request, 'User/SelectRam.html',{'ram':ramdata}) 

def addram(request,rid):
        custom=tbl_customise.objects.get(id=request.session['cid'])
        ram=tbl_ram.objects.get(id=rid)
        tbl_ramhead.objects.create(ram=ram,custom=custom)

        return render(request,'User/SelectRam.html',{'msg':"Ram Card Added"})

def deleteram(request,did):
    tbl_ramhead.objects.get(id=did).delete()
    return render(request,'User/ViewCustomisedComponents.html',{'msgd':" Ram Removed"})

#search Bar
def ajaxsearchram(request):
    name=request.GET.get("name")
    ram=tbl_ram.objects.filter(ram_name__icontains=name) | tbl_ram.objects.filter(ram_details__icontains=name) | tbl_ram.objects.filter(brand__brand_name__istartswith=name)
    return render(request,"User/AjaxSearchRam.html",{"ram":ram})


#SELECT ROM.
def selectrom(request):
    romdata=tbl_rom.objects.all()
    
    return render(request, 'User/SelectRom.html',{'rom':romdata}) 

def addrom(request,rid):
        custom=tbl_customise.objects.get(id=request.session['cid'])
        rom=tbl_rom.objects.get(id=rid)
        tbl_romhead.objects.create(rom=rom,custom=custom)

        return render(request,'User/SelectRom.html',{'msg':"Rom Card Added"})

def deleterom(request,did):
    tbl_romhead.objects.get(id=did).delete()
    return render(request,'User/ViewCustomisedComponents.html',{'msgd':"Rom Removed"})

#search Bar
def ajaxsearchrom(request):
    name=request.GET.get("name")
    rom=tbl_rom.objects.filter(rom_name__icontains=name) | tbl_rom.objects.filter(rom_details__icontains=name) | tbl_rom.objects.filter(brand__brand_name__istartswith=name)
    return render(request,"User/AjaxSearchRom.html",{"rom":rom})


#VIEW CUSTOMISED COMPONENTS.
def viewcustomisedcomponents(request):
    components = tbl_customise.objects.get(user=request.session['uid'], custome_status=0)
    ram = tbl_ramhead.objects.filter(custom_id=components)
    rom = tbl_romhead.objects.filter(custom_id=components)
    total = 0.0
    if components.motherboard:
        total += float(components.motherboard.motherboard_price or 0)
    if components.processor:
        total += float(components.processor.processor_price or 0)
    if components.case:
        total += float(components.case.case_price or 0)
    if components.casecooler:
        total += float(components.casecooler.casecooler_price or 0)
    if components.graphicscard:
        total += float(components.graphicscard.graphicscard_price or 0)
    if components.cpucooler:
        total += float(components.cpucooler.cpucooler_price or 0)
    if components.powersupply:
        total += float(components.powersupply.powersupply_price or 0)
    for ram_item in ram:
        total += float(ram_item.ram.ram_price or 0)
    for rom_item in rom:
        total += float(rom_item.rom.rom_price or 0)
    print(total)
    components.custome_amount=total
    components.save()
    context = {
        'cust': components,
        'ram': ram,
        'rom': rom,
        'total': total,
    }
    return render(request, 'User/ViewCustomisedComponents.html', context)

#CONFIRM CUSTOMISATION.
def confirmcustomising(request,id):
    customise=tbl_customise.objects.get(id=id)
    customise.custome_status=1
    customise.save()

    return render(request,'User/ViewCustomisedComponents.html',{'msg':"Your customised configuration was sended to the team,we will send you a Notification later if it is acceptable."})

#MY CUSTOM BOOKING.
def viewmycustombooking(request):
    custbooking=tbl_customise.objects.filter(user=request.session['uid'],custome_status__gte=1)

    return render(request,"User/MyCustomBooking.html",{'cust':custbooking})

#CUSTOM PC PAYMENT.
def customepayment(request, id):
    custome = tbl_customise.objects.get(id=id)
    amount = custome.custome_amount
    if request.method == "POST":
        custome.custome_status = 4
        custome.save()
        return redirect("User:loader")
    else:
        return render(request,"User/Payment.html",{"total":amount})
    

#VIEW CUSTOM COMPONENTS.
def customcomponents(request,id):
    ccomponents=tbl_customise.objects.get(id=id)
    ram = tbl_ramhead.objects.filter(custom_id=ccomponents)
    rom = tbl_romhead.objects.filter(custom_id=ccomponents)

    return render(request,'User/ViewCustomComponents.html',{'cust':ccomponents,'ram':ram,'rom':rom})


#CHATTING.

def chatpage(request):
    return render(request,"User/Chat.html")

def ajaxchat(request):
    from_user = tbl_user.objects.get(id=request.session["uid"])
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,chat_file=request.FILES.get("file"))
    return render(request,"User/Chat.html")

def ajaxchatview(request):
    # tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.all().order_by('chat_time')
    return render(request,"User/ChatView.html",{"data":chat_data,"user":user})
def clearchat(request):
    tbl_chat.objects.filter(Q(user_from=request.session["uid"]) & Q(user_to=request.session["uid"])).delete()
    return render(request,"User/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})