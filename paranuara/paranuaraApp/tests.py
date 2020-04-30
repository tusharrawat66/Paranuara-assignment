import json

from django.test import Client
from django.test import TestCase
from django.core.management import call_command





class TestAPI(TestCase):
    @classmethod
    def setUp(self):
        call_command('loaddata', *['company_backup.json', 'people_backup.json'])
        client = Client(SERVER_NAME='localhost')



    def test_get_existing_company(self):

        result = self.client.get('/paranuaraApp/empDetails/?company=KOG')
        self.assertEqual(result.status_code, 200)


    def test_get_not_existing_company(self):
        result = self.client.get('/paranuaraApp/empDetails/?company=Lexcorps')
        self.assertEqual(result.status_code, 404)

    def test_get_existing_people(self):
        result = self.client.get('/paranuaraApp/singleDualEntity/?name=Marla Donovan')
        self.assertEqual(result.status_code, 200)

    def test_get_not_existing_people(self):
        result = self.client.get('/paranuaraApp/singleDualEntity/?name=Angus Young')
        self.assertEqual(result.status_code, 404)

    def test_post_existing_two_people(self):
        data = {"names": ["Deleon Orr","Britt Alexander"]}
        result = self.client.post('/paranuaraApp/singleDualEntity/', json.dumps(data), content_type="application/json")
        self.assertEqual(result.status_code, 200)



    def test_post_not_existing_two_people(self):
        data = {"names": ["Larry", "David"]}
        result = self.client.post('/paranuaraApp/singleDualEntity/', json.dumps(data), content_type="application/json")
        self.assertEqual(result.status_code, 404)

