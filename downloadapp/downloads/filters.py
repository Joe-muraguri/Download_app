import django_filters
from django_filters import CharFilter
from .models import FileAdmin


class FileFilter(django_filters.FilterSet):
    title = CharFilter(field_name='title', lookup_expr='icontains')

    class Meta:
        model = FileAdmin
        fields = '__all__'
        exclude = ['adminUpload', 'img']
