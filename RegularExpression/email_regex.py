import re

def find_email_addresses(text):
    # Regular expression pattern for matching email addresses
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    
    # Find all email addresses in the provided text
    email_addresses = re.findall(email_pattern, text)
    
    return email_addresses

# Example text containing email addresses
text = """
Hello John,
Please contact us at support@example.com for any queries.
You can also reach out to sales-info@company.co.uk.
Best regards,
Jane Doe
"""

# Find and print all email addresses
emails = find_email_addresses(text)
print("Email addresses found:", emails)
