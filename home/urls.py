from django.urls import path
from . import views


app_name = 'home'
urlpatterns = [
    # Home
    path('', views.HomeView.as_view(), name='home'),

    # Who we are
    path('aboutus/', views.AboutUsView.as_view(), name='aboutus'),
    path('mission_vision/', views.MissionVisionView.as_view(), name='mission_vision'),
    path('commitment_to_quality/', views.CommitmentView.as_view(), name='commitment'),
    path('costumer_centric_focus/', views.CostumerCentricFocusView.as_view(), name='costumer_centric_focus'),
    path('sustainability_initiatives/', views.SustainabilityInitiativeView.as_view(), name='sustainability_initiatives'),

    # What we do
    path('what-we-do/', views.WhatWeDoView.as_view(), name='what_we_do'),
    # path('what-we-do/<slug:item_slug>/', views.WhatWeDoItemView.as_view(), name='what_we_do_item'),
    path('electrical_equipments/', views.ElectricalEquipmentView.as_view(), name='electrical_equipments'),
    path('solar_systems/', views.SolarSystemView.as_view(), name='solar_systems'),
    path('heavy_machineries/', views.HeavyMachineryView.as_view(), name='heavy_machineries'),
    path('commodities_trading/', views.CommoditiesTradingView.as_view(), name='commodities_trading'),
    path('healthcare_products/', views.HealthcareProductView.as_view(), name='healthcare_products'),

    # Contact Us
    path('contactus/', views.ContactUsView.as_view(), name='contactus'),

    # Partner
    path('partner/<slug:partner_slug>/', views.PartnerView.as_view(), name='partner'),

]

