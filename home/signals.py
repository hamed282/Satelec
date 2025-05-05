from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.management import call_command
from .models import (
    HomeModel, AboutUsPageModel, MissionAndVisionModel,
    CommitmentModel, CustomerCentricFocusModel,
    SustainabilityInitiativeModel, WhatWeDoModel,
    ElectricalEquipmentModel, SolarSystemModel,
    HeavyMachineryModel, CommoditiesTradingModel,
    HealthcareProductModel, PartnerModel, ContactUsPageModel
)
from blog.models import BlogModel

# List of all models that affect the sitemap
SITEMAP_MODELS = [
    HomeModel, AboutUsPageModel, MissionAndVisionModel,
    CommitmentModel, CustomerCentricFocusModel,
    SustainabilityInitiativeModel, WhatWeDoModel,
    ElectricalEquipmentModel, SolarSystemModel,
    HeavyMachineryModel, CommoditiesTradingModel,
    HealthcareProductModel, PartnerModel, ContactUsPageModel,
    BlogModel
]

@receiver(post_save)
def update_sitemap_on_save(sender, **kwargs):
    if sender in SITEMAP_MODELS:
        call_command('update_sitemap')

@receiver(post_delete)
def update_sitemap_on_delete(sender, **kwargs):
    if sender in SITEMAP_MODELS:
        call_command('update_sitemap') 