from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    middle_name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    phone_number = models.CharField(max_length=20)

    objects = models.Manager()

    def __str__(self):
        return f'{self.name} {self.middle_name} {self.last_name}'


GEARBOX_CHOICES = (
    ('manual', 'Механика'),
    ('automatic', 'Автомат'),
    ('вариатор', 'CVT'),
    ('robot', 'Робот')
)

FUEL_TYPE_CHOICES = (
    ('gasoline', 'Бензин'),
    ('diesel', 'Дизель'),
    ('hybrid', 'Гибрид'),
    ('electro', 'Электро')
)

BODY_TYPE_CHOICES = (
    ('sedan', 'Седан'),
    ('hatchback', 'Хэтчбек'),
    ('SUV', 'Внедорожник'),
    ('wagon', 'Универсал'),
    ('minivan', 'Минивэн'),
    ('pickup', 'Пикап'),
    ('coupe', 'Купе'),
    ('cabrio', 'Кабриолет')
)


DRIVE_UNIT_CHOICES = (
    ('rear', 'Задний'),
    ('front', 'Передний'),
    ('full', 'Полный')
)


class Car(models.Model):
    id = models.IntegerField(primary_key=True)
    model = models.CharField(max_length=60)
    year = models.IntegerField()
    color = models.CharField(max_length=60)
    mileage = models.IntegerField()
    volume = models.CharField(max_length=10)
    body_type = models.CharField(max_length=40, choices=BODY_TYPE_CHOICES)
    drive_unit = models.CharField(max_length=40, choices=DRIVE_UNIT_CHOICES)
    gearbox = models.CharField(max_length=40, choices=GEARBOX_CHOICES)
    fuel_type = models.CharField(max_length=40, choices=FUEL_TYPE_CHOICES)
    price = models.DecimalField(max_digits=12, decimal_places=2)
    image = models.ImageField(upload_to="images")

    objects = models.Manager()

    def __str__(self):
        return self.model


class Sale(models.Model):
    id = models.IntegerField(primary_key=True)
    client = models.ManyToManyField(Client)
    car = models.ManyToManyField(Car)
    created_at = models.DateTimeField(auto_now=True)

    objects = models.Manager()
