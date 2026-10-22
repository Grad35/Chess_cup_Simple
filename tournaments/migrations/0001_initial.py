from django.conf import settings
from django.db import migrations,models
import django.db.models.deletion
class Migration(migrations.Migration):
    initial=True
    dependencies=[migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations=[
        migrations.CreateModel(name="Tournament",fields=[("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),("title",models.CharField(max_length=120,verbose_name="Название")),("date",models.DateField(verbose_name="Дата проведения")),("location",models.CharField(max_length=160,verbose_name="Место проведения")),("description",models.TextField(blank=True,verbose_name="Описание")),("is_open",models.BooleanField(default=True,verbose_name="Регистрация открыта"))],options={"ordering":["date"],"verbose_name":"Турнир","verbose_name_plural":"Турниры"}),
        migrations.CreateModel(name="Application",fields=[("id",models.BigAutoField(auto_created=True,primary_key=True,serialize=False,verbose_name="ID")),("created_at",models.DateTimeField(auto_now_add=True,verbose_name="Дата подачи")),("status",models.CharField(choices=[("pending","На рассмотрении"),("accepted","Принята"),("rejected","Отклонена")],default="pending",max_length=12,verbose_name="Статус")),("tournament",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,related_name="applications",to="tournaments.tournament",verbose_name="Турнир")),("user",models.ForeignKey(on_delete=django.db.models.deletion.CASCADE,to=settings.AUTH_USER_MODEL,verbose_name="Участник"))],options={"ordering":["-created_at"],"unique_together":{("user","tournament")},"verbose_name":"Заявка","verbose_name_plural":"Заявки"})]
