from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.chains import SequentialChain
import google.generativeai as genai
import os

def generate_name_and_menu(cuisine, item):
    
    llm = ChatGoogleGenerativeAI(model = "gemini-pro")

    prompt_template_name = PromptTemplate(
        input_variables = ["cuisine"],
        template = "I want to open a restauant for {cuisine} food Suggest me a fancy name for this, only one name"
    )
    name_chain =LLMChain(llm=llm, prompt=prompt_template_name, output_key="restaurant_name")

    prompt_template_items = PromptTemplate(
        input_variables = ["restaurant_name", "item"],
        template = "suggest me top {item} best menu items for {restaurant_name}"
    )
    food_items_chain =LLMChain(llm=llm, prompt=prompt_template_items, output_key="menu_items")

    chain = SequentialChain(
        chains = [name_chain, food_items_chain],
        input_variables = ['cuisine','item'],
        output_variables=['restaurant_name', 'menu_items']
    )

    output=chain({"cuisine" : cuisine, "item":item})
    return output


def clean_menu_items(items):
  """Cleans a list of menu items by removing unnecessary formatting and combining multiple lines.

  Args:
    menu_items: A list of strings representing menu items.

  Returns:
    A list of cleaned menu items.
  """
  menu = str(items)
  menu = menu.strip()
  menu = menu.replace("*",'')
  menu = menu.split(str("\n"))
  return menu


# print(output["restaurant_name"])
# for item in output["menu_items"].split(","):
#     print(item.strip().replace("*",""))