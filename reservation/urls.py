from django.urls import path

from reservation.views import (DiscountList, ReservList, SeatList,
                               TicketTypeList)

urlpatterns = [
    path("seats/", SeatList.as_view(), name="seats"),
    path("tickets/", TicketTypeList.as_view(), name="tickets"),
    path("tickets/<int:pk>/", TicketTypeList.as_view(), name="ticket-detail"),
    path("discount/", DiscountList.as_view(), name="discount"),
    path("", ReservList.as_view(), name="reservations"),
]
