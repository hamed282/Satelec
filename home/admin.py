from django.contrib import admin
from .models import (AddAboutGalleryModel, HomeModel,
                     AddTestimonialModel, AddClientModel, ContactUsModel,
                     AboutUsPageModel, CommitmentModel, AddCommitmentModel,
                     SustainabilityInitiativeModel, AddCustomerCentricFocusModel, AddSustainabilityInitiativeModel,
                     CustomerCentricFocusModel, WhatWeDoModel, AddWhatWeDoModel, AddServiceModel, ContactUsPageModel,
                     MissionAndVisionModel, ElectricalEquipmentModel, HeavyMachineryModel, HealthcareProductModel,
                     SolarSystemModel, CommoditiesTradingModel)


class AboutItemInline(admin.StackedInline):
    model = AddAboutGalleryModel
    extra = 1


class OurServiceInline(admin.StackedInline):
    model = AddServiceModel
    extra = 1


class TestimonialInline(admin.StackedInline):
    model = AddTestimonialModel
    extra = 1


class ClientInline(admin.StackedInline):
    model = AddClientModel
    extra = 1


class CommitmentInline(admin.StackedInline):
    model = AddCommitmentModel
    extra = 1


class SustainabilityInitiativeInline(admin.StackedInline):
    model = AddSustainabilityInitiativeModel
    extra = 1


class CustomerCentricFocusInline(admin.StackedInline):
    model = AddCustomerCentricFocusModel
    extra = 1


class AddWhatWeDoInline(admin.StackedInline):
    model = AddWhatWeDoModel
    extra = 1


class HomeAdmin(admin.ModelAdmin):
    fieldsets = (
        ('Logo Section', {
            'fields': ('logo_header', 'logo_header_alt', 'logo_footer', 'logo_footer_alt',),
            'classes': ('collapse',),
        }),
        ('About Us Section', {
            'fields': ('title_about', 'subtitle_about', 'description_about'),
            'classes': ('collapse',),
        }),
        ('Our Services Section', {
            'fields': ('title_service', 'subtitle_service', 'description_service'),
            'classes': ('collapse',),
        }),
        ('Testimonial Section', {
            'fields': ('title_testimonial', 'header_testimonial', 'image_testimonial'),
            'classes': ('collapse',),
        }),
        ('Clients Section', {
            'fields': ('title_client', 'subtitle_client', 'description_client', ),
            'classes': ('collapse',),
        }),
        ('Blog Section', {
            'fields': ('title_blog', 'subtitle_blog', 'description_blog',),
            'classes': ('collapse',),
        }),
        ('SEO Section', {
            'fields': ('follow', 'index', 'canonical', 'meta_title', 'meta_description', 'schema_markup'),
            'classes': ('collapse',),
        }),
    )
    inlines = [AboutItemInline, OurServiceInline, TestimonialInline, ClientInline]


class CommitmentAdmin(admin.ModelAdmin):
    inlines = (CommitmentInline,)


class AddSustainabilityInitiativeAdmin(admin.ModelAdmin):
    inlines = (SustainabilityInitiativeInline,)


class AddCustomerCentricFocusAdmin(admin.ModelAdmin):
    inlines = (CustomerCentricFocusInline,)


class AddWhatWeDoAdmin(admin.ModelAdmin):
    inlines = (AddWhatWeDoInline,)


admin.site.register(HomeModel, HomeAdmin)
admin.site.register(ContactUsPageModel)
admin.site.register(ContactUsModel)
admin.site.register(AboutUsPageModel)
admin.site.register(MissionAndVisionModel)
admin.site.register(CommitmentModel, CommitmentAdmin)
admin.site.register(SustainabilityInitiativeModel, AddSustainabilityInitiativeAdmin)
admin.site.register(CustomerCentricFocusModel, AddCustomerCentricFocusAdmin)
admin.site.register(WhatWeDoModel, AddWhatWeDoAdmin)
admin.site.register(SolarSystemModel)
admin.site.register(CommoditiesTradingModel)
admin.site.register(ElectricalEquipmentModel)
admin.site.register(HealthcareProductModel)
admin.site.register(HeavyMachineryModel)
