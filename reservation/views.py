import decimal

from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView

from reservation.models import Discount, Reservation, Seat, TicketType
from reservation.serializers import (DiscountSerializer, ReservationSerializer,
                                     SeatSerializer, TicketTypeSerializer)
from user.permissions import IsAdminOrReadOnly, IsAuthenticated


class SeatList(generics.ListCreateAPIView):
    queryset = Seat.objects.all()
    serializer_class = SeatSerializer
    permission_classes = (IsAdminOrReadOnly,)


class TicketTypeList(generics.ListCreateAPIView):
    serializer_class = TicketTypeSerializer
    queryset = TicketType.objects.all()


class TicketTypeDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = TicketTypeSerializer
    queryset = TicketType.objects.all()


class DiscountList(generics.ListCreateAPIView):
    serializer_class = DiscountSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Discount.objects.filter(client=self.request.user)

    def perform_create(self, serializer):
        serializer.save(client=self.request.user)


class ReservList(APIView):
    serializer_class = ReservationSerializer
    # permission_classes = (IsAuthenticated,)

    def get(self, request):
        reservation = Reservation.objects.filter(client=request.user)
        serializer = ReservationSerializer(reservation, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ReservationSerializer(data=request.data)
        if serializer.is_valid():

            showtime = serializer.validated_data["showtime"]
            seat = serializer.validated_data["seat"]
            ticket_type = serializer.validated_data["ticket_type"]
            payment_method = serializer.validated_data["payment_method"]
            discount = serializer.validated_data["discount"]
            payment_value = serializer.validated_data["payment_value"]

            reservation = Reservation.objects.create(
                client=request.user,
                ticket_type=ticket_type,
                discount=discount,
                payment_method=payment_method,
                payment_value=payment_value,
                seat=seat,
                showtime=showtime,
            )

            if reservation:
                discount = Discount.objects.filter(client=self.request.user).first()
                discount.discount_card = discount.discount_card + (
                    decimal.Decimal(reservation.ticket_type.price / 100 * 3)
                )
                discount.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
