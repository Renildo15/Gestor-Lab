from django.test import TestCase, Client
from django.urls import reverse
from laboratorio_app.models import Lab


class LabViewTesCase(TestCase):

    #home_view
    def test_status_code_200(self):
        response = self.client.get(reverse('laboratorio:home'))
        self.assertEquals(response.status_code, 200)

    def test_template_usado(self):
        response = self.client.get(reverse('laboratorio:home'))
        self.assertTemplateUsed(response, 'index.html')

    #view_view

