from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
import re
# Create your views here.
from .models import A2Otest


class Problema1(APIView):
    renderer_classes = [JSONRenderer]

    @staticmethod
    def problema1(t):
        # t = t  # cambiar esto a cualquier cadena de entrada
        n = len(t)
        max_value = 0

        for i in range(n):
            for j in range(i + 1, n + 1):
                sub = t[i:j]
                pattern = re.compile(f'(?={sub})')
                count = len(re.findall(pattern, t))
                value = len(sub) * count
                max_value = max(max_value, value)

        return {'max_f': max_value}

    def get(self, request, *args, **kwargs):
        print('Problema 1-------------------------'+self.kwargs['t'])
        return Response(self.problema1(self.kwargs['t']))


class Problema2(APIView):
    def get_queryset(self):
        return A2Otest.objects.all()
