
from django.urls import path
from Regs import views
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('',views.home,name='home'),
    
]
