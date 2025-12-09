class Phone:
    def __init__(self, brand: str, model: str, price: float,
            color: str, storage_gb: int, is_in_stock: bool) -> None:
        if not brand:
            raise ValueError("Бренд не может быть пустым")
        if not model:
            raise ValueError("Модель не может быть пустой")
        if price <= 0:
            raise ValueError("Цена должна быть положительной")
        if not color:
            raise ValueError("Цвет не может быть пустым")
        if storage_gb <= 0:
            raise ValueError("Объем памяти должен быть положительным")
        if is_in_stock is None:
            raise ValueError("Статус наличия должен быть")
        self._brand = brand
        self._model = model
        self._price = price
        self._color = color
        self._storage_gb = storage_gb
        self._is_in_stock = is_in_stock
    
    def __str__(self) -> str:
        return ''.join(
            map(lambda key: f"{key}: {getattr(self, f'_{key}', 'Unknown')}\n",
                ["brand", "model", "price", "color", "storage_gb", "is_in_stock"]
            )
        )
            

    def get_full_name(self) -> str:
        return f'{self._brand} {self._model}'


    def apply_discount(self, discount_percent: float) -> None:
        if discount_percent >= 0 and discount_percent <= 100:
            self._price = round(self._price * (100 - discount_percent) / 100, 9)


    def check_availability(self) -> str:
        return "В наличии" if self._is_in_stock else "Нет в наличии"