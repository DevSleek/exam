from rest_framework.generics import ListAPIView, CreateAPIView
from rest_framework.response import Response
from django.db.models import Value

from enterprise.serializers import RequestSerializer, ResultSerializer
from enterprise.models import Product, Warehouse


class ResultCreateAPIView(CreateAPIView):
    serializer_class = RequestSerializer

    def post(self, request, *args, **kwargs):
        product = request.data['product']
        quantity = request.data['quantity']

        products = Product.objects.filter(name=product).annotate(
            quantity=Value(quantity)
        ).prefetch_related('product_material')

        serializer = ResultSerializer(instance=products, many=True)

        return Response(
            {
                'result': serializer.data
            }
        )

