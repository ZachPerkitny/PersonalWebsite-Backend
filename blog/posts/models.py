from django.db import models
from django.template.defaultfilters import slugify


class Post(models.Model):
    title = models.CharField(max_length=64)
    content = models.TextField()
    summary = models.TextField(max_length=512)
    created = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(editable=False, unique=True)

    def save(self, *args, **kwargs):
        if not self.id:
            slug = slugify(self.title)
            new_slug = slug
            c = 0
            while Post.objects.filter(slug=new_slug).count() > 0:
                c += 1
                new_slug = '%s-%d' % (slug, c)
            self.slug = new_slug
        super(Post, self).save(*args, **kwargs)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ('-created',)


class Comment(models.Model):
    post = models.ForeignKey(
        Post,
        related_name='comments',
        to_field='slug',
        on_delete=models.CASCADE
    )
    author = models.CharField(max_length=96)
    content = models.TextField(max_length=512)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author

    class Meta:
        verbose_name_plural = 'Comments'
        ordering = ('-created',)