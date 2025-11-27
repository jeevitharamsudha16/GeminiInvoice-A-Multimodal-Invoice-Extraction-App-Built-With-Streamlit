#🧾 **AI-Based Invoice Extraction System — Project Report**
**1. Introduction**

The AI Invoice Extraction System is an advanced application designed to extract structured information from invoice images using Google Gemini 2.5 Flash (Vision Model).
This system automates the traditionally manual process of reading and interpreting invoices, enabling faster and more accurate data extraction.

**2. Objective**

The main objectives of this project are:
- To automate invoice interpretation and data extraction
- To convert unstructured invoice images into structured digital text
- To minimize manual effort in financial document processing
- To provide clear and readable structured output (Markdown format)
- To use AI to identify key invoice components accurately

**3. Technologies Used**

**Programming Language:** Python
**Web Framework :** 	Streamlit
**AI Model	:** Google Gemini 2.5 Flash
**Image Processing :** 	Pillow (PIL)
**Environment Variables :** 	python-dotenv

**4. System Architecture**
User Uploads Invoice Image
        ↓
Streamlit UI receives image
        ↓
Image converted into binary format
        ↓
Sent to Google Gemini Vision Model
        ↓
AI extracts structured invoice details
        ↓
Results displayed cleanly in Markdown

**5. Features**
✔ Automated Invoice Field Extraction

**Extracts:**

Invoice Number

Invoice Date

Due Date

Vendor (Seller) Details

Customer Details

Contact Information

**Tax Details**

Subtotal, Tax, Total

✔ Line Items Table Extraction

The system identifies:

Item Description

Quantity

Unit Price

Item Total

**✔ General Invoice Understanding**

Identifies:

Invoice Type

Notes or Terms

Logos / Company Identifiers

✔ Readable Output

Clean Markdown format

Clear section headers

Organized tables

**6. Workflow**

User uploads a JPG/PNG invoice

Streamlit displays preview

Image is processed into model-readable format

Gemini Vision analyzes and extracts text + structure

The system formats and displays the extracted details

**7. Prompt Used for Extraction**

A custom-designed structured prompt ensures:

Accurate extraction

Stable field detection

Clean Markdown output

No hallucinated details

**8. Results**

The system produces:

Invoice Summary

Vendor Details

Customer Details

Line Items Table

Totals Section

Additional Notes

Output is always clean, readable, and highly structured.

**9. Conclusion**

The AI-powered Invoice Extraction System successfully automates the process of reading and interpreting invoices.
It delivers high accuracy, structured outputs, and saves significant time in financial workflows.

**This system can be extended into:**

Full OCR-based invoice automation

PDF invoice processing

Multi-invoice batch processing

Export to Excel/CSV/Database
