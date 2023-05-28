from django.shortcuts import render
# Import temporal para poder comprobar que funciona la funcion jwt para regresar un token
# Se considera peligroso no agregar un csrf token pero hace sueño.
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
from django.http import HttpResponse
from django.http import JsonResponse

from .utils import JWTUtil
from .google_api import credentials
from .google_api import classroom
import json
from .codes import codes_creator


def index(request):
    return HttpResponse("Hola mundo. Este es el el get de la raiz.")

def jwt_view(request, token):
    jwt = JWTUtil.encodeToken(token)
    return JsonResponse({'jwt': jwt})

def creds_view(request, token):
    credentials.get_user_credentials(token)
    return

def courses_view(request, jwt):
    token = JWTUtil.decodeToken(jwt)['token']
    courses = classroom.get_course_list(token=token)
    response = JsonResponse({'courses': courses})
    return response

def get_aes(request):
    return JsonResponse(codes_creator.get_ae())

def get_ae_crits(request, ae_id):
    return JsonResponse(codes_creator.get_ae_crit(ae_id=ae_id-1))

def get_ae_crit_inds(request, ae_id, crit_id):
    return JsonResponse(codes_creator.get_ae_crit_ind(ae_id=ae_id-1, crit_id=crit_id-1))

def create_code(request, ae, cd, i):
    try:

        return JsonResponse(codes_creator.create_code(ae, cd, i))
    except KeyError:
        return JsonResponse({'message': 'Missing value'}, status = 500)

def get_coursework_info(request, courseId:str, courseworkId: str):

    body = json.loads(request.body)

    token = JWTUtil.decodeToken(body["token"])["token"]

    return JsonResponse(classroom.get_coursework(token, courseId, courseworkId))

def get_course_information(request):
    body = json.loads(request.body)
    token = JWTUtil.decodeToken(body["token"])["token"]

    return JsonResponse(classroom.get_course_information(token, body["courseId"]))
