import factory
from factory import Faker, SubFactory, PostGenerationMethodCall
from factory.django import DjangoModelFactory
from faker import Faker
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
    date_joined=Faker('date_time_this_decade', before_now=True, after_now=False)
    

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

    identifier = Faker('slug')
    visibility = Faker('random_element', elements=[Subrabble.Visibility.PUBLIC, Subrabble.Visibility.PRIVATE])
    community = SubFactory(CommunityFactory)
    subrabble_name = Faker('catch_phrase')
    description = Faker('text', max_nb_chars=200)
    anonymous_permissions = Faker('boolean')
    
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
    title = Faker('sentence', nb_words=6)
    body = Faker('text', max_nb_chars=200)
    anonymity = Faker('boolean')


class CommentFactory(DjangoModelFactory):
    class Meta:
        model = Comment
    
    parent = None
    post = SubFactory(PostFactory)
    user = SubFactory(UserFactory)
    body = Faker('text', max_nb_chars=200)
    anonymity = Faker('boolean')