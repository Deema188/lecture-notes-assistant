import re
from collections import Counter

def clean_text(text):
    # نشيل علامات الترقيم الزيادة ونرجع النص نظيف
    sentences = re.split(r'(?<=[.!?؟])\s+', text.strip())
    return [s for s in sentences if s]

def get_word_frequencies(text):
    # نحسب كم مرة كل كلمة تكررت بالنص
    words = re.findall(r'\w+', text.lower())
    return Counter(words)

def score_sentences(sentences, word_freq):
    # كل جملة تاخذ نقاط حسب أهمية كلماتها
    scores = {}
    for sentence in sentences:
        words = re.findall(r'\w+', sentence.lower())
        score = sum(word_freq.get(word, 0) for word in words)
        scores[sentence] = score
    return scores

def summarize(text, num_sentences=3):
    sentences = clean_text(text)
    
    if len(sentences) <= num_sentences:
        return text
    
    word_freq = get_word_frequencies(text)
    scores = score_sentences(sentences, word_freq)
    
    # ناخذ أعلى الجمل نقاط
    top_sentences = sorted(scores, key=scores.get, reverse=True)[:num_sentences]
    
    # نرتبهم بنفس ترتيبهم الأصلي بالنص
    ordered_summary = [s for s in sentences if s in top_sentences]
    
    return ' '.join(ordered_summary)


# تجربة الدالة
if __name__ == "__main__":
    lecture_text = """
    Artificial intelligence is a branch of computer science focused on building systems capable of learning and making decisions.
    AI relies heavily on large datasets and advanced algorithms to function effectively.
    Some of its most important applications include image recognition and natural language processing.
    Neural networks are one of the key tools used in deep learning.
    Deep learning attempts to mimic the way the human brain processes information.
    Today, artificial intelligence is used in many fields such as medicine, education, and industry.
    """
    
    summary = summarize(lecture_text, num_sentences=2)
    print("Summary:")
    print(summary)