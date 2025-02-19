from crewai import Task
from tools import yt_tool
from agents import researcher, writer

# Tâche de recherche
# Cette tâche a pour but d'identifier et d'analyser les vidéos YouTube pertinentes.
research_task = Task(
    description=(
        "Identifier la vidéo sur le sujet {topic}. "
        "Obtenir des informations détaillées sur la vidéo depuis la chaîne YouTube."
    ),
    expected_output='Un rapport complet de 3 paragraphes basé sur le contenu vidéo du sujet {topic}.',
    tools=[yt_tool],  # Utilisation de l'outil de recherche de chaînes YouTube
    agent=researcher,  # Agent responsable de cette tâche
)

# Tâche de rédaction avec configuration du modèle de langage
# Cette tâche consiste à résumer les informations obtenues des vidéos YouTube pour créer un article de blog.
write_task = Task(
    description=(
        "Utiliser les informations de la chaîne YouTube sur le sujet {topic} "
        "et rédiger un article de blog."
    ),
    expected_output='Résumé des informations de la vidéo YouTube sur le sujet {topic} et création d\'un article de blog.',
    tools=[yt_tool],  # Utilisation de l'outil de recherche de chaînes YouTube
    agent=writer,  # Agent responsable de cette tâche
    async_execution=False,  # Exécution séquentielle de la tâche
    output_file='new-blog-post.md'  # Fichier de sortie pour l'article de blog
)
