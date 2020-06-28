from django.test import TestCase
from core.serializers import RepoSerializer
from core.models import Repo
import datetime

# Create your tests here.

class RepoSerializerTestCase(TestCase):
    def setUp(self):
        self.repo_attributes = {
            "name":"repo",
            "owner":"bob",
            "date": datetime.datetime.today(),
            "user": "bob",
        }

        self.serializer_data = {
            "name":"repo",
            "owner":"jake",
            "date": datetime.datetime.today(),
            "user": "bob",
        }

        self.repo = Repo.objects.create(**self.repo_attributes)
        self.serializer = RepoSerializer(instance=self.repo)

    def test_contains_expected_fields(self):
        data = self.serializer.data
        print(data.keys())
        self.assertEqual(set(data.keys()), set(["id",'name',"owner","date","user","commits"]))

    def test_name_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['name'], self.repo_attributes['name'])

    def test_owner_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['owner'], self.repo_attributes['owner'])

    def test_date_field_content(self):
        data = self.serializer.data
        date = self.repo_attributes['date'].strftime("%d/%m/%Y %H:%M:%S")
        self.assertEqual(data['date'], date)

    def test_user_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['user'], self.repo_attributes['user'])
    
    def test_repo_exists(self):
        serializer = RepoSerializer(data=self.serializer_data)
        serializer.is_valid()
        serializer.save()

        serializer = RepoSerializer(data=self.serializer_data)        
        
        self.assertFalse(serializer.is_valid())
        