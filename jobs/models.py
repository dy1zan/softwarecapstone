from datetime import timedelta

from django.contrib.postgres.search import SearchQuery, SearchVector
from django.core.validators import RegexValidator
from django.db import models
from django.utils import timezone

from entity.models import Company


class Job(models.Model):

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='jobs')
    title = models.CharField(required=True, max_length=30)
    description = models.TextField(max_length=500*5.1)  # average word length=5.1
    contact_email = models.EmailField()
    contact_phone = models.CharField(max_length=15, validators=[
        RegexValidator(regex='^[0-9]*$', message="A phone number can only contain numbers.")
    ])
    expiry = models.DateTimeField(default=(timezone.now+timedelta(days=14)))
    external_link = models.CharField(max_length=2083)  # IE has URL max length=2083

    @classmethod
    def search_jobs(cls, term: str):
        """
        Searches jobs against a given search term. If term is None, show all.
        """
        if term is None:
            result = cls.objects.all()
        
        else:
            search_query = SearchQuery(term)

            search_vector = SearchVector('title') \
                + SearchVector('description')
        
            result = cls.objects.annotate(search=search_vector) \
                .filter(search=search_query)

        return result