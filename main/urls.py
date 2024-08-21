from django.urls import path
from . import views

urlpatterns = [
    #frontend
    path('', views.home, name='home'),
    path('services/', views.service, name='services'),
    path('gallery/headboards/', views.headboard, name='headboard'),
    path('gallery/couches/', views.couch, name='couch'),
    path('gallery/ottomans/', views.ottoman, name='ottoman'),
    path('gallery/blanket_boxes/', views.blanket_box, name='blanket_box'),
    path('gallery/lamp_shades/', views.lamp_shade, name='lamp_shade'),
    path('gallery/curtains/', views.curtain, name='curtain'),
    path('gallery/chairs/', views.chair, name='chair'),
    path('gallery/cushions/', views.cushion, name='cushion'),
    path('gallery/scatter_cushions/', views.scatter_cushion, name='scatter_cushion'),
    path('gallery/romand_blinds/', views.roman_blind, name='roman_blind'),
    path('blog/', views.blog, name='blog'),
    path('add_testimony/', views.add_testimony, name='add_testimony'),
    path('testimonials/', views.testimonials, name='testimonials'),
    path('job_cards/', views.job_cards, name='job_cards'),
    path('home/send_email/', views.send_email, name='send_email'),
    
    #backend
    path('register/', views.registerUser, name='userRegister'),
    path('accounts/login/', views.loginUser, name='login'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('inventory/', views.inventory, name='inventory'),
    path('clients/', views.client, name='clients'),
    path('view_job_cards/', views.viewJobCards, name='viewJobCards'),
    path('add_job/', views.add_job, name='add_job'),
    path('upload_image/', views.add_product, name='add_product'),
    path('all_jobs/', views.allJobs, name='all_jobs'),
    
    path('logout/', views.logoutUser, name='logout')
    
    
]
