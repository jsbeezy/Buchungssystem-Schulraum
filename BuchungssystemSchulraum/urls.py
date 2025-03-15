from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views
from . import BookingController

urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('class-room/<int:id>/add-booking', views.ClassRoomAddBookingView.as_view(), name='class_room_add_booking'),
    path('class-room/<int:id>/options', views.ClassRoomOptionsView.as_view(), name='class_room_options_select'),
    path('class-room/<int:id>/bookings', views.ClassRoomBookingsView.as_view(), name='class_room_bookings'),
    path('bookings', BookingController.BookingForUserView.as_view(), name='view_bookings'),
    path('bookings/<int:id>/add/', BookingController.AddBookingView.as_view(), name='add_booking'),
    path('bookings/<int:id>/edit', BookingController.EditBookingView.as_view(), name='edit_booking'),
    path('bookings/<int:id>', BookingController.ShowEditBookingView.as_view(), name='show_edit_booking'),
    path('bookings/<int:id>/delete', BookingController.DeleteBookingView.as_view(), name='delete_booking'),
]

app_name = "BuchungssystemSchulraum"
