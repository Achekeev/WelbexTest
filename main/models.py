from django.db import models

# С комментариями пока туго, но мне кажется что тут итак всё ясно =)


class TestTable(models.Model):
    date = models.DateField(auto_now_add=True, verbose_name="Дата")
    name = models.CharField(max_length=100, verbose_name="Название")
    amount = models.IntegerField(verbose_name="Количество")
    distance = models.FloatField(verbose_name="Расстояние")

    def __str__(self):
        return self.name
