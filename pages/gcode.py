import streamlit as st
from gcodes import *
import matplotlib.pyplot as plt
import numpy as np

#GUI:
# xmin xmax ymin ymax inputs
# Pattern
# angle
# Gcode
# Plot

col1,col2=st.columns(2)

def on_load():
    st.session_state.refresh=True
    
if 'refresh' not in st.session_state:
    st.session_state.refresh=False
    
if 'points' not in st.session_state:
    st.session_state.points=np.array([])
    
if 'gcode' not in st.session_state:
    st.session_state.gcode=''

with col1:
    st.write('Pattern selection:')
    pattern=st.selectbox('Pattern',kPatterns,key='pattern')
    xmin=st.number_input('xmin',value=0)
    xmax=st.number_input('xmax',value=100)
    ymin=st.number_input('ymin',value=0)
    ymax=st.number_input('ymax',value=100)
    angle=st.number_input('angle')
    st.button('Load',on_click=on_load)    
    
with col2:
    selectedPattern=st.session_state['pattern']
    if st.session_state.refresh:
        points=createPattern(pattern=selectedPattern,xmin=xmin,xmax=xmax,ymin=ymin,ymax=ymax,ang_deg=angle)
        st.session_state.points=points
        st.session_state.gcode=trajectory2gcode(points)
        st.session_state.refresh=False
    if len(st.session_state.points)>0:
        fig, ax = plt.subplots()
        points=st.session_state.points
        gcode=st.session_state.gcode
        ax.plot(points[:,0],points[:,1])
        st.pyplot(fig)
        st.text_area('Gcode',gcode,height=400)
