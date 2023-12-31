import streamlit as st
import pandas as pd
import pickle




page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] > .main {{
  background-color: #d0d0d0;
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load the model from the pickle file
with open("model_xgb_1.pkl", "rb") as f:
    model = pickle.load(f)

def upload_csv_file():
    st.markdown("""
    **:blue[Do upload the csv file to get to know if a website is phishing or not.]**
    """)
    uploaded_file = st.file_uploader("")
    if uploaded_file is not None:
        df = pd.read_csv(uploaded_file)
        return df

def predict(df):
    predictions = model.predict(df)
    return predictions

def main():
    # Set the title color to red
    st.title(':red[Phishing Website detector] :male-detective:')


    st.markdown("""
    **:blue[This app uses a machine learning model to detect phishing websites.]**
    """)
    st.divider()
    df = upload_csv_file()
    if df is not None:
        predictions = predict(df)
        st.markdown("## :blue[Predictions:]")
        #st.write(predictions)
        for i in predictions:
            if i == 0:
                st.write("### :red[Phishing] :sleuth_or_spy:")
            else:
                st.markdown("### :blue[Good Website] :ok:")

if __name__ == "__main__":
    main()


