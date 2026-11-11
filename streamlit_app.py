"""Musica Universalis: galaxies in 3D that move with the music.

The whole experience is one self-contained web page, index.html, drawn with WebGL
in the visitor's browser. This Streamlit app's only job is to serve that page full
screen. All of the rendering and audio runs client-side, so the app needs no data,
no secrets and very little server.
"""

import base64
from pathlib import Path

import streamlit as st

ROOT = Path(__file__).parent

# A second address for the Vivaldi recording, tried if Streamlit's static file
# server cannot be reached from inside the page. Change it if you fork the repo.
RAW = "https://raw.githubusercontent.com/Jefersolitario/galaxy_music/main/"

st.set_page_config(
    page_title="Musica Universalis",
    page_icon="🌌",
    layout="wide",
    initial_sidebar_state="collapsed",
)


def swap(html: str, hook: str, new: str) -> str:
    """Replace one of the page's recording addresses, failing loudly if it has moved."""
    if html.count(hook) != 1:
        raise RuntimeError("index.html no longer contains the recording hook: " + hook)
    return html.replace(hook, new)


@st.cache_data(show_spinner=False)
def load_page() -> str:
    """Return index.html with its recordings pointed at places this app can serve.

    On its own, index.html fetches its recordings from the folder it sits in. Inside
    Streamlit the page runs in an iframe with no folder of its own, so:

    - the Bach recording, which plays first, is embedded in the page as a data URL;
    - the Vivaldi recording is fetched only when the visitor chooses it, from
      Streamlit's static file server (see .streamlit/config.toml), or failing that
      from the copy in the GitHub repository.
    """
    html = (ROOT / "index.html").read_text(encoding="utf-8")
    bach = base64.b64encode((ROOT / "prelude.mp3").read_bytes()).decode("ascii")
    html = swap(html, "url: 'prelude.mp3'", f"url: 'data:audio/mpeg;base64,{bach}'")
    vivaldi = "static/summer-presto.mp3"
    html = swap(html, f"url: '{vivaldi}'", f"url: ['app/{vivaldi}', '{RAW}{vivaldi}']")
    return html


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
