from rest_framework import serializers

from apps.boards.models import Task
from apps.boards.serializers.comment import CommentSerializer


class TaskSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True)

    renamed_field = serializers.CharField(required=False, read_only=True, source='description')
    created_by_email = serializers.EmailField(read_only=True, source='created_by.email')
    created_by_full_name = serializers.SerializerMethodField(method_name='get_author_full_name')

    class Meta:
        model = Task
        fields = ['id', 'name', 'description', 'comments', 'renamed_field', 'created_by_email', 'created_by_full_name']
        # exclude = []

    def get_author_full_name(self, obj: Task) -> str:
        return obj.created_by.get_full_name()
