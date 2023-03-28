from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

class IndexPage(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'page/index.html'
    #resgatar o html

    def get(self, request):
        return Response({})