from django.core.exceptions import ValidationError
from django.db import models


class LogoModel(models.Model):
    logo_header = models.ImageField(upload_to='img/logo')
    logo_header_alt = models.CharField(max_length=200)
    logo_footer = models.ImageField(upload_to='img/logo')
    logo_footer_alt = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Header And Footer Logo'
        verbose_name_plural = 'Header And Footer Logo'

    def clean(self):
        if not self.pk and LogoModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Video you can not add another"
            )


class HomeAboutUsModel(models.Model):
    title = models.CharField(max_length=256)
    subtitle = models.TextField()

    class Meta:
        verbose_name = 'About Us Section'
        verbose_name_plural = 'About Us Section'

    def clean(self):
        if not self.pk and HomeAboutUsModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Video you can not add another"
            )


class AddAboutGalleryModel(models.Model):
    image = models.ImageField(upload_to='img/about_gallery')
    alt = models.CharField(max_length=250)
    about = models.ForeignKey(HomeAboutUsModel, on_delete=models.CASCADE)


class OurServiceModel(models.Model):
    title = models.CharField(max_length=256)
    subtitle = models.TextField()

    class Meta:
        verbose_name = 'Our service Section'
        verbose_name_plural = 'Our Service Section'

    def clean(self):
        if not self.pk and OurServiceModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Video you can not add another"
            )


class ServiceItemModel(models.Model):
    service = models.ForeignKey(OurServiceModel, on_delete=models.CASCADE)

    icon_class = models.CharField(max_length=128)
    title = models.CharField(max_length=32)
    description = models.TextField()
    link = models.CharField(max_length=512)


class TestimonialModel(models.Model):
    title = models.CharField(max_length=64)
    header = models.CharField(max_length=512)
    image = models.ImageField(upload_to='img/testimonial')

    class Meta:
        verbose_name = 'Testimonial Section'
        verbose_name_plural = 'Testimonial Section'

    def clean(self):
        if not self.pk and TestimonialModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Video you can not add another"
            )


class AddTestimonialModel(models.Model):
    testimonial = models.ForeignKey(TestimonialModel, models.CASCADE)
    description = models.TextField()
    full_name = models.CharField(max_length=32)
    role = models.CharField(max_length=128)


class ClientModel(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()

    class Meta:
        verbose_name = 'Client Section'
        verbose_name_plural = 'Client Section'

    def clean(self):
        if not self.pk and ClientModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Video you can not add another"
            )


class AddClientModel(models.Model):
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)

    logo = models.ImageField(upload_to='img/clients')
    logo_alt = models.CharField(max_length=64)
    link = models.CharField(max_length=1024)


class BlogModel(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()

    class Meta:
        verbose_name = 'Blog Section'
        verbose_name_plural = 'Blog Section'

    def clean(self):
        if not self.pk and BlogModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Video you can not add another"
            )


class ContactUsModel(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    email = models.EmailField()
    phone_number = models.CharField(max_length=24)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'Contact Us'
        verbose_name_plural = 'Contact Us'


class AboutPageModel(models.Model):
    banner = models.ImageField(upload_to='img/aboutus')
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    title_about = models.CharField(max_length=128)
    subtitle_about = models.CharField(max_length=128)
    column1_title = models.CharField(max_length=128)
    column1_description = models.TextField(max_length=512)
    column1_link = models.CharField(max_length=512)
    column2_title = models.CharField(max_length=128)
    column2_description = models.TextField(max_length=512)
    column2_link = models.CharField(max_length=512)


class MissionAndVisionModel(models.Model):
    banner = models.ImageField(upload_to='img/mission-vision')
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    title_about = models.CharField(max_length=128)
    subtitle_about = models.CharField(max_length=128)
    column1_title = models.CharField(max_length=128)
    column1_description = models.TextField(max_length=512)
    column1_link = models.CharField(max_length=512)
    column2_title = models.CharField(max_length=128)
    column2_description = models.TextField(max_length=512)
    column2_link = models.CharField(max_length=512)


class CommitmentModel(models.Model):
    banner = models.ImageField(upload_to='img/commitment')
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    description = models.CharField(max_length=256)


class AddCommitmentModel(models.Model):
    commitment = models.ForeignKey(CommitmentModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    link = models.CharField(max_length=512)
    icon_class = models.CharField(max_length=128)


class CustomerCentricFocusModel(models.Model):
    banner = models.ImageField(upload_to='img/customer_centric')
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    description = models.CharField(max_length=256)


class AddCustomerCentricFocusModel(models.Model):
    commitment = models.ForeignKey(CustomerCentricFocusModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    link = models.CharField(max_length=512)
    icon_class = models.CharField(max_length=128)


class SustainabilityInitiativeModel(models.Model):
    banner = models.ImageField(upload_to='img/sustainability')
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    description = models.CharField(max_length=256)


class AddSustainabilityInitiativeModel(models.Model):
    commitment = models.ForeignKey(SustainabilityInitiativeModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    link = models.CharField(max_length=512)
    icon_class = models.CharField(max_length=128)


class WhatWeDoModel(models.Model):
    banner = models.ImageField(upload_to='img/what-we-do')
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    description = models.CharField(max_length=256)


class AddWhatWeDoModel(models.Model):
    commitment = models.ForeignKey(WhatWeDoModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    link = models.CharField(max_length=512)
    image = models.ImageField(upload_to='img/what-we-do')


