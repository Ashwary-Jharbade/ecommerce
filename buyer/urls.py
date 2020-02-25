from django.urls import path
from buyer import views

app_name = 'buyer'

urlpatterns=[
    path('buyerapp/',views.buyerapp),
    path('proddetails/<int:id>/',views.proddetails,name ='proddetails'),
    path('cartitems/',views.cartitems),
    path('removecart/<int:id>/',views.removecart,name='removecart'),
    path('buyitems/<int:id>/',views.buyitems,name='buyitems'),
    path('addDeliveryDetails/<int:id>/',views.addDeliveryDetails,name='addDeliveryDetails'),
    path('history/',views.history),
    path('order/',views.order),
    path('notification/',views.notification),
    path('buyerprofile/',views.buyerprofile),
    path('addressform/',views.addAddress),
    path('checkout/<int:id>/',views.checkout,name='checkout'),
    path('buyallproduct/',views.buyallproduct),
    path('checkoutallprod/',views.checkoutallprod),
]
