"""
Models which defines a company
"""
from django.contrib.postgres.search import SearchQuery, SearchVector
from django.db import models

from entity.models import Entity


class Group(Entity):

    # FIELDS
    description = models.TextField(max_length=500*5.1)  # 5.1 chars = average word length
    website = models.CharField(max_length=2056)

    def __str__(self):
        return "{0} ({1})".format(super().name, self.pk)

    @classmethod
    def search_groups(cls, term: str):
        """
        Searches companies or shows all if `term` is None
        :param term: the search string
        :return: list of companies
        """
        if term is None or term == "":
            result = cls.objects.filter(application__status="approved")

        else:
            search_query = SearchQuery(term)
            search_vector = SearchVector('name') + \
                SearchVector('website')

            result = cls.objects.annotate(search=search_vector) \
                .filter(search=search_query) \
                .filter(application__status="approved")

        return result
