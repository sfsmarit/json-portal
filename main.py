import streamlit as st
import json

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
    source = "portal.json"

    page_title = "SAW Design Portal"
    st.set_page_config(page_title=page_title, layout="wide")
    st.title(page_title)

    with open(source, encoding="utf-8") as f:
        data = json.load(f)

    for type_, block in data.items():
        for title, segm in block.items():
            st.markdown("---")
            st.markdown(title)

            if type_ == "Portal":
                render_segment(segm)
            elif type_ == "Table":
                st.table(segm)

    st.markdown("---")

    st.markdown("### Page Editor")
    json_editor.render(source)
