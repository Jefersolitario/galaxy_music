"""Musica Universalis: galaxies in 3D that move in time with Bach.

The whole experience is one self-contained web page, index.html, drawn with WebGL
in the visitor's browser. This Streamlit app's only job is to serve that page full
screen. All of the rendering and audio runs client-side, so the app needs no data,
no secrets and very little server.
"""

import base64
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).parent

st.set_page_config(
    page_title="Musica Universalis",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed",
)


@st.cache_data(show_spinner=False)
def load_page() -> str:
    """Return index.html with the piano recording embedded in it.

    On its own, index.html fetches prelude.mp3 from the folder it sits in. Inside
    Streamlit the page runs in an iframe with no folder of its own, so the
    recording is inlined as a data URL instead.
    """
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    hook = "url: 'prelude.mp3'"
    if hook not in html:
        raise RuntimeError("index.html no longer contains the recording hook: " + hook)
    audio = base64.b64encode((ROOT / "prelude.mp3").read_bytes()).decode("ascii")
    return html.replace(hook, f"url: 'data:audio/mpeg;base64,{audio}'")


# Strip Streamlit's own chrome and padding and let the page fill the window.
st.markdown(
    """
    <style>
      html, body, .stApp { background: #000003; }
      header[data-testid="stHeader"], [data-testid="stToolbar"],
      [data-testid="stDecoration"], [data-testid="stStatusWidget"], footer { display: none !important; }
      [data-testid="stMainBlockContainer"], .block-container { padding: 0 !important; max-width: none !important; }
      iframe {
        position: fixed; inset: 0;
        width: 100vw !important; height: 100vh !important; height: 100dvh !important;
        border: 0; z-index: 10;
      }
    </style>
    """,
    unsafe_allow_html=True,
)

page = load_page()
if hasattr(st, "iframe"):
    st.iframe(page, height=800)  # the CSS above overrides this with the full window
else:  # Streamlit releases from before st.iframe existed
    import streamlit.components.v1 as components

    components.html(page, height=800)
