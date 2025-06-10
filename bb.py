import streamlit as st
import base64
import random
import re

# ===================== 페이지 설정 ======================
st.set_page_config(
    page_title="이호영 자기소개서",
    page_icon="🔥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ===================== 스타일 =====================
dark_style = """
<style>
body, .stApp {
    background: linear-gradient(135deg, #1e40af 0%, #3b82f6 50%, #60a5fa 100%) !important;
    font-family: 'Noto Sans KR', sans-serif !important;
    color: white !important;
}
.slide-card {
    background: rgba(255,255,255,0.10);
    border-radius: 24px;
    padding: 2.5rem 2.5rem 2rem 2.5rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 32px rgba(30,64,175,0.08);
    backdrop-filter: blur(3px);
}
.slide-header {
    font-size: 2.8rem; 
    font-weight: 800; 
    color: #fff; 
    margin-bottom: 0.7rem; 
    letter-spacing: -2px;
}
.slide-sub {
    color: #fbbf24;
    font-weight: 700;
    font-size: 1.3rem;
}
.slide-hr {
    height: 0.35rem; 
    width: 6rem; 
    background: #fb923c; 
    border-radius: 1rem; 
    margin: 0.5rem 0 1.3rem 0;
}
.slide-section-title {
    color: #fff;
    font-size: 1.4rem;
    font-weight: 700;
    margin-bottom: 0.7rem;
}
.slide-footer {
    opacity: 0.7;
    color: #fff;
    font-size: 1.05rem;
    margin-top: 2.5rem;
}
.slide-number {
    position: fixed;
    bottom: 35px;
    right: 35px;
    z-index: 99;
    background: rgba(31, 41, 55, 0.7);
    border-radius: 1.2rem;
    padding: 0.5rem 1rem;
    color: #fff;
    font-size: 1.07rem;
    font-weight: 600;
    letter-spacing: 1px;
}
.stButton>button {
    background-color: #3b82f6;
    color: white;
    border-radius: 0.5rem;
    padding: 0.5rem 1.2rem;
    font-size: 1.1rem;
    font-weight: 600;
    transition: background-color 0.3s ease;
}
.stButton>button:hover {
    background-color: #2563eb;
    color: white;
}
</style>
"""

light_style = """
<style>
body, .stApp {
    background: #f9fafb !important;
    font-family: 'Noto Sans KR', sans-serif !important;
    color: #111 !important;
}
.slide-card {
    background: #fff;
    border-radius: 24px;
    padding: 2.5rem 2.5rem 2rem 2.5rem;
    margin-bottom: 1.5rem;
    box-shadow: 0 4px 32px rgba(0,0,0,0.1);
}
.slide-header {
    font-size: 2.8rem; 
    font-weight: 800; 
    color: #333; 
    margin-bottom: 0.7rem; 
    letter-spacing: -2px;
}
.slide-sub {
    color: #f59e0b;
    font-weight: 700;
    font-size: 1.3rem;
}
.slide-hr {
    height: 0.35rem; 
    width: 6rem; 
    background: #f97316; 
    border-radius: 1rem; 
    margin: 0.5rem 0 1.3rem 0;
}
.slide-section-title {
    color: #333;
    font-size: 1.4rem;
    font-weight: 700;
    margin-bottom: 0.7rem;
}
.slide-footer {
    opacity: 0.7;
    color: #333;
    font-size: 1.05rem;
    margin-top: 2.5rem;
}
.slide-number {
    position: fixed;
    bottom: 35px;
    right: 35px;
    z-index: 99;
    background: rgba(243, 244, 246, 0.7);
    border-radius: 1.2rem;
    padding: 0.5rem 1rem;
    color: #333;
    font-size: 1.07rem;
    font-weight: 600;
    letter-spacing: 1px;
}
.stButton>button {
    background-color: #f97316;
    color: white;
    border-radius: 0.5rem;
    padding: 0.5rem 1.2rem;
    font-size: 1.1rem;
    font-weight: 600;
    transition: background-color 0.3s ease;
}
.stButton>button:hover {
    background-color: #c2410c;
    color: white;
}
</style>
"""

# ====================== 슬라이드 데이터 =====================
slides = [
    {"title": "1. 자기소개", "content": """
    <div class="slide-card">
        <div class="slide-header">이호영</div>
        <div class="slide-hr"></div>
        <div class="slide-sub">재난안전소방학과 <span style='color:#aeefff;'>| 건양대학교</span></div>
        <div style="font-size:1.15rem; margin:1.5rem 0 0.8rem 0;">
            <span style="font-weight:300;">안녕하세요! 👋<br>
            저는 <span style='color:#fb923c; font-weight:600;'>미래의 안전 전문가</span>재난안전소방학과에서 화재 예방, 구조구급, 재난 대응 등 다양한 전문 지식을 배우며 현장 중심의 경험도 쌓아가고 있습니다.
학업과 동아리, 자원봉사 활동을 통해 위기 상황에서 신속하고 정확한 판단력을 기르고, 팀워크와 리더십도 함께 키워나가고 있습니다.
앞으로는 국민의 생명과 재산을 보호하는 안전관리 전문가로 성장해, 더 안전한 사회를 만드는 데 기여하고자 합니다.
책임감과 침착함을 바탕으로 어떤 상황에서도 흔들림 없이 최선을 다하는 모습을 보여드리겠습니다.
감사합니다.<br>
            지금 보다 더 안전한 사회를 위해 성장하겠습니다.
            </span>
        </div>
        <div style="margin-top:1.8rem;">
            <span style="background:rgba(255,255,255,0.16);border-radius:999px;padding:0.20rem 0.85rem;font-weight:500;display:inline-block;margin-right:0.4rem;">🛡️ 안전관리</span>
            <span style="background:rgba(255,255,255,0.16);border-radius:999px;padding:0.20rem 0.85rem;font-weight:500;display:inline-block;margin-right:0.4rem;">🚑 구조구급</span>
            <span style="background:rgba(255,255,255,0.16);border-radius:999px;padding:0.20rem 0.85rem;font-weight:500;display:inline-block;margin-right:0.4rem;">⚠️ 재난대응</span>
        </div>
    </div>
    """},
    {"title": "2. About Me", "content": """
    <div class="slide-card">
        <div class="slide-header"><span style="font-size:2.3rem;">👤</span> About Me</div>
        <div class="slide-hr"></div>
        <div class="slide-section-title">기본 정보</div>
        <ul style='font-size:1.07rem;'>
          <li>🎓 건양대학교 재난안전소방학과</li>
          <li>📍 논산 캠퍼스</li>
          <li>📅 2025년 3학년 재학중</li>
        </ul>
        <div class="slide-section-title" style="margin-top:1.6rem;">성격 & 특성</div>
        <span style="background:rgba(255,255,255,0.16);border-radius:999px;padding:0.20rem 0.85rem;font-weight:500;display:inline-block;margin-right:0.4rem;">📚 지식 탐구형 — 새로운 정보와 기술에 항상 호기심을 가지고 깊이 있게 탐구합니다.</span>
        <span style="background:rgba(255,255,255,0.16);border-radius:999px;padding:0.20rem 0.85rem;font-weight:500;display:inline-block;margin-right:0.4rem;">🤝 협력적 — 팀원들과의 원활한 소통과 협업을 중요시합니다.</span>
        <span style="background:rgba(255,255,255,0.16);border-radius:999px;padding:0.20rem 0.85rem;font-weight:500;display:inline-block;margin-right:0.4rem;">🎯 목표 지향적— 명확한 목표를 세우고 끝까지 성취하기 위해 노력합니다.</span>
        <span style="background:rgba(255,255,255,0.16);border-radius:999px;padding:0.20rem 0.85rem;font-weight:500;display:inline-block;margin-right:0.4rem;">💪 책임감 강함— 맡은 일에 대해 끝까지 책임지는 자세를 지니고 있습니다.</span>
        <div class="slide-section-title" style="margin-top:1.6rem;">취미 & 관심사</div>
        <ul style='font-size:1.07rem;'>
          <li>📖 독서: 다양한 분야의 지식과 통찰력을 확장하며 사고의 폭을 넓히고 있습니다</li>
          <li>🧑‍🔬 학회 활동: 전문성 개발과 네트워킹을 통해 실무 능력과 인적 자원을 강화하고 있습니다.</li>
        </ul>
        <div style="margin-top:1.5rem; color:#fbbf24; font-style:italic; font-size:1.1rem;">
            "끊임없는 학습과 성장으로 안전한 사회를 만드는 전문가가 되겠습니다"
        </div>
    </div>
    """},
    {"title": "3. 학과 소개", "content": """
    <div class="slide-card">
        <div class="slide-header">재난안전소방학과</div>
        <div class="slide-hr"></div>
        <div style="font-size:1.13rem;">
            현대 사회는 자연재해, 화재, 산업재해 등 다양한 재난 위협에 노출되어 있습니다. <b>재난안전소방학과</b>는 이러한 위험으로부터 국민의 생명과 재산을 안전하게 보호하기 위해 전문 인재를 양성하는 학과입니다.
            <b>재난안전소방학과</b>는 <br> 안전 전문가 양성을 위한 학과입니다.
        </div>
        <div style="margin-top:1rem;">
            <span style="background:rgba(255,255,255,0.16);border-radius:999px;padding:0.20rem 0.85rem;font-weight:500;display:inline-block;margin-right:0.4rem;">🚒 소방-소방기술과 안전관리</span>
            <span style="background:rgba(255,255,255,0.16);border-radius:999px;padding:0.20rem 0.85rem;font-weight:500;display:inline-block;margin-right:0.4rem;">⚠️ 재난대응-재난 대응과 예방</span>
            <span style="background:rgba(255,255,255,0.16);border-radius:999px;padding:0.20rem 0.85rem;font-weight:500;display:inline-block;margin-right:0.4rem;">👨‍🎓 진로지도-체계적인 진로지도와 실무 교육</span>
        </div>
        <div style="margin-top:1rem; color:#fbbf24;">
를 통해 학생들이 현장 중심의 실무 역량과 전문 지식을 갖춘 안전 전문가로 성장할 수 있도록 지원합니다. 미래 사회의 안전을 책임질 인재로 거듭나기 위해 끊임없이 연구하고, 실천하는 재난안전소방학과입니다. 미래를 위한 안전 인재 양성에 집중합니다.
        </div>
    </div>
    """},
    {"title": "4. 활동 & 취미", "content": """
    <div class="slide-card">
        <div class="slide-header">활동 & 취미</div>
        <div class="slide-hr"></div>
        <div class="slide-section-title">2024년 추계활동</div>
        <ul style='font-size:1.07rem;'>
            <li>📅 학술 세미나 참여 - 재난안전 분야의 최신 이슈와 트렌드를 학습하며 전문 지식 강화</li>
            <li>🤝 팀 프로젝트 수행 - 동료들과 협력하여 실무 중심의 문제 해결 능력 배양</li>
            <li>📈 전문성 향상 - 이론과 실무를 연결하는 다양한 경험 쌓기</li>
        </ul>
        <div class="slide-section-title" style="margin-top:1.3rem;">활동 성과</div>
        <ul style='font-size:1.06rem;'>
            <li>✅ 100% 참여율</li>
        </ul>
        <div class="slide-section-title" style="margin-top:1.3rem;">독서 활동</div>
        <ul style='font-size:1.06rem;'>
            <li>🔥 소방안전 전문서적 — 전공 지식을 심화하는 데 집중</li>
            <li>🌱 자기계발서 — 개인 성장과 리더십 역량 강화</li>
            <li>💡 창의적 사고 관련 서적 — 문제 해결력 및 사고력 증진</li>
        </ul>
        <div class="slide-section-title" style="margin-top:1.3rem;">2024년 독서 현황</div>
        <ul style='font-size:1.05rem; columns:2; -webkit-columns:2;'>
            <li>📚 총 25권 이상 독서+</li>
            <li>📆 월 평균 2권 꾸준히 독서</li>
        </ul>
        <div class="slide-section-title" style="margin-top:1.3rem;">향후 활동 계획</div>
        <ul style='font-size:1.05rem; columns:2; -webkit-columns:2;'>
            <li>📜 소방 전문 자격증 취득을 목표로 체계적인 준비 </li>
            <li>🤲 지역사회 안전 교육 봉사활동 참여로 실질적 기여 </li>
            <li>🔬 재난안전 분야 학술 연구 참여를 통해 전문성 심화 </li>
        </ul>
    </div>
    """},
    {"title": "5. 향후 목표 & 포부", "content": """
    <div class="slide-card">
        <div class="slide-header">향후 목표 & 포부</div>
        <div class="slide-hr"></div>
        <div class="slide-section-title">단기 목표 (1~2년)</div>
        <ul style='font-size:1.07rem;'>
            <li>📜 소방 관련 전문 자격증 취득을 위해 체계적이고 집중적인 준비</li>
            <li>📚 전공 지식을 더욱 심화 학습하여 실무 역량 강화</li>
            <li>🧑‍🔬 현장 실습과 다양한 경험을 통해 문제 해결 능력 및 현장 대응력 배양</li>
        </ul>
        <div class="slide-section-title" style="margin-top:1.5rem;">중장기 목표 (3~5년)</div>
        <ul style='font-size:1.07rem;'>
            <li>🛡️ 안전관리 분야의 전문가로 자리매김하며 재난 예방과 대응에 기여</li>
        </ul>
        <div class="slide-section-title" style="margin-top:1.5rem;">개인 비전</div>
        <div style="color:#fbbf24; font-size:1.13rem; font-weight:700; margin-bottom:0.5rem;">
            “안전한 대한민국을 만드는 재난안전 전문가로서, 국민의 생명과 재산을 보호하는 책임감 있는 사람람이 되겠습니다.”끝까지 제 이야기를 들어주셔서 감사합니다.앞으로도 꾸준한 노력과 배움으로 안전한 사회를 만드는 데 기여하는 이호영이 되겠습니다.
        </div>
        <div style="margin-top:1.2rem; font-size:1.04rem;">
            끝까지 들어주셔서 감사합니다.<br>
            앞으로도 꾸준히 성장하며 <span style='color:#fde68a;'>안전한 사회</span>를 만드는데 기여하는 <span style='color:#6ee7b7;'>이호영</span>이 되겠습니다.
        </div>
    
           
      
    </div>
    """},
]

# ====================== 세션 상태 초기화 =====================
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = True
if "slide_idx" not in st.session_state:
    st.session_state.slide_idx = 0
if "view_mode" not in st.session_state:
    st.session_state.view_mode = "card"

# ========= 버전별 rerun 함수 정의 =========
def rerun_app():
    try:
        st.rerun()
    except AttributeError:
        try:
            st.experimental_rerun()
        except AttributeError:
            st.stop()

# ========= 스타일 적용 및 모드 토글 =========
if st.sidebar.button("🌗 다크/라이트 모드 토글"):
    st.session_state.dark_mode = not st.session_state.dark_mode
    rerun_app()

st.markdown(dark_style if st.session_state.dark_mode else light_style, unsafe_allow_html=True)

# ========= 슬라이드 인덱스 보정 =========
max_slide_idx = len(slides) - 1
if st.session_state.slide_idx < 0:
    st.session_state.slide_idx = 0
elif st.session_state.slide_idx > max_slide_idx:
    st.session_state.slide_idx = max_slide_idx

# ========= 사이드바 슬라이드 이동 =========
slide_titles = [s["title"] for s in slides]
selected_title = st.sidebar.selectbox("슬라이드 선택", slide_titles, index=st.session_state.slide_idx, key="slide_selectbox")
selected_idx = slide_titles.index(selected_title)
if selected_idx != st.session_state.slide_idx:
    st.session_state.slide_idx = selected_idx

# ========= 보기 모드 =========
view_mode = st.sidebar.radio("보기 모드", options=["카드 모드", "텍스트 모드"], index=0 if st.session_state.view_mode=="card" else 1, key="view_mode_radio")
st.session_state.view_mode = "card" if view_mode == "카드 모드" else "text"

# ========= 상단 타이틀 & 네비게이션 =========
st.markdown(f"<h1 style='text-align:center; font-size:2.2rem; margin-bottom:0.2rem;'>{slides[st.session_state.slide_idx]['title']}</h1>", unsafe_allow_html=True)

col_nav = st.columns([1, 3, 1])
with col_nav[0]:
    if st.button("⬅ 이전", key="prev_btn"):
        if st.session_state.slide_idx > 0:
            st.session_state.slide_idx -= 1
            rerun_app()
with col_nav[2]:
    if st.button("다음 ➡", key="next_btn"):
        if st.session_state.slide_idx < max_slide_idx:
            st.session_state.slide_idx += 1
            rerun_app()

# ========= 슬라이드 표시 =========
slide = slides[st.session_state.slide_idx]
if st.session_state.view_mode == "card":
    st.markdown(slide["content"], unsafe_allow_html=True)
else:
    text = re.sub(r'<.*?>', '', slide["content"])
    st.text_area("슬라이드 내용 (텍스트 모드)", value=text.strip(), height=400)

# ========= 진행도 표시 =========
progress = (st.session_state.slide_idx + 1) / len(slides)
st.progress(progress)

# ========= 페이지 인덱스 표시 =========
st.markdown(f"<div class='slide-number'>{st.session_state.slide_idx + 1} / {len(slides)}</div>", unsafe_allow_html=True)

# ========= 전체 슬라이드 HTML 내보내기 =========
def generate_full_html(slides):
    slide_htmls = [s["content"] for s in slides]
    full_html = """
    <!DOCTYPE html>
    <html lang="ko">
    <head>
    <meta charset="UTF-8">
    <title>자기소개서 슬라이드</title>
    <style>
    body { font-family: 'Noto Sans KR', sans-serif; background:#111; color:#eee; margin: 2rem; }
    .slide-card { background: rgba(0,0,0,0.7); border-radius: 1rem; padding: 2rem; margin-bottom: 3rem; }
    h1, h2, h3, h4, h5 { color: #fbbf24; }
    </style>
    </head>
    <body>
    """
    for html in slide_htmls:
        full_html += f"<section class='slide-card'>{html}</section>\n"
    full_html += "</body></html>"
    return full_html

def get_download_link(html, filename="full_slides.html"):
    b64 = base64.b64encode(html.encode()).decode()
    href = f'<a href="data:text/html;base64,{b64}" download="{filename}">⬇️ 전체 슬라이드 HTML 다운로드</a>'
    return href

st.markdown("---")
full_html = generate_full_html(slides)
st.markdown(get_download_link(full_html), unsafe_allow_html=True)

if st.button("📄 전체 PDF로 내보내기 (준비중)"):
    st.info("PDF 내보내기 기능은 준비 중입니다. 나중에 추가 예정입니다.")

# ========= 전체 미리보기 =========
with st.expander("👀 전체 슬라이드 미리보기"):
    for idx, s in enumerate(slides):
        st.markdown(f"#### {idx+1}. {s['title']}")
        st.markdown(s["content"], unsafe_allow_html=True)
        st.markdown("---")

# ========= 페이지 바로가기 숫자 버튼 =========
st.markdown("#### 페이지 바로가기")
btn_cols = st.columns(len(slides))
for i, c in enumerate(btn_cols):
    if c.button(str(i+1), key=f"goto_{i}"):
        st.session_state.slide_idx = i
        rerun_app()

# ========= 슬라이드 랜덤 이동 =========
if st.button("🔀 랜덤 슬라이드로 이동", key="random_btn"):
    st.session_state.slide_idx = random.randint(0, len(slides)-1)
    rerun_app()

# ========= 진행률 % 표시 =========
st.markdown(f"<div style='text-align:center; color:#888; font-size:1.1rem;'>진행률: {int(progress*100)}%</div>", unsafe_allow_html=True)
