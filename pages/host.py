import streamlit as st
from gcodes import *
import matplotlib.pyplot as plt
import numpy as np
import serial.tools.list_ports
import serial
import time

kTimeDelay=4.0

ports = sorted(serial.tools.list_ports.comports())

# Port: [<combo box>]
# Connect [button]

# Command: [text input]
# Send [button]

col1,col2=st.columns(2)

if 'points' not in st.session_state:
    st.session_state.points=np.array([])
if 'gcode' not in st.session_state:
    st.session_state.gcode=''
if 'on_command' not in st.session_state:
    st.session_state.on_command=False
if 'on_load' not in st.session_state:
    st.session_state.on_load=False
if 'on_run' not in st.session_state:
    st.session_state.on_run=False
if 'on_connect' not in st.session_state:
    st.session_state.on_connect=False
if 'port' not in st.session_state:
    st.session_state.port=None



def on_load():
    st.session_state.on_load=True
def on_connect():
    st.session_state.on_connect=True
def on_command():
    st.session_state.on_command=True
def on_disconnect():
    st.session_state.port.close()
    st.session_state.port=None
def on_run():
    st.session_state.on_run=True

def sendgcode(gcode):
    if st.session_state.port!=None:
        serialPort=st.session_state.port
        lines=gcode.split('\n')
        for line in lines:
            cmd=line+'\r\n'
            serialPort.write(cmd.encode())
            time.sleep(kTimeDelay)


    

with col1:
    st.write('Port selection:')
    format_func=lambda port: '{} [{}]'.format(port.name,port.description)
    st.selectbox('Port',ports,format_func=format_func,key='selectedPort')
    
    if st.session_state.port==None:
        st.button('Connect',on_click=on_connect)    
    else:
        st.button('Disconnect',on_click=on_disconnect)    
        
    command=st.text_input('Command:')
    st.button('Send',on_click=on_command)    

    if st.session_state.on_connect:
        #Connect to serial and store port in state
        serialPort = serial.Serial(
            port=st.session_state.selectedPort.name, baudrate=57600,timeout=2
        )
        st.session_state.port=serialPort
        st.session_state.on_connect=False
        st.rerun()
    if st.session_state.on_command and st.session_state.port!=None:
        serialPort=st.session_state.port
        cmd=command+'\r\n'
        serialPort.write(cmd.encode())
        st.session_state.on_command=False
    
with col2:
    st.write('Gcode sender:')
    if st.session_state.gcode!='':
        gcode=st.session_state.gcode
        st.text_area('Gcode',gcode,height=400)
        st.button('Run',on_click=on_run)
    if st.session_state.on_run and st.session_state.gcode!='':
        sendgcode(st.session_state.gcode)
        st.session_state.on_run=False


    