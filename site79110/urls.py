from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views  # ✅ Import auth views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),  # ✅ Include your app's URLs

    # ✅ Login and Logout URLs using Django's built-in views
    path('accounts/login/', auth_views.LoginView.as_view(), name='login'),
    path('accounts/logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),
]
