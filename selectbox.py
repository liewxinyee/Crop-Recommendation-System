import streamlit as st

class SelectBox:

    def __init__(self):
        self.apps = []

    def run(select):
        app = st.sidebar.selectbox(
            'Please select an algorithm',
            select.apps,
            format_func=lambda app: app['title'])

        app['function']()

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

class SelectMode:

    def __init__(self):
        self.apps = []

    def run(select):
        app = st.selectbox(
            'Please select a mode',
            select.apps,
            format_func=lambda app: app['title'])

        app['function']()

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })

class SelectCrop:

    def __init__(self):
        self.apps = []

    def run(select):
        app = st.sidebar.selectbox(
            'Please select a crop',
            select.apps,
            format_func=lambda app: app['title'])

        app['function']()

    def add_app(self, title, func):
        self.apps.append({
            "title": title,
            "function": func
        })