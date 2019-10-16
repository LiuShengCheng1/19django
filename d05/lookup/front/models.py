from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        db_table = 'article'

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    category = models.ForeignKey("Category", on_delete=models.CASCADE, null=True, related_name="articles")
    tag_set = models.ManyToManyField("Tag", related_name="articles")

    # 如果这里加上related_name  表名_set 就失效
    def __str__(self):
        return "<Article:(id:%s,title:%s)>" % (self.id, self.title)

    class Meta:
        db_table = 'article'