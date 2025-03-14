from django.urls import path

from . import views
from . import BookingController

app_name = "BuchungssystemSchulraum"
urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path('class-room/<int:id>/', views.ClassRoomView.as_view(), name='view_room'),
    path('bookings', BookingController.BookingsView.as_view(), name='view_bookings'),
    path('bookings/<int:id>/add/', BookingController.AddBookingView.as_view(), name='add_booking'),
    path('bookings/<int:id>/edit', BookingController.EditBookingView.as_view(), name='edit_booking'),
    path('bookings/<int:id>/delete', BookingController.DeleteBookingView.as_view(), name='delete_booking'),
]
