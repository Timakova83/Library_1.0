from django.db import models

class Addresses(models.Model):
    region=models.CharField(
        'Область',
        help_text='Например: Московская'
    )
    district=models.CharField(
        'Район',
        help_text='Например: Подольский'
    )
    city=models.CharField(
        'Город',
        help_text='Например: Подольск'
    )
    street=models.CharField(
        'Улица',
        help_text='Например: ул. Профсоюзная или пр-т Юных Ленинцев'
    )
    house_number = models.CharField(
        'Номер дома',
        help_text='Например: 10 или 10к1'
    )

    def __str__(self):
        return f'{self.region} обл., {self.district} р-он, г. {self.city}, {self.street}, дом {self.house_number}'
    
    class Meta:
        verbose_name = "адрес"
        verbose_name_plural = "Адреса"

class Organizations(models.Model):
    name_organization = models.CharField(
        'Название',
        help_text='Название организации',
        max_length=100
    )
    inn_organization = models.CharField(
        'ИНН',
        help_text='ИНН организации из 12 цифр',
        max_length=12,
    )
    type_organization = models.CharField(
        'Вид',
        help_text='Вид организации',
        choices=[
            ('1', 'Школа'),
            ('2', 'Колледж'),
            ('3',  'Университет')]
    )
    def __str__(self):
        return self.name_organization
    
    class Meta:
        verbose_name = 'организация'
        verbose_name_plural = 'Организации'

class Structures(models.Model):
    name_structure = models.CharField(
        'Название',
        help_text='Название структурного подразделения',
        max_length=100
    )
    adress_structure = models.ForeignKey(
        Addresses,
        on_delete=models.PROTECT,
        verbose_name='Адрес'
    )
    def __str__(self):
        return self.name_structure
    
    class Meta:
        verbose_name = 'подразделение'
        verbose_name_plural = 'Подразделения'

class Classes(models.Model):
    parallel_class = models.CharField(
        'Параллель',
        default=0
    )
    name_class = models.CharField(
        'Название',
        help_text='Название класса',
        unique=True
    )
    name_structure = models.ForeignKey(
        Structures,
        on_delete=models.CASCADE,
        verbose_name='Название школы'
    )
    def __str__(self):
        return self.name_class
    
    class Meta:
        verbose_name = 'класс'
        verbose_name_plural = 'Классы'

class Publishings(models.Model):
    name_publishing = models.CharField(
        'Название',
        help_text='Название издательства'
    )

    def __str__(self):
        return f'Издательство "{self.name_publishing}"'
    
    class Meta:
        verbose_name = 'издательство'
        verbose_name_plural = 'Издательства'

class Authors(models.Model):
    name_author = models.CharField(
        'Автор',
        help_text='Имя автора'
    )
    name_coauthor = models.CharField(
        'Соавтор(-ы)',
        help_text='Соавторы при наличии',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name_author
    
    class Meta:
        verbose_name = 'автор'
        verbose_name_plural = 'Авторы'
    

class Books(models.Model):
    id_book = models.CharField(
        'id книги',
        unique=True
    )
    name_book = models.CharField(
        'Название',
        help_text='Название книги/учебника'

    )
    author_book = models.ForeignKey(
        Authors,
        on_delete=models.CASCADE,
        verbose_name='Автор'

    )
    category_book = models.CharField(
        'Категория',
        choices=[
            ('schoolbook', 'Учебник'),
            ('literature', 'Художественная литература')],
        default='Учебник'
    )
    publishing_book = models.ForeignKey(
        Publishings,
        on_delete=models.CASCADE,
        verbose_name='Издательство'
    )
    publishing_yearv = models.IntegerField(
        'Год изданя',

    )
    name_structure = models.ForeignKey(
        Structures,
        on_delete=models.CASCADE,
        verbose_name='Название школы'
    )

    def __str__(self):
        return f'{self.name_book}, {self.publishing_yearv} год'
    
    class Meta:
        verbose_name = 'книга'
        verbose_name_plural = 'Книги'

class UsersLibrary(models.Model):
    id_user = models.AutoField(
        'id пользователя',
        primary_key=True
    )
    last_name_user = models.CharField(
        'Фамилия'
    )
    first_name_user = models.CharField(
        'Имя'
    )
    patronymic_user = models.CharField(
        'Отчество',
        help_text='При наличии',
        null=True,
        blank=True
    )
    phone_user = models.CharField(
        'Телефон',
        help_text='Пример: +7-999-999-99-99'
    )
    mail_user = models.EmailField(
        'E-mail',
        max_length=254
    )
    name_class = models.ForeignKey(
        Classes,
        on_delete=models.CASCADE,
        help_text='При наличии',
        null=True,
        blank=True
    )
    status_user = models.CharField(
        'Статус',
        choices=[
            ('student', 'ученик'),
            ('teacher', 'учитель')
            ]   
    )
    classroom_teacher = models.BooleanField(
        'Классное руководство',
        default=False,
        null=True,
        blank=True,
    )
    name_structure = models.ForeignKey(
        Structures,
        on_delete=models.CASCADE,
        verbose_name='Название школы'
    )

    def __str__(self):
        return f'{self.last_name_user} {self.first_name_user} {self.patronymic_user}'
    
    class Meta:
        verbose_name = 'пользователь'
        verbose_name_plural = 'Пользователи'