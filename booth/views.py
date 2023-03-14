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
from .permissions import IsAuthorOrReadOnly


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
    
class BoothDetailView(views.APIView):
    serializer_class = BoothDetailSerializer
    permission_classes = [IsAuthorOrReadOnly]

    def get_object(self, pk):
        booth = get_object_or_404(Booth, pk=pk)
        self.check_object_permissions(self.request, booth)
        return booth

    def get(self, request, pk):
        user = request.user
        booth = self.get_object(pk=pk)

        if booth.like.filter(pk=user.id).exists():
            booth.is_liked=True

        serializer = self.serializer_class(booth)

        return Response({'message': '부스 상세 조회 성공', 'data': serializer.data}, status=HTTP_200_OK)

    def patch(self, request, pk):
        booth = self.get_object(pk=pk)
        serializer = self.serializer_class(data=request.data, instance=booth, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response({'message': '부스 정보 수정 성공', 'data': serializer.data}, status=HTTP_200_OK)
        else:
            return Response({'message': '부스 정보 수정 실패', 'data': serializer.errors}, status=HTTP_400_BAD_REQUEST)