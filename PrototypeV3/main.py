from documents import uni_document, synonym_dict, shortforms, stop_words, word_weights
from text_utils import expand_shortforms, expand_synonyms, tokenize, filter_stop_words
from document_ranker import rank_documents, count_weighted_matches_per_document


# Input processing pipeline
user_question = input("Please enter your question: ")

# Step 1: Expand short forms
expanded_question = expand_shortforms(user_question, shortforms)

# Step 2: Expand synonyms
expanded_q = expand_synonyms(expanded_question, synonym_dict)  

# Step 3: Tokenize
user_question_tokens = tokenize(expanded_q)  

# Step 4: Remove stop words
filtered_tokens = filter_stop_words(user_question_tokens, stop_words)

# Step 5: Tokenize documents and remove stop words
uni_document_tokenized = {tokenize(key): value for key, value in uni_document.items()}
document_tokens = list(uni_document_tokenized.keys())
filtered_document_tokens = [filter_stop_words(tokens, stop_words) for tokens in document_tokens]

# Step 6: Count weighted matches and rank documents
match_counts = count_weighted_matches_per_document(filtered_document_tokens, filtered_tokens, word_weights)
# Convert match counts to tuples (index, count) before ranking
match_counts_with_index = [(i, count) for i, count in enumerate(match_counts)]
best_matching_document = rank_documents(match_counts_with_index, list(uni_document.values()))

print(best_matching_document if best_matching_document else "Sorry, I couldn't find an answer to your question.")
