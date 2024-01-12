from django.contrib import admin
from django.urls import path
from dashboard_app import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index',views.index),
    path('submit',views.submit),
    path('',views.dashboard),
    path('register_employee',views.register_employee),
    path('submit_emp_register',views.submit_emp_register),

]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

