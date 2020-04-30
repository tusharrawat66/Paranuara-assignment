import json
from django.views.generic import View
from rest_framework import status
from .models import People, Company, Txnhist
from django.http import JsonResponse
from .serializers import *
from django.db.models import Q
from .utils import companytosql, peopletosql


class Datatosql(View):
    """The Endpoint below uploads the the json data of both Company and People to mysql database."""
    def get(self,request):
        companytosql()
        peopletosql()
        return JsonResponse({'message': 'sucess','data': ['People and Company data uploaded']}
                            , status=status.HTTP_200_OK, safe=False)



class EmpDetails(View):
    """The endpoint below fetches essential details of each employees working in the requested company.

    --The first return statement in the method below handles Index(int)
    passed in parameter instead of Company(str).
    --The second return statement correctly responds after evaluating the strength of
    the workforce(i.e len()) in the requested company.
    """
    def get(self, request):
        # code to lock transaction in database.
        txnHistObj = Txnhist(user=request.user, method= request.method, api='empDetails', parameter=request.
                             GET.get('company'),date=datetime.now())
        txnHistObj.save()

        if Company.objects.filter(company=(request.GET.get('company'))).exists():
            compObj = Company.objects.filter(company=(request.GET.get('company'))).values('index')
            dataObj = People.objects.filter(company_id=compObj[0]['index']).all()

            if len(dataObj) >= 1:
                employee_serializer = CommonDataSerializer(data=dataObj, many=True)

                if employee_serializer.is_valid():
                    employee_serializer.save()
                return JsonResponse({"message": "success", "data": employee_serializer.data}, status=status.HTTP_200_OK,
                                    safe=False)
            else:
                return JsonResponse({"message": "success", "data": [f"{request.GET.get('company')} has no employees."]}
                                    , status=status.HTTP_204_NO_CONTENT, safe=False)
        else:
            return JsonResponse({"message": "failure", "data": [f"Company named {request.GET.get('company')}"
                                    f" doesn't exists on Paranuara"]},safe=False, status=status.HTTP_404_NOT_FOUND)



class SingleDualEntity(View):
    """GET: This endpoint accepts a single name in request and responds with name, age, favorite_fruit and
            favorite_vegetables

       POST: This endpoint accepts two names in json format for eg:- {"name":["Evola", "Tesla"]} and responds with
             name, age, address, phone of each individual along with the list of names of their mutual friends who have
             brown eyes and are still alive.
    """
    def get(self, request):
        # code to lock transaction in database
        txnHistObj = Txnhist(user=request.user, method=request.method, api='singleDualEntity',
                             parameter=request.GET.get('name'), date=datetime.now())
        txnHistObj.save()

        if People.objects.filter(name=request.GET.get('name')).exists():
            dataObj = People.objects.filter(name=request.GET.get('name')).all()
            person_serializer = PersonDataSerializers(data=dataObj, many=True)
            if person_serializer.is_valid():
                person_serializer.save()
            return JsonResponse({"message": "success", "data": person_serializer.data}, status=status.HTTP_200_OK,
                                safe=False)
        else:
            return JsonResponse({"message": 'failure',"data":[f"{request.GET.get('name')} doesn't exists on Paranuara"]}
                                ,status=status.HTTP_404_NOT_FOUND, safe=False)


    # The endpoint below responds to request with two person names.
    def post(self, request):

        pname_list = json.loads(request.body)['names']
        # code to lock transaction in database
        txnHistObj = Txnhist(user=request.user, method=request.method, api='singleDualEntity',
                             parameter= pname_list, date=datetime.now())
        txnHistObj.save()

        if People.objects.filter(name=pname_list[0]).exists() & \
           People.objects.filter(name=pname_list[1]).exists():

            name_list = pname_list
            common_list = []
            personA_list = []
            personB_list = []

            for x in name_list:
                friend_list = People.objects.filter(name=x).values("friends")
                common_list.append(friend_list[0]['friends'])

            personA_list.extend(common_list[0])
            personB_list.extend(common_list[1])

            # intersection: to find common friends
            mutualFriend_list = list(set(personA_list).intersection(personB_list))
            conditionedfriendsobj = People.objects.filter(Q(eye_color='brown') & Q(has_died=False) &
                                                Q(index__in=[m for m in mutualFriend_list])).values_list('name', flat=True)

            personObj=list(People.objects.filter(name__in=[x for x in name_list]).all())
            people_serializer = MutualFreindDataSerializer(data=personObj, many=True)

            if people_serializer.is_valid():
                people_serializer.save()

            data = {'selected_people': list(people_serializer.data),'mutual_friends': list(conditionedfriendsobj)}
            return JsonResponse({'message':'success', 'data': data}, status=status.HTTP_200_OK, safe=False)

        else:
            return JsonResponse({'message': 'failure', 'data':['Either one or both names arent registered in Paranuara']}
                                ,status=status.HTTP_404_NOT_FOUND,safe=False )
