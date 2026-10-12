# 🎈 Streamlit 기반 로또 번호 추첨기 (Lotto Generator)

> 파이썬의 **Streamlit** 라이브러리를 활용하여 만든 간편한 로또 번호 추첨 웹 애플리케이션입니다.  
> 실제 로또 공의 색상 규칙을 적용하여 시각적으로 깔끔한 번호 생성 기능을 제공합니다.

---

## ✨ 주요 기능 (Key Features)

- **🎲 중복 없는 로또 번호 생성**: 1부터 45까지의 숫자 중 중복 없이 6개 번호를 무작위로 추출하여 오름차순으로 보여줍니다.
- **🎨 실제 로또 공 색상 반영**: 번호 구간별로 공식 로또 공 색상(노랑, 파랑, 빨강, 보라/회색, 초록)을 적용하여 시각화했습니다.
  - `1 ~ 10`: 💛 노란색
  - `11 ~ 20`: 💙 파란색
  - `21 ~ 30`: ❤️ 빨간색
  - `31 ~ 40`: 💜 보라색/회색
  - `41 ~ 45`: 💚 초록색
- **🔢 최대 5개 세트 누적**: [로또번호 생성] 버튼을 누를 때마다 최대 5개 세트까지 화면에 차곡차곡 누적됩니다.
- **🔄 초기화 기능**: [초기화] 버튼을 누르면 생성된 번호 기록이 깔끔하게 삭제됩니다.

---

## 📁 프로젝트 구조 (Project Structure)

```text
├── app.py            # Streamlit 로또 추첨기 메인 코드
├── requirements.txt  # 필요한 파이썬 라이브러리 목록
└── README.md         # 프로젝트 설명 문서
```

---

## 🚀 실행 방법 (Getting Started)

### 1. 저장소 복제 (Clone Repository)
```bash
git clone https://github.com/사용자이름/레포지토리이름.git
cd 레포지토리이름
```

### 2. 가상환경 생성 및 활성화 (선택 사항)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. Streamlit 앱 실행
```bash
streamlit run app.py
```
명령어를 입력하면 웹 브라우저가 자동으로 열리며 로또 추첨기가 실행됩니다.

---

## 🛠️ 기술 스택 (Tech Stack)

- **Language**: Python 3.x
- **Framework**: Streamlit
- **Library**: `random` (Python 내장 라이브러리)

---

## 📝 코드 핵심 설명 (For Beginners)

- `random.sample(range(1, 46), 6)`: 1~45 숫중 중복 없이 6개를 무작위 추출합니다.
- `st.session_state`: 웹 페이지가 다시 로드되어도 이전에 생성했던 번호 세트가 유지되도록 저장하는 기능을 담당합니다.
- `HTML/CSS Style`: Inline CSS를 활용해 동그란 로또 공 형태와 볼 색상을 입혔습니다.
