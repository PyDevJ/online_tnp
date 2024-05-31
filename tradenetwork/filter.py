import django_filters
from tradenetwork.models import Supplier


class SupplierFilter(django_filters.rest_framework.FilterSet):
    """Возможность фильтрации объектов по определенной стране."""

    title = django_filters.CharFilter(
        field_name="country",
        lookup_expr="icontains",
    )

    class Meta:
        model = Supplier
        fields = ("country",)
