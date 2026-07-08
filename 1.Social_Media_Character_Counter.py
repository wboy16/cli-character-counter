# 1. The Social Media Character Counter

user_draft = input("Please enter your draft post: ")

post_length = len(user_draft)
remaining_length = 280 - post_length

print(f"Your post is {post_length} characters long. You have {remaining_length} characters remaining.")
