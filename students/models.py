from django.db import models

# Create your models here.
#
# class Student1(models.Model):
#     first_name = models.CharField(max_length=100)
#     last_name = models.CharField(max_length=100)
#     birth_date = models.DateField()
#
#     def __str__(self):
#         return f'{self.first_name} {self.last_name}'
#
# class Grade(models.Model):
#     student = models.ForeignKey(Student1, on_delete=models.CASCADE)
#     subject = models.CharField(max_length=100)
#     score = models.FloatField()
#
#     def __str__(self):
#         return f'{self.subject}: {self.score}'



class MyModel(models.Model):
     """"""
     name = models.CharField(max_length=150)
     description = models.TextField()
     created_at = models.DateTimeField(auto_now_add=True)
     updated_at = models.DateTimeField(auto_now=True)


     def __str__(self):
         return self.name


class Student(models.Model):
    """ Модель приложения студенты. """
    FIRST_YEAR = 'first'
    SECOND_YEAR = 'second'
    THIRD_YEAR = 'third'
    FOURTH_YEAR = 'fourth'

    YEAR_IN_SCHOOL_CHOICES = [
        (FIRST_YEAR, 'Первый курс'),
        (SECOND_YEAR, 'Второй курс'),
        (THIRD_YEAR, 'Третий курс'),
        (FOURTH_YEAR, 'Четвертый курс'),
    ]

    first_name = models.CharField(max_length=150, verbose_name='Имя')
    last_name = models.CharField(max_length=150, verbose_name='Фамилия')
    email = models.EmailField()
    year = models.CharField(
        max_length=6,
        choices=YEAR_IN_SCHOOL_CHOICES,
        default=FIRST_YEAR,
        verbose_name='Курс'
    )
    enrollment_date = models.DateField()

    def __str__(self):
        return f'{self.first_name} {self.last_name}'


    class Meta:
        verbose_name = 'студент'
        verbose_name_plural = 'студенты'
        ordering = ['last_name',]
        permissions =[
            ("can_promote_student", "Can promote student"),
            ("can_expel_student", "Can expel student"),
            #Атрибут permissions принимает список кортежей,
            # где каждый кортеж состоит из двух элементов:
            # кодового имени разрешения и описания разрешения.
        ]



# class Group(models.Model):
#     """ Модель приложения студенты. """
#     name = models.CharField(max_length=100)
#
#
#     def __str__(self):
#         return self.name
#
# class Student(models.Model):
#     """ Модель приложения студенты. """
#     name = models.CharField(max_length=100)
#     group = models.ForeignKey(Group, on_delete=models.CASCADE, related_name='student')
#
#     def __str__(self):
#         return self.name






    # first_name = models.CharField(max_length=150, verbose_name='Имя')
    # # verbose_name - читаемое имя поля которое отображается в административной панели
    # last_name = models.CharField(max_length=150, verbose_name='Фамилия', unique=True)
    # # unique - задаем уникальных параметр
    #
    # age = models.IntegerField(help_text='Введите возраст студента')
    # # help_text - подсказка
    #
    # is_active = models.BooleanField(default=True)
    # description = models.TextField(null=True, blank=True ) # null -> может ли поле принимать пуст ое значение
    # # blank -> данное значение может быть пустым в форме
    # created_at = models.DateTimeField(auto_now=True)
    # # auto_now_add - автоматическое установка даты и времени создания (никогда не изменяется)
    # # auto_now - автоматическое установка даты и времени создания (изменяется при обновлении записи)
    #
    #
    #
    # image = models.ImageField(upload_to='photos/', verbose_name='Фотография')
    # # upload_to - путь до папки куда буду сохраняться изображения данной модели
    #
    # group = models.ForeignKey(Group, on_delete=models.PROTECT)
    # # один ко многим (Group - связь с моделью)
    # # on_delete CASCADE - удаление всех связанных групп студента
    # # on_delete PROTECT - запрет удаления связанных записей
    # # on_delete=models.SET_NULL - устанавливает значения поля в NULL
    # # on_delete = models.SET_DEFAULT - Устанавливает дефолтное значение
    # # on_delete = models.SET - Устанавливает конкретное значение
    # # on_delete = models.DO_NOTHING - Ничего не делает с нашей модудлью
    #
    # profile = models.OneToOneField(Profile, on_delete=models.CASCADE, related_name='student')
    # # один к одному
    # # related_name = 'student' - параметр имени для обратного отношения
    #
    # tags = models.ManyToManyField(Tag) # многие ко многим
    #
    # STATUS_CHOICES = [
    #     ('draft', 'Draft'),
    #     ('published', 'Published'),
    # ]
    # status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='draft')
    # # choices - Используется для создания выпадающи х списков
    #
    #
    # def __str__(self) -> str:
    #     """ Магический метод строкового представления. """
    #     return f"{self.first_name} {self.last_name}"
    #
    #
    # class Meta:
    #     verbose_name = 'студент'
    #     verbose_name_plural = 'студенты'
    #     ordering = ['last_name']
    #     db_table = 'custom_table_name'