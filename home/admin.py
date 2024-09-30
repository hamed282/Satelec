from django.contrib import admin
from .models import (LogoModel, AddAboutGalleryModel, HomeAboutUsModel, OurServiceModel, ServiceItemModel,
                     TestimonialModel, AddTestimonialModel, ClientModel, AddClientModel, BlogModel, ContactUsModel)


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


class HomeAboutUsAdmin(admin.ModelAdmin):
    inlines = (LogoGalleryInline,)


class OurServiceAdmin(admin.ModelAdmin):
    inlines = (OurServiceInline,)


class TestimonialAdmin(admin.ModelAdmin):
    inlines = (TestimonialInline,)


class ClientAdmin(admin.ModelAdmin):
    inlines = (ClientInline,)


admin.site.register(LogoModel)
admin.site.register(HomeAboutUsModel, HomeAboutUsAdmin)
admin.site.register(OurServiceModel, OurServiceAdmin)
admin.site.register(TestimonialModel, TestimonialAdmin)
admin.site.register(ClientModel, ClientAdmin)
admin.site.register(BlogModel)
admin.site.register(ContactUsModel)
