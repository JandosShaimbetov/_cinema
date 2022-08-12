from rest_framework import serializers

from reservation.models import Discount, Reservation, Seat, TicketType


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = Seat
        fields = ["id", "seat_number", "row", "room"]


class TicketTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = TicketType
        fields = "__all__"


class DiscountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Discount
        fields = ["id", "client"]
        read_only_fields = ["discount_card"]


class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservation
        fields = [
            "id",
            "client",
            "ticket_type",
            "price",
            "discount",
            "payment_method",
            "payment_value",
            "seat",
            "showtime",
            "reservation_date",
        ]
        read_only_fields = ["price"]

    def validate(self, attrs):
        seat = attrs.get("seat")
        showtime = attrs.get("showtime")

        if Reservation.objects.filter(seat=seat, showtime=showtime).exists():

            raise serializers.ValidationError("seat is already reserved")
        return attrs
