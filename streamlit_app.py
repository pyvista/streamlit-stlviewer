import tempfile
import streamlit as st
import pyvista as pv
from pyvista import examples


st.sidebar.title("STL viewer")

uploaded_file = st.file_uploader("Upload a STL:", ["stl"], False)
if uploaded_file:
    with tempfile.NamedTemporaryFile(suffix=".stl") as fp:
        fp.write(uploaded_file.getbuffer())
        reader = pv.STLReader(fp.name)
        mesh = reader.read()
else:
    mesh = examples.download_bunny()

color = st.sidebar.color_picker("Pick A Color", "#00f900")
plotter = pv.Plotter(window_size=[800, 400])
plotter.background_color = "white"
plotter.add_mesh(mesh, color=color)

with tempfile.NamedTemporaryFile(suffix=".html") as fp:
    other = plotter.export_html(fp.name, backend="pythreejs")
    with open(fp.name, "r") as f:
        model = f.read()
        st.components.v1.html(model, height=600, width=600)
