import uuid
import math

from django.shortcuts import get_object_or_404
from django.db.models import IntegerField
from django.db.models.functions import Cast, Substr

from rest_framework import views
from rest_framework.status import *
from rest_framework.response import Response

from .models import *
from .serializers import *


class BoothListView(views.APIView):
    serializer_class = BoothListSerializer

    def get(self, request):
        user = request.user
        
        day = request.GET.get('day')
        college = request.GET.get('college')

        params = {'day': day, 'college': college}
        arguments = {}
        for key, value in params.items():
            if value:
                arguments[key] = value

        booths = Booth.objects.filter(**arguments).annotate(
                    number_order = Cast(Substr("number", 2), IntegerField())
                ).order_by("number_order")
        total = booths.__len__()
        total_page = math.ceil(total/10)
        booths = self.paginate_queryset(booths)

        if user:
            for booth in booths:
                if booth.like.filter(pk=user.id).exists():
                    booth.is_liked=True
        
        serializer = self.serializer_class(booths, many=True)
        return Response({'message': '부스 목록 조회 성공', 'total': total, 'total_page' : total_page, 'data': serializer.data}, status=HTTP_200_OK)