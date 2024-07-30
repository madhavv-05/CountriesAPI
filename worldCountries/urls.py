from django.contrib import admin
from django.urls import path
from countries import views


urlpatterns = [
    path('admin/', admin.site.urls),

    path('api/countries/', views.countries_list),
    path('api/countries/<int:pk>/', views.countries_detail),

]
