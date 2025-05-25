def reverse_text(text):
  return text[::-1] 

def is_palindrome(text):
  cleaned_text = text.lower().replace(" ", "") 
  return cleaned_text == cleaned_text[::-1]
