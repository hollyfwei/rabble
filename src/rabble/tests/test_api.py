import pytest
from rest_framework.test import APIClient
from factories import SubRabbleFactory, PostFactory, CommentFactory, UserFactory
from django.urls import reverse
from faker import Faker
from rabble.models import Post

@pytest.fixture
def api_client():
    return APIClient()

@pytest.mark.django_db
def test_subrabble_get(api_client):
    """
    Generates a fake subRabble and the nverifies that a GET request to the 
    endpoint (specifically for the fake subRabble created in the test) correctly
    returns the information about that subRabble.
    """
    user = UserFactory()
    api_client.force_login(user)

    subrabbles = SubRabbleFactory.create_batch(5)
    response = api_client.get(reverse("api-subrabble-list"))
    assert response.status_code == 200
    assert len(response.json()) == len(subrabbles)

@pytest.mark.django_db
def test_post_post(api_client):
    """
    A test that sends a POST request to the correct endpoint and verifies that 
    the post was correctly created.
    """
    user = UserFactory()
    api_client.force_login(user)

    faker = Faker()
    data = {
        "title": faker.sentence(nb_words=4),
        "body": faker.paragraph(nb_sentences=3),
        "anonymity": False
    }
    subrabble = SubRabbleFactory.create(subrabble_name="Test Post API Subrabble")
    response = api_client.post(reverse("api-post-list", kwargs={"identifier": subrabble.identifier}), data=data)
    assert response.status_code == 201, f"Errors: {response.data}"
    
    post = Post.objects.get(pk=response.data['id'])
    assert post.title == data["title"]
    assert post.body == data["body"]
    assert post.subrabble == subrabble
    assert post.user == user

@pytest.mark.django_db
def test_post_patch(api_client):
    """
    A test that generates a fake post, then sends a PATCH request to the correct endpoint
    (specifically for the fake post created in the test) to update its title, and
    verifies that the post was correctly updated.
    """
    user = UserFactory()
    api_client.force_login(user)

    subrabble = SubRabbleFactory.create(subrabble_name="Test Post API Subrabble")
    post = PostFactory.create(title="Old Title", subrabble=subrabble, user=user)
    data = {
        "title": "New Title"
    }
    response = api_client.patch(reverse("api-post-detail", args= [subrabble.identifier, post.pk]), data)
    assert response.status_code == 200

    post.refresh_from_db()
    assert post.title == data["title"]