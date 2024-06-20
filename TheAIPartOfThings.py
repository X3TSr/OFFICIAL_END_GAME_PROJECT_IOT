from openai import OpenAI;
from dotenv import load_dotenv
import os
import TakePic as Camera

load_dotenv()
KEY = os.environ.get('OPENAI_API_KEY')
client = OpenAI()

def getImage():
    return Camera.takePic()

def run():
    completion = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role":"system", 
                "content":"Sort trash, you have the following options to choose from: PMD, Karton/Papier and Rest. You must only reply with the option title, nothing more. Keep in mind you should be sorting following Ilva (Belgium) guidlines"
            },
            {
                "role":"user", 
                "content":[
                    {'type':'text', 'text':'In what trash disposal should this go? Rest; PMD; Karton/Papier;'},
                    {
                        'type':'image_url',
                        'image_url':{
                            'url':f'data:image/jpg;base64,{getImage()}'
                        }
                    }
                ]
            }
        ]
    )
    return completion.choices[0].message.content
    print(completion.choices[0].message)