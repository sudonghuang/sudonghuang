from django.test import TestCase
from  django.shortcuts import reverse
# Create your tests here.
class Test_to_register(TestCase):
    def test_status_code(self):
        response=self.client.get(reverse("toRegister"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'auth/注册.html')

class Test_register(TestCase):
    def test_status_code(self):
        response=self.client.get(reverse("register"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'auth/login.html')

class Test_tologin(TestCase):
    def test_status_code(self):
        response=self.client.get(reverse("tologin"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'auth/login.html')


class Test_login(TestCase):
    def test_status_code(self):
        response=self.client.get(reverse("login"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'auth/tophoto.html')


class Test_toupload(TestCase):
    def test_status_code(self):
        response=self.client.get(reverse("toupload"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'auth/tophoto.html')


class Test_upload(TestCase):
    def test_status_code(self):
        response=self.client.get(reverse("upload"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'auth/load.html')


class Test_upload_image(TestCase):
    def test_status_code(self):
        response=self.client.get(reverse("image_upload"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'upload_image.html')


class Test_view(TestCase):
    def test_status_code(self):
        response=self.client.get(reverse("image_view"))
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'view_image.html')


