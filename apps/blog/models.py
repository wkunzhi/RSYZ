from django.db import models


class StrategyClass(models.Model):
    """攻略分类"""
    title = models.CharField(verbose_name='标题', max_length=32)
    type = models.CharField(verbose_name='攻略类型', max_length=20, choices=(('1', '剧情攻略'), ('2', '角色攻略'), ('3', '活动攻略')))
    desc = models.CharField(verbose_name='简介', max_length=500, null=True, default='')
    image = models.FileField(verbose_name='缩略图', max_length=100, upload_to='strategy/', default='/strategy/default.png')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '攻略分类'
        verbose_name_plural = verbose_name
