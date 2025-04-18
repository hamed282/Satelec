from django.shortcuts import render, get_object_or_404
from django.views import View
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
                   'seo': "seo"}
        return render(request, 'partners/index.html', context=context)
