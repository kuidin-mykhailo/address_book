from django.db import models


class BaseModel(models.Model):
    """Base model from instances"""

    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at', '-update_at']


class Person(BaseModel):
    """Model Person"""

    first_name = models.CharField("First name", max_length=120, default='Misha')
    last_name = models.CharField("Last name", max_length=120, default='Kuidin')
    home_phone = models.CharField("Home number", max_length=15, blank=True, null=True, unique=True)
    work_phone = models.CharField("Work number", max_length=15, blank=True, null=True, unique=True)
    fax = models.PositiveIntegerField("Fax", blank=True, null=True, unique=True)
    email = models.EmailField("Email", max_length=120, unique=True)

    @property
    def full_name(self):
        return f'{self.first_name} {self.last_name}'

    def __str__(self):
        return self.full_name

    def __repr__(self):
        return self.full_name

    class Meta:
        db_table = 'person'


class City(models.Model):
    """Model City"""
    name = models.CharField("Name", max_length=128)

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name

    class Meta:
        db_table = 'city'


class Record(BaseModel):
    """Model Record"""

    city = models.ForeignKey(City, verbose_name="City", related_name='city', on_delete=models.CASCADE)
    person = models.ForeignKey(Person, verbose_name="Person", related_name='person', on_delete=models.CASCADE)
    address = models.CharField("Address", max_length=200)
    zipcode = models.CharField("Zipcode", max_length=20)

    def __str__(self):
        return f'{self.city} | {self.person}'

    class Meta:
        db_table = 'record'
