import streamlit as st
def main():
    """ Deploying Streamlit App2 with Docker"""

    st.title("Streamlit App2")
    st.header("Deploying Streamlit with Docker")


    activities = ["EDA", "Plots","Data", "Prediction"]
    choices = st.selectbox('Select activities',activities)
    if choices == 'EDA':
        st.subheader("EDA")
    elif choices == 'Plots':
        st.subheader("Visualization")
    elif choices == 'Data':
        st.subheader("Data Exploration")
    elif choices == 'Prediction':
        st.subheader("Predict Specie")



if __name__ == '__main__':
    main()