from datetime import datetime
from django.urls import reverse
from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from recortes.models import RecortesRecorte
from recortes.serializers import RecortesSerializer



class RecortesAPITests(APITestCase):
    multi_db = True

    def setUp(self):
        get_user_model().objects \
            .create_user(
                'spiderman', 
                'spider@man.com',
                'spiderman'
            )
        

        numbers_recortes = (30, 40, 50)
        for number in numbers_recortes:
            for i in range(0, number):
                RecortesRecorte.objects.create(
                    data_criacao=datetime.now(),
                    numeracao_unica='{}{}'.format(number, number),
                    recorte='{} registers of this'.format(number),
                    data_publicacao=datetime.now(),
                    codigo_diario='COD{}'.format(number),
                    novo_recorte=True,
                )

    def test_api(self):
        
        url = reverse('recortes')
        client = APIClient()

        # testing the request can't complete without authentication
        params = {'test': 'test'}
        response = client.get(url, kwargs=params)
        self.assertEqual(
            response.status_code,
            status.HTTP_401_UNAUTHORIZED,
            "Asserting user can't request without authentication"
        )
        
        # testing parameters

        client.login(username='spiderman', password='spiderman')

        response = client.get(url, kwargs=params)
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
            "Asserting error when request without an obligatory parameter"
        )

        params = {'nup': 'nup'}
        response = client.get(url, kwargs=params)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            "Asserting can request with \"nup\" parameter"
        )

        params = {'q': 'query'}
        response = client.get(url, kwargs=params)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            "Asserting can request with \"q\" parameter"
        )

        params = {'q': 'query'}
        response = client.get(url, kwargs=params)
        self.assertEqual(
            response.status_code,
            status.HTTP_200_OK,
            "Asserting can request with \"q\" parameter"
        )

        # tests for "nup" parameter

        params = {'nup': '2020'}
        response = client.get(url, kwargs=params)
        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
            "Asserting status when searching for a invalid \"nup\""
        )

        recortes = RecortesRecorte.objects.filter(numeracao_unica='4040') \
                    .order_by('id')
        
        params = {'nup': '4040'}
        serializer = RecortesSerializer(recortes)
        response = client.get(url, kwargs=params)
        self.assertEqual(
            response.data,
            serializer.data,
            "Asserting data when search by \"nup\""
        )

        params = {'nup': '4040', 'size': '10'}
        serializer = RecortesSerializer(recortes[:10])
        response = client.get(url, kwargs=params)
        self.assertEqual(
            response.data,
            serializer.data,
            "Asserting data when search by \"nup\" with \"size\" parameter"
        )

        params = {'nup': '4040', 'offset': '15'}
        serializer = RecortesSerializer(recortes[15:])
        response = client.get(url, kwargs=params)
        self.assertEqual(
            response.data,
            serializer.data,
            "Asserting data when search by \"nup\" with \"offset\" parameter"
        )

        params = {'nup': '4040', 'size': '5', 'offset': '15'}
        serializer = RecortesSerializer(recortes[15:20])
        response = client.get(url, kwargs=params)
        self.assertEqual(
            response.data,
            serializer.data,
            "Asserting data when search by \"nup\" with \"size\" and \"offset\" parameters"
        )
