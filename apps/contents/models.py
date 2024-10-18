from django.db import models


CITY_CHOICES = [
    ('astana', "Астана"),
    ('almaty', "Алматы"),
]


class BaseModel(models.Model):
    created_at = models.DateTimeField(
        auto_now_add=True,
        verbose_name="Дата создания",
        help_text="Дата и время создания записи"
    )
    updated_at = models.DateTimeField(
        auto_now=True,
        verbose_name="Дата обновления",
        help_text="Дата и время последнего обновления записи"
    )

    class Meta:
        abstract = True


class CarImage(BaseModel):
    image = models.ImageField(
        upload_to='car_images/',
        verbose_name="Изображение автомобиля",
        help_text="Загрузите изображение автомобиля в формате JPG или PNG. Рекомендуется использовать фотографии высокого качества, чтобы детализировано показать внешний вид автомобиля."
    )

    car = models.ForeignKey(
        'Car',
        on_delete=models.CASCADE,
        related_name='images',
        verbose_name="Автомобиль",
        help_text="Выберите автомобиль, к которому будет привязано данное изображение. Это позволит отслеживать все фотографии, загруженные для данного транспортного средства."
    )

    def __str__(self):
        return f"Изображение для {self.car.get_name()}"

    class Meta:
        verbose_name = "Изображение автомобиля"
        verbose_name_plural = "Изображения автомобилей"
        # ordering = ['-created_at']


class Car(BaseModel):
    FUEL_CHOICES = [
        ('gasoline', 'Бензин'),
        ('diesel', 'Дизель'),
        ('electric', 'Электричество'),
        ('hybrid', 'Гибрид'),
        ('hydrogen', 'Водород'),
        ('lpg', 'Газ (LPG)'),
        ('cng', 'Сжатый природный газ (CNG)'),
    ]

    status = models.BooleanField(
        default=True,
        verbose_name="Доступен для аренды",
        help_text="Укажите, доступен ли автомобиль для аренды в данный момент."
    )
    brand = models.CharField(
        max_length=100,
        verbose_name="Марка автомобиля",
        help_text="Введите марку автомобиля, например, MERCEDES-BENZ."
    )
    model = models.CharField(
        max_length=100,
        verbose_name="Модель автомобиля",
        help_text="Введите модель автомобиля, например, S223."
    )
    city = models.CharField(
        max_length=100,
        choices=CITY_CHOICES,
        verbose_name="Город аренды",
        help_text="Выберите город, в котором доступна аренда автомобиля, например, Алматы."
    )
    color = models.CharField(
        max_length=50,
        verbose_name="Цвет автомобиля",
        help_text="Укажите цвет автомобиля, например, Серый."
    )
    year = models.IntegerField(
        verbose_name="Год выпуска автомобиля",
        help_text="Введите год выпуска автомобиля, например, 2021."
    )
    drive_type = models.CharField(
        max_length=50,
        blank=True, null=True,
        verbose_name="Тип привода автомобиля",
        help_text="Укажите тип привода автомобиля, например, Задний. Это поле необязательно для заполнения."
    )
    fuel_type = models.CharField(
        max_length=50,
        choices=FUEL_CHOICES,
        default='gasoline',
        verbose_name="Тип топлива автомобиля",
        help_text="Выберите тип топлива, используемого автомобилем, например, Бензин."
    )
    volume = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        verbose_name="Объем двигателя автомобиля",
        help_text="Укажите объем двигателя автомобиля в литрах, например, 2.0."
    )
    license_plate = models.CharField(
        max_length=15,
        verbose_name="Государственный номер",
        help_text="Введите государственный номер автомобиля, например, KZ 123 ABC."
    )
    volume_description = models.CharField(
        max_length=50,
        verbose_name="Дополнительная информация об объеме двигателя",
        help_text="Можете указать дополнительные сведения о двигателе, например, 'Турбированный'. Это поле необязательно для заполнения.",
        null=True,
        blank=True
    )

    price_6_hours = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Стоимость аренды на 6 часов",
        help_text="Стоимость аренды автомобиля на 6 часов, например, 168000 тенге."
    )
    price_12_hours = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Стоимость аренды на 12 часов",
        help_text="Стоимость аренды автомобиля на 12 часов, например, 294000 тенге."
    )
    price_24_hours = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="Стоимость аренды на 24 часа",
        help_text="Стоимость аренды автомобиля на 24 часа, например, 420000 тенге."
    )

    description = models.TextField(
        verbose_name="Общее описание автомобиля",
        help_text="Введите краткое описание автомобиля, например, Автомобиль отличается высокой скоростью и надежностью."
    )
    interior_description = models.TextField(
        verbose_name="Описание салона автомобиля",
        help_text="Опишите салон автомобиля, например, Интерьер автомобиля очень комфортен и уютен. Это поле необязательно для заполнения.",
        blank=True, null=True
    )
    why_this_car = models.TextField(
        verbose_name="Почему этот автомобиль?",
        help_text="Объясните, почему этот автомобиль достоин внимания, например, Этот автомобиль очень удобен и комфортен. Это поле необязательно для заполнения.",
        blank=True, null=True
    )

    def get_name(self):
        return f"{self.brand} {self.model}"
    
    def get_full_volume(self):
        if self.volume_description:
            return f"{self.volume} {self.volume_description}"
        return f"{self.volume}"
    
    def get_full_description(self):
        if self.description and self.interior_description:
            return f"{self.description} {self.interior_description}"
        return None
    
    def get_status(self):
        return "Доступен" if self.status else "Недоступен"

    def __str__(self):
        return f"{self.brand} {self.model} ({self.year})"

    class Meta:
        verbose_name = "Автомобиль"
        verbose_name_plural = "Автомобили"


class Contact(BaseModel):
    full_name = models.CharField(
        max_length=100,
        verbose_name="Полное имя",
        help_text="Введите полное имя клиента, например, Иван Иванов"
    )

    phone_number = models.CharField(
        max_length=20,
        verbose_name="Номер телефона",
        help_text="Введите номер телефона клиента в международном формате, например, +7 777 123 4567"
    )

    date_start = models.DateField(
        verbose_name="Дата начала аренды",
        help_text="Укажите дату, с которой начинается аренда автомобиля"
    )

    date_end = models.DateField(
        verbose_name="Дата окончания аренды",
        help_text="Укажите дату, когда аренда автомобиля заканчивается"
    )

    city = models.CharField(
        max_length=10,
        choices=CITY_CHOICES,
        default='almaty',
        verbose_name="Город аренды",
        help_text="Выберите город, где будет происходить аренда автомобиля"
    )

    auto = models.ForeignKey(
        Car,
        on_delete=models.CASCADE,
        verbose_name="Автомобиль",
        help_text="Введите марку и модель автомобиля, который будет забронирован"
    )

    is_read = models.BooleanField(
        default=False,
        verbose_name="Прочитано",
        help_text="Укажите, прочитано ли это сообщение"
    )

    def __str__(self):
        return self.full_name

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
        ordering = ['-created_at']