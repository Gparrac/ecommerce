from rest_framework import generics
from apps.base.api import GeneralListApiView
from apps.products.api.serializers.product_serializer import ProductSerializer
from rest_framework.response import Response
from rest_framework import status
class ProductListApiView(GeneralListApiView):
    serializer_class = ProductSerializer 
# useful to use list and create in the same class and harness the same endpoint
class ProductListCreateApiView(generics.ListCreateAPIView):
    serializer_class = ProductSerializer
    queryset = serializer_class.Meta.model.objects.filter(state = True)

    #rewrite method to custom post handle
    def post(self, request):
        serializer = self.serializer_class(data = request.data)        
        if serializer.is_valid():
            serializer.save()
            return Response('Producto creado exitosamente', status= status.HTTP_201_CREATED)        
        return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)
    
class ProductRetrieveAPIView(generics.RetrieveAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)

class ProductDestroyAPIView(generics.DestroyAPIView):
    serializer_class = ProductSerializer
    def get_queryset(self):
        return self.get_serializer().Meta.model.objects.filter(state = True)
    def delete(self, request, pk=None):
        product = self.get_queryset().filter(id=pk).first()
        if product:
            product.state = False
            product.save()
            return Response({'message': 'Producto eliminado correctamente'}, status= status.HTTP_200_OK)
        return Response({'error': 'No existe un Producto con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)
class ProductUpdateAPIview(generics.UpdateAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self, pk):
        return self.get_serializer().Meta.model.objects.filter(state = True).filter(id = pk).first()
    def patch(self, request, pk=None):
        product = self.get_queryset(pk)
        if product:
            product_serializer = self.serializer_class(product)
            return Response(product_serializer.data, status = status.HTTP_200_OK)        
        return Response({'error': 'No existe un Producto con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)
    
    def put(self, request, pk=None):
        product = self.get_queryset(pk)
        print('passing', product)
        if product:            
            product_serializer = self.serializer_class(product, data = request.data)  
            if product_serializer.is_valid():      
                product_serializer.save()
                return Response(product_serializer.data, status = status.HTTP_200_OK)        
        return Response({'error': 'No existe un Producto con estos datos!'}, status = status.HTTP_400_BAD_REQUEST)