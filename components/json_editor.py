import streamlit as st
import json


def render(file: str):
    with open(file, encoding="utf-8") as f:
        data = json.load(f)
        json_str = json.dumps(data, indent=4)

    # Filename
    st.write(file)

    # Error message
    if not st.session_state.get("is_valid", True):
        st.error("Invalid JSON format")

    # Button
    button_holder = st.empty()

    # 編集用テキストエリア
    st.text_area("", json_str, key="editor", height=400, label_visibility="collapsed")

    if st.session_state.get("validated", False):
        parsed_json = json.loads(st.session_state["editor"])
        button_holder.button("Save", on_click=save, args=(parsed_json, file))
    else:
        button_holder.button("Validate", on_click=validate)


def validate():
    text = st.session_state["editor"]
    try:
        json.loads(text)
        st.session_state["validated"] = True
        st.session_state["is_valid"] = True
    except json.JSONDecodeError:
        st.session_state["validated"] = False
        st.session_state["is_valid"] = False


def save(text, file):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(text, f, ensure_ascii=False, indent=4)
    st.session_state["validated"] = False
