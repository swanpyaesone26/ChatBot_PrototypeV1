# University FAQ Chatbot - Prototype V1

## 1. Description
This is a simple rule-based chatbot that answers common university-related questions by matching keywords.

**Key Features:**
- Predefined Q&A stored in a dictionary (`uni_document`).
- Tokenizes and compares words for basic keyword matching.
- Returns the best-matched answer.

---

## 2. How It Works

### User Input:
The user asks a question (e.g., "Where is the library?").

### Tokenization:
The question is cleaned (lowercase, no punctuation) and split into words.

### Matching:
The system compares tokens with stored questions in `uni_document`.

### Ranking:
The answer with the most word matches is returned.

---

## 3. Usage

To run the chatbot, execute the script and type your question:

bash : 
python university_chatbot_v1.py 

###Example
>>> Please enter your question: Where is the registration office?  
<<< It's on the first floor of the administration building, Room 102.


# Limitations and Future Improvements

## Limitations

- ❌ **Exact Keyword Dependency**: Misspelled or rephrased questions won't match.
- ❌ **No AI/NLP**: Currently, only basic word matching is implemented (V2/V3 will improve this).
- ❌ **Fixed Database**: New questions require manual updates.

## Future Improvements

### V2:
- Add synonyms, spell-check, and partial matching.

### V3:
- Integrate NLP (e.g., OpenAI, transformers) for smarter responses.
