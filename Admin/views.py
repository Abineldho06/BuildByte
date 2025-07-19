from django.shortcuts import render,redirect
from Admin.models import *
from User.models import*
from django.db.models import Q, Max
from datetime import datetime
from django.utils import timezone



#HOMEPAGE.
def Homepage(request):
    return render(request,'Admin/Homepage.html')

#LOGOUT.
def logout(request):
    del request.session['aid']
    return redirect('Guest:index')

#This section is for Admin.
def adminInsert(request):
    admin=tbl_admin.objects.all()
    if request.method=="POST":
        tbl_admin.objects.create(admin_name=request.POST.get('txt_name'),admin_contact=request.POST.get('txt_contact'),admin_email=request.POST.get('txt_email'),admin_password=request.POST.get('txt_pass'))

        return redirect('Admin:adminInsert')
    else:
        return render(request,'Admin/AdminReg.html',{'ad':admin})
    
#Delete.
def deleteadmin(request,did):
    tbl_admin.objects.get(id=did).delete()
    return redirect('Admin:adminInsert')

#Edit.
def editadmin(request,eid):
    adminedit=tbl_admin.objects.get(id=eid)
    if request.method=='POST':
        adminedit.admin_name=request.POST.get('txt_name')
        adminedit.admin_contact=request.POST.get('txt_contact')
        adminedit.admin_email=request.POST.get('txt_email')
        adminedit.admin_password=request.POST.get('txt_pass')
        adminedit.save()

        return redirect('Admin:adminInsert')
    else:
        return render(request,'Admin/AdminReg.html',{'edit':adminedit})
    

#DISTRICT.
def district(request):
    district=tbl_district.objects.all()
    if request.method=='POST':
        tbl_district.objects.create(district_name=request.POST.get('txt_dis'))

        return render(request,'Admin/district.html',{'msg':"Inserted"})
    else:
        return render(request,'Admin/District.html',{'dis':district})
    
#Delete.
def deletedistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return render(request,'Admin/district.html',{'msgd':"Deleted"})
    
#Edit.
def editdistrict(request,eid):
    district=tbl_district.objects.get(id=eid)
    if request.method=='POST':
        district.district_name=request.POST.get('txt_dis')
        district.save()

        return render(request,'Admin/district.html',{'msgu':"Updated"})
    else:
        return render(request,'Admin/District.html',{'edit':district})



#PLACE.
def place(request):
    disdata=tbl_district.objects.all()
    placedata=tbl_place.objects.all()

    #dropdown.
    if request.method=='POST':
        palcename=request.POST.get('txt_place')
        districtid=tbl_district.objects.get(id=request.POST.get('sel_dis'))
        tbl_place.objects.create(place_name=palcename,district=districtid)
        return render(request,'Admin/Place.html',{'msg':"Inserted"})
    else:
        return render(request,'Admin/Place.html',{'dis':disdata,'plc':placedata})

#Delete.
def deleteplace(request,did):
    tbl_place.objects.get(id=did).delete()

    return render(request,'Admin/place.html',{'msgd':"Deleted"})


#CATEGORY.
def category(request):
    category=tbl_category.objects.all()
    if request.method=="POST":
        tbl_category.objects.create(category_name=request.POST.get('txt_cat'))

        return render(request,'Admin/category.html',{'msg':"Inserted"})
    else:
        return render(request,'Admin/Category.html',{'cat':category})

#Delete.
def deletecategory(request,did):
    tbl_category.objects.get(id=did).delete()

    return render(request,'Admin/category.html',{'msgd':"Deleted"})

#Edit.
def editcategory(request,eid):
    category=tbl_category.objects.get(id=eid)
    if request.method=='POST':
        category.category_name=request.POST.get('txt_cat')
        category.save()

        return render(request,'Admin/category.html',{'msgu':"Updated"})
    else:
        return render(request,'Admin/Category.html',{'edit':category})
    


#SUBCATEGORY.
def subcategory(request):
    categorydata=tbl_category.objects.all()
    subdata=tbl_subcategory.objects.all()
   
    #dropdown
    if request.method=="POST":
        subcategoryname=request.POST.get('txt_sub')
        categoryid=tbl_category.objects.get(id=request.POST.get('sel_cat'))
        tbl_subcategory.objects.create(subcategory_name=subcategoryname,category=categoryid)

        return render(request,'Admin/Subcategory.html',{'msg':"Inserted"})
    else:
        return render(request,'Admin/Subcategory.html',{'cat':categorydata,'sub':subdata})

#delete
def deletesubcategory(request,did):
    tbl_subcategory.objects.get(id=did).delete()

    return render(request,'Admin/subcategory.html',{'msgd':"Deleted"})




#BRANDS.
def brands(request):
    branddata=tbl_brand.objects.all()
    catdata=tbl_category.objects.all()

    if request.method=='POST':
        brandname=request.POST.get('txt_brands')
        categoryid=tbl_category.objects.get(id=request.POST.get('sel_cat'))
        tbl_brand.objects.create(brand_name=brandname,category=categoryid)

        return render(request,'Admin/brands.html',{'msg':"Inserted"})
    else:
        return render(request,'Admin/Brands.html',{'cat':catdata,'brd':branddata})
#Delete.
def deletebrands(request,did):
    tbl_brand.objects.get(id=did).delete()
    return render(request,'Admin/Brands.html',{'msgd':"Deleted"})



#MOTHERBOARD.
def motherboard(request):
    categorydata=tbl_category.objects.all()
    motherdata=tbl_motherboard.objects.all()

     #dropdown.
    if request.method=='POST':
        name=request.POST.get('txt_name')
        details=request.POST.get('txt_details')
        price=request.POST.get('txt_price')
        photo=request.FILES.get('file_photo')
        brandid=tbl_brand.objects.get(id=request.POST.get('sel_brand'))
        tbl_motherboard.objects.create(motherboard_name=name,motherboard_details=details,motherboard_price=price,motherboard_photo=photo,brand=brandid)

        return render(request,'Admin/Motherboard.html',{'msg':"Inserted"})
    else:
        return render(request,'Admin/Motherboard.html',{'cat':categorydata,'mother':motherdata})
#Ajax
def ajaxbrand(request):
    category=tbl_category.objects.get(id=request.GET.get('did'))
    brand=tbl_brand.objects.filter(category=category)
    return render(request,'Admin/Ajaxbrand.html',{'brd':brand})
#Delete.
def deletemotherboard(request,did):
    tbl_motherboard.objects.get(id=did).delete()
    return render(request,'Admin/Motherboard.html',{'msgd':"Deleted"})



#PROCESSOR.
def processor(request):
    categorydata=tbl_category.objects.all()
    processordata=tbl_processor.objects.all()

     #dropdown.
    if request.method=='POST':
        name=request.POST.get('txt_name')
        details=request.POST.get('txt_details')
        price=request.POST.get('txt_price')
        photo=request.FILES.get('file_photo')
        brandid=tbl_brand.objects.get(id=request.POST.get('sel_brand'))
        tbl_processor.objects.create(processor_name=name,processor_details=details,processor_price=price,processor_photo=photo,brand=brandid)

        return render(request,'Admin/Processor.html',{'msg':"Inserted"})
    else:
        return render(request,'Admin/Processor.html',{'cat':categorydata,'pro':processordata})

#Delete.
def deleteprocessor(request,did):
    tbl_processor.objects.get(id=did).delete()
    return render(request,'Admin/Processor.html',{'msgd':"Deleted"})



#RAM.
def ram(request):
    categorydata=tbl_category.objects.all()
    ramdata=tbl_ram.objects.all()

     #dropdown.
    if request.method=='POST':
        name=request.POST.get('txt_name')
        details=request.POST.get('txt_details')
        price=request.POST.get('txt_price')
        photo=request.FILES.get('file_photo')
        brandid=tbl_brand.objects.get(id=request.POST.get('sel_brand'))
        tbl_ram.objects.create(ram_name=name,ram_details=details,ram_price=price,ram_photo=photo,brand=brandid)

        return render(request,'Admin/Ram.html',{'msg':"Inserted"})
    else:
        return render(request,'Admin/Ram.html',{'cat':categorydata,'ram':ramdata})

#Delete.
def deleteram(request,did):
    tbl_ram.objects.get(id=did).delete()
    return render(request,'Admin/Ram.html',{'msgd':"Deleted"})



#ROM.
def rom(request):
    categorydata=tbl_category.objects.all()
    romdata=tbl_rom.objects.all()

     #dropdown.
    if request.method=='POST':
        name=request.POST.get('txt_name')
        details=request.POST.get('txt_details')
        price=request.POST.get('txt_price')
        photo=request.FILES.get('file_photo')
        brandid=tbl_brand.objects.get(id=request.POST.get('sel_brand'))
        tbl_rom.objects.create(rom_name=name,rom_details=details,rom_price=price,rom_photo=photo,brand=brandid)

        return render(request,'Admin/Rom.html',{'msg':"Inserted"})
    else:
        return render(request,'Admin/Rom.html',{'cat':categorydata,'rom':romdata})

#Delete.
def deleterom(request,did):
    tbl_rom.objects.get(id=did).delete()
    return render(request,'Admin/Rom.html',{'msgd':"Deleted"})


#GRAPHICS CARD.
def graphicscard(request):
    categorydata=tbl_category.objects.all()
    graphicscarddata=tbl_graphicscard.objects.all()

     #dropdown.
    if request.method=='POST':
        name=request.POST.get('txt_name')
        details=request.POST.get('txt_details')
        price=request.POST.get('txt_price')
        photo=request.FILES.get('file_photo')
        brandid=tbl_brand.objects.get(id=request.POST.get('sel_brand'))
        tbl_graphicscard.objects.create(graphicscard_name=name,graphicscard_details=details,graphicscard_price=price,graphicscard_photo=photo,brand=brandid)

        return render(request,'Admin/Graphicscard.html',{'msg':"Inserted"})
    else:
        return render(request,'Admin/Graphicscard.html',{'cat':categorydata,'gcard':graphicscarddata})

#Delete.
def deletegraphicscard(request,did):
    tbl_graphicscard.objects.get(id=did).delete()
    return render(request,'Admin/graphicscard.html',{'msgd':"Deleted"})



#CPU CASE.
def case(request):
    categorydata=tbl_category.objects.all()
    casedata=tbl_case.objects.all()

     #dropdown.
    if request.method=='POST':
        name=request.POST.get('txt_name')
        details=request.POST.get('txt_details')
        price=request.POST.get('txt_price')
        photo=request.FILES.get('file_photo')
        brandid=tbl_brand.objects.get(id=request.POST.get('sel_brand'))
        tbl_case.objects.create(case_name=name,case_details=details,case_price=price,case_photo=photo,brand=brandid)

        return render(request,'Admin/Case.html',{'msg':"Inserted"})
    else:
        return render(request,'Admin/Case.html',{'cat':categorydata,'case':casedata})

#Delete.
def deletecase(request,did):
    tbl_case.objects.get(id=did).delete()
    return render(request,'Admin/Case.html',{'msgd':"Deleted"})



#CPU COOLER.
def cpucooler(request):
    categorydata=tbl_category.objects.all()
    cpucoolerdata=tbl_cpucooler.objects.all()

     #dropdown.
    if request.method=='POST':
        name=request.POST.get('txt_name')
        details=request.POST.get('txt_details')
        price=request.POST.get('txt_price')
        photo=request.FILES.get('file_photo')
        brandid=tbl_brand.objects.get(id=request.POST.get('sel_brand'))
        tbl_cpucooler.objects.create(cpucooler_name=name,cpucooler_details=details,cpucooler_price=price,cpucooler_photo=photo,brand=brandid)

        return render(request,'Admin/Cpucooler.html',{'msg':"Inserted"})
    else:
        return render(request,'Admin/Cpucooler.html',{'cat':categorydata,'ccooler':cpucoolerdata})

#Delete.
def deletecpucooler(request,did):
    tbl_cpucooler.objects.get(id=did).delete()
    return render(request,'Admin/Cpucooler.html',{'msgd':"Deleted"})



#CASE COOLER.
def casecooler(request):
    categorydata=tbl_category.objects.all()
    casecoolerdata=tbl_casecooler.objects.all()

     #dropdown.
    if request.method=='POST':
        name=request.POST.get('txt_name')
        details=request.POST.get('txt_details')
        price=request.POST.get('txt_price')
        photo=request.FILES.get('file_photo')
        brandid=tbl_brand.objects.get(id=request.POST.get('sel_brand'))
        tbl_casecooler.objects.create(casecooler_name=name,casecooler_details=details,casecooler_price=price,casecooler_photo=photo,brand=brandid)

        return render(request,'Admin/Casecooler.html',{'msg':"Inserted"})
    else:
        return render(request,'Admin/Casecooler.html',{'cat':categorydata,'casec':casecoolerdata})

#Delete.
def deletecasecooler(request,did):
    tbl_casecooler.objects.get(id=did).delete()
    return render(request,'Admin/Casecooler.html',{'msgd':"Deleted"})



#POWER SUPPLY.
def powersupply(request):
    categorydata=tbl_category.objects.all()
    powersupplydata=tbl_powersupply.objects.all()

     #dropdown.
    if request.method=='POST':
        name=request.POST.get('txt_name')
        details=request.POST.get('txt_details')
        price=request.POST.get('txt_price')
        photo=request.FILES.get('file_photo')
        brandid=tbl_brand.objects.get(id=request.POST.get('sel_brand'))
        tbl_powersupply.objects.create(powersupply_name=name,powersupply_details=details,powersupply_price=price,powersupply_photo=photo,brand=brandid)

        return render(request,'Admin/Powersupply.html',{'msg':"Inserted"})
    else:
        return render(request,'Admin/Powersupply.html',{'cat':categorydata,'power':powersupplydata})

#Delete.
def deletepowersupply(request,did):
    tbl_powersupply.objects.get(id=did).delete()
    return render(request,'Admin/Powersupply.html',{'msgd':"Deleted"})


#PRODUCTS.
def product(request):
    categorydata=tbl_category.objects.all()
    productdata=tbl_product.objects.all()
   
    #dropdown
    if request.method=='POST':
        name=request.POST.get('txt_name')
        details=request.POST.get('txt_details')
        price=request.POST.get('txt_price')
        photo=request.FILES.get('file_photo')
        brandid=tbl_brand.objects.get(id=request.POST.get('sel_brand'))
        
        tbl_product.objects.create(product_name=name,product_details=details,product_price=price,product_photo=photo,brand=brandid)

        return render(request,'Admin/Product.html',{'msg':"Inserted"})
    else:
        return render(request,'Admin/Product.html',{'cat':categorydata,'pro':productdata})
    
#Delete.
def deleteproduct(request,did):
    tbl_product.objects.get(id=did).delete()
    return render(request,'Admin/Product.html',{'msgd':"Deleted"})



#ADD STOCK.
def stock(request,id):
    product=tbl_product.objects.get(id=id)
    stock=tbl_stock.objects.filter(product=id)
    if request.method == "POST":
        tbl_stock.objects.create(stock_qty=request.POST.get("txt_stock"),product=product)
        
        return redirect("Admin:stock",id)
    else:
        return render(request,"Admin/Stock.html",{'stock':stock})
    

#VIEW CUSTOMERS BOOKINGS.
def viewbookings(request):
    bookingdata=tbl_booking.objects.filter(booking_status__gt=1)

    return render(request,"Admin/ViewBookings.html",{'bkg':bookingdata})


#BOOKED PRODUCT.
def bookedproducts(request,pid):
    bookedproduct=tbl_cart.objects.filter(booking=pid,cart_status__gt=0)
    return render(request,"Admin/BookedProducts.html",{'product':bookedproduct})


#ORDER & DELIVERY STATUS.
def orderstatus(request,bid,sts):
    booking=tbl_booking.objects.get(id=bid)
    booking.booking_status=sts
    booking.save()
    return redirect("Admin:viewbookings")

#VIEW COMPLAINT.
def viewcomplaint(request):
    complaintdata=tbl_complaint.objects.filter(complaint_status=0)
    repliedcomplaint=tbl_complaint.objects.filter(complaint_status__gt=0)
    
    return render(request,'Admin/ViewComplaint.html',{'com':complaintdata,'rcom':repliedcomplaint})

#Reply.
def replycomplaint(request,rid):
    reply=tbl_complaint.objects.get(id=rid)
    if request.method=='POST':
        reply.complaint_reply=request.POST.get('txt_reply')
        reply.complaint_status = 1
        reply.save()

        return render(request,'Admin/Reply.html',{'msgu':"Updated"})
    else:
        return render(request,'Admin/Reply.html',{'reply':reply})


#VIEW FEEDBACK.
def viewfeedback(request):
    feedback=tbl_feedback.objects.all()

    return render(request, 'Admin/viewFeedback.html',{'feed':feedback})

#VIEW CUSTOM BOOKINGS.
def viewcustomrequest(request):
    crequest=tbl_customise.objects.filter(custome_status=1)
    for i in crequest:
        ram = tbl_ramhead.objects.filter(custom=i)
        rom = tbl_romhead.objects.filter(custom=i)
        i.ram = ram
        i.rom = rom
    return render(request, 'Admin/ViewCustomRequest.html',{'cust':crequest})

#ACCEPT.
def acceptcustom(request,id):
    accept=tbl_customise.objects.get(id=id)
    accept.custome_status=2
    accept.save()
    
    return render(request,'Admin/ViewCustomRequest.html',{'msga':"Accepted"})

#REJECT.
def rejectcustom(request,id):
    reject=tbl_customise.objects.get(id=id)
    reject.custome_status=3
    reject.save()

    return render(request,'Admin/ViewCustomRequest.html',{'msgr':"Rejected"})


#VIEW CUSTOM BOOKING.
def viewcustombooking(request):
    cbooking=tbl_customise.objects.filter(custome_status__gte=4)

    return render(request,'Admin/ViewCustomBookings.html',{'cust':cbooking})

#UPDATE DELIVERY STATUS.
def custombookingstatus(request,cid,sts):
    customise=tbl_customise.objects.get(id=cid)
    customise.custome_status=sts
    customise.save()
    return redirect("Admin:viewcustombooking")

#VIEW CUSTOM COMPONENTS.
def customcomponents(request,id):
    ccomponents=tbl_customise.objects.get(id=id)
    ram = tbl_ramhead.objects.filter(custom_id=ccomponents)
    rom = tbl_romhead.objects.filter(custom_id=ccomponents)

    return render(request,'Admin/ViewCustomComponents.html',{'cust':ccomponents,'ram':ram,'rom':rom})


#CHATTING.
def chatlist(request):
    chats = tbl_chat.objects.all().order_by('-chat_time')
    
    chat_list = []
    for chat in chats:
        try:
            # Get the sender (user_from)
            sender = tbl_user.objects.get(id=chat.user_from_id)
            chat_list.append({
                'sender': sender,
                'message': chat.chat_content if chat.chat_content else 'File sent',
                'chat_time': chat.chat_time,
                'tid': sender.id  # For navigation to chat page
            })
        except tbl_user.DoesNotExist:
            continue  # Skip messages with invalid user_from

    return render(request, "Admin/ChatList.html", {"chat_list": chat_list})

def chatpage(request,id):
    user  = tbl_user.objects.get(id=id)
    return render(request,"Admin/Chat.html",{"user":user})

def ajaxchat(request):
    from_user = tbl_user.objects.get(id=request.session["uid"])
    to_user = tbl_user.objects.get(id=request.POST.get("tid"))
    tbl_chat.objects.create(chat_content=request.POST.get("msg"),chat_time=datetime.now(),user_from=from_user,chat_file=request.FILES.get("file"))
    return render(request,"Admin/Chat.html")

def ajaxchatview(request):
    tid = request.GET.get("tid")
    user = tbl_user.objects.get(id=request.session["uid"])
    chat_data = tbl_chat.objects.filter((Q(user_from=user) | Q(user_to=user)) ).order_by('chat_time')
    return render(request,"Admin/ChatView.html",{"data":chat_data,"tid":int(tid)})

def clearchat(request):
    tbl_chat.objects.filter(Q(user_from=request.session["uid"]) & Q(user_to=request.GET.get("tid")) | (Q(user_from=request.GET.get("tid")) & Q(user_to=request.session["uid"]))).delete()
    return render(request,"Admin/ClearChat.html",{"msg":"Chat Deleted Sucessfully...."})