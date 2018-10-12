from django.urls import path
from django.conf.urls import url
from .views import company
from .views import group
from .views import get_members

app_name = "entity"

urlpatterns = [
    path('company/apply', company.ApplyCompany.as_view(), name='company_application'),
    path('company/profile/edit', company.edit_comp, name='company_application'),
    path('companies/', company.Listing.as_view(), name='company_listing'),
    path('company/<company>/', company.Profile.as_view(), name='company_profile'),
    path('groups/', group.Listing.as_view(), name='group_listing'),
    path('groups/<group>/', group.Profile.as_view(), name='group_profile'),
    # only restrict the below URL 'entity' to groups or companies
    url(r'^(?P<entity>groups|companies)/(?P<entity_name>[0-9A-Za-z]{0,20})/members', get_members, name='group_members'),
]
