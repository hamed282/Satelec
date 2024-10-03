from django.shortcuts import render
from django.views import View
from .models import (LogoModel, HomeAboutUsModel, AddAboutGalleryModel, ServiceItemModel, OurServiceModel,
                     TestimonialModel, AddTestimonialModel, ClientModel, AddClientModel, BlogModel, ContactUsModel,
                     AboutPageModel, MissionAndVisionModel, SustainabilityInitiativeModel, CustomerCentricFocusModel,
                     CommitmentModel)
from blog.models import BlogModel as Blogs


class HomeView(View):
    def get(self, request):
        logo = LogoModel.objects.all().first()
        about = HomeAboutUsModel.objects.all().first()
        galleries = AddAboutGalleryModel.objects.filter(about=about)
        services = OurServiceModel.objects.all().first()
        item_service = ServiceItemModel.objects.filter(service=services)
        testimonial = TestimonialModel.objects.all().first()
        item_testimonial = AddTestimonialModel.objects.filter(testimonial=testimonial)
        client = ClientModel.objects.all().first()
        item_client = AddClientModel.objects.filter(client=client)
        blog = BlogModel.objects.all().first()
        blogs = Blogs.objects.all()[:9]

        return render(request, 'home/index.html',
                      context={'logo': logo,
                               'about': about, 'galleries': galleries,
                               'services': services, 'item_service': item_service,
                               'testimonial': testimonial, 'item_testimonial': item_testimonial,
                               'client': client, 'item_client': item_client,
                               'blog': blog, 'blogs': blogs})


class AboutUsView(View):
    def get(self, request):
        logo = LogoModel.objects.all().first()
        data = AboutPageModel.objects.all().first()
        return render(request, 'aboutus/index.html', context={'logo': logo, 'data': data})


class ContactUsView(View):
    def get(self, request):
        logo = LogoModel.objects.all().first()

        return render(request, 'contactus/index.html', context={'logo': logo})

    def post(self, request):
        logo = LogoModel.objects.all().first()

        form = request.POST
        ContactUsModel.objects.create(name=form['contact-name'],
                                      surname=form['contact-surname'],
                                      email=form['contact-email'],
                                      phone_number=form['contact-phone'],
                                      message=form['contact-message'])
        return render(request, 'contactus/index.html', context={'logo': logo})


class MissionVisionView(View):
    def get(self, request):
        logo = LogoModel.objects.all().first()
        data = MissionAndVisionModel.objects.all().first()
        return render(request, 'mission_vision/index.html', context={'logo': logo, 'data': data})


class CommitmentView(View):
    def get(self, request):
        logo = LogoModel.objects.all().first()
        data = CommitmentModel.objects.all().first()
        context = {'logo': logo, 'data': data}
        return render(request, 'commitment/index.html', context=context)


class CostumerCentricFocusView(View):
    def get(self, request):
        logo = LogoModel.objects.all().first()
        data = CustomerCentricFocusModel.objects.all().first()
        return render(request, 'customer_centric_focus/index.html', context={'logo': logo, 'data': data})


class SustainabilityInitiativeView(View):
    def get(self, request):
        logo = LogoModel.objects.all().first()
        data = SustainabilityInitiativeModel.objects.all().first()
        return render(request, 'sustainability/index.html', context={'logo': logo, 'data': data})


class WhatWeDoView(View):
    def get(self, request):
        logo = LogoModel.objects.all().first()
        data = SustainabilityInitiativeModel.objects.all().first()
        return render(request, 'what-we-do/index.html', context={'logo': logo, 'data': data})


class ElectricalEquipmentView(View):
    def get(self, request):
        return render(request, 'electrical-equipment/index.html')


class SolarSystemView(View):
    def get(self, request):
        return render(request, 'solar-systems/index.html')


class HeavyMachineryView(View):
    def get(self, request):
        return render(request, 'heavy-machineries/index.html')


class CommoditiesTradingView(View):
    def get(self, request):
        return render(request, 'commodities/index.html')


class HealthcareProductView(View):
    def get(self, request):
        return render(request, 'healthcare-products/index.html')
