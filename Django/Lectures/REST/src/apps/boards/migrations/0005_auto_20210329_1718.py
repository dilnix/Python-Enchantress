# Generated by Django 3.1.7 on 2021-03-29 17:18

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


def forwards_func(apps, schema_editor):
    # We get the model from the versioned app registry;
    # if we directly import it, it'll be the wrong version
    old_Comments = apps.get_model("boards", "Comments")
    Comment = apps.get_model("boards", "Comment")
    db_alias = schema_editor.connection.alias
    Comment.objects.using(db_alias).bulk_create(list(old_Comments.objects.all()))


class Migration(migrations.Migration):
    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('boards', '0004_board_users'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('message', models.TextField(max_length=1000)),
                ('created_by',
                 models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='comments',
                                   to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments',
                                           to='boards.task')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.RunPython(forwards_func),

        migrations.DeleteModel(
            name='Comments',
        ),
    ]
