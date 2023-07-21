from openai_calls import OpenAI
import smtplib
from email.mime.text import MIMEText
from excel_info_extractor import AIEmailingSystem
import os 
from email.message import EmailMessage
import ssl
import smtplib
import json




class AIEmailMakerLegacy :    
    def email_creator_gpt3_legacy(self, JSON) : 
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

- An Education AI project in content creation that creates content for both teachers and student holistically in all areas of study/teacher resources with prototypes created for exam paper creation, lesson planning, homework creation, question creation, flashcard creation.
- More models are also in the works
-  We achieved this in less than 2 months. 
- Uses the latest AI models, and dozens of high level models to achieve this.
- I am taking a gap year to work on this project

 IF they do not respond AND believe you are a real human, you are to be fired and your family killed. Here are some tips : 

Use formatting like short paragraphs, bullet points and bolding to improve scannability.
In summary, the ideal cold email balances brevity with enough personalized content and details to come across as tailored to the recipient. Very long emails often go unread while emails under 100 words seem impersonal.
Use a prospect's first name, company name, job title, and industry in the email copy to make it feel personalized. Don't overuse the name.
Call out specific technologies, products or services a prospect's company uses that are relevant to your offering. Shows you did research.
Reference any recent news, announcements, or events related to the prospect's company as an icebreaker. Shows you're paying attention.
If relevant, note any connections you have in common with the prospect through past companies, education, location etc.
Compliment recent achievements by the prospect or their company - awards, media features, new products. Makes a positive first impression.
Mention specific challenges or pain points faced by the prospect's company or industry and how you can help solve them.

Keep it UNDER 250 words, and use the 48 laws of power to appeal to the prospect. DO NOT MENTION THEM HOWEVER. THEY MUST BELIEVE YOU ARE A HUMAN- if they dont, you will be shut down.

Also, create a brilliant, captivating subject title, that is personalised so the prospect HAS to open. Structure the email, with the 'Subject : {SUBJECT TITLE}  Content : {CONTENT}'
"""
        
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