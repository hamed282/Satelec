from django.db import models


class LogoModel(models.Model):
    logo_header = models.ImageField(upload_to='img/logo')
    logo_header_alt = models.CharField(max_length=200)
    logo_footer = models.ImageField(upload_to='img/logo')
    logo_footer_alt = models.CharField(max_length=200)

    class Meta:
        verbose_name = 'Header And Footer Logo'
        verbose_name_plural = 'Header And Footer Logo'


class HomeAboutUsModel(models.Model):
    title = models.CharField(max_length=256)
    subtitle = models.TextField()

    class Meta:
        verbose_name = 'About Us Section'
        verbose_name_plural = 'About Us Section'


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


class AddTestimonialModel(models.Model):
    testimonial = models.ForeignKey(TestimonialModel, models.CASCADE)
    description = models.TextField()
    full_name = models.CharField(max_length=32)
    role = models.CharField(max_length=128)


class ClientModel(models.Model):
    title = models.CharField(max_length=128)
    description = models.TextField()


class AddClientModel(models.Model):
    client = models.ForeignKey(ClientModel, on_delete=models.CASCADE)

    logo = models.ImageField(upload_to='img/clients')
    logo_alt = models.CharField(max_length=64)
    link = models.CharField(max_length=1024)


class BlogModel(models.Model):
    title = models.CharField(max_length=64)
    description = models.TextField()


class ContactUsModel(models.Model):
    name = models.CharField(max_length=32)
    surname = models.CharField(max_length=32)
    email = models.EmailField()
    phone_number = models.CharField(max_length=24)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
