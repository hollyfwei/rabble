
from faker import Faker
from factories import UserFactory, CommunityFactory, SubRabbleFactory, PostFactory, CommentFactory
from django.urls import reverse
import random
from rabble.models import Post
import pytest

@pytest.mark.django_db(transaction=True)
def test_index_view(client):
    """
    Generates five fake subRabbles and verifies that the index view correctly
    lists all of them. All subRabbles are a part of the default community.
    """
    user = UserFactory()
    client.force_login(user)  

    community = CommunityFactory.create(community_name="default")
    subrabbles = SubRabbleFactory.create_batch(5, community=community)   

    response = client.get(reverse("index"))

    assert 'subrabbles' in response.context
    assert len(response.context['subrabbles']) == len(subrabbles)
    assert response.status_code == 200

    html = response.content.decode()
    for subrabble in subrabbles:
        assert subrabble.identifier in html
        assert subrabble.subrabble_name in html
        assert subrabble.description in html

@pytest.mark.django_db(transaction=True)
def test_subrabble_detail_view(client):
    """
    Generates a fake subRabble and at least five posts in it where each post 
    has at least one comment. The test verifies that the details view for the 
    subRabble correctly displays all the posts and numbers of comments.
    """
    user = UserFactory()
    client.force_login(user)  

    subrabble = SubRabbleFactory.create(subrabble_name="Test Subrabble")
    num_posts = random.randint(5, 7)
    posts = PostFactory.create_batch(num_posts, subrabble=subrabble)
    num_comments = random.randint(1, 3) # number of comments per post same for all
    for post in posts:
        CommentFactory.create_batch(num_comments, post=post)

    response = client.get(reverse("subrabble-detail", args=[subrabble.identifier]))

    assert 'subrabble' in response.context
    assert len(response.context['posts']) == len(posts)
    assert response.status_code == 200

    html = response.content.decode()
    for post in posts:
        assert post.title in html
        assert post.user.username in html
        assert post.body in html
        assert str(num_comments) in html

@pytest.mark.django_db(transaction=True)
def test_post_create_view(client):
    """
    Tests the submission of a form for creating a post and verifies that the 
    post was correctly created.
    """
    user = UserFactory()
    client.force_login(user)
    faker = Faker()  

    subrabble = SubRabbleFactory.create(subrabble_name="Test Post Subrabble")
    data = {
        "title": faker.sentence(nb_words=4),
        "body": faker.paragraph(nb_sentences=3),
    }
    response = client.post(reverse("post-create", kwargs={"identifier": subrabble.identifier}), data=data)

    assert response.status_code == 302
    post = Post.objects.latest('id')
    assert post.title == data["title"]
    assert post.body == data["body"]
    assert post.subrabble == subrabble