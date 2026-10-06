from django.db import models


class FacultyInfo(models.Model):
    title = models.CharField(max_length=255, default="Факультет охорони здоров'я НаУКМА")
    description = models.TextField(verbose_name="Опис факультету")
    contacts = models.TextField(verbose_name="Контактна інформація")

    class Meta:
        verbose_name = "Інформація про факультет"
        verbose_name_plural = "Інформація про факультет"

    def __str__(self):
        return self.title


class Department(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва кафедри")
    head_name = models.CharField(max_length=255, verbose_name="Завідувач кафедри")

    def __str__(self):
        return self.name


class Specialty(models.Model):
    name = models.CharField(max_length=255, verbose_name="Назва спеціальності")
    code = models.CharField(max_length=50, verbose_name="Код спеціальності")
    description = models.TextField(verbose_name="Опис")
    coordinator_name = models.CharField(max_length=255, verbose_name="Ім'я координатора")
    coordinator_contact = models.CharField(max_length=255, verbose_name="Контакт координатора")
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name="specialties",
        verbose_name="Випускова кафедра"
    )
    disciplines = models.TextField(
        help_text="Перелік дисциплін (через кому або з нового рядка)",
        verbose_name="Список дисциплін"
    )

    def short_description(self):
        words = self.description.split()
        if len(words) > 50:
            return " ".join(words[:50]) + "..."
        return self.description

    def disciplines_list(self):
        return [d.strip() for d in self.disciplines.split('\n') if d.strip()]

    def __str__(self):
        return f"{self.code} {self.name}"


class Teacher(models.Model):
    name = models.CharField(max_length=255, verbose_name="Ім'я викладача")
    position = models.CharField(max_length=255, verbose_name="Посада")
    degree = models.CharField(max_length=255, verbose_name="Науковий ступінь")
    department = models.ForeignKey(
        Department,
        on_delete=models.CASCADE,
        related_name='teachers',
        verbose_name="Кафедра"
    )

    def __str__(self):
        return f"{self.name} ({self.position})"

class ExchangeProgram(models.Model):
    university_name = models.CharField(max_length=255, verbose_name="Назва університету", default="")
    country = models.CharField(max_length=100, verbose_name="Країна", default="")
    languages = models.TextField(verbose_name="Мови навчання")
    places = models.IntegerField(verbose_name="Кількість місць", default=1)
    deadline = models.DateField(verbose_name="Дедлайн подачі")
    description = models.TextField(verbose_name="Опис")


    @property
    def is_active(self):
        from datetime import date
        return self.deadline >= date.today()

    def __str__(self):
        return self.university


