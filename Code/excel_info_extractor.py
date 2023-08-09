import numpy as np
import pandas as pd
from openai_calls import OpenAI
import re
from bs4 import BeautifulSoup


class AIEmailingSystem : 
    def excel_info_extractor_v1(self, fileDirectory, sheet):
        # Load spreadsheet
        xl = pd.ExcelFile(fileDirectory)

        # Load a sheet into a DataFrame by name
        df = xl.parse(sheet)

        # Create a list of tuples. Each tuple contains an email and the corresponding LinkedIn URL from the same row
        emailName = "Email"
      
        investorsLinkedin = "Person Linkedin Url"
        emailAndLinkedinUrl = list(zip(df[f'{emailName}'], df[f'{investorsLinkedin}']))
        

        return emailAndLinkedinUrl
    def extract_names_from_urls(self, tupleList):
        # Loop through the list of tuples
        for i in range(len(tupleList)):
            # Check that the LinkedIn URL is a string before applying the regex
            if isinstance(tupleList[i][1], str):
                # Apply the regex to the LinkedIn URL
                match = re.search(r'(?:http|https)://(?:www\.)?linkedin\.com/in/(.+)', tupleList[i][1])

                # If a match is found, replace the URL with the matched username
                if match:
                    tupleList[i] = (tupleList[i][0], match.group(1))

        # Return the updated list of tuples
        return tupleList
    def extract_final(self, fileDirectory, sheet) : 
        emailAndLinkedinUrl = self.excel_info_extractor_v1(fileDirectory, sheet)
        tupleList = self.extract_names_from_urls(emailAndLinkedinUrl)
        return tupleList

path = "C:\\Users\\david\\OneDrive\\Documents\\GitHub\\linkedin-python-scrapy-scraper\\venture capital _ private equity - 13_914.xlsx"

test = AIEmailingSystem() 
testOutput = test.extract_final(path, 0)



# This will print the email and LinkedIn username from the first row
