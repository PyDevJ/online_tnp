from django.db import models
from users.models import User

NULLABLE = {'blank': True, 'null': True}


class Product(models.Model):
    """Продукты"""

    title = models.CharField(max_length=255, verbose_name="название")
    product_model = models.CharField(max_length=255, verbose_name="модель")
    launch_date = models.DateField(verbose_name="дата выхода товара на рынок")

    def __str__(self):
        return f"{self.title} {self.product_model}"

    class Meta:
        verbose_name = "продукт"
        verbose_name_plural = "продукты"


class Supplier(models.Model):
    """Поставщики"""

    class Level(models.IntegerChoices):
        """Уровень поставщика"""

        FACTORY = 0, "Завод"
        RETAIL = 1, "Розничная сеть"
        ENTREPRENEUR = 2, "Индивидуальный предприниматель"

    product = models.ManyToManyField(Product, verbose_name="Продукт")
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Автор поставщика", **NULLABLE)
    supply = models.ForeignKey("self", on_delete=models.PROTECT, verbose_name="Поставщик", **NULLABLE)
    title = models.CharField(max_length=200, verbose_name="Название")
    email = models.EmailField(unique=True, verbose_name="Электронная почта")
    country = models.CharField(max_length=200, verbose_name="Страна")
    city = models.CharField(max_length=200, verbose_name="Город")
    street = models.CharField(max_length=200, verbose_name="Улица")
    house = models.CharField(max_length=100, verbose_name="Номер дома")
    network_level = models.IntegerField(choices=Level.choices, verbose_name="Уровень структуры")
    debt_to_supplier = models.DecimalField(decimal_places=2, max_digits=15, verbose_name="Задолженность", **NULLABLE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.title}, {self.country},{self.city}"

    class Meta:
        verbose_name = "поставщик"
        verbose_name_plural = "поставщики"
