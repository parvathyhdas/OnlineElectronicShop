from django.urls import path
from ShopApp import views

urlpatterns = [path('indexPage/',views.indexPage,name="indexPage"),
                path('addShop/',views.addShop,name="addShop"),
                path('saveshop/',views.saveshop,name="saveshop"),
                path('addCategory/',views.addCategory,name="addCategory"),
                path('saveCategory/',views.saveCategory,name="saveCategory"),
                path('displayCategory/',views.displayCategory,name="displayCategory"),
                path('editCategory/<int:dataid>/',views.editCategory,name="editCategory"),
                path('updateCategory/<int:dataid>/',views.updateCategory,name="updateCategory"),
                path('deleteCategory/<int:dataid>/',views.deleteCategory,name="deleteCategory"),
                path('AddProduct/',views.AddProduct,name="AddProduct"),
                path('saveProduct/',views.saveProduct,name="saveProduct"),
                path('displayProduct/',views.displayProduct,name="displayProduct"),
                path('editProduct/<int:dataid>/',views.editProduct,name="editProduct"),
                path('updateProduct/<int:dataid>/',views.updateProduct,name="updateProduct"),
                path('deleteProduct/<int:dataid>/',views.deleteProduct,name="deleteProduct"),
                path('adminLogin/',views.adminLogin,name="adminLogin"),
                path('adminLoginPage/',views.adminLoginPage,name="adminLoginPage"),
                path('admin_logout/',views.admin_logout,name="admin_logout"),
                path('displayContact/',views.displayContact,name="displayContact"),
                path('deleteContact/<int:dataid>/',views.deleteContact,name="deleteContact"),
               ]