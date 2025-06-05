from collections import defaultdict, Counter
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
from math import log2, sqrt
import nltk

nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')

def get_sample_documents():
    return {
        "1": (
            "Python is a versatile programming language widely used in various domains such as web development, "
            "data science, artificial intelligence, and automation. It has a clean syntax and a strong community "
            "which makes it a popular choice for beginners and professionals alike."
        ),
        "2": (
            "Implementing a neural network in Python can be done using libraries like TensorFlow or PyTorch. "
            "Understanding how backpropagation and activation functions work is key to building efficient models."
        ),
        "3": (
            "The Internet of Things (IoT) is revolutionizing smart homes and cities by enabling devices to communicate "
            "and automate processes. From smart thermostats to traffic management systems, IoT increases efficiency and convenience."
        ),
        "4": (
            "Web development involves a range of technologies. Python offers frameworks like Django and Flask, while JavaScript, "
            "often paired with HTML and CSS, powers dynamic front-end experiences. Choosing between them depends on the project's goals."
        ),
        "5": (
            "TF-IDF stands for Term Frequency-Inverse Document Frequency, a numerical statistic used in text mining to evaluate "
            "how important a word is to a document in a collection. It is widely used in information retrieval systems like search engines."
        ),
        "6": (
            "Machine learning is a subset of artificial intelligence that focuses on building systems that can learn from and adapt "
            "to new data without explicit programming. It powers applications like speech recognition, recommendation systems, and fraud detection."
        ),
        "7": (
            "Cybersecurity is crucial in today's digital world. As more services move online, protecting user data and ensuring system "
            "integrity against threats like phishing, malware, and ransomware becomes increasingly important."
        ),
        "8": (
            "Data visualization helps make sense of complex data by transforming numbers into visual context such as charts, graphs, and maps. "
            "Tools like Matplotlib, Seaborn, and Tableau are widely used for this purpose."
        )
    }

def preprocess(text):
    stop_words = set(stopwords.words("english"))
    lemmatizer = WordNetLemmatizer()
    tokens = word_tokenize(text.lower())
    return [lemmatizer.lemmatize(w) for w in tokens if w.isalnum() and w not in stop_words]

def build_inverted_index(docs):
    index = defaultdict(list)
    for doc_id, text in docs.items():
        tokens = preprocess(text)
        freqs = Counter(tokens)
        for term, freq in freqs.items():
            index[term].append((doc_id, freq))
    return index

def compute_tfidf(index, total_docs):
    tfidf = defaultdict(dict)
    for term, postings in index.items():
        df = len(postings)
        idf = log2(total_docs / df)
        for doc_id, tf in postings:
            weight = (1 + log2(tf)) * idf
            tfidf[doc_id][term] = weight
    return tfidf

def vectorize_query(query, index, total_docs):
    tokens = preprocess(query.lower())
    vec = {}
    for t in tokens:
        df = len(index.get(t, [])) or 1
        idf = log2(total_docs / df)
        tf = tokens.count(t)
        vec[t] = (1 + log2(tf)) * idf
    return vec

def cosine_similarity(qvec, dvec):
    common = set(qvec) & set(dvec)
    numerator = sum(qvec[t]*dvec[t] for t in common)
    denom = sqrt(sum(v**2 for v in qvec.values())) * sqrt(sum(v**2 for v in dvec.values()))
    return numerator / denom if denom else 0

def euclidean_distance(qvec, dvec):
    all_terms = set(qvec) | set(dvec)
    return sqrt(sum((qvec.get(t, 0)-dvec.get(t, 0))**2 for t in all_terms))

if __name__ == "__main__":
    docs = get_sample_documents()
    total_docs = len(docs)
    index = build_inverted_index(docs)
    tfidf_index = compute_tfidf(index, total_docs)

    query = input("검색어를 입력하세요: ")
    qvec = vectorize_query(query, index, total_docs)

    print("\n[Frequency Ranking]")
    tf_scores = {}
    for term in qvec:
        for doc_id, freq in index.get(term, []):
            tf_scores[doc_id] = tf_scores.get(doc_id, 0) + freq
    for doc, score in sorted(tf_scores.items(), key=lambda x: -x[1])[:5]:
        print(f"Doc {doc} - Score: {score} - Contents: {docs[doc]}")

    print("\n[TF-IDF Ranking]")
    tfidf_scores = [(doc_id, sum(qvec.get(t,0) * tfidf.get(t,0) for t in qvec)) for doc_id, tfidf in tfidf_index.items()]
    for doc, score in sorted(tfidf_scores, key=lambda x: -x[1])[:5]:
        print(f"Doc {doc} - Score: {score:.3f} - Contents: {docs[doc]}")

    print("\n[Cosine Similarity]")
    cos_scores = [(doc_id, cosine_similarity(qvec, tfidf)) for doc_id, tfidf in tfidf_index.items()]
    for doc, score in sorted(cos_scores, key=lambda x: -x[1])[:5]:
        print(f"Doc {doc} - Similarity: {score:.3f} - Contents: {docs[doc]}")

    print("\n[Euclidean Distance]")
    euc_scores = [(doc_id, euclidean_distance(qvec, tfidf)) for doc_id, tfidf in tfidf_index.items()]
    for doc, score in sorted(euc_scores, key=lambda x: x[1])[:5]:
        print(f"Doc {doc} - Distance: {score:.3f} - Contents: {docs[doc]}")
