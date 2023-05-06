import os

# Set an environment variable
os.environ['OPENAI_API_KEY'] = 'MY_KEY'

# Print the environment variable
print(os.environ['OPENAI_API_KEY'])  # Output: 'my_value'

# # Update the environment variable
# os.environ['OPENAI_API_KEY'] = 'OPENAI_API_KEY'

# # Print the updated environment variable
# print(os.environ['OPENAI_API_KEY'])  # Output: 'new_value'