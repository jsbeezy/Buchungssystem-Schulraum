from django.urls import path
from django.contrib import admin
from django.contrib.auth import views as auth_views

from . import views_index
from . import views_bookings

urlpatterns = [
    # Index view
    path("", views_index.HomeView.as_view(), name="index"),

    # Auth views
    path('admin/', admin.site.urls),
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),

    # Booking views
    path('class-room/<int:id>/options', views_bookings.ClassRoomOptionsView.as_view(), name='class_room_options_select'),
    path('class-room/<int:id>/add-booking', views_bookings.AddBookingToClassroom.as_view(), name='class_room_add_booking'),
    path('class-room/<int:id>/bookings', views_bookings.ClassRoomBookingsView.as_view(), name='class_room_bookings'),
    path('bookings', views_bookings.BookingForUserView.as_view(), name='view_bookings'),
    path('bookings/<int:id>/add/', views_bookings.AddBookingView.as_view(), name='add_booking'),
    path('bookings/<int:id>/edit', views_bookings.EditBookingView.as_view(), name='edit_booking'),
    path('bookings/<int:id>', views_bookings.ShowEditBookingView.as_view(), name='show_edit_booking'),
    path('bookings/<int:id>/delete', views_bookings.DeleteBookingView.as_view(), name='delete_booking'),
    path('class-room/search', views_bookings.RoomSearchView.as_view(), name='room_search'),
]

app_name = "BuchungssystemSchulraum"
