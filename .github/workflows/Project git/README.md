
# TF-IDF 기반 문서 검색 엔진

이 프로젝트는 사용자가 입력한 검색어(Query)를 기반으로, 여러 문서 중 관련성 높은 문서를 찾아주는 검색 시스템입니다.
TF, TF-IDF, 코사인 유사도, 유클리드 거리 등의 정보 검색 기법을 활용합니다.

---

## 📁 파일 구조

- `git과제.py` : 메인 코드 파일로, 문서 검색 엔진 전체 기능이 구현되어 있음
- `README.md` : 프로젝트 설명서 (이 파일)

---

## 💾 실행 환경

- Python 3.x
- 필요한 패키지:
  - nltk

### 🔧 설치 방법

```bash
pip install nltk
```

### 📦 NLTK 리소스 다운로드 (최초 1회 실행 필요)

```python
import nltk
nltk.download('punkt')
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('omw-1.4')
```

---

## 🔍 주요 기능 및 코드 설명

### 1. `get_sample_documents()`
- XML 없이 하드코딩된 8개의 예시 문서를 반환
- 각 문서는 기술, 프로그래밍, 인공지능, 보안 등 다양한 주제 포함

---

### 2. `preprocess(text)`
- 소문자 변환
- 토큰화 (단어 나누기)
- 불용어(stopwords) 제거
- 어간 추출 (Lemmatization)  
→ 검색 정확도 향상

---

### 3. `build_inverted_index(docs)`
- 문서 전체를 단어 단위로 나누고
- 단어가 등장하는 문서 ID와 빈도수로 구성된 역색인 생성

---

### 4. `compute_tfidf(index, total_docs)`
- 단어별 TF-IDF 점수 계산
- TF (Term Frequency): 문서 내 단어 빈도
- IDF (Inverse Document Frequency): 해당 단어가 등장한 문서 수 기반
- TF-IDF: `(1 + log2(tf)) * log2(total_docs / df)`

---

### 5. `vectorize_query(query, index, total_docs)`
- 사용자가 입력한 검색어를 벡터화하여 문서들과 비교 가능하게 만듬

---

### 6. 유사도 계산 함수
- `cosine_similarity(qvec, dvec)` : 코사인 유사도 기반 문서 간 각도 비교
- `euclidean_distance(qvec, dvec)` : 두 벡터 간 거리 계산
- `TF Ranking` : 단어 빈도 기반
- `TF-IDF Ranking` : 가중치를 포함한 관련성 기반

---

### 7. 실행 흐름 (`__main__`)
- 문서 불러오기
- 역색인과 TF-IDF 벡터화
- 검색어 입력
- 4가지 방법으로 관련 문서 상위 5개 출력

---

## ▶️ 실행 예시

```bash
python git과제.py
```

입력 예:
```
검색어를 입력하세요: python neural network
```

출력 예:
```
[TF-IDF Ranking]
Doc 2 - Score: 5.123 - Contents: Implementing a neural network in Python...

[Cosine Similarity]
Doc 2 - Similarity: 0.923 - Contents: Implementing a neural network...
```

---

