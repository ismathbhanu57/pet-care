"""
URL configuration for pets_cares_owners_communication_systems project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from pets_cares_owners_communication_systems_app import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index,name="index"),
    path('about',views.about,name="about"),
    path('blog',views.blog,name="blog"),
    path('blog_details',views.blog_details,name="blog_details"),
    path('contact',views.contact,name="contact"),
    path('services',views.services,name="services"),
    path('customer_login',views.customer_login,name="customer_login"),
    path('customer_register',views.customer_register,name="customer_register"),
    path('customer_home',views.customer_home,name="customer_home"),
    path('my_profile',views.my_profile,name="my_profile"),
    path('customer_logout',views.customer_logout,name="customer_logout"),
    path('admin_home',views.admin_home,name="admin_home"),
    path('admin_view_contact',views.admin_view_contact,name="admin_view_contact"),
    path('admin_view_customer',views.admin_view_customer,name="admin_view_customer"),
    path('admin_logout',views.admin_logout,name="admin_logout"),
    path('admin_login', views.admin_login, name="admin_login"),
    path('accept_customer/<int:id>',views.accept_customer,name="accept_customer"),
    path('reject_customer/<int:id>',views.reject_customer,name="reject_customer"),
    path('my_profile_edit',views.my_profile_edit,name="my_profile_edit"),
    path('update_my_profile',views.update_my_profile,name="update_my_profile"),
    path('doctors_home',views.doctors_home,name="doctors_home"),
    path('doctors_profile',views.doctors_profile,name="doctors_profile"),
    path('doctors_register',views.doctors_register,name="doctors_register"),

    path('doctors_login',views.doctors_login,name="doctors_login"),
    path('doctor_logout',views.doctor_logout,name="doctor_logout"),
    path('accept_appoitments/<int:id>',views.accept_appoitments,name="accept_appoitments"),
    path('reject_appoitments/<int:id>',views.reject_appoitments,name="reject_appoitments"),
    path('change_password',views.change_password,name="change_password"),
    path('admin_change_password',views.admin_change_password,name="admin_change_password"),
    path('deactivate/<int:id>',views.deactivate,name="deactivate"),
    path('add_notifications',views.add_notifications,name="add_notifications"),

    path('view_notification', views.view_notification, name="view_notification"),
    path('add_pet',views.add_pet,name="add_pet"),
    # path('templates',views.my_pets,name="templates"),
    path('add_pet',views.add_pet,name="add_pet"),
    path('my_pets',views.my_pets,name="my_pets"),
    path('view_doctors', views.view_doctors, name="view_doctors"),
    path('delete_view_notification/<int:id>',views.delete_view_notification,name="delete_view_notification"),
    path('delete_view_pet/<int:id>', views.delete_view_pet, name="delete_view_pet"),
    path('pet_edit/<int:id>',views.pet_edit,name="pet_edit"),
    path('delete_view_doctor/<int:id>', views.delete_view_doctor, name="delete_view_doctor"),
    path('pet_update',views.pet_update,name="pet_update"),
    path('book_now/<int:id>',views.book_now,name="book_now"),
    path('view_bookings', views.view_bookings, name="view_bookings"),
    path('add_prescriptions/<int:id>', views.add_prescriptions, name="add_prescriptions"),
    path('view_precautions', views.view_precautions, name="view_precautions"),

    path('add_precautions', views.add_precautions, name="add_precautions"),
    path('quote_view', views.quote_view, name='quote_view'),
    path('add_quote',views.add_quote, name="add_quote"),
    path('add_reviews/<int:id>', views.add_reviews, name="add_reviews"),
    path('view_reviews/<int:id>', views.view_reviews, name="view_reviews"),
    path('doctors_view_reviews', views.doctors_view_reviews, name='doctors_view_reviews'),
    path('view_prescription',views.view_prescription, name='view_prescription'),
    path('customers_view_notification', views.customers_view_notification, name="customers_view_notification"),
    path('view_all_pets', views.view_all_pets, name='view_all_pets'),
    path('admin_view_doctors', views.admin_view_doctors, name='admin_view_doctors'),

    path('accept_doctors/<int:id>', views.accept_doctors, name="accept_doctors"),
    path('reject_doctors/<int:id>', views.reject_doctors, name="reject_doctors"),
    path('doctors_profile_edit', views.doctors_profile_edit, name='doctors_profile_edit'),
    path('update_doctors_profile', views.update_doctors_profile, name='update_doctors_profile'),
    path('doctors_change_password', views.doctors_change_password, name='doctors_change_password'),
    path('customers_view_precautions', views.customers_view_precautions, name='customers_view_precautions'),
    path('add_appoitments/<int:id>', views.add_appoitments, name='add_appoitments'),

    path('my_appoitments', views.my_appoitments, name='my_appoitments'),
    path('doctors_view_appoitments', views.doctors_view_appoitments, name='doctors_view_appoitments'),
    path('view_prescriptions/<int:id>', views.view_prescriptions, name='view_prescriptions'),
    path('view_all_customers', views.view_all_customers, name='view_all_customers'),
    path('add_friends_requests/<int:id>', views.add_friends_requests, name='add_friends_requests'),
    path('view_friends_requests', views.view_friends_requests, name='view_friends_requests'),
    path('accept_friends_requests/<int:id>', views.accept_friends_requests, name='accept_friends_requests'),
    path('reject_friends_requests/<int:id>', views.reject_friends_requests, name='reject_friends_requests'),
    path('my_friends', views.my_friends, name='my_friends'),
    path('add_posts', views.add_posts, name='add_posts'),
    path('my_posts', views.my_posts, name='my_posts'),
    path('view_posts', views.view_posts, name='view_posts'),
    path('admin_view_posts', views.admin_view_posts, name='admin_view_posts'),
    path('accept_posts/<int:id>', views.accept_posts, name='accept_posts'),
    path('reject_posts/<int:id>', views.reject_posts, name='reject_posts'),
    path('posts_edit/<int:id>', views.posts_edit, name='posts_edit'),
    path('posts_update', views.posts_update, name='posts_update'),
    path('delete_posts/<int:id>', views.delete_posts, name='delete_posts'),
    path('like_post/<int:post_id>', views.like_post, name='like_post'),


    path('view_posts_likes/<int:id>', views.view_posts_likes, name='view_posts_likes'),
    path('add_comments/<int:id>', views.add_comments, name='add_comments'),
    path('view_posts_comments/<int:id>', views.view_posts_comments, name='view_posts_comments'),
    path('express_interest/<int:pet_id>', views.express_interest, name='express_interest'),




    path('toggle_sell_status/<int:id>', views.toggle_sell_status, name='toggle_sell_status'),
    path('view_pets_requests/<int:id>', views.view_pets_requests, name='view_pets_requests'),
    path('like_pets/<int:pets_id>', views.like_pets, name='like_pets'),
    path('view_pets_likes/<int:id>', views.view_pets_likes, name='view_pets_likes'),
    path('doctors_view_notifications', views.doctors_view_notifications, name='doctors_view_notifications'),

]
if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

