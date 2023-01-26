import json

from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient

from .views import CalculationView

requests = APIRequestFactory()


class CalculationTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        super().setUp()

    def testAddEndpoint(self):
        payload = {"first": 1, "second": 2}
        request = requests.post("/calculation/add", data=json.dumps(payload), content_type='application/json')
        response = CalculationView.as_view({'post': 'add'})(request)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, {"result": 3})

