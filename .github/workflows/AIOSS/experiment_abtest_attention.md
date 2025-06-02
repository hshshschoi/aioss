🧪 Experiment Brief: 제품 결함 탐지 프로젝트 A/B 테스트 설계

 🎯 연관 OKR

Objective: 
제품 결함 탐지 프로젝트에서 모델의 실효성과 사용 편의성을 높이기 위한 개선 실험 수행

Key Results:
- [ ] A/B 테스트를 통해 기존 모델 대비 결함 탐지 정확도 5% 이상 향상된 결과 도출
- [ ] 사용자 피드백 기반 실험 설계 1건 이상 완료
- [ ] 실험 결과 정량 지표로 정리 후 프로젝트 발표 자료에 반영

---

 🧠 실험 가설 (Hypothesis)

> 만약 기존 GLASS 기반 모델의 후반부에 Attention Layer를 삽입하면,  
> 제품 결함 이미지의 Heatmap이 더 집중된 영역을 생성하여  
> 결함 검출 정확도가 향상될 것이다.

---

 🧪 실험 설계 (A/B 테스트 구성)

| 항목 | A 버전 (Control) | B 버전 (Experimental) |
|------|------------------|------------------------|
| **모델 구성** | GLASS 백본 + WideResNet18 | GLASS 백본 + WideResNet18 + Self-Attention Layer |
| **입력 데이터** | MVTec + 자체 결함 이미지 | 동일 |
| **평가 지표** | F1 Score, Precision, Recall, Heatmap 집중도 | 동일 |
| **사용자군** | 팀원 3명 (내부 평가자) | 동일 |
| **실험 기간** | 7일 | 7일 |

---

 📈 기대 효과 (Expected Impact)

- F1 Score가 **5% 이상 향상**
- 불필요한 배경 영역 검출 감소
- Heatmap 집중도가 시각적으로 향상되어 결과 해석력 증가
- 발표 자료에서 성능 향상 사례로 활용 가능

---

 ⚙️ 실험 조건 (Conditions)

- 데이터셋: MVTec Anomaly Dataset + 자체 촬영 결함 이미지
- 학습 환경: 동일한 학습 epoch, batch size, 이미지 해상도
- 분석 도구: confusion matrix, Grad-CAM 시각화, 사용자 평가 (3점 척도)

---

 🔄 실험 후 검토 계획 (Retrospective)

- A/B 버전의 F1 Score, Precision, Recall 정량 비교
- Grad-CAM 결과의 중심 좌표 집중도 비교
- 가설이 기각되면 Attention 구조 재설계 또는 다른 모듈 대체 실험 기획

---

 💡 후속 실험 아이디어

- Self-Supervised 방식 도입 시 성능 비교
- 결함 크기(소형/대형)에 따른 모델 민감도 분석
- Inference 시간 및 리소스 사용량 측정

---
2025/06/02 최혜성

