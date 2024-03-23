import streamlit as st
import pyvista as pv
from pyvista import examples

pv.set_jupyter_backend('pythreejs')

uploaded_file = st.file_uploader("Upload a STL:",["stl"],False)

st.sidebar.title("STL viewer")

if uploaded_file:
    color = st.sidebar.selectbox("Pick a color:",["white","green","blue"])
    stlTemp = "./temp.stl"
    with open(stlTemp, "wb") as f: 
        f.write(uploaded_file.getbuffer())
    reader = pv.STLReader(stlTemp)
    plotter = pv.Plotter(
        border=True,
        window_size=[580,400]) 
    plotter.background_color = "white"
    mesh = reader.read()
    plotter.add_mesh(mesh, color=color)
    model_html = "model.html"
    other = plotter.export_html(model_html, backend='pythreejs')
    with open(model_html,'r') as file: 
        model = file.read()
    st.components.v1.html(model,height=600, width=600)
