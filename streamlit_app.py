import streamlit as st
import pyvista as pv
from pyvista import examples

## Using pythreejs as pyvista backend
pv.set_jupyter_backend('pythreejs')

## Download an stl file
# filename = examples.download_cad_model(load=False)
uploadedFile = st.file_uploader("Upload a STL:",["stl"],False)

## Streamlit layout
st.sidebar.title("STL viewer")

if uploadedFile:
    
    stlTemp = "./temp.stl"
    with open(stlTemp, "wb") as f: 
        f.write(uploadedFile.getbuffer())

    color = st.sidebar.selectbox("Pick a color:",["white","green","blue"])

    ## Initialize pyvista reader and plotter
    reader = pv.STLReader(stlTemp)
    plotter = pv.Plotter(
        border=True,
        window_size=[580,400]) 
    plotter.background_color = "white"

    ## Read data and send to plotter
    mesh = reader.read()
    plotter.add_mesh(mesh,color=color)

    ## Export to an external pythreejs
    model_html = "model.html"
    other = plotter.export_html(model_html, backend='pythreejs')

    ## Read the exported model
    with open(model_html,'r') as file: 
        model = file.read()

    ## Show in webpage
    st.components.v1.html(model,height=600, width=600)
