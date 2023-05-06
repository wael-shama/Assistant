import os

# Set an environment variable
os.environ['OPENAI_API_KEY'] = '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'

# Print the environment variable
print(os.environ['OPENAI_API_KEY'])  # Output: 'my_value'

# # Update the environment variable
# os.environ['OPENAI_API_KEY'] = 'OPENAI_API_KEY'

# # Print the updated environment variable
# print(os.environ['OPENAI_API_KEY'])  # Output: 'new_value'