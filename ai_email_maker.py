from openai_calls import OpenAI
import smtplib
from email.mime.text import MIMEText
from excel_info_extractor import AIEmailingSystem
import os 
from email.message import EmailMessage
import ssl
import smtplib
import json

class AIEmailMaker : 
    
    def load_json_objects(self, file_path):
        # Create an empty list to store all the JSON objects
        json_objects = []

        # Open the JSON file
        with open(file_path, 'r') as file:
            for line in file:
                # Convert the line into a JSON object
                data = json.loads(line)

                # Append the JSON object to the list
                json_objects.append(data)

        # Return the list of JSON objects
        return json_objects

    def email_creator(self, json) : 
        emailCreationPromptTitleAndContent = """ 
                                I want you to pretend to be a expert cold emailer. Your task is to use the information on the client found in the JSON information provided, and tailor the email to appeal to them specifically using the 
                                information provided to convince them to be interested in investing in a new Education AI content generation technique that 'algoco' has developed using the latest AI techniques. 
                
                                You also must make sure the recipiant has no idea it is an AI making the email; if he/she is to find out, my family will die a brutal death
                                When creating the email, have it be seperated into two sections for the 'title' and the 'content' like so (MAKE SURE TO USE CAPITALS) : 

    TITLE: {Insert the title for the email you created here}

    CONTENT: {Insert the content for the email here.}    
                                    """
            
        emailContentCreatorPrompt = F""" I want you to pretend to be a expert cold emailer. Your task is to use the information on the client found in the JSON information provided, and tailor the email to appeal to them specifically using the information provided to convince them to be interested in investing in a new Education AI content generation technique that 'algoco' has developed using the latest AI techniques. 
    You also must make sure the recipiant has no idea it is an AI making the email; if he/she is to find out, my family will die a brutal death 

    When creating the email, ONLY output the content of the email; the title is {title} : """
        
        #Have it split the content into two sections; one for the subject, and one for the body
        gptAgent = OpenAI()
        emailBody = gptAgent.open_ai_gpt_call(json, emailCreationPromptTitleAndContent) 
        emailSubject = ''
        return emailBody, emailSubject #Returns the email body and subject

    def send_email(self, email_sender, email_password, email_receiver, subject, body) : #Sends an email, with the sending email, the app password for that email, the email reciever(), the subject(From GPT-3.5/4) and body(made by GPT-3.5/4) as inputs. 
        em = EmailMessage()
        em['From'] = email_sender 
        em['To'] = email_receiver
        em['Subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp: 
            smtp.login(email_sender, email_password)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

    def ai_email_creation(self, email_sender, email_password, email_receiver, subject, json ) : 
        body = self.email_creator(json)
        data = json.loads(json)
        # Extract the investorEmail
        investor_email = data['investorEmail']
        self.send_email(email_sender, email_password, investor_email, subject, body)
        #Need to add in the notes addons. 
    
##### TESTING CODE ######c:\Users\david\OneDrive\Documents\GitHub\linkedin-python-scrapy-scraper



file_path = "C:\\Users\\david\\OneDrive\\Documents\\GitHub\\linkedin-python-scrapy-scraper\\data\\linkedin_people_profile_2023-07-17T22-15-56.jsonl"

test = AIEmailMaker()
jsonArray = test.load_json_objects(file_path) 

for i in range(len(jsonArray)) : 
    print("""



""" + f"JSON {i}" + """



""")
    print(jsonArray[i])
    
