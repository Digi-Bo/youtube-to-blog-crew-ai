from crewai import Agent
from tools import yt_tool
from dotenv import load_dotenv
load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
os.environ["OPENAI_MODEL_NAME"] = "gpt-4o"

# Création d'un agent récupérateur de contenu avec mémoire et mode verbeux
researcher = Agent(
    role='Chercheur de contenu de blogs à partir de vidéos YouTube',
    goal='Obtenir le contenu vidéo pertinent pour le sujet {topic} à partir de la chaîne YouTube',
    verbose=True,
    memory=True,
    backstory=(
        "Expert dans la compréhension des vidéos sur l'IA, l'apprentissage automatique et l'IA générative, "
        "et fournissant des suggestions pertinentes."
    ),
    tools=[yt_tool],
    allow_delegation=True
)

# Création d'un agent rédacteur
writer = Agent(
    role='Rédacteur',
    goal='Raconter des histoires technologiques captivantes sur la vidéo {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Avec un talent pour simplifier les sujets complexes, vous créez des récits engageants qui captivent "
        "et éduquent, mettant en lumière de nouvelles découvertes de manière accessible."
    ),
    tools=[yt_tool],
    allow_delegation=False
)
