from rest_framework.serializers import ValidationError


class SimultaneousSelectionValidator:
    """
    Проверка на соответствие иерархической структуры
    """

    def __init__(self, supply, network_level):
        self.supplier = supply
        self.network_level = network_level

    def __call__(self, val):
        supply = val.get(self.supplier)
        network_level = val.get(self.network_level)
        if supply:
            if network_level == 0 and supply != self:
                raise ValidationError(
                    "A zero-level supplier cannot have another supplier"
                )
            elif network_level == 1 and supply.network_level == 2:
                raise ValidationError(
                    "A first-level supplier cannot have a second-level supplier"
                )