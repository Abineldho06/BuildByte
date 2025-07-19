from django.db import models
from Admin.models import*
from Guest.models import*
# Create your models here.

#CUSTOMIZE
class tbl_customise(models.Model):
    custome_date=models.DateField(auto_now_add=True)
    custome_amount=models.IntegerField(null=True)
    custome_status=models.IntegerField(default=0)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)
    motherboard=models.ForeignKey(tbl_motherboard,on_delete=models.CASCADE,null=True)
    processor=models.ForeignKey(tbl_processor,on_delete=models.CASCADE,null=True)
    case=models.ForeignKey(tbl_case,on_delete=models.CASCADE,null=True)
    graphicscard=models.ForeignKey(tbl_graphicscard,on_delete=models.CASCADE,null=True)
    cpucooler=models.ForeignKey(tbl_cpucooler,on_delete=models.CASCADE,null=True)
    casecooler=models.ForeignKey(tbl_casecooler,on_delete=models.CASCADE,null=True)
    powersupply=models.ForeignKey(tbl_powersupply,on_delete=models.CASCADE,null=True)

#RAM HEAD.
class tbl_ramhead(models.Model):
    ram=models.ForeignKey(tbl_ram,on_delete=models.CASCADE)
    custom=models.ForeignKey(tbl_customise,on_delete=models.CASCADE)

#ROM HEAD.
class tbl_romhead(models.Model):
    rom=models.ForeignKey(tbl_rom,on_delete=models.CASCADE)
    custom=models.ForeignKey(tbl_customise,on_delete=models.CASCADE)

#BOOKING
class tbl_booking(models.Model):
    booking_date=models.DateField(auto_now_add=True)
    booking_status=models.IntegerField(default=0)
    booking_amount=models.CharField(max_length=30)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)


#CART
class tbl_cart(models.Model):
    cart_qty=models.IntegerField(default=1)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)
    booking=models.ForeignKey(tbl_booking,on_delete=models.CASCADE)
    cart_status=models.IntegerField(default=0)


#COMPLAINT
class tbl_complaint(models.Model):
    complaint_date=models.DateField(auto_now_add=True)
    complaint_title=models.CharField(max_length=30)
    complaint_content=models.CharField(max_length=30)
    complaint_reply=models.CharField(max_length=30)
    complaint_status=models.IntegerField(default=0)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

#FEEDBACK
class tbl_feedback(models.Model):
    feedback_content=models.CharField(max_length=30)
    feedback_date=models.DateField(auto_now_add=True)
    user=models.ForeignKey(tbl_user,on_delete=models.CASCADE)

#CHATTING.
class tbl_chat(models.Model):
    chat_content = models.CharField(max_length=500)
    chat_time = models.DateTimeField()
    chat_file = models.FileField(upload_to='ChatFiles/')
    user_from = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_from")
    user_to = models.ForeignKey(tbl_user,on_delete=models.CASCADE,related_name="user_to",null=True)

    