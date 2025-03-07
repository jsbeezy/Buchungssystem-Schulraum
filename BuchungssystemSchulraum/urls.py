from django.urls import path

from . import views

app_name = "BuchungssystemSchulraum"
urlpatterns = [
    path("", views.HomeView.as_view(), name="index"),
    path('class-room/<str:id>/book/', views.ClassRoomBookView.as_view(), name='book_room'),
]
