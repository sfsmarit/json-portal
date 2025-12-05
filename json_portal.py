import streamlit as st
import json

import config
from components import json_editor


def render_segment(segm: dict):
    values = list(segm.values())

    if isinstance(values[0], str):
        for name, url in segm.items():
            st.markdown(f'{name} <a href="{url}">:material/link:</a>', unsafe_allow_html=True)
    else:
        cols = st.columns(len(segm))
        for col, (col_name, urls) in zip(cols, segm.items()):
            with col:
                st.markdown(col_name)
                for name, url in urls.items():
                    st.markdown(f'{name} <a href="{url}">:material/link:</a>', unsafe_allow_html=True)


if __name__ == "__main__":
    with open(config.SOURCE_FILE, encoding="utf-8") as f:
        data = json.load(f)

    page_title = data["Title"]
    st.set_page_config(page_title=page_title, layout="wide")
    st.title(page_title)

    for key, block in data.items():
        if key not in ["Portal", "Table"]:
            continue

        for title, segm in block.items():
            st.markdown("---")
            st.markdown(title)

            if key == "Portal":
                render_segment(segm)
            elif key == "Table":
                st.table(segm)

    st.markdown("---")

    st.markdown("### Page Editor")
    json_editor.render(config.SOURCE_FILE)
