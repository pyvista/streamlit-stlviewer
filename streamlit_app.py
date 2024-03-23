import tempfile
import streamlit as st
import pyvista as pv
from pyvista import examples

pv.start_xvfb()

uploaded_file = st.file_uploader("Upload a STL:", ["stl"], False)
st.sidebar.title("STL viewer")

if uploaded_file:
    with tempfile.NamedTemporaryFile(suffix=".stl") as fp:
        fp.write(uploaded_file.getbuffer())
        reader = pv.STLReader(fp.name)
        dataset = reader.read()
else:
    dataset = examples.download_bunny()

color = st.sidebar.color_picker("Pick A Color", "#00f900")
plotter = pv.Plotter(window_size=[580, 400])
plotter.background_color = "white"
plotter.add_mesh(dataset, color=color)

with tempfile.NamedTemporaryFile(suffix=".html") as fp:
    other = plotter.export_html(fp.name, backend="pythreejs")
    with open(fp.name, "r") as f:
        model = f.read()
        st.components.v1.html(model, height=600, width=600)
