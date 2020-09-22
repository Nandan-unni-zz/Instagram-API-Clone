from django.test import TestCase
from colorama import Fore, Style
from rest_framework.test import APIClient

client = APIClient()

def message(msg):
    print(Fore.MAGENTA, Style.BRIGHT, '\b\b\b[#]', Fore.RED, msg, Style.RESET_ALL)


class LoginUserTest(TestCase):

    def test_login_user_success(self):
        message('Testing Login User API')
        client.post('/create/',
                    {'full_name': 'Test User A',
                     'username': 'test_user_a',
                     'email': 'testusera@gmail.com',
                     'password': 'test1user1a'})
        response = client.post('/login/',
                               {'username': 'test_user_a',
                                'password': 'test1user1a'})
        self.assertEqual(response.status_code, 200)

    def test_login_user_failure(self):
        message('Testing Login User API')
        client.post('/create/',
                    {'full_name': 'Test User A',
                     'username': 'test_user_a',
                     'email': 'testusera@gmail.com',
                     'password': 'test1user1a'})
        response = client.post('/login/',
                               {'username': 'test_user_a',
                                'password': 'a_wrong_password'})
        self.assertEqual(response.status_code, 203)


class CreateUserTest(TestCase):

    def test_create_user_success(self):
        message('Testing Create User API')
        response = client.post('/create/',
                               {'full_name': 'Test User A',
                                'username': 'test_user_a',
                                'email': 'testusera@gmail.com',
                                'password': 'test1user1a'})
        self.assertEqual(response.status_code, 201)

    def test_create_user_failure(self):
        response = client.post('/create/',
                               {'full_name': 'Test User A',
                                'email': 'testusera@gmail.com',
                                'password': 'test1user1a'})
        self.assertEqual(response.status_code, 203)


class UpdateUserTest(TestCase):

    def test_update_user_success(self):
        message('Testing Update User API')
        client.post('/create/',
                    {'full_name': 'Test User A',
                     'username': 'test_user_a',
                     'email': 'testusera@gmail.com',
                     'password': 'test1user1a'})
        response = client.patch('/update/1/',
                                {'full_name': 'Test User 1'})
        self.assertEqual(response.status_code, 200)

    def test_update_user_failure(self):
        client.post('/create/',
                    {'full_name': 'Test User A',
                     'username': 'test_user_a',
                     'email': 'testusera@gmail.com',
                     'password': 'test1user1a'})
        response = client.patch('/update/1/',
                                {'full_name': 'Test User A with a name more than 30 letters.'})
        self.assertEqual(response.status_code, 400)


class DeleteUserTest(TestCase):

    def test_delete_user_success(self):
        message('Testing Delete User API')
        client.post('/create/',
                    {'full_name': 'Test User A',
                     'username': 'test_user_a',
                     'email': 'testusera@gmail.com',
                     'password': 'test1user1a'})
        response = client.post('/delete/1/', {'password': 'test1user1a'})
        self.assertEqual(response.status_code, 204)

    def test_delete_user_failure(self):
        client.post('/create/',
                    {'full_name': 'Test User A',
                     'username': 'test_user_a',
                     'email': 'testusera@gmail.com',
                     'password': 'test1user1a'})
        response = client.post('/delete/1/', {'password': 'a_wrong_password'})
        self.assertEqual(response.status_code, 203)


class FollowUserTest(TestCase):

    def test_follow_user_success(self):
        message('Testing Follow User API')
        client.post('/create/',
                    {'full_name': 'Test User A',
                     'username': 'test_user_a',
                     'email': 'testusera@gmail.com',
                     'password': 'test1user1a'})
        client.post('/create/',
                    {'full_name': 'Test User B',
                     'username': 'test_user_b',
                     'email': 'testuserb@gmail.com',
                     'password': 'test1user1b'})
        response = client.get('/follow/1/2/')
        self.assertEqual(response.status_code, 200)

    def test_follow_user_failure(self):
        message('Testing Follow User API')
        client.post('/create/',
                    {'full_name': 'Test User A',
                     'username': 'test_user_a',
                     'email': 'testusera@gmail.com',
                     'password': 'test1user1a'})
        client.post('/create/',
                    {'full_name': 'Test User B',
                     'username': 'test_user_b',
                     'email': 'testuserb@gmail.com',
                     'password': 'test1user1b'})
        response = client.get('/follow/4/2/')
        self.assertEqual(response.status_code, 404)
