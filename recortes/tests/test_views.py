from datetime import datetime, date
from django.db.models import Q
from django.contrib.auth import get_user_model
from django.urls import reverse
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
            recorte_text = "Content:\n"
            n = date_day = 0
            date_month = 1
            for i in range(0, number):
                next_mult_ten = i + (10 - i % 10)
                if next_mult_ten > n:
                    n = next_mult_ten
                    recorte_text += "{}\n".format(str(n)*3)

                date_day += 1
                if date_day > 20:
                    date_month += 1
                    date_day -= 20

                RecortesRecorte.objects.create(
                    data_criacao=datetime.now(),
                    numeracao_unica='{}{}'.format(number, number),
                    recorte=recorte_text,
                    data_publicacao=date(2000, date_month, date_day),
                    codigo_diario='COD{}'.format(number),
                    novo_recorte=True,
                )

    def test_api(self):

        url = reverse('recortes')
        client = APIClient()

        # testing the request can't complete request without authentication
        params = {'test': 'test'}
        response = client.get(url, params)
        self.assertEqual(
            response.status_code,
            status.HTTP_403_FORBIDDEN,
            "Asserting user can't request without authentication"
        )

        # testing parameters

        client.login(username='spiderman', password='spiderman')

        response = client.get(url, params)
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
            "Asserting error when request without an obligatory parameter"
        )

        # tests for "nup" parameter

        params = {'nup': '2020'}
        response = client.get(url, params)
        self.assertEqual(
            response.status_code,
            status.HTTP_404_NOT_FOUND,
            "Asserting status when searching for a invalid \"nup\""
        )

        recortes = RecortesRecorte.objects.filter(numeracao_unica='4040') \
                    .order_by('id')

        params = {'nup': '4040'}
        serializer = RecortesSerializer(recortes, many=True)
        response = client.get(url, params)
        self.assertEqual(
            response.data,
            serializer.data,
            "Asserting data when search by \"nup\""
        )

        params = {'nup': '4040', 'size': '10'}
        serializer = RecortesSerializer(recortes[:10], many=True)
        response = client.get(url, params)
        self.assertEqual(
            response.data,
            serializer.data,
            "Asserting data when search by \"nup\" with \"size\" parameter"
        )

        params = {'nup': '4040', 'offset': '15'}
        serializer = RecortesSerializer(recortes[15:], many=True)
        response = client.get(url, params)
        self.assertEqual(
            response.data,
            serializer.data,
            "Asserting data when search by \"nup\" with \"offset\" parameter"
        )

        params = {'nup': '4040', 'size': '5', 'offset': '15'}
        serializer = RecortesSerializer(recortes[15:20], many=True)
        response = client.get(url, params)
        self.assertEqual(
            response.data,
            serializer.data,
            "Asserting data when search by \"nup\" with \"size\" and \"offset\" parameters"
        )


        # tests for "q" param

        recortes = RecortesRecorte.objects.all().order_by('id')

        params = {'q': '404040'}
        serializer = RecortesSerializer(recortes.filter(recorte__contains='404040'), many=True)
        response = client.get(url, params)
        self.assertEqual(
            response.data,
            serializer.data,
            "Asserting data when search by \"q\" parameter"
        )

        params = {'q': '404040-101010'}
        filter_q_recortes = recortes.filter(Q(recorte__contains='404040') &
                            Q(recorte__contains='101010'))

        serializer = RecortesSerializer(filter_q_recortes, many=True)
        response = client.get(url, params)
        self.assertEqual(
            response.data,
            serializer.data,
            "Asserting data when search by multiple \"q\" parameters"
        )

        params['nup'] = '5050'
        serializer = RecortesSerializer(filter_q_recortes.filter(numeracao_unica='5050'), many=True)
        response = client.get(url, params)
        self.assertEqual(
            response.data,
            serializer.data,
            "Asserting data when search by multiple \"q\" and \"nup\" parameters"
        )

        # tests for "t" param
        params = {'t': '55132156'}
        response = client.get(url, params)
        self.assertEqual(
            response.status_code,
            status.HTTP_400_BAD_REQUEST,
            "Asserting error when \"t\" is an invalid date"
        )

        params = {'t': '13012000'}
        response = client.get(url, params)
        filter_t_recortes = recortes.filter(data_publicacao='2000-01-13')
        serializer = RecortesSerializer(filter_t_recortes, many=True)
        self.assertEqual(
            response.data,
            serializer.data,
            "Asserting data when search by \"t\" parameter"
        )

        params['q'] = '101010'
        params['nup'] = '3030'
        serializer = RecortesSerializer(filter_t_recortes.filter(numeracao_unica='3030', \
                    recorte__contains='101010'), many=True)
        response = client.get(url, params)
        self.assertEqual(
            response.data,
            serializer.data,
            "Asserting data when search by \"t\", \"q\" and \"nup\" parameters"
        )
