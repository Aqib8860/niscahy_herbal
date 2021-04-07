from django.db import models

# Create your models here.


class DigitalProfile(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT, null=True)
    company_name = models.CharField(max_length=80, null=True)
    company_logo = models.ImageField(null=True, upload_to="DigitalProfile/Company/")
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return str(self.company_name)


class PersonalDetail(models.Model):
    digital_profile = models.ForeignKey(DigitalProfile, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=80, null=True)
    mobile = models.CharField(max_length=12, null=True)
    designation = models.CharField(max_length=40, null=True)
    email = models.EmailField(max_length=60, null=True)
    whatsapp = models.CharField(max_length=12, null=True)
    address = models.CharField(max_length=150, null=True)
    website = models.URLField(null=True, blank=True)
    location = models.CharField(max_length=40, null=True)
    about_us = models.TextField(max_length=250, null=True)

    def __str__(self):
        return str(self.digital_profile)


class SocialMediaLinks(models.Model):
    digital_profile = models.ForeignKey(DigitalProfile, on_delete=models.CASCADE, null=True)
    facebook_link = models.URLField(null=True, blank=True)
    instagram_link = models.URLField(null=True, blank=True)
    twitter_link = models.URLField(null=True, blank=True)
    youtube_link = models.URLField(null=True, blank=True)
    linkedin_link = models.URLField(null=True, blank=True)
    other_link = models.URLField(null=True, blank=True)

    def __str__(self):
        return str(self.digital_profile)


class PaymentDetail(models.Model):
    digital_profile = models.ForeignKey(DigitalProfile, on_delete=models.CASCADE, null=True)
    paytm_number = models.CharField(max_length=12, null=True, blank=True)
    paytm_qr_code = models.ImageField(null=True, blank=True, upload_to="DigitalProfile/PaymentDetail/")
    google_pay_number = models.CharField(max_length=12, null=True, blank=True)
    google_pay_qr_code = models.ImageField(null=True, blank=True, upload_to="DigitalProfile/PaymentDetail/")
    phonepe_number = models.CharField(max_length=12, null=True, blank=True)
    phonepe_qr_code = models.ImageField(null=True, blank=True, upload_to="DigitalProfile/PaymentDetail/")
    account_number = models.CharField(max_length=40, null=True)
    account_holder_name = models.CharField(max_length=50, null=True)
    re_account_number = models.CharField(max_length=40, null=True)
    ifsc_code = models.CharField(max_length=20, null=True)
    branch_name = models.CharField(max_length=60, null=True)
    gst_number = models.CharField(max_length=60, null=True)

    def __str__(self):
        return str(self.digital_profile)


class Services(models.Model):
    digital_profile = models.ForeignKey(DigitalProfile, on_delete=models.CASCADE, null=True)
    service_name1 = models.CharField(max_length=50, null=True, blank=True)
    service_image1 = models.ImageField(blank=True, null=True, upload_to="DigitalProfile/Services/")
    service_name2 = models.CharField(max_length=50, null=True, blank=True)
    service_image2 = models.ImageField(blank=True, null=True, upload_to="DigitalProfile/Services/")
    service_name3 = models.CharField(max_length=50, null=True, blank=True)
    service_image3 = models.ImageField(blank=True, null=True, upload_to="DigitalProfile/Services/")

    def __str__(self):
        return str(self.digital_profile)


class Ecommerce(models.Model):
    digital_profile = models.ForeignKey(DigitalProfile, on_delete=models.CASCADE, null=True)
    product_image = models.ImageField(blank=True, null=True, upload_to="DigitalProfile/Ecommerce/")
    product_name = models.CharField(max_length=80, null=True, blank=True)
    product_mrp = models.CharField(max_length=100, null=True, blank=True)
    selling_price = models.CharField(max_length=100, null=True, blank=True)
    category = models.CharField(max_length=100, null=True, blank=True)
    description = models.TextField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.digital_profile)


class Gallery(models.Model):
    digital_profile = models.ForeignKey(DigitalProfile, on_delete=models.CASCADE, null=True)
    image1 = models.ImageField(null=True, upload_to="DigitalProfile/Gallery/", blank=True)
    image2 = models.ImageField(null=True, upload_to="DigitalProfile/Gallery", blank=True)
    image3 = models.ImageField(null=True, upload_to="DigitalProfile/Gallery", blank=True)
    image4 = models.ImageField(null=True, upload_to="DigitalProfile/Gallery", blank=True)
    image5 = models.ImageField(null=True, upload_to="DigitalProfile/Gallery", blank=True)

    def __str__(self):
        return str(self.digital_profile)