from django.contrib import admin
from .models import (LogoModel, AddAboutGalleryModel, HomeAboutUsModel, OurServiceModel, ServiceItemModel,
                     TestimonialModel, AddTestimonialModel, ClientModel, AddClientModel, BlogModel, ContactUsModel,
                     AboutPageModel, MissionAndVisionModel, CommitmentModel, AddCommitmentModel,
                     SustainabilityInitiativeModel, AddCustomerCentricFocusModel, AddSustainabilityInitiativeModel,
                     CustomerCentricFocusModel, WhatWeDoModel, AddWhatWeDoModel)


class LogoGalleryInline(admin.TabularInline):
    model = AddAboutGalleryModel
    extra = 1


class OurServiceInline(admin.TabularInline):
    model = ServiceItemModel
    extra = 1


class TestimonialInline(admin.TabularInline):
    model = AddTestimonialModel
    extra = 1


class ClientInline(admin.TabularInline):
    model = AddClientModel
    extra = 1


class CommitmentInline(admin.TabularInline):
    model = AddCommitmentModel
    extra = 1


class SustainabilityInitiativeInline(admin.TabularInline):
    model = AddSustainabilityInitiativeModel
    extra = 1


class CustomerCentricFocusInline(admin.TabularInline):
    model = AddCustomerCentricFocusModel
    extra = 1


class AddWhatWeDoInline(admin.TabularInline):
    model = AddWhatWeDoModel
    extra = 1


class HomeAboutUsAdmin(admin.ModelAdmin):
    inlines = (LogoGalleryInline,)


class OurServiceAdmin(admin.ModelAdmin):
    inlines = (OurServiceInline,)


class TestimonialAdmin(admin.ModelAdmin):
    inlines = (TestimonialInline,)


class ClientAdmin(admin.ModelAdmin):
    inlines = (ClientInline,)


class CommitmentAdmin(admin.ModelAdmin):
    inlines = (CommitmentInline,)


class AddSustainabilityInitiativeAdmin(admin.ModelAdmin):
    inlines = (SustainabilityInitiativeInline,)


class AddCustomerCentricFocusAdmin(admin.ModelAdmin):
    inlines = (CustomerCentricFocusInline,)


class AddWhatWeDoAdmin(admin.ModelAdmin):
    inlines = (AddWhatWeDoInline,)


admin.site.register(LogoModel)
admin.site.register(HomeAboutUsModel, HomeAboutUsAdmin)
admin.site.register(OurServiceModel, OurServiceAdmin)
admin.site.register(TestimonialModel, TestimonialAdmin)
admin.site.register(ClientModel, ClientAdmin)
admin.site.register(BlogModel)
admin.site.register(ContactUsModel)
admin.site.register(AboutPageModel)
admin.site.register(MissionAndVisionModel)
admin.site.register(CommitmentModel, CommitmentAdmin)
admin.site.register(SustainabilityInitiativeModel, AddSustainabilityInitiativeAdmin)
admin.site.register(CustomerCentricFocusModel, AddCustomerCentricFocusAdmin)
admin.site.register(WhatWeDoModel, AddWhatWeDoAdmin)
