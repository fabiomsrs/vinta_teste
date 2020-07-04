from django.test import TestCase
from model_mommy import mommy


class TestUser(TestCase):

    def setUp(self):
        self.user = mommy.make('users.User', email='email')

    def test_to_representation(self):
        self.assertEqual(str(self.user),self.user.email)