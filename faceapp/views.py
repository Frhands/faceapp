from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
import sys

from faceapp import face_api

test_faceset_id = "test002"

# Create your views here.
def index(request):
    # template = loader.get_template(sys.path[0]+'\\faceapp\\templates\\index.html')
    # return HttpResponse(template.render(request))
     return render(request, 'index.html')

def add_face(request):
    if request.method == 'POST':
        pic1 = request.POST
        print("get post")
        # pic1=list(pic1.dict())[0]+list(pic1.dict())[1]
        # pic1=pic1.replace("data:image/jpeg","")
        # pic1=pic1.replace(" ","+")+"=="
        # pic1=pic1.replace("base64,","")
        # 此处获得pic1的base64编码
        # print(pic1)
        img_base64 = ...
        name = ...

        response = {}
        response['result'] = face_api.addface_to_faceset(img_base64, test_faceset_id, name)
        return JsonResponse(response)  
    else
        return JsonResponse( {'result':'error'} )

def ret_gender_and_age(request):
    if request.method == 'POST':
        pic1 = request.POST
        print("get post")
        # pic1=list(pic1.dict())[0]+list(pic1.dict())[1]
        # pic1=pic1.replace("data:image/jpeg","")
        # pic1=pic1.replace(" ","+")+"=="
        # pic1=pic1.replace("base64,","")
        # 此处获得pic1的base64编码
        # print(pic1)
        img_base64 = ...
        face_feat = face_api.get_gender_and_age(img_base64)

        response = {}
        response['face_feat'] = face_feat
        return JsonResponse(response)  
    else
        return JsonResponse( {'result':'error'} )

def search_face(request):
    if request.method == 'POST':
        pic1 = request.POST
        print("get post")
        # pic1=list(pic1.dict())[0]+list(pic1.dict())[1]
        # pic1=pic1.replace("data:image/jpeg","")
        # pic1=pic1.replace(" ","+")+"=="
        # pic1=pic1.replace("base64,","")
        # 此处获得pic1的base64编码
        # print(pic1)
        img_base64 = ...
        face_feat = face_api.search_face(img_base64, test_faceset_id)

        response = {}
        response['face_feat'] = face_feat
        return JsonResponse(response)  
    else
        return JsonResponse( {'result':'error'} )

# def add_face(request):
#     pass

