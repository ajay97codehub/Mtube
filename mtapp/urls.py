from django.urls import path
from . import views


urlpatterns = [
    path('', views.home_page),
    path('home_page/', views.home_page),
    path('search/', views.search_page),
    path('contact/', views.contact_page),
    path('about/', views.about_page),
    # path('download/', views.download_page),
    path('download/<str:m_id>/', views.download_page),
]