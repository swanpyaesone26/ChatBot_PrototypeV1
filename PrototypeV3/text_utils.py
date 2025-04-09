import re
from documents import stop_words

# Tokenizer function (tokenizes only the key)
def tokenize(text):
    """
    Tokenizes and cleans text by:
    - Converting to lowercase
    - Removing punctuation (including ?,!)
    - Splitting into words
    - Removing stop words from a custom list
    """
    # Lowercase and remove punctuation
    tokens = re.sub(r'[^\w\s]', '', text.lower()).split()
    
    # Remove stop words
    filtered_tokens = [word for word in tokens if word not in stop_words]
    
    return tuple(filtered_tokens)

# Function to expand short forms in user queries and this is the updated function in Version 2
def expand_shortforms(query, shortforms_dict):
    """Expands abbreviations in user queries using the shortforms dictionary."""
    words = query.split()
    expanded_words = []
    
    # Check for multi-word abbreviations
    query_lower = query.lower()
    for abbreviation, expansion in shortforms_dict.items():
        # Use regex to replace multi-word abbreviations
        if abbreviation in query_lower:
            query = query.replace(abbreviation, expansion)
    
    words = query.split()
    
    for word in words:
        lower_word = word.lower()
        if lower_word in shortforms_dict:
            # Preserve original capitalization of the first letter if present
            if word[0].isupper():
                expanded = shortforms_dict[lower_word].capitalize()
            else:
                expanded = shortforms_dict[lower_word]
            expanded_words.append(expanded)
        else:
            expanded_words.append(word)
    
    return ' '.join(expanded_words)

# Function to expand synonyms in user queries this is the updated function in Version 2
def expand_synonyms(query, synonym_dict):
    words = query.split()
    expanded_query = []
    for word in words:
        lower_word = word.lower()
        # Check if word is a synonym key or value
        for canonical, variants in synonym_dict.items():
            if lower_word == canonical or lower_word in variants:
                expanded_query.append(canonical)
                break
        else:
            expanded_query.append(word)
    return ' '.join(expanded_query)

# Function to filter out stop words from a list of tokens. This is the updated function in Version 3
def filter_stop_words(tokens, stop_words):
    """
    Remove stop words from a list of tokens
    
    Args:
        tokens (list): List of tokenized words
        stop_words (set): Set of stop words to remove
        
    Returns:
        list: List of tokens without stop words
    """
    return [token for token in tokens if token.lower() not in stop_words]