from django.urls import path
from . import views

urlpatterns = [
    path('add_profile/',views.add_profile,name='add_hospital_profile'),
    path('edit_profile/',views.edit_profile,name='edit_hospital_profile'),
    path('view_profile/',views.view_profile,name='view_hospital_profile'),
    path('request_for_blood/',views.request_for_blood,name='request_for_blood'),
    path('view_blood_requests/',views.view_blood_requests,name='view_hospital_blood_requests'),
    path('view_accepted_donors/<request_id>/',views.view_accepted_donors,name='view_accepted_donors'),
    path('is_suitable_donor/<donor_id>/',views.is_suitable_donor,name='is_suitable_donor'),
    path('view_accepted_blood_banks/<request_id>/',views.view_accepted_blood_banks,name='view_accepted_blood_banks'),
    path('view_accepted_blood_bank_inventory/<blood_bank_id>/',views.view_accepted_blood_bank_inventory,name='view_accepted_blood_bank_inventory'),
    path('accept_blood_donation_from_donor/<request_id>/<donor_id>/',views.accept_blood_donation_from_donor,name='accept_blood_donation_from_donor'),
    path('accept_blood_donation_from_blood_bank/<request_id>/<blood_bank_id>/',views.accept_blood_donation_from_blood_bank,name='accept_blood_donation_from_blood_bank')
]