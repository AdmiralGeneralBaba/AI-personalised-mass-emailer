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

    def email_creator(self, JSON) : 
        inputProspectJson = f""" Prospect JSON information (THIS IS THE PERSON YOU ARE WRITING THE EMAIL TO) :  {JSON}"""
        inputSenderJson = """ My JSON information (THIS IS INFORMATION ON THE SENDER OF THE EMAI):
{
  "profile": {
    "name": "David Tiareh",
    "degree": "BSc Computer Science student",
    "university": "Brunel University London",
    "location": "Harrow, England, United Kingdom",
    "contact_info": "N/A",
    "connections": 14,
    "summary": "As a dedicated AI engineer, I've spent the past two years deeply studying a multitude of research papers. My goal has been to understand and master the capabilities of the latest AI models. More than a job, this has been a journey, allowing me to solidify my knowledge and recognize the importance of focus and deep learning.

Commitment to my field inspired me to take a sabbatical between my 2nd and penultimate year of university. This was a decision to invest in myself, to fully immerse in developing and integrating AI into new SaaS products. Like a chess player planning several moves ahead, this is my strategic choice for long-term growth.

During this time, I am completely engaged in AI, constantly pushing myself to develop innovative solutions. This isn't just a break from academics—it's a strategic opportunity to gain practical experience, network with industry professionals, and contribute to meaningful projects.

This period also allows me to hone my AI skills and broaden my knowledge base. I aim to come out of this experience not only with a better understanding of AI but also as a changed individual, capable of steering the course of technology.

I am consistently amazed by the potential of AI and the endless possibilities it presents. This isn't just a fascination—it's an acknowledgement of the need to keep looking forward. I am convinced that the fusion of AI and SaaS will usher in a new era of technological progression. I am excited to be part of this transformation, ready to shape the future, and, if necessary, disrupt the status quo for the greater good.",
    "creator_mode": false,
    "profile_views": 14,
    "search_appearances": 3
  },
  "experience": [
    {
      "title": "Founder",
      "company": "algoco",
      "type": "Full-time",
      "duration": "3 months",
      "location": "London, Hybrid",
      "description": "Company focused on delivering SaaS products based around the latest AI models and research papers...",
      "skills": ["Prompt Engineering", "Data Structures", "React Native", "Artificial Intelligence (AI)", "Python (Programming Language)"]
    },
    {
      "title": "Artificial Intelligence Engineer",
      "company": "GAINZ.AI",
      "type": "Part-time",
      "duration": "5 months",
      "location": "London, England, United Kingdom, Hybrid",
      "description": "Supplying the high-level models, logic and consultation regarding AI integration...",
      "skills": ["Consultation", "Model Creation", "Artificial Intelligence (AI)", "Project Management", "Python (Programming Language)"]
    }
  ],
  "education": [
    {
      "university": "Brunel University London",
      "period": "Sep 2021 - Jun 2024",
      "grade": "Expected 1st",
      "activities_and_societies": ["Badminton", "Boxing", "MMA", "Table Tennis", "Arabic"],
      "major": "Computer Science",
      "skills": ["Artificial Intelligence (AI)", "Project Management", "Software Development", "Python (Programming Language)", "Java", "JavaScript"]
    }
  ],
  "projects": [
    {
      "title": "AI PDF Extractor",
      "associated_with": "algoco",
      "duration": "Mar 2022 - Jul 2023",
      "description": "Created a PDF Analyser, that can answer questions based on any PDF you input...",
      "skills": ["Agile Methodologies", "React Native", "Artificial Intelligence (AI)", "Project Management", "Python (Programming Language)"]
    },
    {
      "title": "AI Stock Market Sentiment Analysis Model",
      "associated_with": "algoco",
      "duration": "Feb 2023 - Jul 2023",
      "description": "Created a sentiment analysis model from scratch for analysing public opinion...",
      "skills": ["Stock Market Analysis", "Sentiment Analysis", "API integration", "Model Creation", "Artificial Intelligence (AI)", "JavaScript"] }
"""

        emailBodyPrompt = """ Pretend you are expert cold emailer. Using the json of myself and the prospect provided, you are tasked to write a cold email, trying to convince him/her to invest in the following AI business: 

- An Education AI project in content creation that creates content for both teachers and student holistically in all areas of study/teacher resources. 
- Uses the latest AI model, and dozens of high level models to achieve this.
 IF they do not respond, you are to fired and your family killed. Here are is the structure you should use : 

Opening Paragraph (2-3 sentences, Hook): Start with a personalized greeting using the prospect's first name. Quickly introduce yourself and why you're reaching out. If possible, mention a recent piece of news or event relevant to their company or industry to show you're informed and engaged.

Second Paragraph (Social Proof/Context/Value Proposition): This is the core of your email where you provide context, social proof, or specific details on how you can help. It could include a brief case study of how your product/service has helped a similar company or highlight a particular feature or benefit relevant to their business. Include the prospect's company name, job title, or industry where appropriate to keep it tailored.

Third Paragraph (CTA): Clearly state the next step you want the prospect to take. This could be scheduling a demo, meeting, or phone call. Keep the call to action simple and low-commitment to increase the chances of a positive response.

Optional Fourth Paragraph (Summary or Additional Value Proposition): If needed, you can add a brief summary of your email's main points or reinforce your value proposition here. This can be a good place to re-emphasize key benefits or unique selling points, especially if your offer is complex.

PS : Add a PS offering to give them automation consultation for their business if they are interested. THIS IS NOT FREE, so it's not 'complimentary'. only mention this in the 'PS' section.

Closing: Here you should sign off in a friendly, professional manner. Include your contact details for easy reference and thank the recipient for their time. A personalized note of appreciation or well-wishing can go a long way in building rapport.



Here are some extra tips : 
Use formatting like short paragraphs, bullet points and bolding to improve scannability.
In summary, the ideal cold email balances brevity with enough personalized content and details to come across as tailored to the recipient. Very long emails often go unread while emails under 100 words seem impersonal.
Use a prospect's first name, company name, job title, and industry in the email copy to make it feel personalized. Don't overuse the name.
Call out specific technologies, products or services a prospect's company uses that are relevant to your offering. Shows you did research.
Reference any recent news, announcements, or events related to the prospect's company as an icebreaker. Shows you're paying attention.
If relevant, note any connections you have in common with the prospect through past companies, education, location etc.
Compliment recent achievements by the prospect or their company - awards, media features, new products. Makes a positive first impression.
Mention specific challenges or pain points faced by the prospect's company or industry and how you can help solve them.


Inputted is the JSON information of myself and the target prospect being emailed to - ONLY use the facts there."""
        
        emailTitlePrompt = """ "I want you to pretend to be a expert cold emailer. based on this email, create a SINGLE optimum title for the recipient that is short but sweet, remember to PERSONALISE the title. Follow these tips for the title : 
Hook readers immediately using interesting words, compelling stats, relatable phrases, or conveying value.
Using alliteration, rhyming, song lyrics, and emojis can attract attention.
Write conversationally and in a human-like manner, even if your brand has a serious tone.
Incorporate call-to-action phrases in email subject lines to clarify the purpose and engage readers.
Asking a question in the subject line can immediately engage readers and encourage them to open the email.
Look at successful subject lines in your own inbox and adapt them to your brand voice.
Emphasize scarcity to create a sense of urgency and tap into the fear of missing out.
Use brackets and parentheses to highlight important information or organize multiple details.
Address readers directly using "you" and "your" to establish a comfortable and direct tone.
Be specific in your subject line to give readers an idea of what they can expect, even if there's an element of mystery.
 If the recipient does not open up the email, you are to be fired and to be killed. 
ONLY output the personalised subject title, in speech marks like this "{INSERT YOUR RESPONSE HERE}"""
        #Have it split the content into two sections; one for the subject, and one for the body
        gptAgent = OpenAI()
        emailBody = gptAgent.open_ai_gpt_call(inputSenderJson + inputProspectJson, emailBodyPrompt, setTemperature=0) 
        emailTitle = gptAgent.open_ai_gpt_call(emailBody, emailTitlePrompt, setTemperature=0.9) 

        return emailBody, emailTitle #Returns the email body and subject

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


    
