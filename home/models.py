from django.core.exceptions import ValidationError
from django.db import models


class HomeModel(models.Model):
    # Logo Section
    logo_header = models.ImageField(upload_to='img/logo')
    logo_header_alt = models.CharField(max_length=200)
    logo_footer = models.ImageField(upload_to='img/logo')
    logo_footer_alt = models.CharField(max_length=200)

    # About Us Section
    title_about = models.CharField(max_length=256)
    subtitle_about = models.CharField(max_length=256)
    description_about = models.TextField()

    # Our service Section
    title_service = models.CharField(max_length=256)
    subtitle_service = models.TextField()
    description_service = models.TextField()

    # Testimonial Section
    title_testimonial = models.CharField(max_length=64)
    header_testimonial = models.CharField(max_length=512)
    image_testimonial = models.ImageField(upload_to='img/testimonial')

    # Client Section
    title_client = models.CharField(max_length=128)
    subtitle_client = models.CharField(max_length=128)
    description_client = models.TextField()

    # Blog Section
    title_blog = models.CharField(max_length=64)
    subtitle_blog = models.CharField(max_length=64)
    description_blog = models.TextField()

    #
    class Meta:
        verbose_name = 'Home Page'
        verbose_name_plural = 'Home Page'

    def clean(self):
        if not self.pk and HomeModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Video you can not add another"
            )


class AddAboutGalleryModel(models.Model):
    image = models.ImageField(upload_to='img/about_gallery')
    alt = models.CharField(max_length=250)
    about = models.ForeignKey(HomeModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'About Item'
        verbose_name_plural = 'About Items'


class AddServiceModel(models.Model):
    service = models.ForeignKey(HomeModel, on_delete=models.CASCADE)

    icon_class = models.CharField(max_length=128)
    title = models.CharField(max_length=32)
    description = models.TextField()
    link = models.CharField(max_length=512)

    class Meta:
        verbose_name = 'Service Item'
        verbose_name_plural = 'Service Items'


class AddTestimonialModel(models.Model):
    testimonial = models.ForeignKey(HomeModel, models.CASCADE)
    description = models.TextField()
    full_name = models.CharField(max_length=32)
    role = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Testimonial Item'
        verbose_name_plural = 'Testimonial Items'


class AddClientModel(models.Model):
    client = models.ForeignKey(HomeModel, on_delete=models.CASCADE)

    logo = models.ImageField(upload_to='img/clients')
    logo_alt = models.CharField(max_length=64)
    link = models.CharField(max_length=1024)

    class Meta:
        verbose_name = 'Client Item'
        verbose_name_plural = 'Client    Items'


class ContactUsPageModel(models.Model):
    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='img/contactus')
    map = models.CharField(max_length=512)
    address = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64)
    email = models.EmailField()

    class Meta:
        verbose_name = 'ContactUs Page'
        verbose_name_plural = 'ContactUs Page'


class ContactUsModel(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    email = models.EmailField()
    phone_number = models.CharField(max_length=24)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = 'ContactUs Submitted'
        verbose_name_plural = 'ContactUs Submitted'


class AboutUsPageModel(models.Model):
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

    class Meta:
        verbose_name = 'AboutUs Page'
        verbose_name_plural = 'AboutUs Page'


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

    class Meta:
        verbose_name = 'Mission And Vision Page'
        verbose_name_plural = 'Mission And Vision Page'


class CommitmentModel(models.Model):
    banner = models.ImageField(upload_to='img/commitment')
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Commitment To Quality Page'
        verbose_name_plural = 'Commitment To Quality Page'


class AddCommitmentModel(models.Model):
    commitment = models.ForeignKey(CommitmentModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    link = models.CharField(max_length=512)
    icon_class = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Commitment To Quality Item'
        verbose_name_plural = 'Commitment To Quality Items'


class CustomerCentricFocusModel(models.Model):
    banner = models.ImageField(upload_to='img/customer_centric')
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Customer Centric Focus Page'
        verbose_name_plural = 'Customer Centric Focus Page'


class AddCustomerCentricFocusModel(models.Model):
    commitment = models.ForeignKey(CustomerCentricFocusModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    link = models.CharField(max_length=512)
    icon_class = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Customer Centric Focus Item'
        verbose_name_plural = 'Customer Centric Focus Items'


class SustainabilityInitiativeModel(models.Model):
    banner = models.ImageField(upload_to='img/sustainability')
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'Sustainability Initiative Page'
        verbose_name_plural = 'Sustainability Initiative Page'


class AddSustainabilityInitiativeModel(models.Model):
    commitment = models.ForeignKey(SustainabilityInitiativeModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    link = models.CharField(max_length=512)
    icon_class = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Sustainability Initiative Item'
        verbose_name_plural = 'Sustainability Initiative Items'


class WhatWeDoModel(models.Model):
    banner = models.ImageField(upload_to='img/what-we-do')
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    description = models.CharField(max_length=256)

    class Meta:
        verbose_name = 'What We Do Page'
        verbose_name_plural = 'What We Do Page'


class AddWhatWeDoModel(models.Model):
    commitment = models.ForeignKey(WhatWeDoModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    description = models.CharField(max_length=256)
    link = models.CharField(max_length=512)
    image = models.ImageField(upload_to='img/what-we-do')

    class Meta:
        verbose_name = 'What We Do Item'
        verbose_name_plural = 'What We Do Items'


class WhatWeDoItemModel(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='img/what-we-do')
    body = models.TextField()
    slug = models.SlugField()

    class Meta:
        verbose_name = 'What We Do SubMenu'
        verbose_name_plural = 'What We Do SubMenu'
