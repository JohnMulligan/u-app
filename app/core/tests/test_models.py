#TestCase is a built-in method for django to facilitate unit testing
from django.test import TestCase

##there is a get user model helper in django
from django.contrib.auth import get_user_model

#define a custom model for tests, building on the TestCase model
#and presumably we'll be using the native user model he defined
class ModelTests(TestCase):
    def test_create_user_with_email_successful(self):
        email = 'johnm@test.com'
        password = 'pass'
        user=get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email,email)
        self.assertTrue(user.check_password(password))
    
    def test_new_user_email_normalized(self):
        #est the email for a new user is normalized by our user class function
        email='john@TEST.com'
        user=get_user_model().objects.create_user(email,'test')
        self.assertEqual(user.email)
