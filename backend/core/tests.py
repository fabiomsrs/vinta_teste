from django.test import Client, RequestFactory, TestCase
from django.contrib.sessions.middleware import SessionMiddleware
from core.serializers import RepoSerializer
from core.models import Repo
from .views import *
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
        

class CoreViewsTestCase(TestCase):
    def setUp(self):
        # Every test needs access to the request factory.
        self.factory = RequestFactory()
    
    def test_get_commitviewset(self):
        # Create an instance of a GET request.
        request = self.factory.get('/commit/')
        view = CommitViewSet.as_view({'get':'list'})(request)
        self.assertEqual(view.status_code, 200)

    def test_get_repoviewset(self):
        # Create an instance of a GET request.
        request = self.factory.get('/repos/')
        view = RepoViewSet.as_view({'get':'list'})(request)
        self.assertEqual(view.status_code, 200)

    def test_post_repoviewset(self):
        # Create an instance of a POST request.
        body = {
            "name" : "tcc",
            "owner": {"login":"fabiomsrs"},
            "created_at": "2017-03-31T05:29:44Z"
        }
        request = self.factory.post('/repos/?access_token=123&user=fabiomsrs',body, content_type='application/json')  
        middleware = SessionMiddleware()
        middleware.process_request(request)
        request.session.save()  
        view = RepoViewSet.as_view({'post':'create'})(request)        
        self.assertEqual(view.status_code, 201)