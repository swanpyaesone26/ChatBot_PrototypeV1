from documents import uni_document, synonym_dict, shortforms
from text_utils import expand_shortforms, expand_synonyms, tokenize
from document_ranker import count_matches_per_document, rank_documents


# Input processing pipeline
user_question = input("Please enter your question: ")

# Step 1: Expand short forms
expanded_question = expand_shortforms(user_question, shortforms)

# Step 2: Expand synonyms
expanded_q = expand_synonyms(expanded_question, synonym_dict)  # This is the version we want to use

# Step 3: Tokenize the FULLY expanded question 
user_question_tokens = tokenize(expanded_q)  # Changed from expanded_question to expanded_q

# Rest remains the same...
uni_document_tokenized = {tokenize(key): value for key, value in uni_document.items()}
document_tokens = list(uni_document_tokenized.keys())
match_counts = count_matches_per_document(document_tokens, user_question_tokens)
best_matching_document = rank_documents(match_counts, list(uni_document.values()))

print(best_matching_document if best_matching_document else "Sorry, I couldn't find an answer to your question.")







