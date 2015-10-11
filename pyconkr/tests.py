# -*- coding: utf-8 -*-

import pytest
from django.test import TestCase
from django.http import HttpResponse
from django.test import Client
from django.core.urlresolvers import reverse_lazy, reverse
from django.contrib.auth import get_user_model

from pyconkr.helper import render_io_error

User = get_user_model()


@pytest.mark.django_db
class HelperFunctionTestCase(TestCase):
    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_render_io_error(self):
        a = render_io_error("test reason")
        self.assertEqual(a.status_code, 406, "render io error status code must be 406")


@pytest.mark.django_db
class PaymentTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user('testname', 'test@test.com', 'testpassword')
        self.client.login(username='testname', password='testpassword')

    def tearDown(self):
        pass

    def test_view_registration_payment(self):
        a = 1
        url = reverse('registration_payment')
        response = self.client.post(url, {'test': 1})
        self.assertNotEqual(response['content-type'], 'application/javascript', 'error raise and must be ajax' )
