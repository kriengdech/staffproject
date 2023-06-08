"""StaffProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from App import views


urlpatterns = [
    #path to access the admin page
    path('admin/', admin.site.urls),
    #path to render HomePage
    path('', views.frontend,name = 'frontend'), 
    #path Login/Logout
    path('login/', include('django.contrib.auth.urls')), 
    # ===============
    # Backend Section
    # ===============
    path('backend/', views.backend,name = 'backend'),  
    #คำอธิบาย   1.backend/ คือ browser url 2.views.backend คือ function ใน views
    #  name ='backend' คือ url inside html file  
    #
    #path to add new staff
    path('add_staff', views.add_staff,name = 'add_staff'),   

    #path to access the staff individually
    path('staff/<str:staff_id>', views.edit_staff,name = 'edit_staff'), 

    #path to save staff
    path('save_staff', views.save_staff,name = 'save_staff'),  

    #path to delete the staff 
    path('delete_staff/<str:staff_id>', views.delete_staff,name = 'delete_staff')     

]
