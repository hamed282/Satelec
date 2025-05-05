from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import HttpResponse
from django.template.loader import render_to_string
from .models import (AddAboutGalleryModel, HomeModel, AddServiceModel,
                     AddTestimonialModel, AddClientModel, ContactUsModel,
                     AboutUsPageModel, MissionAndVisionModel, SustainabilityInitiativeModel, CustomerCentricFocusModel,
                     CommitmentModel, ContactUsPageModel, AddCommitmentModel, AddCustomerCentricFocusModel,
                     AddSustainabilityInitiativeModel, WhatWeDoModel, AddWhatWeDoModel, SolarSystemModel,
                     HealthcareProductModel, HeavyMachineryModel, ElectricalEquipmentModel, CommoditiesTradingModel,
                     PartnerModel, AddPartnerProductModel, AddPartnerFeatureModel, AddPartnerGalleryModel)
from blog.models import BlogModel as Blogs
from django.conf import settings
from django.core.mail import send_mail
from django.utils import timezone


class HomeView(View):
    def get(self, request):

        blogs = Blogs.objects.all()[:9]
        data = HomeModel.objects.all().first()
        about_items = AddAboutGalleryModel.objects.all()
        service_items = AddServiceModel.objects.all()
        testimonial_items = AddTestimonialModel.objects.all()
        client_items = PartnerModel.objects.all().order_by('priority')
        seo = HomeModel.objects.all().first()
        context = {'blogs': blogs,
                   'data': data,
                   'about_items': about_items,
                   'service_items': service_items,
                   'testimonial_items': testimonial_items,
                   'client_items': client_items,
                   'seo': seo}
        return render(request, 'home/index.html',
                      context=context)


class AboutUsView(View):
    def get(self, request):
        data = HomeModel.objects.all().first()
        about = AboutUsPageModel.objects.all().first()
        seo = AboutUsPageModel.objects.all().first()
        client_items = PartnerModel.objects.all().order_by('priority')
        context = {'data': data,
                   'about': about,
                   'client_items': client_items,
                   'seo': seo}
        return render(request, 'aboutus/index.html', context=context)


class ContactUsView(View):
    def get(self, request):
        data = HomeModel.objects.all().first()
        contact = ContactUsPageModel.objects.all().first()
        seo = ContactUsPageModel.objects.all().first()
        client_items = PartnerModel.objects.all().order_by('priority')
        context = {'data': data,
                   'contact': contact,
                   'client_items': client_items,
                   'seo': seo}
        return render(request, 'contactus/index.html', context=context)

    def post(self, request):
        data = HomeModel.objects.all().first()
        contact = ContactUsPageModel.objects.all().first()
        seo = ContactUsPageModel.objects.all().first()

        context = {'data': data,
                   'contact': contact,
                   'seo': seo}

        form = request.POST
        ContactUsModel.objects.create(name=form['contact-name'],
                                      surname=form['contact-surname'],
                                      email=form['contact-email'],
                                      phone_number=form['contact-phone'],
                                      message=form['contact-message'])

        subject = 'Contact Us'
        message_provider = f'New Submit \n' \
                           f'Name: {form["contact-name"]} \n' \
                           f'SurName: {form["contact-surname"]} \n' \
                           f'Email: {form["contact-email"]} \n' \
                           f'Phone Number: {form["contact-phone"]} \n' \
                           f'Message: {form["contact-message"]}'
        email_from = settings.EMAIL_HOST_USER
        send_mail(subject, message_provider, email_from, ['hamed@healfit.ae'])

        return render(request, 'contactus/index.html', context=context)


class MissionVisionView(View):
    def get(self, request):
        data = HomeModel.objects.all().first()
        mission_vision = MissionAndVisionModel.objects.all().first()
        seo = MissionAndVisionModel.objects.all().first()
        client_items = PartnerModel.objects.all().order_by('priority')
        context = {'data': data,
                   'mission_vision': mission_vision,
                   'client_items': client_items,
                   'seo': seo}
        return render(request, 'mission_vision/index.html', context=context)


class CommitmentView(View):
    def get(self, request):
        data = HomeModel.objects.all().first()
        commitment = CommitmentModel.objects.all().first()
        add_commitment = AddCommitmentModel.objects.all()
        seo = CommitmentModel.objects.all().first()
        client_items = PartnerModel.objects.all().order_by('priority')
        context = {'data': data,
                   'commitment': commitment,
                   'add_commitment': add_commitment,
                   'client_items': client_items,
                   'seo': seo}
        return render(request, 'commitment/index.html', context=context)


class CostumerCentricFocusView(View):
    def get(self, request):
        data = HomeModel.objects.all().first()
        customer = CustomerCentricFocusModel.objects.all().first()
        add_customer = AddCustomerCentricFocusModel.objects.all()
        seo = CustomerCentricFocusModel.objects.all().first()
        client_items = PartnerModel.objects.all().order_by('priority')
        context = {'data': data,
                   'customer': customer,
                   'add_customer': add_customer,
                   'client_items': client_items,
                   'seo': seo}
        return render(request, 'customer_centric_focus/index.html', context=context)


class SustainabilityInitiativeView(View):
    def get(self, request):
        data = HomeModel.objects.all().first()
        sustainability = SustainabilityInitiativeModel.objects.all().first()
        add_sustainability = AddSustainabilityInitiativeModel.objects.all()
        seo = SustainabilityInitiativeModel.objects.all().first()
        client_items = PartnerModel.objects.all().order_by('priority')
        context = {'data': data,
                   'sustainability': sustainability,
                   'add_sustainability': add_sustainability,
                   'client_items': client_items,
                   'seo': seo}
        return render(request, 'sustainability_initiative/index.html', context=context)


class WhatWeDoView(View):
    def get(self, request):
        data = HomeModel.objects.all().first()
        what_we_do = WhatWeDoModel.objects.all().first()
        add_what_we_do = AddWhatWeDoModel.objects.all()
        seo = WhatWeDoModel.objects.all().first()
        client_items = PartnerModel.objects.all().order_by('priority')
        context = {'data': data,
                   'what_we_do': what_we_do,
                   'add_what_we_do': add_what_we_do,
                   'client_items': client_items,
                   'seo': seo}
        return render(request, 'what-we-do/index.html', context=context)


class ElectricalEquipmentView(View):
    def get(self, request):
        data = HomeModel.objects.all().first()
        content = ElectricalEquipmentModel.objects.all().first()
        seo = ElectricalEquipmentModel.objects.all().first()
        client_items = PartnerModel.objects.all().order_by('priority')
        context = {'data': data,
                   'content': content,
                   'client_items': client_items,
                   'seo': seo}
        return render(request, 'what-we-do-item/index.html', context=context)


class SolarSystemView(View):
    def get(self, request):
        data = HomeModel.objects.all().first()
        content = SolarSystemModel.objects.all().first()
        seo = SolarSystemModel.objects.all().first()
        client_items = PartnerModel.objects.all().order_by('priority')
        context = {'data': data,
                   'content': content,
                   'client_items': client_items,
                   'seo': seo}
        return render(request, 'what-we-do-item/index.html', context=context)


class HeavyMachineryView(View):
    def get(self, request):
        data = HomeModel.objects.all().first()
        content = HeavyMachineryModel.objects.all().first()
        seo = HeavyMachineryModel.objects.all().first()
        client_items = PartnerModel.objects.all().order_by('priority')
        context = {'data': data,
                   'content': content,
                   'client_items': client_items,
                   'seo': seo}
        return render(request, 'what-we-do-item/index.html', context=context)


class CommoditiesTradingView(View):
    def get(self, request):
        data = HomeModel.objects.all().first()
        content = CommoditiesTradingModel.objects.all().first()
        seo = CommoditiesTradingModel.objects.all().first()
        client_items = PartnerModel.objects.all().order_by('priority')
        context = {'data': data,
                   'content': content,
                   'client_items': client_items,
                   'seo': seo}
        return render(request, 'what-we-do-item/index.html', context=context)


class HealthcareProductView(View):
    def get(self, request):
        data = HomeModel.objects.all().first()
        content = HealthcareProductModel.objects.all().first()
        seo = HealthcareProductModel.objects.all().first()
        client_items = PartnerModel.objects.all().order_by('priority')
        context = {'data': data,
                   'content': content,
                   'client_items': client_items,
                   'seo': seo}
        return render(request, 'what-we-do-item/index.html', context=context)


class PartnerView(View):
    def get(self, request, partner_slug):
        data = HomeModel.objects.all().first()
        content = get_object_or_404(PartnerModel, slug=partner_slug)
        products = AddPartnerProductModel.objects.filter(partner=content)
        features = AddPartnerFeatureModel.objects.filter(partner=content)
        gallery = AddPartnerGalleryModel.objects.filter(partner=content)
        client_items = PartnerModel.objects.all().order_by('priority')
        context = {'data': data,
                   'content': content,
                   'products': products,
                   'features': features,
                   'gallery': gallery,
                   'client_items': client_items,
                   'seo': content}
        return render(request, 'partners/index.html', context=context)


class SitemapView(View):
    def get(self, request):
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
        
        sitemap = render_to_string('sitemap.xml', context)
        return HttpResponse(sitemap, content_type='application/xml')
