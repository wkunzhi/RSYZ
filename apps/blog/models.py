from django.db import models


class StrategyClass(models.Model):
    """攻略主题"""
    title = models.CharField(verbose_name='标题', max_length=32)
    type = models.CharField(verbose_name='攻略类型', max_length=20, choices=(('1', '剧情攻略'), ('2', '角色攻略'), ('3', '活动攻略')))
    desc = models.CharField(verbose_name='简介', max_length=500, null=True, default='')
    image = models.FileField(verbose_name='缩略图', max_length=100, upload_to='media/strategy/',
                             default='/media/strategy/default.png')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '攻略主题'
        verbose_name_plural = verbose_name


class StrategyArticle(models.Model):
    """文章"""
    strategyClass = models.ForeignKey(verbose_name='所属主题', to='StrategyClass', to_field='id', default=1,
                                      on_delete=models.CASCADE)
    title = models.CharField(max_length=50, verbose_name='文章标题')
    desc = models.CharField(max_length=255, verbose_name='文章描述', default='', null=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    content = models.TextField(verbose_name='文章内容')
    read_count = models.IntegerField(verbose_name='浏览次数', default=0)
    tag = models.ManyToManyField(verbose_name='所属标签（最多选2个）', to='Tag')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '攻略文章'
        verbose_name_plural = verbose_name


class Tag(models.Model):
    """标签分类"""
    title = models.CharField(verbose_name='标签名', max_length=32)
    color = models.CharField(verbose_name='标签配色状态', max_length=10,
                             choices=(('default', 'default'),
                                      ('primary', 'primary'),
                                      ('success', 'success'),
                                      ('info', 'info'),
                                      ('warning', 'warning'),
                                      ('danger', 'danger'),
                                      ),
                             default='default')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '标签分类'
        verbose_name_plural = verbose_name
