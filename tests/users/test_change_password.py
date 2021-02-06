from rest_framework.test import APITestCase
from rest_framework import status
from users.models import CustomUser


class ChangePasswordTestCase(APITestCase):
    '''
        Creating a user for change_password api
    '''
    def setUp(self):
        self.email = "test@gmail.com"
        self.password = "testmode"
        self.otp = "1234"

        self.user = CustomUser.objects.create_user(
            email = self.email,
            username = self.email,
            first_name = "test",
            last_name = "ltest",
            contact = "+919999999999",
            password = "password"
        )

    def tearDown(self):
        self.user.delete()

    def test_fail_incorrect_emailformat(self):
        '''
            Test with incorrect email format
        '''
        data = {
            "email" : 'wrong.email.com',
            "password" : self.password,
            "otp" : self.otp
        }
        response = self.client.post("/users/change_password/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_fail_without_email(self):
        '''
            Test without email field
        '''
        data = {
            "password" : self.password,
            "otp" : self.otp
        }
        response = self.client.post("/users/change_password/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_fail_without_password(self):
        '''
            Test without password field
        '''
        data = {
            "email" : self.email,
            "otp" : self.otp
        }
        response = self.client.post("/users/change_password/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_fail_without_otp(self):
        '''
            Test without otp field
        '''
        data = {
            "email" : self.email,
            "password" : self.password
        }
        response = self.client.post("/users/change_password/", data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_fail_unregistered_email(self):
        '''
            Test for unregistered email
        '''
        data = {
            "email" : "unregistermail@gmail.com",
            "password" : self.password,
            "otp" : self.otp
        }
        response = self.client.post("/users/change_password/", data)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_success_with_correctdata(self):
        '''
            Generating otp using forgot_password api
        '''
        response1 = self.client.post("/users/forgot_password/", {"email" : self.email})

        '''
            Checking the credentials and get the user
        '''
        user = CustomUser.objects.get(email=self.email)
        data = {
            "email": self.email,
            "password": self.password,
            "otp": user.otp
        }
        response = self.client.post("/users/change_password/", data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        '''
            Getting confirmed whether the password changed with login_api
        '''
        data1 = {
            "email" : self.email,
            "password" : self.password
        }
        response2 = self.client.post("/users/login/", data1)
        self.assertEqual(response2.status_code, status.HTTP_202_ACCEPTED)

    def test_fail_incorrect_otp(self):
        '''
            Generating otp using forgot_password api
        '''
        response1 = self.client.post("/users/forgot_password/", {"email": self.email})

        '''
            Checking the credentials and get the user
        '''
        user = CustomUser.objects.get(email=self.email)
        data = {
            "email": self.email,
            "password": self.password,
            "otp": self.otp
        }
        response = self.client.post("/users/change_password/", data)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)
        
