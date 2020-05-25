from shared.serializers import PageSerializer


class UserListSerializer(PageSerializer):
    resource_name = 'users'
