from django.db import models


#Models of Admin.

#District
class tbl_district(models.Model):
    district_name=models.CharField(max_length=30)

#Category
class tbl_category(models.Model):
    category_name=models.CharField(max_length=30)

#Admin
class tbl_admin(models.Model):
    admin_name=models.CharField(max_length=30)
    admin_contact=models.CharField(max_length=30)
    admin_email=models.CharField(max_length=30)
    admin_password=models.CharField(max_length=30)

#Place
class tbl_place(models.Model):
    place_name=models.CharField(max_length=30)
    district=models.ForeignKey(tbl_district,on_delete=models.CASCADE)

#Subcategory
class tbl_subcategory(models.Model):
    subcategory_name=models.CharField(max_length=30)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)


#Brand
class tbl_brand(models.Model):
    brand_name=models.CharField(max_length=30)
    category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)

#MotherBoard
class tbl_motherboard(models.Model):
    motherboard_name=models.CharField(max_length=30)
    motherboard_details=models.CharField(max_length=30)
    motherboard_price=models.CharField(max_length=30)
    motherboard_photo=models.FileField(upload_to="Assets/Admin/Photo/")
    brand=models.ForeignKey(tbl_brand,on_delete=models.CASCADE)

#Processor.
class tbl_processor(models.Model):
    processor_name=models.CharField(max_length=30)
    processor_details=models.CharField(max_length=30)
    processor_price=models.CharField(max_length=30)
    processor_photo=models.FileField(upload_to="Assets/Admin/Photo/")
    brand=models.ForeignKey(tbl_brand,on_delete=models.CASCADE)

#RAM.
class tbl_ram(models.Model):
    ram_name=models.CharField(max_length=30)
    ram_details=models.CharField(max_length=30)
    ram_price=models.CharField(max_length=30)
    ram_photo=models.FileField(upload_to="Assets/Admin/Photo/")
    brand=models.ForeignKey(tbl_brand,on_delete=models.CASCADE)

#ROM
class tbl_rom(models.Model):
    rom_name=models.CharField(max_length=30)
    rom_details=models.CharField(max_length=30)
    rom_price=models.CharField(max_length=30)
    rom_photo=models.FileField(upload_to="Assets/Admin/Photo/")
    brand=models.ForeignKey(tbl_brand,on_delete=models.CASCADE)

#GRAPHICSCARD
class tbl_graphicscard(models.Model):
    graphicscard_name=models.CharField(max_length=30)
    graphicscard_details=models.CharField(max_length=30)
    graphicscard_price=models.CharField(max_length=30)
    graphicscard_photo=models.FileField(upload_to="Assets/Admin/Photo/")
    brand=models.ForeignKey(tbl_brand,on_delete=models.CASCADE)

#CASE
class tbl_case(models.Model):
    case_name=models.CharField(max_length=30)
    case_details=models.CharField(max_length=30)
    case_price=models.CharField(max_length=30)
    case_photo=models.FileField(upload_to="Assets/Admin/Photo/")
    brand=models.ForeignKey(tbl_brand,on_delete=models.CASCADE)

#CPU COOLER
class tbl_cpucooler(models.Model):
    cpucooler_name=models.CharField(max_length=30)
    cpucooler_details=models.CharField(max_length=30)
    cpucooler_price=models.CharField(max_length=30)
    cpucooler_photo=models.FileField(upload_to="Assets/Admin/Photo/")
    brand=models.ForeignKey(tbl_brand,on_delete=models.CASCADE)

#CASE COOLER
class tbl_casecooler(models.Model):
    casecooler_name=models.CharField(max_length=30)
    casecooler_details=models.CharField(max_length=30)
    casecooler_price=models.CharField(max_length=30)
    casecooler_photo=models.FileField(upload_to="Assets/Admin/Photo/")
    brand=models.ForeignKey(tbl_brand,on_delete=models.CASCADE)


#POWER SUPPLY
class tbl_powersupply(models.Model):
    powersupply_name=models.CharField(max_length=30)
    powersupply_details=models.CharField(max_length=30)
    powersupply_price=models.CharField(max_length=30)
    powersupply_photo=models.FileField(upload_to="Assets/Admin/Photo/")
    brand=models.ForeignKey(tbl_brand,on_delete=models.CASCADE)
    

#PRODUCT
class tbl_product(models.Model):
    product_name=models.CharField(max_length=30)
    product_details=models.CharField(max_length=30)
    product_price=models.CharField(max_length=30)
    product_photo=models.FileField(upload_to="Assets/Admin/Photo/")
    brand=models.ForeignKey(tbl_brand,on_delete=models.CASCADE)


#STOCK
class tbl_stock(models.Model):
    stock_qty=models.CharField(max_length=30)
    product=models.ForeignKey(tbl_product,on_delete=models.CASCADE)