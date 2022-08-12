from django.test import TestCase

from movie.models import Cinema, Movie, Room, Showtime


class TestMovieModel(TestCase):
    def test_str_method(self):
        movie = Movie.objects.create(name="test_name", description="test_desc")
        m_l_n = movie._meta.get_field("name").max_length
        m_l_d = movie._meta.get_field("description").max_length
        self.assertEqual(movie.__str__(), "test_name")
        self.assertEqual(m_l_n, 255)
        self.assertEqual(m_l_d, 255)


class TestCinemaModel(TestCase):
    def test_str_method(self):
        cinema = Cinema.objects.create(
            name="test_name",
            description="test_desc",
            address="test_address",
            contact="test_contact",
            open_time="09:00:00",
            close_time="18:00:00",
        )
        self.assertEqual(cinema.__str__(), "test_name")

    def test_max_length(self):
        cinema = Cinema.objects.create(
            name="test_name",
            description="test_desc",
            address="test_address",
            contact="test_contact",
            open_time="09:00:00",
            close_time="18:00:00",
        )
        m_l_n = cinema._meta.get_field("name").max_length
        m_l_d = cinema._meta.get_field("description").max_length
        m_l_a = cinema._meta.get_field("address").max_length
        m_l_c = cinema._meta.get_field("contact").max_length
        self.assertEqual(m_l_n, 255)
        self.assertEqual(m_l_d, 255)
        self.assertEqual(m_l_a, 255)
        self.assertEqual(m_l_c, 200)


class TestRoomModel(TestCase):
    def test_str_method(self):
        cinema = Cinema.objects.create(
            name="test_name",
            description="test_desc",
            address="test_address",
            contact="test_contact",
            open_time="09:00:00",
            close_time="18:00:00",
        )
        m_l = cinema._meta.get_field("name").max_length
        room = Room.objects.create(name="test_name", cinema=1)
        self.assertEqual(room.__str__(), "test_name")
        self.assertEqual(m_l, 200)

    def test_max_length(self):
        cinema = Cinema.objects.create(
            name="test_name",
            description="test_desc",
            address="test_address",
            contact="test_contact",
            open_time="09:00:00",
            close_time="18:00:00",
        )
        m_l = cinema._meta.get_field("name").max_length
        self.assertEqual(m_l, 200)


class TestShowTimeModel(TestCase):
    def test_str_method(self):
        movie = Movie.objects.create(name="test_name", description="test_desc")
        cinema = Cinema.objects.create(
            name="test_name",
            description="test_desc",
            address="test_address",
            contact="test_contact",
            open_time="09:00:00",
            close_time="18:00:00",
        )
        room = Room.objects.create(name="test_name", cinema=cinema)
        show_time = Showtime.objects.create(
            movie=movie, room=room, start_time="03/08/2022 09:00", end_time="03/08/2022 12:00"
        )
        self.assertEqual(show_time.__str__(), "1 in 1 at 03/08/2022 09:00")
