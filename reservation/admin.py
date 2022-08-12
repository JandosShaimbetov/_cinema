from django.contrib import admin

from reservation.models import Discount, Reservation, Room, Seat, TicketType

admin.site.register(Room)
admin.site.register(Seat)
admin.site.register(Reservation)
admin.site.register(TicketType)
admin.site.register(Discount)
