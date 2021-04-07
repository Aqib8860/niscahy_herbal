from django.db import models

# Create your models here.


INDUSTRY = (
    ("Accountancy", "Accountancy"),
    ("Business", "Business"),
    ("Charity and Voluntary Work", "Charity and Voluntary Work"),
    ("Creative Arts and Design", "Creative Arts and Design"),
    ("Energy and Utilities", "Energy and Utilities"),
    ("Creative Arts and Design", "Creative Arts and Design"),
    ("Engineering and Manufacturing", "Engineering and Manufacturing"),
    ("Environment and Agriculture", "Environment and Agriculture"),
    ("Healthcare", "Healthcare"),
    ("Hospitality and Event Management", "Hospitality and Event Management"),
    ("Information Technology", "Information Technology"),
    ("Law", "Law"),
    ("Leisure, Sports, and Tourism", "Leisure, Sports, and Tourism"),
    ("Marketing, Advertising, and PR", "Marketing, Advertising, and PR"),
    ("Media and Internet", "Media and Internet"),
    ("Property and Consultation", "Property and Consultation"),
    ("Public Services and Administration", "Public Services and Administration"),
    ("Recruitment and HR", "Recruitment and HR"),
    ("Retail", "Retail"),
    ("Sales", "Sales"),
    ("Science and Pharmaceuticals", "Science and Pharmaceuticals"),
    ("Social Care", "Social Care"),
    ("Teacher Training and Education", "Teacher Training and Education"),
    ("Transport and Logistics", "Transport and Logistics"),
)

STATUS = (
    ("Applied", "Applied"),
    ("Selected", "Selected"),
    ("Not Selected", "Not Selected"),
    ("Shortlisted", "Shortlisted"),
)


class JobRecruiter(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT, null=True)
    company_name = models.CharField(max_length=80, null=True)
    job_title = models.CharField(max_length=80, null=True)
    location = models.CharField(max_length=50, null=True)
    your_name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=12, null=True)
    industry = models.CharField(max_length=80, null=True, choices=INDUSTRY)
    experience = models.CharField(max_length=20, null=True)
    salary_from = models.CharField(max_length=20, null=True)
    salary_to = models.CharField(max_length=20, null=True)
    date = models.DateField(auto_now_add=True)
    approved = models.BooleanField(default=False)
    description = models.TextField(null=True)
    requirements = models.TextField(null=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return str(self.job_title)


class JobSeeker(models.Model):
    user = models.ForeignKey('core.User', on_delete=models.PROTECT, null=True)
    resume = models.FileField(null=True, blank=True, upload_to="Job/Resume/")
    job = models.ForeignKey('job.JobRecruiter', on_delete=models.PROTECT, null=True)
    date = models.DateField(auto_now_add=True)
    saved = models.BooleanField(default=False)
    applied = models.BooleanField(default=False)
    status = models.CharField(max_length=50, null=True, choices=STATUS, default="Applied")
    extra_field = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self):
        return str(self.user)

    """@property
    def resume_url(self):
        if self.resume and hasattr(self.resume, 'url'):
            return self.resume.url"""
