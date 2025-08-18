import os
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain.chains import LLMChain
from langchain.chains import SequentialChain
from pprint import pprint

# Load environment variables from .env
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

openai_llm = ChatOpenAI(model="gpt-3.5-turbo")

template_1 = """Your job is to come up with a classic dish from the area that the users suggests.
                {location}
                
                YOUR RESPONSE:
"""
prompt_template_1 = PromptTemplate(template=template_1, input_variables=['location'])

# chain 1
location_chain = LLMChain(llm=openai_llm, prompt=prompt_template_1, output_key='meal')

template_2 = """Given a meal {meal}, give a short and simple recipe on how to make that dish at home.

                YOUR RESPONSE:
"""
prompt_template_2 = PromptTemplate(template=template_2, input_variables=['meal'])

# chain 2
dish_chain = LLMChain(llm=openai_llm, prompt=prompt_template_2, output_key='recipe')

template_3 = """Given the recipe {recipe}, estimate how much time I need to cook it.

                YOUR RESPONSE:
"""
prompt_template_3 = PromptTemplate(template=template_3, input_variables=['recipe'])

# chain 3
recipe_chain = LLMChain(llm=openai_llm, prompt=prompt_template_3, output_key='time')

# overall chain
overall_chain = SequentialChain(chains=[location_chain, dish_chain, recipe_chain],
                                      input_variables=['location'],
                                      output_variables=['meal', 'recipe', 'time'],
                                      verbose= True)


inp = input("Enter a location: ")
pprint(overall_chain.invoke(input={'location': inp}))
