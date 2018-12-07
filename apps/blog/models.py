from django.db import models


class StrategyClass(models.Model):
    """攻略分类"""
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
    """攻略文章表"""
    title = models.CharField(max_length=50, verbose_name='文章标题')
    desc = models.CharField(max_length=255, verbose_name='文章描述', default='', null=True)
    create_time = models.DateTimeField(verbose_name='创建时间', auto_now_add=True)
    content = models.TextField(verbose_name='文章内容')
    read_count = models.IntegerField(verbose_name='浏览次数', default=0)
    category = models.ForeignKey(verbose_name='文章分类', to='Category', to_field='id', null=True, on_delete=models.CASCADE)
    strategyClass = models.ForeignKey(verbose_name='所属主题', to='StrategyClass', to_field='id', null=True,
                                      on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '攻略文章'
        verbose_name_plural = verbose_name


class Category(models.Model):
    """攻略标签分类"""
    title = models.CharField(verbose_name='分类标题', max_length=32)
    blog = models.ForeignKey(verbose_name='所属攻略', to='StrategyClass', to_field='id', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '攻略对应标签'
        verbose_name_plural = verbose_name
