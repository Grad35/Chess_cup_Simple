from django.conf import settings
from django.db import models
class Tournament(models.Model):
    title=models.CharField("Название",max_length=120)
    date=models.DateField("Дата проведения")
    location=models.CharField("Место проведения",max_length=160)
    description=models.TextField("Описание",blank=True)
    is_open=models.BooleanField("Регистрация открыта",default=True)
    class Meta:
        ordering=["date"]; verbose_name="Турнир"; verbose_name_plural="Турниры"
    def __str__(self): return self.title
class Application(models.Model):
    STATUS=[("pending","На рассмотрении"),("accepted","Принята"),("rejected","Отклонена")]
    user=models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,verbose_name="Участник")
    tournament=models.ForeignKey(Tournament,on_delete=models.CASCADE,related_name="applications",verbose_name="Турнир")
    created_at=models.DateTimeField("Дата подачи",auto_now_add=True)
    status=models.CharField("Статус",max_length=12,choices=STATUS,default="pending")
    class Meta:
        unique_together=("user","tournament"); ordering=["-created_at"]
        verbose_name="Заявка"; verbose_name_plural="Заявки"
    def __str__(self): return f"{self.user.username} — {self.tournament.title}"
