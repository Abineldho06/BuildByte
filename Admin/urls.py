from django.urls import path,include
from Admin import views
app_name="Admin"
urlpatterns = [

    path('Homepage/',views.Homepage,name="homepage"),
    
    #ADMIN.
    path('adminreg/',views.adminInsert,name="adminInsert"),
    path('deleteadmin/<int:did>',views.deleteadmin,name="deleteadmin"),
    path('editadmin/<int:eid>',views.editadmin,name="editadmin"),

    #DISTRICT.
    path('district/',views.district,name="district"),
    path('deletedistrict/<int:did>',views.deletedistrict,name="deletedistrict"),
    path('editdistrict/<int:eid>',views.editdistrict,name='editdistrict'),

    #PLACE.
    path('place/',views.place,name="place"),
    path('deleteplace/<int:did>',views.deleteplace,name="deleteplace"),

    #CATEGORY.
    path('category/',views.category,name="category"),
    path('deltecategory/<int:did>',views.deletecategory,name="deletecategory"),
    path('editcategory/<int:eid>',views.editcategory,name="editcategory"),

    #SUBCATE.
    path('subcategory/',views.subcategory,name="subcategory"),
    path('deletesubcategory/<int:did>',views.deletesubcategory,name="deletesubcategory"),

    #BRANDS.
    path('brands/',views.brands,name="brands"),
    path('deletebrands/<int:did>',views.deletebrands,name="deletebrands"),


    #CPU COMPONENTS.

    path('motherboard/',views.motherboard,name="motherboard"),
    path('ajaxbrand/',views.ajaxbrand,name="ajaxbrand"),
    path('deletemotherboard/<int:did>',views.deletemotherboard,name="deletemotherboard"),

    path('processor/',views.processor,name="processor"),
    path('deleteprocessor/<int:did>',views.deleteprocessor,name="deleteprocessor"),

    path('ram/',views.ram,name="ram"),
    path('deleteram/<int:did>',views.deleteram,name="deleteram"),

    path('rom/',views.rom,name="rom"),
    path('deleterom/<int:did>',views.deleterom,name="deleterom"),

    path('graphicscard/',views.graphicscard,name="graphicscard"),
    path('deletegraphicscard/<int:did>',views.deletegraphicscard,name="deletegraphicscard"),

    path('case/',views.case,name="case"),
    path('deletecase/<int:did>',views.deletecase,name="deletecase"),

    path('cpucooler/',views.cpucooler,name="cpucooler"),
    path('deletecpucooler/<int:did>',views.deletecpucooler,name="deletecpucooler"),

    path('casecooler/',views.casecooler,name="casecooler"),
    path('deletecasecooler/<int:did>',views.deletecasecooler,name="deletecasecooler"),

    path('powersupply/',views.powersupply,name="powersupply"),
    path('deletepowersupply/<int:did>',views.deletepowersupply,name="deletepowersupply"),

    #PRODUCTS ADDING.
    path('product/',views.product,name="product"),
    path('deleteproduct/<int:did>',views.deleteproduct,name="deleteproduct"),

    #STOCK.
    path('stock/<int:id>',views.stock,name="stock"),

    #BOOKINGS.
    path('viewbookings/',views.viewbookings,name="viewbookings"),
    path('bookedproducts/<int:pid>',views.bookedproducts,name="bookedproducts"),
    path('orderstatus/<int:bid>/<int:sts>',views.orderstatus,name="orderstatus"),

    #COMPLAINTS.
    path('viewcomplaint/',views.viewcomplaint,name="viewcomplaint"),
    path('replycomplaint/<int:rid>',views.replycomplaint,name="replycomplaint"),

    #FEEDBACK.
    path('viewfeedback/',views.viewfeedback,name="viewfeedback"),

    #CUSTOM PC REQUEST.
    path('viewcustomrequest/',views.viewcustomrequest,name="viewcustomrequest"),
    path('acceptcustom/<int:id>',views.acceptcustom,name="acceptcustom"),
    path('rejectcustom/<int:id>',views.rejectcustom,name="rejectcustom"),

    #CUSTOM PC BOOKINGS.
    path('viewcustombooking/',views.viewcustombooking,name="viewcustombooking"),
    path('customcomponents/<int:id>',views.customcomponents,name="customcomponents"),
    path('custombookingstatus/<int:cid>/<int:sts>',views.custombookingstatus,name="custombookingstatus"),

    #CHATTING.
    path('chatpage/<int:id>',views.chatpage,name="chatpage"),
    path('ajaxchat/',views.ajaxchat,name="ajaxchat"),
    path('ajaxchatview/',views.ajaxchatview,name="ajaxchatview"),
    path('clearchat/',views.clearchat,name="clearchat"),
    path('chatlist/', views.chatlist, name='chatlist'),

    #LOG OUT.
    path('logout/',views.logout,name="logout"),
]
