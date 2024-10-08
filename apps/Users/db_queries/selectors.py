from ..serializers import OutputSerializers
from ..models import User


def get_user_info(request):
    target_user = User.objects.get(id=request.user.id)
    user = OutputSerializers.UserInfoSerializer(target_user, many=False)
    return user.data
