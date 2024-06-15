from crewai import Crew, Process 
from tools import yt_tool
from agents import researcher, writer
from tasks import research_task, write_task

# Forming the tech-focused crew with some enhanced configurations
crew = Crew(
agents= [researcher, writer],
tasks=[research_task, write_task],
process=Process.sequential, # Optional: Sequential task execution is default
memory=True,
cache=True,
max _rpm=15,
share_crew=True
)