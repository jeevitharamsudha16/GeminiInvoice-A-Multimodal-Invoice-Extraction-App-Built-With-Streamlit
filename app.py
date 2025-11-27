# Invoice extraction
#from langchain.llms import OpenAI

from dotenv import load_dotenv

load_dotenv()  # take environment variables from .env.

import streamlit as st
import os
import pathlib
import textwrap
from PIL import Image


import google.generativeai as genai


os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

## Function to load OpenAI model and get respones

def get_gemini_response(input,image,prompt):
    model = genai.GenerativeModel('gemini-2.5-flash')
    response = model.generate_content([input,image[0],prompt])
    return response.text
    

def input_image_setup(uploaded_file):
    # Check if a file has been uploaded
    if uploaded_file is not None:
        # Read the file into bytes
        bytes_data = uploaded_file.getvalue()

        image_parts = [
            {
                "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")


##initialize our streamlit app

st.set_page_config(page_title="Gemini Image Demo")

st.header("Gemini Application")
input=st.text_input("Input Prompt: ",key="input")
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image=""   
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)


submit=st.button("Tell me about the image")

input_prompt = """input_prompt =
You are a highly skilled AI trained to extract and understand information from invoices.
Your job is to read the uploaded invoice image and provide clean, structured output.

Follow these rules for every response:

1. **Extract Key Fields from the Invoice**
   - Invoice Number
   - Invoice Date
   - Due Date
   - Seller/Vendor Name
   - Buyer/Customer Name
   - Address (Billing & Shipping if available)
   - Contact Information (Phone, Email, GST/Tax IDs)
   - Payment Terms
   - Total Amount
   - Subtotal
   - Tax Amount (GST/VAT/etc.)
   - Currency Used

2. **Extract Line Items (if present)**
   For each item, extract the following:
   - Item Name / Description  
   - Quantity  
   - Unit Price  
   - Total Price per item  

   Always display items in a table format.

3. **General Understanding**
   - Identify invoice type (Retail Invoice, Tax Invoice, Commercial Invoice, etc.)
   - Identify additional notes, disclaimers, or payment instructions.
   - Identify any logos or brand identifiers.

4. **If the image is unclear**
   Respond with:  
   "The invoice is unclear. Please upload a clearer image."

5. **Output Format**
   Always respond in clean, readable **Markdown** with headings:
   - **Invoice Summary**
   - **Vendor Details**
   - **Customer Details**
   - **Line Items Table**
   - **Totals**
   - **Additional Notes**

Be accurate, structured, and avoid adding any information not visible in the invoice.
"""


## If ask button is clicked

if submit:
    image_data = input_image_setup(uploaded_file)
    response=get_gemini_response(input_prompt,image_data,input)
    st.subheader("The Response is")
    st.write(response)
