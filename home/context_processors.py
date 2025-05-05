from .models import (
    HomeModel, AboutUsPageModel, MissionAndVisionModel, 
    CommitmentModel, CustomerCentricFocusModel, 
    SustainabilityInitiativeModel, WhatWeDoModel,
    ElectricalEquipmentModel, SolarSystemModel,
    HeavyMachineryModel, CommoditiesTradingModel,
    HealthcareProductModel, PartnerModel, ContactUsPageModel
)


def seo_data(request):
    try:
        # Get the current URL path
        current_path = request.path_info
        
        # Default SEO data from HomeModel
        default_seo = HomeModel.objects.first()
        seo_data = {
            'meta_title': default_seo.meta_title,
            'meta_description': default_seo.meta_description,
            'follow': default_seo.follow,
            'index': default_seo.index,
            'canonical': default_seo.canonical,
            'schema_markup': default_seo.schema_markup,
        }
        
        # Check which page we're on and get its specific SEO data
        if current_path == '/about-us/':
            page_seo = AboutUsPageModel.objects.first()
        elif current_path == '/mission-vision/':
            page_seo = MissionAndVisionModel.objects.first()
        elif current_path == '/commitment/':
            page_seo = CommitmentModel.objects.first()
        elif current_path == '/customer-centric-focus/':
            page_seo = CustomerCentricFocusModel.objects.first()
        elif current_path == '/sustainability-initiative/':
            page_seo = SustainabilityInitiativeModel.objects.first()
        elif current_path == '/what-we-do/':
            page_seo = WhatWeDoModel.objects.first()
        elif current_path == '/electrical-equipments/':
            page_seo = ElectricalEquipmentModel.objects.first()
        elif current_path == '/solar-systems/':
            page_seo = SolarSystemModel.objects.first()
        elif current_path == '/heavy-machineries/':
            page_seo = HeavyMachineryModel.objects.first()
        elif current_path == '/commodities-trading/':
            page_seo = CommoditiesTradingModel.objects.first()
        elif current_path == '/healthcare-products/':
            page_seo = HealthcareProductModel.objects.first()
        elif current_path == '/contact-us/':
            page_seo = ContactUsPageModel.objects.first()
        elif current_path.startswith('/partner/'):
            # For partner pages, we need to get the specific partner
            partner_slug = current_path.split('/')[-2]
            page_seo = PartnerModel.objects.filter(slug=partner_slug).first()
        else:
            page_seo = None
            
        # If we found specific SEO data for the page, use it
        if page_seo:
            seo_data = {
                'meta_title': page_seo.meta_title or default_seo.meta_title,
                'meta_description': page_seo.meta_description or default_seo.meta_description,
                'follow': page_seo.follow if hasattr(page_seo, 'follow') else default_seo.follow,
                'index': page_seo.index if hasattr(page_seo, 'index') else default_seo.index,
                'canonical': page_seo.canonical or default_seo.canonical,
                'schema_markup': page_seo.schema_markup or default_seo.schema_markup,
            }
            
        return {'seo': seo_data}
        
    except Exception as e:
        # Fallback to default values if anything goes wrong
        return {
            'seo': {
                'meta_title': 'Satelec',
                'meta_description': 'Satelec',
                'follow': False,
                'index': False,
                'canonical': request.build_absolute_uri(),
                'schema_markup': '',
            }
        } 