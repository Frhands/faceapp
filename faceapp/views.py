from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader
import sys
import base64
import chardet

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
        img_base64 = request.POST['image']
        name = request.POST['name']
        print(type(img_base64), ':')
        print("name:",name)
        # pic1=list(pic1.dict())[0]+list(pic1.dict())[1]
        # pic1=pic1.replace("data:image/jpeg","")
        # pic1=pic1.replace(" ","+")+"=="
        # pic1=pic1.replace("base64,","")
        
        response = face_api.addface_to_faceset(img_base64,test_faceset_id,[name])
        print( response )        
        # response = face_api.search_all_face_in_img(img_base64, test_faceset_id)
        # response = face_api.search_face_with_name(img_base64,name,test_faceset_id)
        return JsonResponse(response)  
    else:
        return JsonResponse( {'result':'error'} )

def ret_gender_and_age(request):
    if request.method == 'POST':
        pic1 = request.POST
        print("get post")
        img_base64 = request.POST['image']
        # pic1=list(pic1.dict())[0]+list(pic1.dict())[1]
        # pic1=pic1.replace("data:image/jpeg","")
        # pic1=pic1.replace(" ","+")+"=="
        # pic1=pic1.replace("base64,","")
        # print(pic1)
        response = face_api.get_gender_and_age(img_base64)

        return JsonResponse(response)  
    else:
        return JsonResponse( {'result':'error'} )

def search_face(request):
    if request.method == 'POST':
        img_base64 = request.POST['image']
        print("get post")
        # pic1=list(pic1.dict())[0]+list(pic1.dict())[1]
        # pic1=pic1.replace("data:image/jpeg","")
        # pic1=pic1.replace(" ","+")+"=="
        # pic1=pic1.replace("base64,","")
        # print(pic1)
        # img_base64 = ...
        # face_feat = face_api.search_face(img_base64, test_faceset_id)

        response = face_api.search_all_face_in_img(img_base64, test_faceset_id)
        # response['face_feat'] = face_feat
        print( response )
        return JsonResponse(response)  
    else:
        return JsonResponse( {'result':'error'} )

def pick_face(request):
    
    if request.method == 'POST':
        print("get post")
        image = request.POST['image']
        name = request.POST['name']
        print(type(image), ':')
        print("name:",name)
        response = face_api.search_face_with_name(image,name,test_faceset_id)
        
        return JsonResponse(response)
    else:
        return JsonResponse( {'result':'error'} )

def get_namelist(request):
    response = {}
    response['namelist'] = face_api.get_name_list_from_faceset(test_faceset_id)
    if len(response['namelist']) == 0:
        return {"result":-1, "errmsg":"no stored name"}
    response['result'] = 1
    return JsonResponse( response )
       


