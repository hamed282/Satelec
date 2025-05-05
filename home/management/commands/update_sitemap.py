from django.core.management.base import BaseCommand
from django.template.loader import render_to_string
from django.utils import timezone
from home.models import (
    HomeModel, AboutUsPageModel, MissionAndVisionModel,
    CommitmentModel, CustomerCentricFocusModel,
    SustainabilityInitiativeModel, WhatWeDoModel,
    ElectricalEquipmentModel, SolarSystemModel,
    HeavyMachineryModel, CommoditiesTradingModel,
    HealthcareProductModel, PartnerModel, ContactUsPageModel
)
from blog.models import BlogModel
import os

class Command(BaseCommand):
    help = 'Updates the sitemap.xml file'

    def handle(self, *args, **options):
        # Get all models
        home = HomeModel.objects.first()
        about = AboutUsPageModel.objects.first()
        mission = MissionAndVisionModel.objects.first()
        commitment = CommitmentModel.objects.first()
        customer = CustomerCentricFocusModel.objects.first()
        sustainability = SustainabilityInitiativeModel.objects.first()
        whatwedo = WhatWeDoModel.objects.first()
        electrical = ElectricalEquipmentModel.objects.first()
        solar = SolarSystemModel.objects.first()
        heavy = HeavyMachineryModel.objects.first()
        commodities = CommoditiesTradingModel.objects.first()
        healthcare = HealthcareProductModel.objects.first()
        contact = ContactUsPageModel.objects.first()
        
        # Get all blogs and partners
        blogs = BlogModel.objects.all()
        partners = PartnerModel.objects.all()
        
        # Get last modification dates
        context = {
            'home_lastmod': home.updated_at.strftime('%Y-%m-%d') if home else timezone.now().strftime('%Y-%m-%d'),
            'about_lastmod': about.updated_at.strftime('%Y-%m-%d') if about else timezone.now().strftime('%Y-%m-%d'),
            'mission_lastmod': mission.updated_at.strftime('%Y-%m-%d') if mission else timezone.now().strftime('%Y-%m-%d'),
            'commitment_lastmod': commitment.updated_at.strftime('%Y-%m-%d') if commitment else timezone.now().strftime('%Y-%m-%d'),
            'customer_lastmod': customer.updated_at.strftime('%Y-%m-%d') if customer else timezone.now().strftime('%Y-%m-%d'),
            'sustainability_lastmod': sustainability.updated_at.strftime('%Y-%m-%d') if sustainability else timezone.now().strftime('%Y-%m-%d'),
            'whatwedo_lastmod': whatwedo.updated_at.strftime('%Y-%m-%d') if whatwedo else timezone.now().strftime('%Y-%m-%d'),
            'electrical_lastmod': electrical.updated_at.strftime('%Y-%m-%d') if electrical else timezone.now().strftime('%Y-%m-%d'),
            'solar_lastmod': solar.updated_at.strftime('%Y-%m-%d') if solar else timezone.now().strftime('%Y-%m-%d'),
            'heavy_lastmod': heavy.updated_at.strftime('%Y-%m-%d') if heavy else timezone.now().strftime('%Y-%m-%d'),
            'commodities_lastmod': commodities.updated_at.strftime('%Y-%m-%d') if commodities else timezone.now().strftime('%Y-%m-%d'),
            'healthcare_lastmod': healthcare.updated_at.strftime('%Y-%m-%d') if healthcare else timezone.now().strftime('%Y-%m-%d'),
            'contact_lastmod': contact.updated_at.strftime('%Y-%m-%d') if contact else timezone.now().strftime('%Y-%m-%d'),
            'blog_lastmod': blogs.first().updated_at.strftime('%Y-%m-%d') if blogs.exists() else timezone.now().strftime('%Y-%m-%d'),
            'partners_lastmod': partners.first().updated_at.strftime('%Y-%m-%d') if partners.exists() else timezone.now().strftime('%Y-%m-%d'),
            'blogs': blogs,
            'partners': partners,
        }
        
        # Render the sitemap template
        sitemap_content = render_to_string('sitemap.xml', context)
        
        # Write to static/sitemap.xml
        static_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(__file__)))), 'static')
        sitemap_path = os.path.join(static_dir, 'sitemap.xml')
        
        with open(sitemap_path, 'w', encoding='utf-8') as f:
            f.write(sitemap_content)
        
        self.stdout.write(self.style.SUCCESS('Successfully updated sitemap.xml')) 