import factory
from factory import Faker, SubFactory, PostGenerationMethodCall
from factory.django import DjangoModelFactory
from django.utils import timezone
from django.utils.text import slugify
from rabble.models import User, Community, Subrabble, Post, Comment

class UserFactory(DjangoModelFactory):
    class Meta:
        model = User

    first_name = Faker('first_name')
    last_name = Faker('last_name')

    @factory.lazy_attribute
    def username(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}"
    
    @factory.lazy_attribute
    def email(self):
        return f"{self.first_name.lower()}.{self.last_name.lower()}@example.com"
    
    password = PostGenerationMethodCall('set_password', 'Password123!')
    is_staff=False
    is_active=True
    date_joined=timezone.now()
    

class CommunityFactory(DjangoModelFactory):
    class Meta: 
        model = Community
    
    community_name = Faker('company')
    owner = SubFactory(UserFactory)
    
    @factory.post_generation
    def users(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for user in extracted:
                self.users.add(user)
        else:
            for _ in range(5):
                self.users.add(UserFactory())
                

class SubRabbleFactory(DjangoModelFactory):
    class Meta:
        model = Subrabble

    visibility = Faker('random_element', elements = [Subrabble.Visibility.PUBLIC, Subrabble.Visibility.PRIVATE])
    community = SubFactory(CommunityFactory)
    subrabble_name = Faker('catch_phrase')
    description = Faker('text', max_nb_chars=200)
    anonymous_permissions = Faker('boolean')
    
    @factory.lazy_attribute
    def identifier(self):
        return slugify(self.subrabble_name)

    @factory.post_generation
    def users(self, create, extracted, **kwargs):
        if not create:
            return
        if extracted:
            for user in extracted:
                self.users.add(user)
        else:
            for _ in range(5):
                self.users.add(UserFactory())
    

class PostFactory(DjangoModelFactory):
    class Meta:
        model = Post
    
    subrabble = SubFactory(SubRabbleFactory)
    user = SubFactory(UserFactory)
    title = Faker('sentence',nb_words=4)
    body = Faker('paragraph', nb_sentences=3)
    anonymity = Faker('boolean')


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment
    
    parent = None
    post = SubFactory(PostFactory)
    user = SubFactory(UserFactory)
    body = Faker('text', max_nb_chars=200)
    anonymity = Faker('boolean')
