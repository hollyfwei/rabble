from factories import CommunityFactory, SubRabbleFactory, PostFactory, CommentFactory
from django.urls import reverse
import random

def test_index_view(client):
    """
    Generates five fake subRabbles and verifies that the index view correctly
    lists all of them. All subRabbles are a part of the default community.
    """

    community = CommunityFactory.create(community_name="default")
    subrabbles = SubRabbleFactory.create_batch(5, community=community)   

    response = client.get(reverse("index"))

    assert 'index' in response.context
    assert len(response.context['index']) == len(subrabbles)
    assert response.status_code == 200

    html = response.content.decode()
    for subrabble in subrabbles:
        assert subrabble.identifier in html
        assert subrabble.subrabble_name in html
        assert subrabble.community in html

def test_subrabble_detail_view(client):
    """
    Generates a fake subRabble and at least five posts in it where each post 
    has at least one comment. The test verifies that the details view for the 
    subRabble correctly displays all the posts and numbers of comments.
    """

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
        assert num_comments in html

def test_post_create_view(client):
    """
    Tests the submission of a form for creating a post and verifies that the 
    post was correctly created.
    """