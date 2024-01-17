from django.contrib import admin
from django.urls import path
from dashboard_app import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index),
    path('submit',views.submit),
    path('',views.home),
    path('u_login',views.u_login),
    path('register_employee',views.register_employee),
    path('submit_emp_register',views.submit_emp_register),
    path('employees_table',views.employee_table),
    path('dashboard',views.dashboard),
    path('c_user',views.c_user),
    path('login_page',views.login_page),
    path('edit/<id>',views.edit),
    path('delete/<str:id>',views.delete),
    path('update/<id>', views.update),
    

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

