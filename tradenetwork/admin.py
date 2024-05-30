from django.contrib import admin
from tradenetwork.models import Supplier, Product


@admin.register(Supplier)
class SupplierAdmin(admin.ModelAdmin):
    """
    Ссылка на поставщика в админ-панели
    """

    list_display = (
        "author",
        "title",
        "network_level",
        "country",
        "city",
        "debt_to_supplier",
        "created_at",
    )
    list_filter = (
        "network_level",
        "title",
        "product",
        "country",
    )
    search_fields = ("network_level", "product", "country")
    actions = ["clear_debt"]

    @admin.action(description="Clearing the debt to the supplier")
    def clear_debt(self, request, queryset):
        """
        «admin action», очищающий задолженность перед поставщиком у выбранных объектов.
        """
        queryset.update(debt_to_supplier=0)


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    """
    Ссылка на товары в админ-панели
    """

    list_display = ("title", "product_model", "launch_date")
