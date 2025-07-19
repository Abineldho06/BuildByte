from django.urls import path,include
from User import views
app_name='User'

urlpatterns = [
    path('Homepage/',views.Homepage,name="homepage"),
    path('Myprofile/',views.myprofile,name="Myprofile"),
    path('Editprofile/',views.editprofile,name="Editprofile"),
    path('Changepassword/',views.changepassword,name="Changepassword"),

    path('ViewProducts/',views.viewproducts,name="ViewProducts"),
    path('ajaxsearch/',views.ajaxsearch,name="ajaxsearch"),

    path('Addcart/<int:pid>',views.Addcart, name='Addcart'), 
    path('Mycart/',views.Mycart, name='Mycart'),   
    path("DelCart/<int:did>", views.DelCart,name="delcart"),
    path("CartQty/", views.CartQty,name="cartqty"),


    path('loader/',views.loader, name='loader'),
    path('paymentsuc/',views.paymentsuc, name='paymentsuc'),
    path("productpayment/", views.productpayment,name="productpayment"),

    path('viewmybooking/',views.viewmybookings,name="viewmybookings"),

    path('viewmyproduct/<int:pid>',views.viewmyproduct,name="viewmyproduct"),

    path('complaint/',views.complaint,name="complaint"),
    path('deletecomplaint/<int:did>',views.deletecomplaint,name="deletecomplaint"),

    path('feedback/',views.feedback,name="feedback"),
    path('deletefeedback/<int:did>',views.deletefeedback,name="deletefeedback"),

    #Custom CPU urls.
    path('customcpu/',views.customcpu,name="customcpu"),
    
    path('selectmotherboard/',views.selectmotherboard,name="selectmotherboard"),
    path('ajaxsearchmotherboard/',views.ajaxsearchmotherboard,name="ajaxsearchmotherboard"),
    path('addmotherboard/<int:mid>',views.addmotherboard,name="addmotherboard"),

    path('selectprocessor/',views.selectprocessor,name="selectprocessor"),
    path('ajaxsearchprocessor/',views.ajaxsearchprocessor,name="ajaxsearchprocessor"),
    path('addprocessor/<int:pid>',views.addprocessor,name="addprocessor"),

    path('selectcase/',views.selectcase,name="selectcase"),
    path('ajaxsearchcase/',views.ajaxsearchcase,name="ajaxsearchcase"),
    path('addcase/<int:caseid>',views.addcase,name="addcase"),

    path('selectcasecooler/',views.selectcasecooler,name="selectcasecooler"),
    path('ajaxsearchcasecooler/',views.ajaxsearchcasecooler,name="ajaxsearchcasecooler"),
    path('addcasecooler/<int:ccid>',views.addcasecooler,name="addcasecooler"),

    path('selectcpucooler/',views.selectcpucooler,name="selectcpucooler"),
    path('ajaxsearchcpucooler/',views.ajaxsearchcpucooler,name="ajaxsearchcpucooler"),
    path('addcpucooler/<int:cpucid>',views.addcpucooler,name="addcpucooler"),

    path('selectgraphicscard/',views.selectgraphicscard,name="selectgraphicscard"),
    path('ajaxsearchgraphicscard/',views.ajaxsearchgraphicscard,name="ajaxsearchgraphicscard"),
    path('addgraphicscard/<int:gid>',views.addgraphicscard,name="addgraphicscard"),

    path('selectpowersupply/',views.selectpowersupply,name="selectpowersupply"),
    path('ajaxsearchpowersupply/',views.ajaxsearchpowersupply,name="ajaxsearchpowersupply"),
    path('addpowersupply/<int:psid>',views.addpowersupply,name="addpowersupply"),
    
    path('selectram/',views.selectram,name="selectram"),
    path('ajaxsearchram/',views.ajaxsearchram,name="ajaxsearchram"),
    path('addram/<int:rid>',views.addram,name="addram"),
    path('deleteram/<int:did>',views.deleteram,name="deleteram"),

    path('selectrom/',views.selectrom,name="selectrom"),
    path('ajaxsearchrom/',views.ajaxsearchrom,name="ajaxsearchrom"),
    path('addrom/<int:rid>',views.addrom,name="addrom"),
    path('deleterom/<int:did>',views.deleterom,name="deleterom"),

    #Confirm Customisation
    path('viewcustomisedcomponents/',views.viewcustomisedcomponents,name="viewcustomisedcomponents"),
    path('confirmcustomising/<int:id>',views.confirmcustomising,name="confirmcustomising"),

    path('viewmycustombooking/',views.viewmycustombooking,name="viewmycustombooking"),
    path('customepayment/<int:id>',views.customepayment,name="customepayment"),
    path('customcomponents/<int:id>',views.customcomponents,name="customcomponents"),

    path('logout/',views.logout,name="logout"),

    #CHATTING.
    path('chatpage/',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),
]
   
