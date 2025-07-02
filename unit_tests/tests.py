from django.test import TestCase, Client
from .forms import RegistrationForm
from .models import User
from django.urls import reverse


# Create your tests here.
class RegistrationFormTest(TestCase):
    def test_valid_registration_form(self):
        form_data = {
            'user_name' : 'testuser',
            'password1' : 'testpassword',
            'password2' : 'testpassword',
            'email' : 'test@email.com',
            'age' : 25,
            'birth_date' : '2000-02-07'
        }
        form = RegistrationForm(data = form_data)
        self.assertTrue(form.is_valid())


    def test_invalid_password(self):
        form_data1 = {
            'user_name' : 'testuser',
            'password1' : '123',
            'password2' : '123',
            'email' : 'test@email.com',
            'age' : 25,
            'birth_date' : '2000-02-07'
        }
        small_pass_form = RegistrationForm(data=form_data1)
        self.assertFalse(small_pass_form.is_valid())
        self.assertIn('password1', small_pass_form.errors)


    def test_invalid_birth_date(self):
        form_data = {
            'user_name' : 'testuser',
            'password1' : '123',
            'password2' : '123',
            'email' : 'test@email.com',
            'age': -1,
            'birth_date': '2030-01-01'
        }
        form = RegistrationForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertIn('birth_date', form.errors)


class UserModelTest(TestCase):
    def setUp(self):
        User.objects.create_user(
            user_name='testuser',
            password='testpassword',
            email='test@mail.com',
            age=25,
            birth_date='1996-01-01'
        )

    
    def test_user_creation(self):
        user = User.objects.filter(user_name='testuser').first()
        self.assertEqual(user.email, 'test@mail.com')
        self.assertEqual(user.age, 25)
        self.assertEqual(str(user.birth_date), '1996-01-01')

    def tearDown(self):
        User.objects.filter(username='testuser').delete()


    class RegisterViewTest(TestCase):
        def test_registration_view_get(self):
            client = Client()
            response = client.get(reverse('register'))
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'register.html')

        def test_register_view_post(self):
            client = Client()
            data = {
                'user_name' : 'testuser',
                'password1' : 'testpassword',
                'password2' : 'testpassword',
                'email' : 'test@email.com',
                'age' : 25,
                'birth_date' : '2000-02-07'
            }
            response = client.post(reverse('register'), data=data)
            self.assertEqual(response.status_code, 302)
            self.assertRedirects(response, reverse('login'))

            user = User.objects.get(username='testuser')
            self.assertEqual(user.email, 'john.doe@example.com')
            self.assertEqual(user.age, 25)
            self.assertEqual(str(user.birth_date), '1996-01-01')