from django.contrib import admin
from django.urls import path, include
from .import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signup/', views.signup_view, name="signup"),
    path('delete/<int:id>', views.delete_v, name="delete"),
]
