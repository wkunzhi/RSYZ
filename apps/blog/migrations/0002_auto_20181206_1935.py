# Generated by Django 2.1.2 on 2018-12-06 19:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='StrategyClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=32, verbose_name='标题')),
                ('type', models.CharField(choices=[('1', '剧情攻略'), ('2', '角色攻略'), ('3', '活动攻略')], max_length=20, verbose_name='攻略类型')),
                ('desc', models.CharField(default='', max_length=500, null=True, verbose_name='简介')),
                ('image', models.FileField(default='/strategy/default.png', upload_to='strategy/', verbose_name='缩略图')),
            ],
            options={
                'verbose_name': '攻略分类',
                'verbose_name_plural': '攻略分类',
            },
        ),
        migrations.DeleteModel(
            name='Strategy',
        ),
    ]
