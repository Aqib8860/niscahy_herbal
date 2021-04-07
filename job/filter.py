from .models import *
import django_filters
from django_filters import DateRangeFilter,DateFilter


class ViewJobFilter(django_filters.FilterSet):
    applied = django_filters.BooleanFilter()
    saved = django_filters.BooleanFilter()
    date = DateRangeFilter()

    class Meta:
        model = JobSeeker
        fields = ['applied', 'saved', 'date']
