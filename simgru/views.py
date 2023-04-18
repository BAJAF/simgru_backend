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

"""
Metodo para POST

def jwt_view(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        jwt = JWTUtil.encodeToken(token)
        return JsonResponse({'jwt': jwt})
    else:
        return JsonResponse({'error': 'Method not allowed'}, status=405)

"""
