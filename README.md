University FAQ Chatbot - Prototype V1


1. Description (ဖော်ပြချက်)
This is a simple rule-based chatbot that answers common university-related questions by matching keywords.
(ဒီသည် တက္ကသိုလ်ဆိုင်ရာ မေးခွန်းများကို အလိုအလျောက်ဖြေပေးသည့် အခြေခံ chatbot ဖြစ်သည်။)

Key Features (အဓိက လုပ်ဆောင်ချက်များ):

Predefined Q&A stored in a dictionary (uni_document).

Tokenizes and compares words for basic keyword matching.

Returns the best-matched answer.

2. How It Works (အလုပ်လုပ်ပုံ)
User Input: The user asks a question (e.g., "Where is the library?").

Tokenization: The question is cleaned (lowercase, no punctuation) and split into words.

Matching: The system compares tokens with stored questions in uni_document.

Ranking: The answer with the most word matches is returned.

(၁) သုံးသူက မေးခွန်းမေးသည်။
(၂) စာကြောင်းကို စကားလုံးများအဖြစ် ခွဲထုတ်သည်။
(၃) uni_document ထဲရှိ မေးခွန်းများနှင့် တိုက်စစ်သည်။
(၄) အလိုက်ဖက်ဆုံး အဖြေကို ပြသည်။

3. Usage (အသုံးပြုနည်း)
Run the script and type your question:

python
Copy
python university_chatbot_v1.py
(ဖိုင်ကို run ၍ မေးခွန်းကို ရိုက်ထည့်ပါ။)

Example (နမူနာ):

Copy
>> Please enter your question: Where is the registration office?  
<< It's on the first floor of the administration building, Room 102.
4. Limitations (ကန့်သတ်ချက်များ)
❌ Exact keyword dependency – Misspelled or rephrased questions won’t match.

❌ No AI/NLP – Only basic word matching (V2/V3 will improve this).

❌ Fixed database – New questions require manual updates.

(✔ V2/V3 တွင် AI, NLP နှင့် ပိုမိုတိုးတက်အောင် လုပ်ဆောင်သွားမည်။)
