from django.shortcuts import render
from django.http import HttpResponse
import ast
from django.views.decorators.csrf import csrf_exempt
from django.core.serializers.json import DjangoJSONEncoder  
from ast import literal_eval as make_tuple
from ast import literal_eval
import json
import  pandas
from django.http import JsonResponse
# Create your views here.
from os import path

#print("inside view")
filename = 'C:/Users/DELL/Desktop/Staffbase/staffbase_anjali_task/task_backend_api/question.json'
listObj = []

def get_user(request):
    #print("inside get_user")
    user={
        "users":[
            {
                "userId": 1,
                "userName": "Anjali"
            },
            {
                "userId": 2,
                "userName": "Satvik"
            },
            {
                "userId": 3,
                "userName": "Ramon"
            },
            {
                "userId": 4,
                "userName": "Alina"
            }
        ]
    }

    if request.method == "GET" :
        # return HttpResponse(json.dumps(user.users),content_type="application/json")
        return JsonResponse(user)
        



print("above ask_question")
@csrf_exempt


def ask_question(request):
    
    print("inside")
    if  request.method =="POST":
        body_unicode = request.body.decode('utf-8')
        body = json.loads(body_unicode)

        quest_id = body['quest_id']
        user_id = body['user_id']
        question =  body['question']

        if path.isfile(filename) is False:
            raise Exception("File not found")


        with open(filename) as fp:
            listObj = json.load(fp)

        print(listObj)

        print(type(listObj))

         
        listObj.append(body)

        print(listObj)
 
        with open(filename, 'w') as json_file:
            json.dump(listObj, json_file, 
                                indent=4,  
                                separators=(',',': '))

            
    return JsonResponse(body)




print("get_quest")

def get_questions(request):
    user={}
    if request.method == "GET":
        print("isnide get ques")

    with open(filename) as fp:
        listObj = json.load(fp)

    # for key,value in listObj.items():
    #     print(key,value)
    print(listObj)
    data=  json.dumps(listObj)
    data = data.replace('\\"', '')
    data=  json.loads(data)
    return JsonResponse(json.dumps(data),safe=False)

