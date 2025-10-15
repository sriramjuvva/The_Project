from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect,Http404,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User


@csrf_exempt
def new_user_form(request):
    if request.method == 'POST':
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        if not email or not username or not password:
            return JsonResponse({"success": False, "message": "All three fields are required."}, status=400)

        if User.objects.filter(username=username).exists():
            return JsonResponse({"success": False, "message": "Username already exists."}, status=200)

        User.objects.create(username=username, password=password)
        return JsonResponse({"success": True, "message": f"User '{username}' created successfully."}, status=201)

    return JsonResponse({"success": False, "message": "Only POST method allowed."}, status=405)

