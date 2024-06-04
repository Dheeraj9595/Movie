from django.urls import path
from . import views

urlpatterns = [
	path('', views.seats),
	path('book/', views.book),
        path('ticket/',views.ticket),
        path('bookings/',views.bookings),
        path('cancel_ticket/<int:ticket_id>/', views.cancel_ticket, name='cancel_ticket'),
]