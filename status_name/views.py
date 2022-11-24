from django.views.decorators.cache import cache_page
from rest_framework.decorators import api_view
from rest_framework.response import Response


@cache_page(5*60)
@api_view(['GET'])
def status_view(request):
    content = {
        1: "Active", 
        0: 'Inactive',
    }
    return Response(content)