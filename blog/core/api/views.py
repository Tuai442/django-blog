from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from core.models import Recipe  # Import your models here

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def toggleLike(request):
    recipe_id = request.data.get('recipe_id')

    try:
        recipe = Recipe.objects.get(id=recipe_id)
    except Recipe.DoesNotExist:
        return Response({'error': 'Recipe not found'}, status=404)

    user = request.user
    print(recipe)
    if recipe.likes.filter(id=user.id).exists():
        recipe.likes.remove(user)
    else:
        recipe.likes.add(user)

    return Response({'success': 'OK'})
