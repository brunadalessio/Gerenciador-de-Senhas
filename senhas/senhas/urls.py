from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from main.forms import LoginForm

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include("main.urls")),
    path('login/', auth_views.LoginView.as_view(template_name="registration/login.html", authentication_form=LoginForm), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name= 'logout'),
]

urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)