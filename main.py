def generate_hashtag(s):
    # Remove leading/trailing whitespace and split into words
    words = s.strip().split()
    # If there are no words or the result is too long, return False
    if not words or sum(len(word) for word in words) + len(words) > 140:
        return False
    # Capitalize first letter of each word and concatenate with #
    return '#' + ''.join(word.capitalize() for word in words)
    pass
