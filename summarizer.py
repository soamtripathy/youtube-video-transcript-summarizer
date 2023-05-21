import spacy
from spacy.lang.en.stop_words import STOP_WORDS
from string import punctuation
from heapq import nlargest

text="""I wanted to improve my spoken English but I couldn't and it was because of my hectic job hi I am Nikita and I'm a full start developer at a company in Bangalore believe me it's a really stressful job and not only it is stressful because of the workload but also because when you are working in a big Corporation you need to have good communication skills which I didn't because of that I had very little contribution during meetings and so I was hardly given any appraisal I felt lonely and depressed I wanted to build up my confidence and improve my fluency but the problem was I didn't have enough time I was working 10 to 12 hours every single day you know and I was too exhausted to focus on anything I Tried reading books but soon realized it was not for me I couldn't concentrate for even five minutes without falling asleep during the weekends I tried watching self-improvement videos but they weren't really effective I was really desperate but didn't know what to do that's when I saw a natural clapping go they talked about how one-on-one communication is the best way to learn any language and I'm not gonna lie I didn't believe it initially I thought this was a waste of money but still I give it to go and booked a 15-minute demo class and after that everything changed it was probably one of my best decisions even though I was usually tired in the evening I still enjoyed having conversations with the tutors and surprisingly I started improving my communication within just 30 days I started having amazing interactions with my colleagues I didn't feel underappreciated at work anymore moreover the tutors were extremely friendly and supported me throughout my journey I can't thank them enough so if you are also someone who wants to improve their English in the shortest possible time just book a session at clapping room"""

stopwords=list(STOP_WORDS)

nlp=spacy.load("en_core_web_sm")
doc=nlp(text)
tokens=[token.text for token in doc]
word_freq={}
for word in doc:
    if word.text.lower() not in stopwords and word.text.lower() not in punctuation:
        if word.text not in word_freq.keys():
            word_freq[word.text]=1
        else:
            word_freq[word.text]+=1


max_freq=max(word_freq.values())
for word in word_freq.keys():
    word_freq[word]=word_freq[word]/max_freq

sent_tokens=[sent for sent in doc.sents] 

sent_scores={}
for sent in sent_tokens:
    for word in sent:
        if word.text in word_freq.keys():
            if sent not in sent_scores.keys():
                sent_scores[sent]=word_freq[word.text]
            else:
                sent_scores[sent]+=word_freq[word.text]

select_len = int(len(sent_tokens)*0.3)
summary = nlargest(select_len,sent_scores,key=sent_scores.get)
final_summary=[word.text for word in summary]
summary=" ".join(final_summary)
print(text,summary,sep="\n\n\n")