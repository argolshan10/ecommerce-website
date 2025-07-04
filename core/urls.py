from django.urls import path 
from . import views 

urlpatterns = [
    path('' , views.home , name = 'home') , 
    path('about/' , views.About , name = 'About') , 
    path('login/' , views.login_user , name = 'login') , 
    path('logout/' , views.logout_user , name = 'logout') ,   
    path('register/' , views.register_user , name = 'register') ,
    path('update_password/' , views.update_password , name = 'update_password') ,
    path('update_user/' , views.update_user , name = 'update_user') ,
    path('update_info/' , views.update_info , name = 'update_info') ,
    path('product/<int:pk>' , views.product_detail , name = 'product') , 
    path('category/<str:sth>' , views.category_detail , name='category') ,
    path('category_summary/' , views.category_summary , name='category_summary') ,
    path('search/' , views.search , name = 'search') ,
] 
 
