import json
from dateutil import parser
from .models import *
from decimal import Decimal
from nltk.corpus import wordnet as wn




def companytosql():
    datas = None
    with open('paranuaraApp/json_files/companies.json', encoding='utf-8') as data_file:
        datas = json.loads(data_file.read())
    if datas:
        for data in datas:
            company = Company()
            company.index = data['index']
            company.company = data['company']
            company.save()
            print(f"save company {company.index}")


def get_fruit_list():
    fruit = wn.synset('fruit.n.01')
    fruit_list = list(set([w for s in fruit.closure(lambda s: s.hyponyms()) for w in s.lemma_names()]))
    return fruit_list
# get fruit list from Wordnet(nltk corpus)



def peopletosql():
    datas = None
    with open('paranuaraApp/json_files/people.json', encoding='utf-8') as data_file:
        datas = json.loads(data_file.read())
    if datas:
        fruit_list = get_fruit_list()

        for data in datas:
            people = People()
            people.uid = data['_id']
            people.guid = data['guid']
            people.index = data['index']
            people.name = data['name']
            people.age = data['age']
            people.has_died = False if data['has_died'] == "false" or data['has_died']== False else True
            people.balance = Decimal(data['balance'].strip('$').replace(',', ''))
            people.picture = data['picture']
            people.eye_color = data['eyeColor']
            people.gender = data['gender']
            people.company_id = data['company_id']

            people.email = data['email']


            people.phone = data['phone']
            people.address = data['address']
            people.about = data['about']

            try:
                people.registered = parser.parse(data['registered'])
            except Exception as e:
                pass

            people.tags = data['tags']

            frend_var = [fav['index'] for fav in data['friends']]
            people.friends = frend_var

            people.greeting = data['greeting']

            people.favouriteFood= data['favouriteFood']
            for food in data['favouriteFood']:
                if food in fruit_list:
                    people.favourite_fruit.append(food)
                else:
                    people.favourite_vegetable.append(food)
            people.save()
            print(f"save people {people.index}")
