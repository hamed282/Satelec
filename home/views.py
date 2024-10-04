from django.shortcuts import render
from django.views import View
from .models import (AddAboutGalleryModel, HomeModel, AddServiceModel,
                     AddTestimonialModel, AddClientModel, ContactUsModel,
                     AboutUsPageModel, MissionAndVisionModel, SustainabilityInitiativeModel, CustomerCentricFocusModel,
                     CommitmentModel, ContactUsPageModel)
from blog.models import BlogModel as Blogs


class HomeView(View):
    def get(self, request):

        blogs = Blogs.objects.all()[:9]
        data = HomeModel.objects.all().first()
        about_items = AddAboutGalleryModel.objects.all()
        service_items = AddServiceModel.objects.all()
        testimonial_items = AddTestimonialModel.objects.all()
        client_items = AddClientModel.objects.all()
        context = {'blogs': blogs,
                   'data': data,
                   'about_items': about_items,
                   'service_items': service_items,
                   'testimonial_items': testimonial_items,
                   'client_items': client_items}
        return render(request, 'home/index.html',
                      context=context)


class AboutUsView(View):
    def get(self, request):
        data = HomeModel.objects.all().first()
        about = AboutUsPageModel.objects.all().first()
        context = {'data': data,
                   'about': about}
        return render(request, 'aboutus/index.html', context=context)


class ContactUsView(View):
    def get(self, request):
        data = ContactUsPageModel.objects.all().first()
        context = {'data': data}
        return render(request, 'contactus/index.html', context=context)

    def post(self, request):
        logo = ContactUsModel.objects.all().first()

        form = request.POST
        ContactUsModel.objects.create(name=form['contact-name'],
                                      surname=form['contact-surname'],
                                      email=form['contact-email'],
                                      phone_number=form['contact-phone'],
                                      message=form['contact-message'])
        return render(request, 'contactus/index.html', context={'logo': logo})


class MissionVisionView(View):
    def get(self, request):
        data = HomeModel.objects.all().first()
        mission_vision = MissionAndVisionModel.objects.all().first()
        context = {'data': data,
                   'mission_vision': mission_vision}
        return render(request, 'mission_vision/index.html', context=context)


class CommitmentView(View):
    def get(self, request):
        logo = ContactUsModel.objects.all().first()
        data = CommitmentModel.objects.all().first()
        context = {'logo': logo, 'data': data}
        return render(request, 'commitment/index.html', context=context)


class CostumerCentricFocusView(View):
    def get(self, request):
        logo = ContactUsModel.objects.all().first()
        data = CustomerCentricFocusModel.objects.all().first()
        return render(request, 'customer_centric_focus/index.html', context={'logo': logo, 'data': data})


class SustainabilityInitiativeView(View):
    def get(self, request):
        logo = ContactUsModel.objects.all().first()
        data = SustainabilityInitiativeModel.objects.all().first()
        return render(request, 'sustainability/index.html', context={'logo': logo, 'data': data})


class WhatWeDoView(View):
    def get(self, request):
        logo = ContactUsModel.objects.all().first()
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
