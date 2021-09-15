%%writefile app.py
 
import pickle
import streamlit as st
 
# loading the trained model
import joblib
classifier = joblib.load('modelJoblib')
 
@st.cache()
  
# defining the function which will make the prediction using the data which the user inputs 
def prediction(retailer_id, product_id, regular_price, quantity, limited):   
 
    # Making predictions 
    prediction = classifier.predict( 
        [[retailer_id, product_id, regular_price, quantity, limited]])
     
    return prediction
      
  
# this is the main function in which we define our webpage  
def main():       
    # front end elements of the web page 
    html_temp = """ 
    <div style ="background-color:yellow;padding:13px"> 
    <h1 style ="color:black;text-align:center;">Streamlit Down Price Prediction App</h1> 
    </div> 
    """
      
    # display the front end aspect
    st.markdown(html_temp, unsafe_allow_html = True) 
      
    # following lines create boxes in which user can enter data required to make prediction 
    #Gender = st.selectbox('Gender',("Male","Female"))
   # Married = st.selectbox('Marital Status',("Unmarried","Married")) 
    #ApplicantIncome = st.number_input("Applicants monthly income") 
    retailer_id = st.number_input('retailer_id')
    product_id = st.number_input('product_id')
    regular_price = st.number_input('regular_price')
    quantity = st.number_input('quantity')
    limited = st.number_input('limited')

    #Credit_History = st.selectbox('Credit_History',("Unclear Debts","No Unclear Debts"))
    result =""
      
    # when 'Predict' is clicked, make the prediction and store it 
    if st.button("Predict offer_price"): 
        result = prediction(retailer_id, product_id, regular_price, quantity, limited) 
        st.success('Your offer_price is {}'.format(result))
        print(LoanAmount)
if __name__=='__main__': 
    main()
