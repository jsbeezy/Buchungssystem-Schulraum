from django.urls import path
from django.contrib import admin

from . import views
from . import BookingController
from . import RoomController
from . import UserController

app_name = "BuchungssystemSchulraum"
urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path('admin/', admin.site.urls),
    path('class-room/<int:id>/', views.ClassRoomView.as_view(), name='view_room'),
    path('bookings', BookingController.BookingListView.as_view(), name='view_bookings'),
    path('bookings/<int:id>/add/', BookingController.AddBookingView.as_view(), name='add_booking'),
    path('bookings/<int:id>/edit', BookingController.EditBookingView.as_view(), name='edit_booking'),
    path('bookings/<int:id>/delete', BookingController.DeleteBookingView.as_view(), name='delete_booking'),
    path('rooms/', RoomController.RoomListView.as_view(), name='room_list'),
    path('rooms/add/', RoomController.AddRoomView.as_view(), name='add_room'),
    path('rooms/edit/<int:id>/', RoomController.EditRoomView.as_view(), name='edit_room'),
    path('rooms/delete/<int:id>/', RoomController.DeleteRoomView.as_view(), name='delete_room'),
    path('users/', UserController.UserListView.as_view(), name='user_list'),
    path('users/add/', UserController.AddUserView.as_view(), name='add_user'),
    path('users/edit/<int:id>/', UserController.EditUserView.as_view(), name='edit_user'),
    path('users/delete/<int:id>/', UserController.DeleteUserView.as_view(), name='delete_user'),
]
