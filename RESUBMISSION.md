# HW2 RESUBMISSION

Rubric Item (1) : If a field with a choices parameter does not use an IntegerChoices or TextChoices class (or similar)
  Used the wrong type for visibility in the subrabble class in line 39. Changed SmallPositiveIntegerField to IntegerField.

Rubric Item (2) : Missing migrations. Make sure to run python3 manage.py makemigrations, and that all migration files are added to your repository.
  Made migrations.
  
# HW3 RESUBMISSION

Rubric Item (1) : rabble-fixture.json file has errors that prevent it from loading
  Passwords were adjusted to hashed passwords for users. Fixed password for user chris.

# HW4 RESUBMISSION

Rubric Item (1) : Submitting POST request in API.md fails or does not create a post.
  Was having an issue with verifying the user because there was no authentication and my code was attempting to get the user from the request, now the user can be specified in the post field.
  
