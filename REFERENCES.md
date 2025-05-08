[References Used]

# HW1 References

ChatGPT Link: https://chatgpt.com/share/67f48bab-d204-8008-84c8-a38c1e0234d3
& GitHub Copilot within VSCode (minor)

# HW2 References

Models written manually...
    User
    Community
    Subrabble
    Conversation


Models generated with Generative AI systems...
    Follow
    Post
    Comment
    Like
    Message

    *used VSCode Copilot autofill to generate, then checked over and edited as necessary 
    edits included removing the primary key and using the autoincrementing built-in,
    making sure that the string has all of the neccessary information, substituted out 
    .CheckConstraint method for unique_together in Like model, added .ManyToManyField
    methods for N-to-M relationship mappings & went over all models afterwards to 
    ensure consistency

Additional Tasks
    ChatGPT - indicated task should be completed in the admin.py file 

# HW3 References

Main Tasks
    Used ChatGPT as a reference to help solve issue with user needing to be assigned in 
    post_edit and post_create
    
Additional Tasks
    ChatGPT - indicated that tasks should be completed by using the @login_required 
    decorator 
    ChatGPT - indicated that user.is_authenticated could be used in the index.html page
    Used copilot AI as a reference to help add messages (added to base.html as an extra 
    functionality - not assigned in hw)

# HW4 References

Main Tasks
    Used ChatGPT to troubleshoot task 1 and to understand the .SerializerMethodField() in task 2

# HW5 References

Main Tasks
    Used Faker documentation to see list of prompts (like company, catch phrase, etc.) available
    Used ChatGPT to ...
        - (1) troubleshoot issues encountered with test_post_create_view - referenced the addition of a create method to a serializer to dictate how a post is made with validated data and to 
        - (2) improve my factories by referencing how to add lazy_attributes that are attributes based on other existing attributes - for example, username and email of users will be based on the first and last names

