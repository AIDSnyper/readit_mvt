from django.db import models

import team.models


class Tag(models.Model):
    tag = models.CharField(max_length=55)

    def __str__(self):
        return self.tag


class Category(models.Model):
    cat = models.CharField(max_length=55)

    def __str__(self):
        return self.cat


class Articles(models.Model):
    user = models.ForeignKey(team.models.User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='articles/')
    title = models.CharField(max_length=404)
    about = models.TextField()
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    twitter = models.URLField(blank=True, null=True, default="https://twitter.com/?lang=ru")
    facebook = models.URLField(blank=True, null=True, default="https://www.facebook.com/")
    instagram = models.URLField(blank=True, null=True, default="https://www.instagram.com/")
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_commets(self):
        return Comment.objects.filter(post=self)


class Comment(models.Model):
    post = models.ForeignKey(Articles, on_delete=models.CASCADE)
    user = models.ForeignKey(team.models.User, on_delete=models.CASCADE)
    message = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    parent = models.ForeignKey('self', null=True, blank=True, on_delete=models.CASCADE, related_name='replies')

    def __str__(self):
        return f'{self.user.username} : {self.message} > {self.parent}'

    @property
    def children(self):
        return Comment.objects.filter(parent=self).reverse()

    @property
    def is_parent(self):
        if self.parent is None:
            return True
        return False
