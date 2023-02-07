from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from rest_framework.authtoken.models import Token


class EventAPITestCase(APITestCase):
    def test_post(self):
        user = User.objects.create_user(username='john', password='glass onion')
        url = reverse('event-list')

        client = APIClient()
        client.post('/login/', {'username': 'john', 'password': 'glass onion'}, format='json')
        token = Token.objects.get(user__username='john')
        client.credentials(HTTP_AUTHORIZATION='Token ' + token.key)

        data = {
            "event_type": 'HW',
            "info": {1: 2},
            "timestamp": "2023-01-02 01:01:01"
        }

        incorect_data = {
            "event_type": 1,
            "info": {1: 2},
            "timestamp": "2023-01-02 01:01:01"
        }

        expected_data = {
            "event_type": 1,
            "info": {1: 2},
            "timestamp": "2023-01-02 01:01:01"
        }

        response_1 = client.post(url, data, format='json')
        response_2 = client.post(url, data, format='json')
        response_3 = client.post(url, incorect_data, format='json')

        self.assertEqual(response_1.status_code, status.HTTP_200_OK)
        self.assertEqual(response_2.data['title']['event_type'], expected_data['event_type'])
        self.assertEqual(response_3.data, 'incorrect request')

