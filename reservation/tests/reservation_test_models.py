from django.test import TestCase

from movie.models import Cinema
from reservation.models import Discount, Room, Seat, TicketType
from user.models import CustomUser


class TestSeatModel(TestCase):
    def test_str_method(self):
        cinema = Cinema.objects.create(
            name="test_name",
            description="test_desc",
            address="test_address",
            contact="test_contact",
            open_time="09:00:00",
            close_time="18:00:00",
        )
        room = Room.objects.create(name="test_name", cinema=cinema)
        seat = Seat.objects.create(seat_number=1, row=1, room=room)
        self.assertEqual(seat.__str__(), 1)


class TestTicketTypeModel(TestCase):
    def test_str_method(self):
        ticket = TicketType.objects.create(name="test_name", price=100)
        self.assertEqual(ticket.__str__(), "test_name")


class TestDiscountModel(TestCase):
    def test_str_method(self):
        client = CustomUser.objects.create_user(
            email="email@gmail.com", username="test_name", password="password", role=2
        )
        discount = Discount.objects.create(client=client, discount_card=1)
        self.assertEqual(discount.__str__(), "1 discount card")
