from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='posts/', blank=True, null=True)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)


class Comment(models.Model):
    comment = models.CharField(max_length=200)
    added_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    post_obj = models.ForeignKey(Post, on_delete=models.CASCADE)


class Like(models.Model):
    post_obj = models.ForeignKey(Post, on_delete=models.CASCADE)
    owner_obj = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('owner_obj', 'post_obj')


class Follow(models.Model):
    follower = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following_set'
    )
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower_set'
    )

    class Meta:
        unique_together = ('follower', 'following')