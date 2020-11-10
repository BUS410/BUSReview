from django.db import models


class Category(models.Model):
    name = models.CharField(verbose_name='Категория', max_length=80, unique=True)

    def __repr__(self):
        return f'<Category {self.name}>'

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'


class Review(models.Model):
    title = models.CharField(verbose_name='Заголовок', max_length=255)
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    object = models.CharField(verbose_name='Объект', max_length=255)
    stars = models.IntegerField(verbose_name='Оценка')
    content = models.TextField(verbose_name='Содержание')
    image_url = models.URLField(verbose_name='Ссылка на картинку',
                                default="https://repairsyourself.ru/wp-content/uploads/2020/03/404.png")
    author = models.CharField(verbose_name='Автор', max_length=80,
                              blank=True, null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 verbose_name='Категория')

    def __repr__(self):
        return f'<Review {self.title}, {self.content[:24]}>'

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Рецензия'
        verbose_name_plural = 'Рецензии'


class Comment(models.Model):
    author = models.CharField(verbose_name='Автор', max_length=80,
                              blank=True, null=True)
    content = models.TextField(verbose_name='Содержание')
    stars = models.IntegerField(verbose_name='Оценка')
    date = models.DateTimeField('Дата публикации', auto_now_add=True)
    review = models.ForeignKey(Review, on_delete=models.CASCADE,
                               verbose_name='Рецензия')

    def __repr__(self):
        return f'<Comment {self.content[:24]}>'

    def __str__(self):
        return self.content[:12]

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
