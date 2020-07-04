from common.utils.tests import TestCaseUtils
from model_mommy import mommy

class TestUserView(TestCaseUtils):

    def test_login_normal_user(self):
        self.social = mommy.prepare("users.SocialUser", user=self.user)        
        self.social.save()
        response = self.auth_client.get(self.reverse('users:login'))
        self.assertResponse302(response)
    
    def test_login_super_user(self):        
        self.user.is_staff = True
        self.user.save()
        response = self.auth_client.get(self.reverse('users:login'))          
        self.assertResponse200(response)
    
    def test_retrieve(self):
        self.social = mommy.prepare("users.SocialUser", user=self.user)        
        self.social.save()
        response = self.auth_client.get(self.reverse('users:get_user'))
        self.assertResponse200(response)

    def test_retrieve_with_no_social(self):        
        response = self.auth_client.get(self.reverse('users:get_user'))        
        self.assertResponse401(response)
