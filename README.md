# 영화 추천 서비스 프로젝트

## 1. 팀원 정보 및 업무 분담 내역

- **박희원**
  - 역할: 조장
  - 주요 업무:
    - AI 모델 데이터 수집
    - 주요 API 연결
    - 회원 관련 기능, 영화 상세 및 리뷰 기능, AI 모델 기반 추천 기능, 일간 박스오피스 기반 추천, 돌림판 기능에 대한 백엔드 및 프론트엔드 작업 (김민지와 공동 작업)

- **김민지**
  - 역할: 팀원
  - 주요 업무:
    - 전반적인 디자인 통일성 유지 및 조정
    - AI 모델과 뷰 서버 간 연결 작업
    - 회원 관련 기능, 영화 상세 및 리뷰 기능, AI 모델 기반 추천 기능, 일간 박스오피스 기반 추천, 돌림판 기능에 대한 백엔드 및 프론트엔드 작업 (박희원과 공동 작업)

---

## 2. 목표 서비스 구현 및 실제 구현 정도

**목표 서비스 구현**  
- 본 프로젝트는 "재미"를 주제로 한 영화 추천 서비스를 목표로 하며, AI와 데이터를 활용해 사용자에게 새로운 방식의 영화 추천 경험을 제공합니다.  
- 추천 과정에서 탐색의 재미를 더하는 엔터테인먼트적 요소를 포함하며, 기존 영화 정보 및 추천 서비스에서는 제공하지 않았던 독창적인 추천 방식을 도입합니다.  
- 사용자가 자신의 영화 관람 및 기록 활동을 통해 개인적인 영화 문화 생활을 관리할 수 있도록 지원하며, 다른 사용자와 리뷰와 댓글을 통해 소통하며 영화 관람 경험을 공유할 수 있도록 설계되었습니다.

**실제 구현 정도**

1. **AI 기반 추천 기능**
   - Teachable Machine과 TensorFlow를 활용해 사용자가 입력한 이미지를 기반으로 닮은 한국 배우를 추천.
   - 해당 배우의 필모그래피를 기반으로 영화 추천 기능 구현 (필모그래피 탐색 과정에서 개선 필요).

2. **API 기반 추천 기능**
   - 영화진흥위원회 오픈 API와 TMDB API를 활용해 **일간 박스오피스 추천 기능** 구현.
   - TMDB와 돌림판 라이브러리를 활용한 **랜덤 인기 영화 추천 기능** 구현.
   - 돌림판 추천 기능에 **영화 설명 키워드 기반 유해 영화 포스터 차단 기능** 추가 도입.

3. **사용자 기록 및 소통 기능**
   - 사용자가 영화에 대한 상세 정보를 얻고 해당 영화에 대한 리뷰를 남길 수 있음.
   - 사용자는 아직 보지 않은 영화에 대해 "보고 싶어요"를 남길 수 있으며, 이를 프로필 페이지에서 확인 가능.
   - 본인이 남긴 리뷰와 보고 싶은 영화 목록을 관리할 수 있음.
   - 다른 사용자의 리뷰에 댓글을 달거나, 좋아요를 통해 리뷰를 평가하며 소통 가능.

---

## 3. 데이터베이스 모델링 (ERD)

**설명**  
- 본 프로젝트의 데이터베이스는 영화 정보, 사용자 활동, 리뷰 및 추천 기능을 효율적으로 관리하기 위해 설계되었습니다.  
- 주요 테이블과 관계:
  - **User 테이블**: 회원 정보 및 프로필 관리 (리뷰, 보고싶어요 기록 등 사용자 활동 추적).
  - **Movie 테이블**: 영화에 대한 기본 정보(제목, 장르, 설명 등) 저장.
  - **Review 테이블**: 사용자가 남긴 리뷰와 댓글을 관리하며, 리뷰에 대한 좋아요 관계를 정의.
  - **Recommendation 테이블**: AI 및 API를 통해 생성된 추천 영화 데이터를 저장.
- 주요 관계:
  - User와 Movie는 리뷰 및 보고싶어요를 통해 다대다(M:N) 관계로 연결됨.
  - Review와 Comment는 일대다(1:N) 관계로 설계되어 리뷰당 여러 댓글을 작성할 수 있음.

**ERD 링크**  

https://dbdiagram.io/d/673bf007e9daa85acae60bbd

---

## 4. 영화 추천 알고리즘에 대한 기술적 설명

**AI 활용 기반 추천 알고리즘**
- GPT 모델을 활용하여 인기 배우 상위 50명을 추천받습니다.
- 크롤링을 통해 추천받은 배우들의 얼굴 이미지를 수집합니다.
- Teachable Machine을 이용해 배우들의 이미지와 클래스 데이터를 로드하여, 사용자가 입력한 이미지가 속한 클래스 결과물을 도출합니다.
- 도출된 클래스 결과물 중 최상위 퍼센트를 가진 배우를 선정한 뒤, TMDB API를 활용하여 해당 배우의 필모그래피(영화 이력)를 추출하여 사용자에게 전달합니다.

**돌림판 추천 알고리즘**
- TMDB API를 이용하여 인기 영화 데이터를 수집하고, 해당 영화의 포스터 이미지를 로드합니다.
- 돌림판 라이브러리를 활용해 사용자가 랜덤으로 영화를 추천받을 수 있는 기능을 제공합니다.
- 돌림판 결과는 모달 창으로 사용자에게 안내됩니다.
- GPT를 활용하여 유해할 수 있는 키워드 목록을 수집한 후, 추천된 영화의 설명 정보에서 유해 키워드가 포함되어 있는지 검사합니다.
- 유해 키워드가 포함된 경우, 영화 포스터 이미지를 블러 처리하고 유해 콘텐츠 가능성이 있음을 사용자에게 안내하여 안전한 사용 경험을 제공합니다.

---

## 5. 핵심 기능에 대한 설명

**1. 회원 관리 기능**
- 회원가입 및 로그인.
- 프로필 관리 및 수정 가능.

**2. 영화 추천 기능**
- AI 기반 영화 추천: 사용자의 선호도를 분석하여 맞춤형 영화 추천.
- 박스오피스 기반 추천: 최신 인기 영화를 일간 데이터를 활용해 추천.
- 돌림판 추천: 랜덤 방식으로 추천받는 재미 요소 추가.

**3. 영화 상세 정보**
- 선택한 영화에 대한 상세 정보 제공 (장르, 감독, 출연진, 줄거리 등).
- 사용자 리뷰 및 별점 확인 가능.

**4. 사용자 기록 기능**
- 관람한 영화와 보고 싶은 영화 목록 관리.
- 프로필 페이지에서 기록 확인 가능.

**5. 사용자 소통 기능**
- 리뷰 작성 및 댓글 기능.
- 리뷰에 좋아요를 통해 사용자 간 의견 교환 가능.

---

## 6. 생성형 AI를 활용한 부분

**1. 데이터 생성 및 수집**
- GPT를 활용해 인기 배우 또는 키워드 목록을 생성.
- 유해 콘텐츠 필터링을 위한 키워드 데이터 자동 수집.

**2. 사용자 맞춤 추천**
- GPT를 기반으로 사용자의 선호도와 입력 데이터를 분석하여 맞춤형 영화 추천 제공.

**3. 콘텐츠 관리**
- 영화 추천 시 유해 콘텐츠 필터링 작업에 GPT로 생성된 키워드 활용.
- 돌림판 추천 기능의 블러 처리 여부를 판단하는 데이터 소스로 사용.

---

## 7. 기타 (느낀점, 후기 등)

**1. 프로젝트를 통해 배운 점**
- 협업 과정에서 효과적인 소통과 업무 분담의 중요성을 체감했습니다.
- AI 모델과 API를 결합하여 실질적인 기능을 구현하는 과정을 배우는 데 큰 도움이 되었습니다.

**2. 어려웠던 점**
- 데이터 크롤링 및 유해 콘텐츠 필터링 과정에서 예상보다 많은 시간이 소요되었습니다.
- AI 모델의 성능을 높이기 위한 데이터 수집과 학습 과정에서 한계가 있었습니다.

**3. 개선할 점**
- API로 가져온 영화 정보 중 사용자가 리뷰를 작성하고 싶을 경우, 해당 내용을 데이터베이스에 저장하는 기능이 필요합니다.
- 소셜 로그인, 이메일 인증, 비밀번호 변경 등 계정 관련 추가 기능을 통해 회원 정보 보안 및 사용 편의성을 강화할 필요가 있습니다.

**4. 팀원 후기**
- 프로젝트를 통해 서로의 강점을 살려 효과적으로 협업할 수 있었습니다.
- 일정 조율과 문제 해결 과정에서 많은 성장을 느꼈습니다.
