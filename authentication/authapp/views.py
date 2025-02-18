from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import send_mail
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.template.loader import render_to_string
from django.contrib.auth.decorators import login_required
from .forms import PasswordResetRequestForm
from django.conf import settings
from django.contrib.auth.forms import SetPasswordForm
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from rest_framework import status
from .models import Member,DeaconInfo
from django.contrib.auth.views import PasswordResetConfirmView
from django.urls import reverse_lazy
from .serializers import MemberSerializer
from django.contrib.auth.decorators import permission_required
from django.contrib.auth.tokens import default_token_generator
from django.shortcuts import redirect
from django.contrib.auth.tokens import default_token_generator
from django.contrib.auth.forms import AuthenticationForm
from django.views import View
import json


@login_required
def dashboard(request):
    return render(request, 'registration/dashboard.html', {'section':'dashboard'})


def logged_out(request):
    return render(request, 'registration/logged-out.html') 

@login_required
def services(request):
    return render(request, 'registration/services.html') 

@login_required
def forms(request):
    return render(request, 'registration/forms.html')


def setie(request):
    return render(request,'registration/settings.html')

@login_required
def profile(request):
    return render(request, 'registration/profile.html')


def password_reset_done(request):
    return render(request, 'registration/password_reset_done.html')

@login_required
@csrf_exempt  # If you're using the Fetch API with JavaScript, you'll need this to bypass CSRF checks
def create_member(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)  # Parse the incoming JSON request body
            
            # Create a new member and save the data to the database
            member = Member(
                name=data.get('name'),
                changamoto=data.get('changamoto'),
                Biblia=data.get('Biblia'),
                kesha=data.get('kesha'),
                date=data.get('date'),
                lesson=data.get('lesson'),
                deacon=data.get('deacon'),
                nyimbo=data.get('nyimbo'),
                maombi=data.get('maombi'),
                maombitime=data.get('maombitime'),
                ibada=data.get('ibada'),
                jtano=data.get('jtano'),
                ijumaa=data.get('ijumaa'),
                sabato=data.get('sabato'),
                zaka=data.get('zaka'),
                sadaka=data.get('sadaka'),
                makambi=data.get('makambi'),
                michango=data.get('michango'),
                misaada=data.get('misaada'),
                thamani=data.get('thamani'),
                injili=data.get('injili'),
                mudawakuhubiri=data.get('mudawakuhubiri'),
            )
            member.save()  # Save to the database

            return JsonResponse({'message': 'Member data saved successfully!'}, status=201)
        
        except json.JSONDecodeError:
            return JsonResponse({'error': 'Invalid JSON data!'}, status=400)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Only POST requests are allowed!'}, status=400)

# View to handle retrieving all members (GET request)
class MemberListView(View):
    def get(self, request, *args, **kwargs):
        members = Member.objects.all()  # Get all members
        members_list = list(members.values())  # Convert queryset to a list of dictionaries
        return JsonResponse(members_list, safe=False)
    


# for deacons informations to post and view

@csrf_exempt  # If you're using the Fetch API with JavaScript, you'll need this to bypass CSRF checks
def create_report(request):
    if request.method == 'POST':
        try:
            # Parse the incoming JSON data from the request body
            data = json.loads(request.body)

            # Get the data from the JSON payload
            deacon_name = data.get('deaconName')
            date = data.get('date')
            report = data.get('report')

            # Validate that the required fields are provided
            if not deacon_name or not date or not report:
                return JsonResponse({'error': 'All fields are required.'}, status=400)

            # Create a new DeaconInfo object and save the data to the database
            new_report = DeaconInfo(
                name=deacon_name,
                date=date,
                jumla=report  # assuming 'jumla' is the field for the number of visited members
            )
            new_report.save()  # Save the new record to the database

            # Return a success response if the report is created successfully
            return JsonResponse({'message': 'Report created successfully!'}, status=201)

        except json.JSONDecodeError:
            # Handle errors if the incoming data is not valid JSON
            return JsonResponse({'error': 'Invalid JSON data!'}, status=400)

        except Exception as e:
            # Handle any other unexpected errors
            return JsonResponse({'error': str(e)}, status=500)

    # Return an error if the request method is not POST
    return JsonResponse({'error': 'Invalid request method.'}, status=400)
# View to handle retrieving all DeaconInfo records (GET request)
class DeaconListView(View):
    def get(self, request, *args, **kwargs):
        deacons = DeaconInfo.objects.all()  # Get all deacon records
        deacon_list = list(deacons.values())  # Convert queryset to a list of dictionaries
        return JsonResponse(deacon_list, safe=False)  # Return as JSON response