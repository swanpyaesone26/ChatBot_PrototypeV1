# Function to count matches for the query in a document
def count_matches(doc_tokens, query_tokens):
    """Counts the number of query words present in a document."""
    matches = 0
    document_set = set(doc_tokens)
    for token in query_tokens:
        if token in document_set:
            matches += 1
    return matches

# Function to count weighted matches for the query in a document. This is the updated function in Version 3
def count_weighted_matches(document_tokens, user_tokens, word_weights):
    """
    Count matches between document and user tokens, applying word weights
    
    Args:
        document_tokens (list): List of tokens from the document
        user_tokens (list): List of tokens from user query
        word_weights (dict): Dictionary of word weights
        
    Returns:
        int: Weighted match count
    """
    match_count = 0
    for token in user_tokens:
        if token in document_tokens:
            weight = word_weights.get(token.lower(), 1.0)  # Default weight of 1.0 if not found
            match_count += weight
    return match_count

# Function to count matches for each document
def count_matches_per_document(documents, query_tokens):
    """Counts matches for each document."""
    match_counts = []
    for index, doc_tokens in enumerate(documents):  
        matches = count_matches(doc_tokens, query_tokens)
        match_counts.append((index, matches))
    return match_counts

# Function to count weighted matches for each document
def count_weighted_matches_per_document(documents, query_tokens, word_weights):
    """Counts weighted matches for each document."""
    match_counts = []
    for index, doc_tokens in enumerate(documents):  
        matches = count_weighted_matches(doc_tokens, query_tokens, word_weights)
        match_counts.append(matches)
    return match_counts

# Function to rank documents based on match counts
def rank_documents(match_counts, documents):
    """Ranks documents based on match counts."""
    # Sort the documents by match count (descending) and original index (ascending)
    sorted_count = sorted(match_counts, key=lambda x: (-x[1], x[0]))
    
    # Return the top 1 document (first in the sorted list)
    return documents[sorted_count[0][0]] if sorted_count else None

