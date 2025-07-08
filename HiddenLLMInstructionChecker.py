'''   

HiddenLLMInstructionChecker.py

Author: Satya Allamraju
Date: July 8, 2025

Description:
              Check for any hidden instructions in documents which will impact the LLM based Automation Tasks...
              

Ver 0.1   -   Currently supports PDF and reports any text whose font size < 0.1
              Note: This is just a work-in-process and not a good indicator for hiddent prompts.
              
'''

import sys
from PyPDF2 import PdfReader

results = dict()
curr_page = -1000

def visitor_body(text, cm, tm, fontDict, fontSize):
     # Courtesy: PyPDF2 docs
     
     if fontSize < 0.1: 
           print(fontSize)
           results[curr_page]    =  text
           
 
if __name__ == "__main__":
    if len(sys.argv) < 2:
         print("Please supply .pdf file to be analyzed for hidden prompts ....")
         sys.exit(1)
        
    reader = PdfReader(sys.argv[1])
               
    for page_number, page in enumerate(reader.pages):
           curr_page = page_number
           _ = page.extract_text(visitor_text=visitor_body)
        
    if len(results) > 0:
        print('-'*50)
        print('Possible hidden LLM prompts noticed as below')
        print('-'*50)
 
        
        for key, value in results.items():
            print(f'Page: {key} - Text: {value}')
            
    else:
            print('No  hidden LLM prompts noticed - may need further checks...')
     
    pass
    