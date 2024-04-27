import tempfile
import streamlit as st
import pyvista as pv
from pyvista import examples


st.sidebar.title("STL viewer")

uploaded_file = st.file_uploader("Upload a STL:", ["stl"], False)
if uploaded_file:
    reader = pv.STLReader(uploaded_file.name)
    mesh = reader.read()
else:
    mesh = examples.download_bunny()

plotter = pv.Plotter(window_size=[800, 600])
plotter.background_color = st.sidebar.color_picker(
    "Background color of this renderer.", "#000000"
)
plotter.add_mesh(
    mesh,
    color=st.sidebar.color_picker(
        "Use to make the entire mesh have a single solid color.", "#00f900"
    ),
)

with tempfile.NamedTemporaryFile(suffix=".html") as fp:
    other = plotter.export_html(fp.name, backend="pythreejs")
    with open(fp.name, "r") as f:
        model = f.read()
        st.components.v1.html(model, width=800, height=600)
