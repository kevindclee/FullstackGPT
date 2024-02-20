from langchain.prompts import PromptTemplate, ChatPromptTemplate

template = PromptTemplate.from_template(
    "What is the distance between {country_a} and {country_b}"
)

prompt = template.format(
    country_a = "Mexico",
    country_b = "Thailand"
)

# chat2.predict(prompt)

messages = ChatPromptTemplate.from_messages([
    ("system", "You are a geography expert. And you only reply in {language}."),
    ("ai", "Ciao, mi chiamo {name}!"),
    (
        "human", 
        "What is the distance between {country_a} and {country_b}. Also what is your name?"
    )
])

# chat2.predict_messages(messages)