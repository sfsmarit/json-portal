import streamlit as st
import json


def render(file: str):
    with open(file, encoding="utf-8") as f:
        data = json.load(f)

    # JSONを文字列に変換
    json_str = json.dumps(data, indent=4)

    # 編集用テキストエリア
    edited_json_str = st.text_area(file, json_str, height=400)

    # バリデーションと表示
    try:
        parsed_json = json.loads(edited_json_str)
        is_valid = True
    except json.JSONDecodeError:
        st.error("Invalid JSON format")
        is_valid = False

    if is_valid:
        st.button("Save", on_click=save, args=(parsed_json, file))


def save(text, file):
    with open(file, "w", encoding="utf-8") as f:
        json.dump(text, f, ensure_ascii=False, indent=4)
