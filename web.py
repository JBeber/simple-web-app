
# import streamlit.components.v1 as components
import streamlit as st
from functions import *

mod_time, item_lst = read_list()

def add_todo():
    item = st.session_state.input
    mod_time = add_item(item_lst, item)
    write_list(mod_time, item_lst)
    st.session_state['input'] = ''  # reset the input text field
    # js_counter()

# def js_counter():
#     st.session_state['counter'] += 1

st.title("Simple To-do App")
st.subheader('Web interface for a basic to-do list')
st.write(f'Last modified on {mod_time}')

for index, item in enumerate(item_lst):
    cb = st.checkbox(label=item, key=item)
    if cb:
        mod_time = remove_item(item_lst, index)
        write_list(mod_time, item_lst)
        del st.session_state[item]

        ''' streamlit recommends not using the 'rerun'method if a 
            callback fn can be used instead 
        '''
        # TODO: implement callback to replace rerun
        st.rerun()

# if 'counter' not in st.session_state:
#     st.session_state['counter'] = 0

# components.html(
#     f"""
#         <div>hidden container to set input field focus</div>
#         <p></p>
#         <script>
#             var input = window.parent.document.querySelectorAll("input[type=text]");

#             for (var i = 0; i < input.length; ++i) {{
#                 input[i].focus();
#             }}
#         </script>
#     """,
#     height=0, width=0
# )

# Can't use commented code below because we need to call 
# more than one function when user enters text.
# Will use a new function instead

# Initialize the 'add_item' key:value pair on first run
# if 'add_item' not in st.session_state:
#     st.session_state.add_item = ''
#     # alternate syntax
#     # st.session_state['add_item'] = ''

# st.text_input(label='', placeholder='Add a new to-do...',
#               key='add_item',
#               on_change=add_item,
#               args=(item_lst, st.session_state['add_item']))

st.text_input(label='Default label', placeholder='Add a new to-do...',
              key='input', on_change=add_todo,
              label_visibility='collapsed')

# prints the 'session_state' object to the webpage for development purposes
# st.session_state