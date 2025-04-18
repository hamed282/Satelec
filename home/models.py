from django.core.exceptions import ValidationError
from django.db import models
from tinymce.models import HTMLField


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
    description_service = HTMLField()

    # Testimonial Section
    title_testimonial = models.CharField(max_length=64)
    header_testimonial = models.CharField(max_length=512)
    image_testimonial = models.ImageField(upload_to='img/testimonial')
    testimonial_alt = models.CharField(max_length=200)

    # Client Section
    title_client = models.CharField(max_length=128)
    subtitle_client = models.CharField(max_length=128)
    description_client = models.TextField()

    # Blog Section
    title_blog = models.CharField(max_length=64)
    subtitle_blog = models.CharField(max_length=64)
    description_blog = HTMLField()

    # SEO Section
    follow = models.BooleanField(default=False)
    index = models.BooleanField(default=False)
    canonical = models.CharField(max_length=256, null=True, blank=True)
    meta_title = models.CharField(max_length=60, blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    schema_markup = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Home Page'
        verbose_name_plural = 'Home Page'

    def clean(self):
        if not self.pk and HomeModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Object you can not add another"
            )

    def __str__(self):
        return 'Home'


class AddAboutGalleryModel(models.Model):
    image = models.ImageField(upload_to='img/about_gallery')
    alt = models.CharField(max_length=250)
    about = models.ForeignKey(HomeModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'About Item'
        verbose_name_plural = 'About Items'

    def __str__(self):
        return 'About'


class AddServiceModel(models.Model):
    service = models.ForeignKey(HomeModel, on_delete=models.CASCADE)

    icon_class = models.CharField(max_length=128)
    title = models.CharField(max_length=32)
    description = models.TextField()
    link = models.CharField(max_length=512)

    class Meta:
        verbose_name = 'Service Item'
        verbose_name_plural = 'Service Items'

    def __str__(self):
        return f'{self.title}'


class AddTestimonialModel(models.Model):
    testimonial = models.ForeignKey(HomeModel, models.CASCADE)
    description = models.TextField()
    full_name = models.CharField(max_length=32)
    role = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Testimonial Item'
        verbose_name_plural = 'Testimonial Items'

    def __str__(self):
        return f'{self.full_name}'


class AddClientModel(models.Model):
    client = models.ForeignKey(HomeModel, on_delete=models.CASCADE)

    logo = models.ImageField(upload_to='img/clients')
    logo_alt = models.CharField(max_length=64)
    link = models.CharField(max_length=1024)
    slug = models.SlugField()

    class Meta:
        verbose_name = 'Client Item'
        verbose_name_plural = 'Client    Items'

    def __str__(self):
        return 'Client'


class ContactUsPageModel(models.Model):
    title = models.CharField(max_length=64)
    subtitle = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='img/contactus')
    image_alt = models.CharField(max_length=200)
    longitude_map = models.CharField(max_length=16)
    latitude_map = models.CharField(max_length=16)
    address = models.CharField(max_length=64)
    phone_number = models.CharField(max_length=64)
    email = models.EmailField()

    # SEO Section
    follow = models.BooleanField(default=False)
    index = models.BooleanField(default=False)
    canonical = models.CharField(max_length=256, null=True, blank=True)
    meta_title = models.CharField(max_length=60, blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    schema_markup = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'ContactUs Page'
        verbose_name_plural = 'ContactUs Page'

    def clean(self):
        if not self.pk and ContactUsPageModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Object you can not add another"
            )

    def __str__(self):
        return 'ContactUs'


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

    def __str__(self):
        return self.email


class AboutUsPageModel(models.Model):
    banner = models.ImageField(upload_to='img/aboutus')
    banner_alt = models.CharField(max_length=200)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    description = HTMLField()

    title_about = models.CharField(max_length=128)
    subtitle_about = models.CharField(max_length=128)
    column1_title = models.CharField(max_length=128)
    column1_description = models.TextField(max_length=2000)
    column1_link = models.CharField(max_length=512)
    # column2_title = models.CharField(max_length=128)
    # column2_description = models.TextField(max_length=2000)
    # column2_link = models.CharField(max_length=512)

    # SEO Section
    follow = models.BooleanField(default=False)
    index = models.BooleanField(default=False)
    canonical = models.CharField(max_length=256, null=True, blank=True)
    meta_title = models.CharField(max_length=60, blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    schema_markup = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'AboutUs Page'
        verbose_name_plural = 'AboutUs Page'

    def clean(self):
        if not self.pk and AboutUsPageModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Object you can not add another"
            )

    def __str__(self):
        return 'AboutUs'


class MissionAndVisionModel(models.Model):
    banner = models.ImageField(upload_to='img/mission-vision')
    banner_alt = models.CharField(max_length=200)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    description = HTMLField()

    title_about = models.CharField(max_length=128)
    subtitle_about = models.CharField(max_length=128)
    column1_title = models.CharField(max_length=128)
    column1_description = models.TextField(max_length=2000)
    column1_link = models.CharField(max_length=512)
    column2_title = models.CharField(max_length=128)
    column2_description = models.TextField(max_length=2000)
    column2_link = models.CharField(max_length=512)

    # SEO Section
    follow = models.BooleanField(default=False)
    index = models.BooleanField(default=False)
    canonical = models.CharField(max_length=256, null=True, blank=True)
    meta_title = models.CharField(max_length=60, blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    schema_markup = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Mission And Vision Page'
        verbose_name_plural = 'Mission And Vision Page'

    def clean(self):
        if not self.pk and MissionAndVisionModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Object you can not add another"
            )

    def __str__(self):
        return 'Mission And Vision'


class CommitmentModel(models.Model):
    banner = models.ImageField(upload_to='img/commitment')
    banner_alt = models.CharField(max_length=200)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    description = HTMLField()

    # SEO Section
    follow = models.BooleanField(default=False)
    index = models.BooleanField(default=False)
    canonical = models.CharField(max_length=256, null=True, blank=True)
    meta_title = models.CharField(max_length=60, blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    schema_markup = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Commitment To Quality Page'
        verbose_name_plural = 'Commitment To Quality Page'

    def clean(self):
        if not self.pk and CommitmentModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Object you can not add another"
            )

    def __str__(self):
        return 'Commitment'


class AddCommitmentModel(models.Model):
    commitment = models.ForeignKey(CommitmentModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2000)
    link = models.CharField(max_length=512)
    icon_class = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Commitment To Quality Item'
        verbose_name_plural = 'Commitment To Quality Items'

    def __str__(self):
        return f'{self.title}'


class CustomerCentricFocusModel(models.Model):
    banner = models.ImageField(upload_to='img/customer_centric')
    banner_alt = models.CharField(max_length=200)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    description = HTMLField()

    # SEO Section
    follow = models.BooleanField(default=False)
    index = models.BooleanField(default=False)
    canonical = models.CharField(max_length=256, null=True, blank=True)
    meta_title = models.CharField(max_length=60, blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    schema_markup = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Customer Centric Focus Page'
        verbose_name_plural = 'Customer Centric Focus Page'

    def clean(self):
        if not self.pk and CustomerCentricFocusModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Object you can not add another"
            )

    def __str__(self):
        return 'Customer Centric Focus'


class AddCustomerCentricFocusModel(models.Model):
    customer = models.ForeignKey(CustomerCentricFocusModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2000)
    link = models.CharField(max_length=512)
    icon_class = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Customer Centric Focus Item'
        verbose_name_plural = 'Customer Centric Focus Items'

    def __str__(self):
        return f'{self.title}'


class SustainabilityInitiativeModel(models.Model):
    banner = models.ImageField(upload_to='img/sustainability')
    banner_alt = models.CharField(max_length=200)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    description = HTMLField()

    # SEO Section
    follow = models.BooleanField(default=False)
    index = models.BooleanField(default=False)
    canonical = models.CharField(max_length=256, null=True, blank=True)
    meta_title = models.CharField(max_length=60, blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    schema_markup = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Sustainability Initiative Page'
        verbose_name_plural = 'Sustainability Initiative Page'

    def clean(self):
        if not self.pk and SustainabilityInitiativeModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Object you can not add another"
            )

    def __str__(self):
        return 'Sustainability Initiative'


class AddSustainabilityInitiativeModel(models.Model):
    sustainability = models.ForeignKey(SustainabilityInitiativeModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    description = models.TextField(max_length=2000)
    link = models.CharField(max_length=512)
    icon_class = models.CharField(max_length=128)

    class Meta:
        verbose_name = 'Sustainability Initiative Item'
        verbose_name_plural = 'Sustainability Initiative Items'

    def __str__(self):
        return f'{self.title}'


class WhatWeDoModel(models.Model):
    banner = models.ImageField(upload_to='img/what-we-do')
    banner_alt = models.CharField(max_length=200)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    description = HTMLField()

    # SEO Section
    follow = models.BooleanField(default=False)
    index = models.BooleanField(default=False)
    canonical = models.CharField(max_length=256, null=True, blank=True)
    meta_title = models.CharField(max_length=60, blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    schema_markup = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'What We Do Page'
        verbose_name_plural = 'What We Do Page'

    def clean(self):
        if not self.pk and WhatWeDoModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Object you can not add another"
            )

    def __str__(self):
        return 'What We Do'


class AddWhatWeDoModel(models.Model):
    what_we_do = models.ForeignKey(WhatWeDoModel, on_delete=models.CASCADE)
    title = models.CharField(max_length=128)
    subtitle = models.CharField(max_length=128)
    description = models.TextField(max_length=2000)
    link = models.CharField(max_length=512)
    image = models.ImageField(upload_to='img/what-we-do')
    image_alt = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'What We Do Item'
        verbose_name_plural = 'What We Do Items'

    def __str__(self):
        return f'{self.title}'


class ElectricalEquipmentModel(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='img/what-we-do')
    image_alt = models.CharField(max_length=64)
    body = HTMLField()

    # SEO Section
    follow = models.BooleanField(default=False)
    index = models.BooleanField(default=False)
    canonical = models.CharField(max_length=256, null=True, blank=True)
    meta_title = models.CharField(max_length=60, blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    schema_markup = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Electrical Equipment Page'
        verbose_name_plural = 'Electrical Equipment Page'

    def clean(self):
        if not self.pk and ElectricalEquipmentModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Object you can not add another"
            )

    def __str__(self):
        return 'Electrical Equipment'


class SolarSystemModel(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='img/what-we-do')
    image_alt = models.CharField(max_length=64)
    body = HTMLField()

    # SEO Section
    follow = models.BooleanField(default=False)
    index = models.BooleanField(default=False)
    canonical = models.CharField(max_length=256, null=True, blank=True)
    meta_title = models.CharField(max_length=60, blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    schema_markup = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Solar System Page'
        verbose_name_plural = 'Solar System Page'

    def clean(self):
        if not self.pk and SolarSystemModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Object you can not add another"
            )

    def __str__(self):
        return 'Solar System'


class HeavyMachineryModel(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='img/what-we-do')
    image_alt = models.CharField(max_length=64)
    body = HTMLField()

    # SEO Section
    follow = models.BooleanField(default=False)
    index = models.BooleanField(default=False)
    canonical = models.CharField(max_length=256, null=True, blank=True)
    meta_title = models.CharField(max_length=60, blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    schema_markup = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Heavy Machinery Page'
        verbose_name_plural = 'Heavy Machinery Page'

    def clean(self):
        if not self.pk and HeavyMachineryModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Object you can not add another"
            )

    def __str__(self):
        return 'Heavy Machinery'


class CommoditiesTradingModel(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='img/what-we-do')
    image_alt = models.CharField(max_length=64)
    body = HTMLField()

    # SEO Section
    follow = models.BooleanField(default=False)
    index = models.BooleanField(default=False)
    canonical = models.CharField(max_length=256, null=True, blank=True)
    meta_title = models.CharField(max_length=60, blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    schema_markup = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Commodities Trading Page'
        verbose_name_plural = 'Commodities Trading Page'

    def clean(self):
        if not self.pk and CommoditiesTradingModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Object you can not add another"
            )

    def __str__(self):
        return 'Commodities Trading'


class HealthcareProductModel(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()
    image = models.ImageField(upload_to='img/what-we-do')
    image_alt = models.CharField(max_length=64)
    body = HTMLField()

    # SEO Section
    follow = models.BooleanField(default=False)
    index = models.BooleanField(default=False)
    canonical = models.CharField(max_length=256, null=True, blank=True)
    meta_title = models.CharField(max_length=60, blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    schema_markup = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = 'Healthcare Product Page'
        verbose_name_plural = 'Healthcare Product Page'

    def clean(self):
        if not self.pk and HealthcareProductModel.objects.exists():
            # This below line will render error by breaking page, you will see
            raise ValidationError(
                "There can be only one Object you can not add another"
            )

    def __str__(self):
        return 'Healthcare Product'


class PartnerModel(models.Model):
    name = models.CharField(max_length=64)
    title = models.CharField(max_length=64)
    logo = models.ImageField(upload_to='img/clients')
    logo_alt = models.CharField(max_length=64)
    description = models.TextField()
    overview = models.TextField()
    website = models.CharField(max_length=160)
    video = models.FileField(upload_to='video/partner')
    # products = models.TextField()
    # features = models.TextField()
    slug = models.SlugField()

    # SEO Section
    follow = models.BooleanField(default=False)
    index = models.BooleanField(default=False)
    canonical = models.CharField(max_length=256, null=True, blank=True)
    meta_title = models.CharField(max_length=60, blank=True, null=True)
    meta_description = models.CharField(max_length=160, blank=True, null=True)
    schema_markup = models.TextField(null=True, blank=True)


class AddPartnerProductModel(models.Model):
    product = models.CharField(max_length=64)
    description = models.TextField()
    partner = models.ForeignKey(PartnerModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Partner Product'
        verbose_name_plural = 'Partner products'

    def __str__(self):
        return f'{self.partner}'


class AddPartnerFeatureModel(models.Model):
    feature = models.CharField(max_length=64)
    description = models.TextField()
    partner = models.ForeignKey(PartnerModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Partner Feature'
        verbose_name_plural = 'Partner Features'

    def __str__(self):
        return f'{self.partner}'


class AddPartnerGalleryModel(models.Model):
    image = models.ImageField(upload_to='img/partner_gallery')
    alt = models.CharField(max_length=250)
    partner = models.ForeignKey(PartnerModel, on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Partner Feature'
        verbose_name_plural = 'Partner Features'

    def __str__(self):
        return f'{self.partner}'
