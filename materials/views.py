from rest_framework.viewsets import ModelViewSet
from .models import Material
from .serializers import MaterialSerializer
# from users.permissions import IsAdminUserOrReadOnly

class MaterialViewSet(ModelViewSet):
    queryset = Material.objects.all()
    serializer_class = MaterialSerializer
    # permission_classes = [IsAdminUserOrReadOnly]





