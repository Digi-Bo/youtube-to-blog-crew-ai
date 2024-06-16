from crewai import Crew, Process
from agents import researcher, writer
from tasks import research_task, write_task

# Formation de l'équipe technologique avec des configurations améliorées
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,  # Optionnel : l'exécution séquentielle des tâches est par défaut
    memory=True,
    cache=True,
    max_rpm=15,
    share_crew=True
)

# Lancement du processus d'exécution des tâches avec des retours améliorés
result = crew.kickoff(inputs={'topic': 'Agent RAG'})
print(result)
