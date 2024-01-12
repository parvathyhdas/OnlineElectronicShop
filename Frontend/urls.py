from django.urls import path
from Frontend import views

urlpatterns = [path('homePage/',views.homePage,name="homePage"),
                path('productStore/',views.productStore,name="productStore"),
                path('single_productPage/<int:proid>/',views.single_productPage,name="single_productPage"),
                path('productFiltered/<cat_name>/',views.productFiltered,name="productFiltered"),
                path('aboutPage/',views.aboutPage,name="aboutPage"),
                path('contactPage/',views.contactPage,name="contactPage"),
                path('services/',views.services,name="services"),
                path('saveContact/',views.saveContact,name="saveContact"),
                path('RegisterPage/',views.RegisterPage,name="RegisterPage"),
                path('saveRegister/',views.saveRegister,name="saveRegister"),
                path('',views.UserLogin,name="UserLogin"),
                path('UserLogout/',views.UserLogout,name="UserLogout"),
                path('cartPage/',views.cartPage,name="cartPage"),
                path('saveCart/',views.saveCart,name="saveCart"),
                path('deletecart/<int:dataid>/',views.deletecart,name="deletecart"),
                path('checkoutPage/',views.checkoutPage,name="checkoutPage"),

               ]