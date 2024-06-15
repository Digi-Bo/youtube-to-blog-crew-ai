from crewai import Agent
from tools import yt_tool

# Création d'un agent récupérateur de contenu avec mémoire et mode verbeux
researcher = Agent(
  role='Blog Researcher from Youtube Videos',
  goal='get the relevant video content for the topic{topic} from Yt channel',
  verbose=True,
  memory=True,
  backstory=(
    "Expert in understanding videos in AI, Machine Learning and GEN AI and providing suggestions"
  ),
  tools=[tool],
  allow_delegation=True
)

# Création d'un agent rédacteur 
writer = Agent(
  role='Writer',
  goal='Narrate compelling tech stories about the video {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."
  ),
  tools=[yt_tool],
  allow_delegation=False
)