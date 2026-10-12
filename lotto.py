import random
import streamlit as st

# 1. 페이지 기본 설정
st.set_page_config(page_title="로또 번호 추첨기", page_icon="🎰", layout="centered")


# 2. 로또 번호별 공 색상(HTML) 생성 함수 (줄바꿈 없이 한 줄로 처리하여 인식 오류 해결)
def get_ball_html(number):
    if number <= 10:
        bg_color, text_color = "#fbc400", "#000000"  # 노란색
    elif number <= 20:
        bg_color, text_color = "#69c8f2", "#ffffff"  # 파란색
    elif number <= 30:
        bg_color, text_color = "#ff7272", "#ffffff"  # 빨간색
    elif number <= 40:
        bg_color, text_color = "#aaa", "#ffffff"  # 회색
    else:
        bg_color, text_color = "#b0d840", "#ffffff"  # 초록색

    # HTML 텍스트 안의 줄바꿈과 공백을 없애서 렌더링 오류를 방지합니다.
    return f'<div style="display:inline-block; width:45px; height:45px; line-height:45px; border-radius:50%; background-color:{bg_color}; color:{text_color}; font-weight:bold; font-size:18px; text-align:center; margin:4px; box-shadow:2px 2px 5px rgba(0,0,0,0.2);">{number}</div>'


# 3. 세션 상태(Session State) 초기화 (추첨 이력 저장용)
if "lotto_history" not in st.session_state:
    st.session_state.lotto_history = []

# 4. 타이틀 및 안내
st.title("🎰 행운의 로또 번호 추첨기")
st.write("버튼을 누르면 1~45 사이의 중복 없는 번호 6개를 추첨합니다. (최대 5세트)")

# 5. [로또번호 생성] 버튼
if st.button("🎲 로또번호 생성", type="primary"):
    if len(st.session_state.lotto_history) >= 5:
        st.warning(
            "⚠️ 최대 5개 세트까지만 생성할 수 있습니다! [초기화] 버튼을 눌러주세요."
        )
    else:
        new_numbers = sorted(random.sample(range(1, 46), 6))
        st.session_state.lotto_history.append(new_numbers)

# 6. 추첨된 로또 번호 출력
if st.session_state.lotto_history:
    st.markdown("---")
    st.subheader("📋 추첨 결과")

    for idx, numbers in enumerate(st.session_state.lotto_history, 1):
        balls_html = "".join([get_ball_html(num) for num in numbers])

        # st.html() 또는 markdown + unsafe_allow_html 로 예쁜 공 출력
        st.markdown(
            f"**{idx}회차:** &nbsp;&nbsp; {balls_html}", unsafe_allow_html=True
        )

    st.write("")
    # 7. 초기화 버튼
    if st.button("🔄 번호 초기화"):
        st.session_state.lotto_history = []
        st.rerun()