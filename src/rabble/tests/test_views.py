from factories import CommunityFactory, SubRabbleFactory
from django.urls import reverse

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
    subRabble correctly displays all the posts and numbers of comments."""

def test_post_create_view(client):
    """
    Tests the submission of a form for creating a post and verifies that the 
    post was correctly created.
    """