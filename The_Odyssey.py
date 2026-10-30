import streamlit as st
import pandas as pd
import random
from datetime import datetime
import os

# 1. 페이지 설정 (탭 제목, 아이콘, 레이아웃 넓게 쓰기)
st.set_page_config(
    page_title='오디세우스의 여정', page_icon='🌊', layout='wide'
)

# 💡 CSS를 활용해 상단 기본 여백(padding)을 줄이기
st.markdown(
    """
    <style>
        /* Streamlit 기본 상단 여백 줄이기 */
        .block-container {
            padding-top: 3rem;
            padding-bottom: 2rem;
        }
    </style>
    """,
    unsafe_allow_html=True,
)


# 2. 최상단: 지중해 여정 지도 (컬럼을 활용해 이미지 크기를 한눈에 들어오게 축소)
IMAGE_PATH = r"C:\workspace\streamlit_basic\data\odyssey.png"

# 좌우 여백(1.5)을 두고 중앙 컬럼(3)의 비율을 줄여 이미지 크기를 적절히 맞춥니다.
col_left, col_center, col_right = st.columns([1.5, 3, 1.5])

with col_center:
  if os.path.exists(IMAGE_PATH):
    st.image(
        IMAGE_PATH,
        caption="트로이에서 이타카까지의 20년 대장정 지도",
        use_container_width=True,  # 중앙 컬럼 크기에 맞춰 축소
    )
  else:
    st.error(f"이미지 파일을 찾을 수 없습니다: {IMAGE_PATH}")


# 3. 지도 바로 하단: 한 줄 타임라인 선택기
st.markdown(
    "<p style='text-align: center; font-weight: bold; margin-top: 15px;"
    " margin-bottom: 5px;'>🌐 지중해 여정 타임라인 선택</p>",
    unsafe_allow_html=True,
)

selected_step = st.radio(
    "여정 단계",
    [
        "10년차: 트로이 탈출",
        "시련: 폴리페모스",
        "유혹: 세이렌",
        "딜레마: 스킬라와 카리브디스",
        "금기: 아폴론의 가축",
        "17년차: 칼립소의 섬",
        "20년차: 이타카 귀환",
    ],
    horizontal=True,
    label_visibility="collapsed",
)

st.divider()

# 4. 하단: 넓은 공간을 온전히 사용하는 상세 아카이브 영역
st.markdown(
    "<h3 style='font-size: 1.35rem; font-weight: bold;'>📜 상세 아카이브 및"
    " 인문학적 고찰</h3>",
    unsafe_allow_html=True,
)

if "트로이" in selected_step:
  st.markdown(
      "<h4 style='font-size: 1.25rem; font-weight: bold;'>🐴 트로이 목마와 자만의"
      " 시작 (Year 10)</h4>",
      unsafe_allow_html=True,
  )
  st.write(
      "오디세우스는 신성한 환대의 법과 제우스의 질서를 역이용하는 간교한"
      " 기지로 10년 만에 트로이 전쟁을 승리로 이끕니다. 그러나 상대를 속이기"
      " 위해 신성마저 도구화한 이 탁월한 승리는 역설적으로 영웅의 내면에"
      " 지울 수 없는 죄책감의 씨앗을 뿌리고, 거대한 '오만(Hubris)'의"
      " 도화선이 됩니다."
  )
  with st.expander("원문 구절 및 인문학적 성찰 보기"):
    st.info(
        "“우리는 신들의 법을 비틀어 성을 무너뜨렸나, 그 기지가 가져올 거대한"
        " 대가를 그때는 알지 못했다.”"
    )

elif "폴리페모스" in selected_step:
  st.markdown(
      "<h4 style='font-size: 1.25rem; font-weight: bold;'>👁️ 사이클롭스"
      " 폴리페모스와 실책 (Year 1 ~ 2)</h4>",
      unsafe_allow_html=True,
  )
  st.write(
      "'아무도 아니다(Outis)'라는 고도의 재치로 거인의 굴을 빠져나오는 데"
      " 성공했으나, 배에 오른 후 자신의 탁월한 지혜를 과시하고 싶은"
      " 자만심을 참지 못하고 굳이 진짜 이름을 밝히는 치명적인 실책을"
      " 범합니다. 이 '지혜로 인한 자만'은 결국 바다의 신 포세이돈의 무서운"
      " 저주를 불러오는 결정적 계기가 됩니다."
  )
  with st.expander("원문 구절 및 인문학적 성찰 보기"):
    st.info(
        "“만약 누군가 너에게 눈이 멀게 된 이유를 묻거든, 라에르테스의 아들"
        " 오디세우스가 그랬다고 말하라!”"
    )

elif "세이렌" in selected_step:
  st.markdown(
      "<h4 style='font-size: 1.25rem; font-weight: bold;'>🧜‍♀️ 세이렌의 유혹과"
      " 자발적 결박</h4>",
      unsafe_allow_html=True,
  )
  st.write(
      " 밀랍으로 막고 자신은 돛대에 묶인 채 그 노래를 온전히 품에 안습니다."
      " 지혜로운 자로서 세상의 모든 지식을 알고자 했던 순수한 호기심이었으나,"
      " 막상 그 치명적인 유혹의 소리를 직접 들은 뒤에는 영혼을 갉아먹는 듯한"
      " 극심한 후회와 심리적 반작용에 시달리게 됩니다. 지혜를 시험하려던"
      " 오만은 결국 지혜로 인해 감당해야 하는 내면의 상처로 돌아옵니다."
  )
  with st.expander("원문 구절 및 인문학적 성찰 보기"):
    st.info(
        "“나를 돛대에 더 세게 묶어라. 내 지혜조차 유혹 앞에서는 한갓 무력한"
        " 욕망에 불과할지니.”"
    )

elif "스킬라" in selected_step:
  st.markdown(
      "<h4 style='font-size: 1.25rem; font-weight: bold;'>🐙 스킬라와"
      " 카리브디스: 차악(次惡)의 선택</h4>",
      unsafe_allow_html=True,
  )
  st.write(
      "머리 여섯 개 괴물 스킬라를 지나야 한다는 사실을 알면서도, 오디세우스는"
      " 공포로 인해 부하들이 아예 노를 놓아버릴까 두려워 미리 알리지"
      " 않습니다. 결국 동료들은 영문도 모른 채 괴물의 먹이가 되어 죽어간"
      " 뒤에야 '지도자가 이 사실을 처음부터 알고 있었다'는 진실을 깨닫고"
      " 참담한 배신감에 휩싸입니다. 이 비정한 선택과 부하들의 원망은"
      " 오디세우스의 가슴에 평생 지워지지 않을 무거운 죄책감의 낙인을"
      " 더해줍니다."
  )
  with st.expander("원문 구절 및 인문학적 성찰 보기"):
    st.info(
        "“그들은 죽음의 문턱에서야 내가 모든 것을 알고도 침묵했음을"
        " 깨달았고, 그 원망 어린 눈빛은 괴물의 이빨보다 내 심장을 더 깊이"
        " 찔렀다.”"
    )

elif "금기" in selected_step:
  st.markdown(
      "<h4 style='font-size: 1.25rem; font-weight: bold;'>🐂 트리나키아 섬:"
      " 금기를 깨뜨린 오만과 부하들의 종말</h4>",
      unsafe_allow_html=True,
  )
  st.write(
      "태양신 헬리오스의 가축에 손대지 말라는 거듭된 경고에도 불구하고,"
      " 굶주림에 한계에 다란 부하들은 지도자가 잠든 사이 신성한 금기를"
      " 범합니다. 신의 진노를 부를 것을 알면서도 막지 못한 리더십의 공백과"
      " 부하들의 경솔함은 결국 제우스의 벼락을 불러와 배를 산산조각 냈고,"
      " 오디세우스를 제외한 모든 동료는 바다에 수장됩니다. 홀로 살아남았다는"
      " 사실 그 자체가 영웅에게는 평생을 짓누르는 가장 가혹한 형벌이자"
      " 지옥이 됩니다."  )
  with st.expander("원문 구절 및 인문학적 성찰 보기"):
    st.info(
        "“나 홀로 살아남아 파도 밀려오는 해변에 앉았을 때, 모든 동료를 잃은"
        " 그 침묵의 바다는 어떤 승리보다도 잔인한 고독이었다.”"
    )

elif "칼립소" in selected_step:
  st.markdown(
      "<h4 style='font-size: 1.25rem; font-weight: bold;'>🌴 오기기아, 칼립소의"
      " 섬과 7년의 억류 (Year 17)</h4>",
      unsafe_allow_html=True,
  )
  st.write(
      "모든 동료와 배를 잃고 표류하다 다다른 오기기아 섬. 여신 칼립소는"
      " 영생과 절대적인 안락을 약속하며 7년이라는 세월 동안 그의 발을"
      " 묶어둡니다. 그러나 이 오랜 시간은 단순한 유혹을 넘어, 거친 시련에"
      " 지친 영웅이 현실의 책임과 상처로부터 도피하여 스스로를 방치했던"
      " '영혼의 유예 기간'이었습니다. 가장 지혜로운 자조차 모든 것을 잃은"
      " 절망 속에서는 안식이라는 환상에 무력하게 침전될 수 있음을"
      " 보여줍니다."
  )
  with st.expander("원문 구절 및 인문학적 성찰 보기"):
    st.info(
        "“여신이 베푼 영원한 젊음과 안락 속에서도, 그의 눈물은 매일 바다를"
        "향해 흘렀다. 안식은 고향을 잃은 자에게는 또 다른 감옥일 뿐이니.”"
    )

elif "이타카" in selected_step:
  st.markdown("“기나긴 고통과 상실의 바다를 건너 마침내 마주한 고향은, 자아를"
        " 완전히 비워내고 티끌처럼 낮아진 자에게만 비로소 문을"
        " 열어주었다.”"
      "<h4 style='font-size: 1.25rem; font-weight: bold;'>🏹 이타카 귀환과"
      " 정의의 심판 (Year 20)</h4>",
      unsafe_allow_html=True,
  )
  st.write(
      "출정 후 20년, 방황을 시작한 지 10년 만에 마침내 마주한 고향 이타카."
      " 그러나 그는 화려한 영웅의 모습이 아니라 모든 것을 바다에 빼앗긴"
      " 초라한 이방인의 모습으로 돌아옵니다. 거친 20년의 세월 동안 지혜라는"
      " 이름의 오만과 기지를 온전히 비워내고, 비로소 겸손과 인내를 체득한"
      " 자만이 가정을 좀먹던 구태의 질서를 바로 세우고 진정한 안식에"
      " 도달할 수 있음을 보여주는 대장정의 종착점입니다."
  )
  with st.expander("원문 구절 및 인문학적 성찰 보기"):
    st.info(
        "“기나긴 고통과 상실의 바다를 건너 마침내 마주한 고향은, 자아를"
        " 완전히 비워내고 티끌처럼 낮아진 자에게만 비로소 문을"
        " 열어주었다.”"
    )