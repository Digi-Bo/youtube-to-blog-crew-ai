
# Automatisation de la création de blogs avec CrewAI


Ce projet explore l'automatisation de la création de contenu de blog à partir de vidéos YouTube en utilisant CrewAI. L'objectif principal de ce projet est de démontrer comment les technologies d'intelligence artificielle peuvent être utilisées pour simplifier et accélérer le processus de production de contenu en ligne. En configurant des agents intelligents pour rechercher, analyser et rédiger des articles basés sur des vidéos, nous pouvons réduire le temps et les efforts nécessaires pour générer du contenu de haute qualité. Ce projet illustre non seulement l'efficacité de CrewAI dans la gestion des tâches automatisées, mais aussi son adaptabilité à divers cas d'utilisation, en particulier dans le domaine du marketing de contenu et de la gestion des médias sociaux.



## Présentation de CrewAI

CrewAI est une plateforme qui a pour but d'automatiser la réalisation de tâches complexes en les déléguant à une équipe d'agents intelligents spécialisés qui vont travailler ensemble pour les réaliser.
Chaque agent est une entité autonome capable de réaliser des tâches spécifiques, interagir avec d'autres agents et s'adapter à divers cas d'utilisation.

CrewAI permet une gestion efficace des agents, en facilitant leur création, leur configuration et leur supervision. Cela assure une orchestration harmonieuse des tâches et des processus automatisés.

**Fonctionnalités du framework CrewAI**
- **Création d'agents** : Permet de configurer plusieurs agents spécialisés dans des tâches distinctes. Dans notre projet, nous aurons notamment un agent chargé de récupérer la transcription des vidéos Youtube et un autre chargé de rédiger des articles sur la base de la transcription.
- **Répartition des tâches** : Chaque agent peut se concentrer sur ses tâches spécifiques sans interruption.
- **Outils utilisés** : Pour réaliser leurs tâches, les agents peuvent utiliser des outils. Par exemple, pour récupéerer les vidéos Youtube, notre agents chargé de la récupération utilisera un outil mis à disposition par Youtube.
- **Gestion en parallèle des agents** : Les agents peuvent travailler en parallèle, ce qui accélère le processus global.
- **Communication entre agents** : CrewAI intègre des mécanismes de communication inter-agents qui permettent une interaction fluide et efficace. Les agents peuvent partager des informations, déléguer des tâches et collaborer de manière harmonieuse.
- **Allocation des tâches** : CrewAI gère l'assignation des tâches aux agents, en fonction de leurs compétences et de leur disponibilité. Cela garantit que chaque tâche est réalisée par l'agent le plus adapté.
- **Surveillance et reporting des performances des agents** : CrewAI inclut des outils de surveillance qui permettent de suivre les performances des agents, d'identifier les goulots d'étranglement et de générer des rapports détaillés sur l'efficacité des processus.

**Avantages de CrewAI**

- **Flexibilité et adaptabilité** : Possibilité de personnaliser les agents selon les besoins spécifiques de chaque projet.- **Interface utilisateur intuitive** : CrewAI offre une interface conviviale qui simplifie la gestion des agents et des tâches, même pour les utilisateurs non techniques.
- **Compatibilité avec divers outils et API** : CrewAI peut intégrer et interagir avec une variété d'outils et d'API, ce qui étend ses capacités et permet une personnalisation avancée des processus automatisés.
- **Efficacité et gain de temps** : Automatisation des tâches répétitives et chronophages.




#### Comparaison avec Langchain

**Similitudes entre CrewAI et Langchain**

- **Objectifs communs** : Les deux plateformes visent à automatiser des tâches complexes et à améliorer l'efficacité des processus.
- **Utilisation de concepts similaires** : Les deux utilisent des agents pour réaliser des tâches spécifiques et gèrent ces agents de manière autonome.

**Différences principales**

- **Communication inter-agents plus efficace avec CrewAI** : CrewAI est conçu pour faciliter une communication fluide et efficace entre les agents, ce qui améliore la coordination et réduit les erreurs.
- **Capacités de personnalisation et d'intégration de CrewAI** : CrewAI offre des options de personnalisation plus avancées et une meilleure intégration avec des outils tiers.
- **Facilité d'utilisation et courbe d'apprentissage** : CrewAI propose une interface plus intuitive et une courbe d'apprentissage moins abrupte, ce qui le rend accessible à un plus large éventail d'utilisateurs.

**Cas d'utilisation spécifiques**

- **Scénarios où CrewAI excelle par rapport à Langchain** : CrewAI est particulièrement efficace dans les projets nécessitant une coordination complexe entre plusieurs agents et l'intégration avec divers systèmes et outils.
- **Avantages en termes de scalabilité et de gestion de projets complexes** : CrewAI est conçu pour gérer des projets de grande envergure avec de nombreux agents et tâches, offrant une scalabilité robuste.

#### Utilisation dans des cas réels

- **Comment CrewAI peut être appliqué à des projets spécifiques** : CrewAI peut être utilisé pour automatiser une variété de tâches, telles que la gestion de contenu, l'analyse de données, et la coordination de projets complexes.

- Par exemple, une entreprise de marketing peut utiliser CrewAI pour automatiser la création de contenus et la gestion des campagnes.

- Un service de vente peut utiliser CrewAI pour gérer les dossiers clients et les rappels de rendez-vous.


- **Étapes pour intégrer CrewAI dans un flux de travail existant** : Pour intégrer CrewAI, il est recommandé de commencer par identifier les tâches répétitives et chronophages, de configurer les agents nécessaires, et de tester progressivement l'automatisation dans un environnement contrôlé avant de l'étendre à l'ensemble du flux de travail.


## Étude de Cas : Création automatisée d'articles de blogs

L'objectif de ce projet est d'automatiser la création d'articles de blogs à partir des vidéos YouTube d'une chaîne en utilisant CrewAI pour gérer et exécuter les tâches nécessaires. 
Ce type d'action est particulièrement pertinent pour générer rapidement du contenus qui pourra être diffusé dans d'autres cannaux tel que le site web ou les réseaux sociaux améliorant ainsi la présence en ligne et l'engagement des utilisateurs.

### Défi de la création manuelle de blogs

La création manuelle de d'articles de blogs à partir de centaines de vidéos représente un volume de travail immense, impliquant des tâches répétitives et chronophages. La complexité réside dans la recherche et l'extraction de contenu pertinent pour chaque vidéo, ainsi que la rédaction de blogs structurés, informatifs et intéressants. 

### Bénéfices de l'automatisation

- **Gain de temps** : Réduction significative du temps de traitement pour la rédaction de chaque article. 
- **Scalabilité** : Capacité à gérer un grand nombre d'articles sans effort supplémentaire.



## Quels agents définir pour notre projet ?

**Les différents rôles à définir :** Pour automatiser la rédaction d'articles de blog à partir des vidéos d'une chaine youtube, nous devons définir plusieurs rôles. Pour commencer, notre équipe sera composée d'un récupérateur de contenu, puis d'un rédacteurs. Nous devons définir un workflow, définir la spécialité de chaque agent, les tâches qu'il doit réaliser et nous assurer que chaque tâche se déroule dans l'ordre oportun.


**Workflow :**

- **Étape 1 : Récupération du contenu**
  - L'agent récupérateur explore les vidéos de la chaîne YouTube.
  - Utilise des outils pour extraire les transcriptions et résumer le contenu.

- **Étape 2 : Rédaction**
  - L'agent rédacteur utilise les informations fournies par le récupérateur de contenu pour rédiger un article de blog structuré et informatif.




## Schéma du projet

```mermaid
graph TD
    A[Projet d'automatisation d'articles de blog] --> B[Configuration de l'environnement]
    B --> C[Chargement des variables d'environnement Conda]
    C --> D[Configuration du modèle de langage]
    D --> E[Création des agents]
    E --> F[Définition des tâches]
    F --> G[Formation de l'équipe]
    G --> H[Lancement du processus]

    E --> E1[Agent de recherche]
    E --> E2[Agent de rédaction]

    F --> F1[Tâche de recherche]
    F --> F2[Tâche de rédaction]

    H --> I[Exécution séquentielle des tâches]
    I --> J[Recherche de vidéos YouTube]
    J --> K[Extraction des transcriptions]
    K --> L[Rédaction d'articles de blog]
    L --> M[Stockage du résultat]

    style A fill:#f9f,stroke:#333,stroke-width:2px;
    style M fill:#bbf,stroke:#333,stroke-width:2px;
```

### Explication du schéma

1. **Configuration de l'environnement** : Initialisation de l'environnement, notamment le chargement des variables d'environnement.
2. **Configuration du modèle de langage** : Configuration des modèles de langage à utiliser, par exemple ceux de Hugging Face.
3. **Création des agents** : 
    - **Agent de recherche** : Agent dédié à la recherche et à l'extraction de données.
    - **Agent de rédaction** : Agent responsable de la rédaction des articles de blog.
4. **Définition des tâches** :
    - **Tâche de recherche** : Identification et analyse des vidéos YouTube pertinentes.
    - **Tâche de rédaction** : Rédaction d'articles de blog basés sur les données extraites.
5. **Formation de l'équipe** : Configuration de l'équipe d'agents avec les tâches définies.
6. **Lancement du processus** : Démarrage du processus d'exécution.
7. **Exécution séquentielle des tâches** : Les tâches sont exécutées dans l'ordre.
    - **Recherche de vidéos YouTube** : Recherche des vidéos pertinentes.
    - **Extraction des transcriptions** : Extraction du contenu des vidéos.
    - **Rédaction d'articles de blog** : Création des articles basés sur les transcriptions.
    - **Stockage du résultat** : Sauvegarde des articles rédigés.







## Mise en Place du Projet

### Création d'un environnement de développement

**Installation de Conda**

Pour commencer, visitez le site officiel de Conda pour télécharger le fichier d'installation approprié pour votre système d'exploitation. Exécutez l'installateur et suivez les instructions à l'écran pour terminer l'installation. Une fois l'installation terminée, vous pouvez vérifier que Conda est correctement installé en utilisant la commande `conda --version`. Il est également recommandé de mettre à jour Conda avec la commande `conda update conda` pour s'assurer que vous disposez de la version la plus récente.

**Création et activation de l'environnement virtuel**

Créez un nouvel environnement virtuel avec la commande `conda create -n nom_de_votre_environnement python=3.12`, où vous spécifiez le nom de l'environnement et la version de Python souhaitée. Activez ensuite l'environnement en utilisant la commande `conda activate nom_de_votre_environnement`. Vous saurez que l'activation a réussi en observant le changement dans le prompt de commande. Pour désactiver l'environnement après utilisation, utilisez la commande `conda deactivate`. Cette désactivation est importante pour éviter les conflits avec d'autres environnements.

### Installation des dépendances

**Fichier requirements.txt**

Créez un fichier `requirements.txt` en ouvrant un éditeur de texte tel que VS Code ou Sublime Text. Dans ce fichier, listez les bibliothèques nécessaires avec leurs versions respectives. Voici un exemple de contenu pour `requirements.txt` :

```
crewai
python-dotenv
crewai_tools
langchain_openai
langchain_community
langchain_huggingface
```

Chaque bibliothèque a un rôle spécifique :
- **CrewAI** : Pour la gestion des agents et des tâches.
- **python-dotenv** : Pour la gestion des variables d'environnement.
- **crewai_tools** : Pour des outils supplémentaires liés à CrewAI.
- **langchain_openai** : Pour l'intégration avec OpenAI.
- **langchain_community** : Pour les outils communautaires de Langchain.
- **langchain_huggingface** : Pour l'intégration avec Hugging Face.

**Installation des bibliothèques nécessaires**

Pour installer les dépendances listées dans `requirements.txt`, utilisez la commande `pip install -r requirements.txt`. Vérifiez ensuite que toutes les bibliothèques ont été installées correctement. En cas d'erreur d'installation, vérifiez les versions des bibliothèques pour résoudre les conflits potentiels et consultez la documentation spécifique des bibliothèques concernées pour des solutions précises. Si nécessaire, mettez à jour les bibliothèques avec la commande `pip install --upgrade nom_de_la_bibliothèque`.



## Création des Agents

### Définition de l'agent de recherche

**Rôle : Chercheur de contenu de blog**

L'agent de recherche est responsable de l'exploration et de l'analyse des vidéos YouTube pour extraire le contenu pertinent destiné aux articles de blog. Ce rôle nécessite une expertise en analyse de données ainsi qu'une compréhension approfondie des sujets abordés dans les vidéos, notamment l'intelligence artificielle et la data science.

**Objectif : Trouver des vidéos pertinentes sur YouTube**

L'agent doit identifier des vidéos alignées avec le sujet du blog. Les critères de pertinence incluent l'alignement avec le sujet, la popularité et l'engagement des vidéos, ainsi que la qualité et la profondeur du contenu. Le processus de recherche implique l'utilisation d'outils de recherche YouTube pour extraire et analyser les transcriptions vidéo.

**Paramètres : mémoire, verbosité, outils**

- **Mémoire (memory)** : L'agent conserve les informations extraites pour une utilisation future, assurant la persistance des données pour améliorer les performances.
- **Verbosité (verbose)** : Le niveau de détail dans les sorties de l'agent est crucial pour le débogage et la vérification des processus.
- **Outils** : 
  - **YouTubeChannelSearchTool** : Cet outil permet de rechercher des vidéos sur un canal YouTube spécifique, initialisé avec le handle du canal.

### Définition de l'agent de rédaction

**Rôle : Rédacteur de contenu**

L'agent de rédaction est chargé de rédiger des articles de blog basés sur le contenu vidéo fourni par l'agent de recherche. Il crée des narratives captivantes et informatives, rendant les sujets complexes accessibles et intéressants pour les lecteurs.

**Objectif : Rédiger des articles de blog captivants**

L'agent de rédaction doit produire des articles clairs et fluides, précis et exacts, tout en engageant les lecteurs. Le processus de rédaction commence par la réception des informations de l'agent de recherche, suivie de la structuration et de la rédaction de l'article.

**Paramètres : mémoire, verbosité, outils**

- **Mémoire (memory)** : L'agent conserve les drafts et les révisions pour une consultation ultérieure, améliorant ainsi la cohérence des articles.
- **Verbosité (verbose)** : Les détails des logs et des messages de sortie sont utilisés pour le suivi du processus, le contrôle de qualité et l'optimisation des performances.
- **Outils** :
  - **YouTubeChannelSearchTool** : Cet outil utilise les transcriptions et les résumés fournis par l'agent de recherche, adapté aux besoins spécifiques de la rédaction.

Ces agents, une fois configurés et activés, travailleront en tandem pour automatiser la création de blogs à partir de vidéos YouTube, chacun apportant son expertise spécifique au processus global.



## Configuration des Outils

### Introduction des outils nécessaires

**Rôle des outils dans CrewAI**

Les outils jouent un rôle essentiel dans CrewAI en facilitant les tâches des agents et en intégrant des fonctionnalités spécifiques nécessaires à l'exécution des processus automatisés. Ils permettent aux agents de rechercher des informations, de transcrire du contenu, et de traiter des textes, améliorant ainsi l'efficacité globale du système.

**Types d'outils utilisés**

- **Outils de recherche** : Utilisés pour explorer et identifier des informations pertinentes sur le web.
- **Outils de transcription** : Utilisés pour convertir des contenus audio et vidéo en texte.
- **Outils de traitement de texte** : Utilisés pour formater et structurer le contenu textuel.

**Importance des outils**

Les outils sont cruciaux pour l'automatisation des processus manuels, ce qui permet non seulement de gagner du temps mais aussi d'améliorer l'efficacité et la précision des agents. En utilisant des outils spécifiques, les agents peuvent effectuer des tâches complexes de manière plus rapide et avec moins d'erreurs.

### Exemple : Outil de recherche de chaînes YouTube

**Présentation de l'outil**

- **Nom de l'outil** : YouTubeChannelSearchTool
- **Fonction principale** : Rechercher des vidéos sur une chaîne YouTube spécifique.

**Fonctionnement de l'outil**

**Initialisation**

L'outil est configuré avec le handle de la chaîne YouTube. Par exemple :

```python
from crewai_tools import YoutubeChannelSearchTool
tool = YoutubeChannelSearchTool(youtube_channel_handle='@krishnaik06')
```

**Recherche et extraction**

L'outil est utilisé pour rechercher des vidéos pertinentes sur la chaîne et pour extraire des transcriptions et des métadonnées des vidéos.

### Intégration avec les agents

**Agent de recherche**

L'agent de recherche utilise l'outil YouTubeChannelSearchTool pour identifier et analyser les vidéos pertinentes. Par exemple :

```python
from crewai import Agent
from tools import tool

researcher = Agent(
  role='Blogs Creator from Youtube Videos',
  goal='provide the relevant video suggestions for the topic {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "Expert in understanding videos in AI Data Science, Machine Learning and GEN AI and providing suggestions"
  ),
  tools=[tool],
  allow_delegation=True
)
```

**Agent de rédaction**

L'agent de rédaction utilise les résultats de l'outil de recherche pour rédiger des articles de blog. Par exemple :

```python
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
  tools=[tool],
  allow_delegation=False
)
```

### Personnalisation et extension

**Ajout de nouvelles fonctionnalités**

L'outil peut être étendu pour inclure des fonctionnalités supplémentaires, comme l'intégration avec une API de transcription pour améliorer l'extraction de contenu. Par exemple :

```python
from crewai_tools import YoutubeChannelSearchTool, TranscriptionTool

search_tool = YoutubeChannelSearchTool(youtube_channel_handle='@krishnaik06')
transcription_tool = TranscriptionTool(api_key='your_api_key')

researcher = Agent(
  role='Blogs Creator from Youtube Videos',
  goal='provide the relevant video suggestions for the topic {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "Expert in understanding videos in AI Data Science, Machine Learning and GEN AI and providing suggestions"
  ),
  tools=[search_tool, transcription_tool],
  allow_delegation=True
)
```

**Configuration avancée**

Il est possible de paramétrer l'outil pour des recherches spécifiques, par exemple en filtrant les vidéos par date de publication, nombre de vues, etc., pour affiner les résultats et répondre à des besoins particuliers.





## Définition des Tâches

### Tâche de recherche

**Description : Identifier et analyser les vidéos YouTube**

La tâche de recherche consiste à identifier les vidéos pertinentes sur la chaîne YouTube et à analyser leur contenu pour extraire des informations clés. Cette tâche a pour objectifs d'identifier les vidéos alignées avec le sujet spécifié, d'analyser le contenu pour extraire les points clés, et de synthétiser les informations obtenues.

**Objectifs de la tâche**

- Identifier les vidéos pertinentes sur la chaîne YouTube.
- Analyser le contenu des vidéos pour extraire des informations clés.

**Processus de réalisation**

1. **Recherche des vidéos** : L'agent utilise des outils de recherche pour trouver des vidéos en fonction du sujet spécifié.
2. **Extraction et analyse des transcriptions** : Utilisation d'outils pour extraire les transcriptions des vidéos et analyser le contenu.
3. **Synthèse des informations** : Compilation des informations extraites en un rapport structuré.

**Résultat attendu : Rapport détaillé**

Le rapport détaillé résume les vidéos analysées, présente les points clés et fournit des recommandations basées sur le contenu vidéo.

- **Contenu du rapport**
  - Résumé des vidéos analysées.
  - Points clés et informations importantes.
  - Insights et recommandations.

- **Format du rapport**
  Le rapport est structuré en paragraphes avec des sections pour organiser les informations. Exemple de format de rapport :

  ```markdown
  # Rapport de Recherche
  ## Vidéo 1 : Titre de la Vidéo
  - **Résumé :** Description succincte de la vidéo
  - **Points Clés :** Liste des informations importantes
  - **Recommandations :** Suggestions basées sur le contenu

  ## Vidéo 2 : Titre de la Vidéo
  - **Résumé :** Description succincte de la vidéo
  - **Points Clés :** Liste des informations importantes
  - **Recommandations :** Suggestions basées sur le contenu
  ```

**Outils utilisés**

- **YouTubeChannelSearchTool**
  - Fonction : Recherche de vidéos sur la chaîne YouTube.
  - Configuration : Initialisation avec le handle de la chaîne.
- **TranscriptionTool**
  - Fonction : Extraction des transcriptions des vidéos.
  - Configuration : API clé pour l'accès.

### Tâche de rédaction

**Description : Rédiger un article de blog basé sur les vidéos**

La tâche de rédaction implique de créer un article de blog informatif et captivant en utilisant les informations fournies par l'agent de recherche. Cette tâche a pour objectifs d'analyser le rapport de l'agent de recherche, de structurer l'article, et de rédiger un contenu attrayant et précis.

**Objectifs de la tâche**

- Utiliser les informations fournies par l'agent de recherche.
- Créer un article de blog informatif et captivant.

**Processus de réalisation**

1. **Réception et analyse du rapport** : L'agent de rédaction reçoit et analyse le rapport de l'agent de recherche.
2. **Structuration de l'article** : Organisation de l'article en sections logiques et cohérentes.
3. **Rédaction et révision** : Rédaction du contenu, suivie d'une révision pour assurer la qualité et la précision.

**Résultat attendu : Article formaté en markdown**

L'article doit être clair, informatif, et bien structuré, en utilisant le format markdown pour la mise en forme.

- **Contenu de l'article**
  - Introduction au sujet.
  - Développement des points clés extraits des vidéos.
  - Conclusion et perspectives.

- **Format de l'article**
  Exemple de format d'article en markdown :

  ```markdown
  # Titre de l'Article
  ## Introduction
  Introduction au sujet abordé dans les vidéos.

  ## Développement
  ### Point Clé 1
  Description et explication du premier point clé.

  ### Point Clé 2
  Description et explication du deuxième point clé.

  ## Conclusion
  Résumé des points discutés et perspectives futures.
  ```

**Outils utilisés**

- **MarkdownEditorTool**
  - Fonction : Rédaction et formatage de l'article en markdown.
  - Configuration : Paramètres pour le style et la mise en page.
- **ContentReviewTool**
  - Fonction : Vérification et révision du contenu rédigé.
  - Configuration : Critères de qualité et de cohérence.




## Exécution du Processus

### Configuration du processus séquentiel

**Définition du processus séquentiel**

Un processus séquentiel exécute les tâches dans un ordre défini où chaque tâche doit être complétée avant de passer à la suivante. Ce type de processus simplifie la gestion des dépendances entre les tâches et réduit les risques de conflits ou d'incohérences.

**Avantages du processus séquentiel**

- Simplification de la gestion des dépendances entre les tâches.
- Réduction des risques de conflits ou d'incohérences.

**Paramètres de configuration**

**Agents impliqués**

Les agents impliqués dans ce processus sont définis comme suit : un chercheur et un rédacteur. Voici un exemple de configuration :

```python
from crewai import Crew, Process
from agents import researcher, writer
from task import research_task, write_task

crew = Crew(
  agents=[researcher, writer],
  tasks=[research_task, write_task],
  process=Process.sequential,  # Définition du processus séquentiel
  memory=True,
  cache=True,
  max_rpm=100,
  share_crew=True
)
```

**Processus séquentiel**

Le processus est configuré pour une exécution séquentielle en utilisant l'option `Process.sequential`.

### Initialisation et exécution des tâches

**Préparation des agents et des tâches**

**Importation des modules nécessaires**

Les agents et les tâches définis précédemment doivent être importés :

```python
from agents import researcher, writer
from task import research_task, write_task
```

**Initialisation des agents**

Les agents (chercheur et rédacteur) sont créés et configurés :

```python
researcher = Agent(...)
writer = Agent(...)
```

**Initialisation des tâches**

Les tâches (recherche et rédaction) sont créées et configurées :

```python
research_task = Task(...)
write_task = Task(...)
```

**Lancement du processus**

**Exécution des tâches**

La méthode `kickoff` est utilisée pour démarrer le processus :

```python
result = crew.kickoff(inputs={'topic': 'AI vs ML VS DL VS Data Science'})
print(result)
```

**Suivi et monitoring**

L'état d'avancement des tâches est vérifié en utilisant des logs et des messages de sortie pour assurer le suivi du processus.

### Gestion des erreurs et des clés API

**Gestion des erreurs**

**Types d'erreurs possibles**

- Erreurs de configuration (ex. : paramètres incorrects).
- Erreurs d'exécution (ex. : échec d'une tâche).

**Stratégies de gestion des erreurs**

Des mécanismes de détection et de gestion des erreurs doivent être mis en place. Voici un exemple de gestion des erreurs :

```python
try:
  result = crew.kickoff(inputs={'topic': 'AI vs ML VS DL VS Data Science'})
  print(result)
except Exception as e:
  print(f"Erreur lors de l'exécution : {e}")
```

**Gestion des clés API**

**Utilisation des variables d'environnement**

Les clés API doivent être stockées dans un fichier `.env` et chargées au démarrage du script :

```python
from dotenv import load_dotenv
load_dotenv()

import os
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")
```

**Sécurité et bonnes pratiques**

Pour garantir la sécurité, les clés API ne doivent jamais être exposées dans le code source. L'utilisation de bibliothèques comme `python-dotenv` permet de gérer les variables d'environnement de manière sécurisée.




## Finalisation et Résultats

### Vérification du fichier de sortie

**Accès au fichier de sortie**

Une fois le processus de création du blog terminé, le fichier de sortie est généré et enregistré dans le dossier spécifié lors de la configuration. Par exemple, le chemin du fichier pourrait être `./output/new-blog-post.md`. Pour ouvrir et inspecter le fichier, vous pouvez utiliser un éditeur de texte ou un visualiseur de markdown. Voici une commande pour afficher le contenu du fichier dans le terminal :

```bash
cat ./output/new-blog-post.md
```

**Validation du contenu**

Pour s'assurer que le contenu généré répond aux attentes, il est important de vérifier plusieurs aspects :

**Conformité avec les attentes**

Le contenu doit correspondre au sujet spécifié et aux critères de qualité définis. Cela inclut la vérification de la précision des informations et de leur pertinence par rapport au sujet traité.

**Structure et format**

La structure du document doit être claire et bien organisée, avec des titres et des sections appropriés. La mise en forme markdown doit être validée pour s'assurer qu'elle est correcte et cohérente. Voici un exemple de structure de document attendu :

```markdown
# Titre de l'Article
## Introduction
Introduction au sujet abordé dans les vidéos.

## Développement
### Point Clé 1
Description et explication du premier point clé.

### Point Clé 2
Description et explication du deuxième point clé.

## Conclusion
Résumé des points discutés et perspectives futures.
```

Cette vérification permet de garantir que le blog généré est conforme aux standards de qualité et qu'il est prêt à être publié.







# Revue de code : 


### Objectifs et Logique de Fonctionnement

L'objectif principal de ce projet est d'automatiser la création de blogs à partir de vidéos YouTube en utilisant la plateforme CrewAI. Pour ce faire, le projet utilise des agents pour rechercher des vidéos, extraire leur contenu et rédiger des articles de blog. La logique de fonctionnement repose sur l'utilisation d'outils spécifiques pour chaque tâche et la définition claire des rôles et des objectifs de chaque agent.

### Fichiers 

#### 1. `requirements.txt`

**But :** Définir et installer toutes les dépendances nécessaires pour le projet.

**Contenu :**
```plaintext
crewai
python-dotenv
crewai_tools
langchain_openai
langchain_community
langchain_huggingface
```

**Installation des dépendances :**
Pour installer les dépendances listées dans `requirements.txt`, utilisez la commande suivante :
```bash
pip install -r requirements.txt
```

**Explication :**
- `crewai` : Bibliothèque principale pour la gestion des agents et des tâches.
- `python-dotenv` : Utilisé pour gérer les variables d'environnement de manière sécurisée.
- `crewai_tools` : Outils supplémentaires pour CrewAI.
- `langchain_openai`, `langchain_community`, `langchain_huggingface` : Intégrations et outils pour utiliser les modèles de Langchain et Hugging Face.


#### 2. `agents.py`

**But :** Définir les agents de recherche et de rédaction avec les outils appropriés.

**Code :**
```python
from crewai import Agent
from tools import tool

# Création d'un agent récupérateur de contenu avec mémoire et mode verbeux
researcher = Agent(
  role='Blogs Creator from Youtube Videos',
  goal='provide the relevant video suggestions for the topic {topic}',
  verbose=True,
  memory=True,
  backstory=(
    "Expert in understanding videos in AI Data Science, Machine Learning and GEN AI and providing suggestions"
  ),
  tools=[tool],
  allow_delegation=True
)

# Création d'un agent rédacteur avec des outils personnalisés et capacité de délégation
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
  tools=[tool],
  allow_delegation=False
)
```

**Explication :**

**Création des agents :**
- **Agent de recherche (researcher)** :
  - **Rôle** : Chercheur de contenu de blog.
  - **Objectif** : Fournir des suggestions de vidéos pertinentes pour un sujet spécifié.
  - **Attributs** :
    - `verbose=True` : Mode verbeux pour des sorties détaillées.
    - `memory=True` : Utilisation de la mémoire pour conserver les informations.
    - `tools=[tool]` : Utilisation de l'outil de recherche de chaînes YouTube.
    - `allow_delegation=True` : Permet la délégation des tâches à d'autres agents.
  
**Agent de rédaction (writer)** :
  - **Rôle** : Rédacteur de contenu.
  - **Objectif** : Rédiger des articles de blog captivants basés sur les vidéos.
  - **Attributs** :
    - `verbose=True` : Mode verbeux pour des sorties détaillées.
    - `memory=True` : Utilisation de la mémoire pour conserver les informations.
    - `tools=[tool]` : Utilisation de l'outil de recherche de chaînes YouTube.
    - `allow_delegation=False` : Ne permet pas la délégation des tâches.




#### 3. `tools.py`

**But :** Définir les outils nécessaires pour les agents.

**Code :**
```python
from crewai_tools import YoutubeChannelSearchTool

# Initialiser l'outil avec un handle spécifique de chaîne YouTube
tool = YoutubeChannelSearchTool(youtube_channel_handle='@krishnaik06')
```

**Explication :**
- **Importation du module** : `YoutubeChannelSearchTool` est importé depuis `crewai_tools`.
- **Initialisation de l'outil** : Un objet `YoutubeChannelSearchTool` est créé et configuré pour rechercher des vidéos sur la chaîne YouTube spécifiée par le handle `@krishnaik06`.


## 4. `task.py`

L'objectif de ce fichier est de définir les tâches que les agents devront exécuter. Ces tâches comprennent la recherche de vidéos pertinentes sur YouTube et la rédaction d'articles de blog basés sur le contenu de ces vidéos. Le fichier `task.py` crée deux tâches distinctes : une tâche de recherche et une tâche de rédaction, chacune avec des objectifs et des configurations spécifiques.

### Fonctionnement des Tâches

#### 1. Importation des modules nécessaires

Le fichier commence par importer les classes et outils nécessaires pour définir les tâches.

```python
from crewai import Task
from tools import tool
from agents import researcher, writer
```

- **`Task`** : Classe fournie par CrewAI pour définir des tâches.
- **`tool`** : Outil défini dans `tools.py` pour rechercher des vidéos sur YouTube.
- **`researcher` et `writer`** : Agents définis dans `agents.py` pour exécuter les tâches.

#### 2. Définition de la tâche de recherche

La tâche de recherche est responsable de l'identification et de l'analyse des vidéos YouTube pertinentes.

```python
# Tâche de recherche
research_task = Task(
  description=(
    "Identify the video {topic}."
    "Get detailed information about the video from the channel."
  ),
  expected_output='A comprehensive 3 paragraphs long report based on the {topic} of video content.',
  tools=[tool],
  agent=researcher,
)
```

- **Description** : La tâche consiste à identifier des vidéos sur un sujet spécifié et à obtenir des informations détaillées sur ces vidéos.
- **Résultat attendu** : Un rapport complet de trois paragraphes basé sur le contenu vidéo du sujet spécifié.
- **Outils utilisés** : L'outil de recherche de chaînes YouTube défini dans `tools.py`.
- **Agent** : L'agent de recherche (`researcher`) défini dans `agents.py`.

#### 3. Définition de la tâche de rédaction

La tâche de rédaction consiste à rédiger des articles de blog en utilisant les informations fournies par la tâche de recherche.

```python
# Tâche de rédaction avec configuration du modèle de langage
write_task = Task(
  description=(
    "get the info from the youtube channel on the topic {topic}."
  ),
  expected_output='Summarize the info from the youtube channel video on the topic {topic}',
  tools=[tool],
  agent=writer,
  async_execution=False,
  output_file='new-blog-post.md'  # Exemple de personnalisation de sortie
)
```

- **Description** : La tâche consiste à obtenir des informations sur le sujet spécifié à partir des vidéos YouTube et à les résumer.
- **Résultat attendu** : Un résumé des informations des vidéos YouTube sur le sujet spécifié.
- **Outils utilisés** : L'outil de recherche de chaînes YouTube.
- **Agent** : L'agent de rédaction (`writer`).
- **Exécution asynchrone** : Configuré à `False` pour exécuter la tâche de manière séquentielle.
- **Fichier de sortie** : `new-blog-post.md` pour stocker l'article de blog généré.

### Code complet de `task.py`

```python
from crewai import Task
from tools import tool
from agents import researcher, writer

# Tâche de recherche
# Cette tâche a pour but d'identifier et d'analyser les vidéos YouTube pertinentes.
research_task = Task(
    description=(
        "Identifier la vidéo {topic}."
        "Obtenir des informations détaillées sur la vidéo depuis la chaîne."
    ),
    expected_output='Un rapport complet de 3 paragraphes basé sur le contenu vidéo du sujet {topic}.',
    tools=[tool],  # Utilisation de l'outil de recherche de chaînes YouTube
    agent=researcher,  # Agent responsable de cette tâche
)

# Tâche de rédaction avec configuration du modèle de langage
# Cette tâche consiste à résumer les informations obtenues des vidéos YouTube pour créer un article de blog.
write_task = Task(
    description=(
        "Obtenir les informations de la chaîne YouTube sur le sujet {topic}."
    ),
    expected_output='Résumé des informations de la vidéo YouTube sur le sujet {topic}.',
    tools=[tool],  # Utilisation de l'outil de recherche de chaînes YouTube
    agent=writer,  # Agent responsable de cette tâche
    async_execution=False,  # Exécution séquentielle de la tâche
    output_file='new-blog-post.md'  # Fichier de sortie pour l'article de blog
)
```

Le fichier `task.py` définit deux tâches principales à l'aide de la classe `Task` de CrewAI. La tâche de recherche, exécutée par l'agent `researcher`, a pour but d'identifier et d'analyser des vidéos pertinentes sur YouTube en fonction d'un sujet donné, en utilisant l'outil `YoutubeChannelSearchTool`. La tâche produit un rapport détaillé de trois paragraphes.

La tâche de rédaction, réalisée par l'agent `writer`, consiste à rédiger un article de blog basé sur les informations obtenues par la tâche de recherche. Cette tâche utilise également l'outil `YoutubeChannelSearchTool` pour extraire les transcriptions et les résumer. Le résultat est un article de blog formaté en markdown, stocké dans le fichier `new-blog-post.md`.

Chaque tâche est configurée avec des paramètres spécifiques pour assurer une exécution fluide et efficace, en suivant un processus séquentiel pour garantir que chaque étape est complétée avant de passer à la suivante.


## 5. app.py


L'objectif principal du fichier `app.py` est de configurer l'environnement, initialiser les agents et les tâches, puis exécuter un processus séquentiel pour automatiser la recherche et la rédaction de contenu basé sur des vidéos YouTube. Ce fichier utilise plusieurs bibliothèques et outils pour configurer les agents avec des capacités spécifiques et lancer le processus de manière orchestrée.


#### 1. Importation et configuration de l'environnement


**Code :**
```python
import os
from dotenv import load_dotenv

load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
os.environ["OPENAI_API_KEY"] = ""
```

**Explication :**
- **Chargement des variables d'environnement** : Utilisation de `load_dotenv()` pour charger les variables d'environnement à partir d'un fichier `.env`.
- **Configuration des tokens API** : Les tokens pour Hugging Face et OpenAI sont définis dans les variables d'environnement.

#### 2. Configuration du modèle de langage

**But :** Configurer un modèle de langage depuis Hugging Face.

**Code :**
```python
from langchain_community.llms import HuggingFaceHub

repo_id = "mistralai/Mistral-7B-Instruct-v0.2"  # Voir https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads pour d'autres options
llm = HuggingFaceHub(
    repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_tokens": 4096}
)
```

**Explication :**
- **Importation du modèle** : Utilisation de `HuggingFaceHub` pour configurer le modèle de langage.
- **Configuration du modèle** : Le modèle est configuré avec un `repo_id` spécifique et des paramètres de modèle (`temperature` et `max_tokens`).

#### 3. Création des agents

**But :** Définir et configurer les agents de recherche et de rédaction.

**Code :**
```python
from crewai import Agent
from crewai_tools import SerperDevTool

search_tool = SerperDevTool()

# Création d'un agent chercheur senior avec mémoire et mode verbeux
researcher = Agent(
    role='Senior Researcher',
    goal='Uncover groundbreaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
    ),
    tools=[search_tool],
    llm=llm,
    allow_delegation=True
)

# Création d'un agent rédacteur avec des outils personnalisés et capacité de délégation
writer = Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[search_tool],
    llm=llm,
    allow_delegation=False
)
```

**Explication :**
- **Création de l'agent de recherche (researcher)** :
  - **Rôle** : Chercheur senior.
  - **Objectif** : Découvrir des technologies révolutionnaires sur un sujet spécifique.
  - **Attributs** : Mode verbeux, mémoire activée, utilisation de `SerperDevTool` et du modèle de langage configuré.
- **Création de l'agent de rédaction (writer)** :
  - **Rôle** : Rédacteur.
  - **Objectif** : Rédiger des articles captivants sur un sujet spécifique.
  - **Attributs** : Mode verbeux, mémoire activée, utilisation de `SerperDevTool` et du modèle de langage configuré.

#### 4. Définition des tâches

**But :** Définir les tâches de recherche et de rédaction.

**Code :**
```python
from crewai import Task

# Tâche de recherche
research_task = Task(
    description=(
        "Identify the next big trend in {topic}."
        "Focus on identifying pros and cons and the overall narrative."
        "Your final report should clearly articulate the key points,"
        "its market opportunities, and potential risks."
    ),
    expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
    tools=[search_tool],
    agent=researcher,
)

# Tâche de rédaction avec configuration du modèle de langage
write_task = Task(
    description=(
        "Compose an insightful article on {topic}."
        "Focus on the latest trends and how it's impacting the industry."
        "This article should be easy to understand, engaging, and positive."
    ),
    expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
    tools=[search_tool],
    agent=writer,
    async_execution=False,
    output_file='new-blog-post.md'  # Exemple de personnalisation de sortie
)
```

**Explication :**
- **Tâche de recherche (research_task)** :
  - **Description** : Identifier les prochaines grandes tendances en IA et rédiger un rapport détaillé.
  - **Résultat attendu** : Un rapport complet de trois paragraphes sur les dernières tendances en IA.
  - **Agent** : Utilisation de l'agent de recherche.
- **Tâche de rédaction (write_task)** :
  - **Description** : Composer un article perspicace sur un sujet spécifique en IA.
  - **Résultat attendu** : Un article de quatre paragraphes formaté en markdown.
  - **Agent** : Utilisation de l'agent de rédaction.
  - **Exécution asynchrone** : Configuré à `False` pour exécuter la tâche de manière séquentielle.
  - **Fichier de sortie** : `new-blog-post.md`.

#### 5. Formation et exécution du processus

**But :** Former l'équipe d'agents et exécuter les tâches de manière séquentielle.

**Code :**
```python
from crewai import Crew, Process

# Formation de l'équipe technique avec des configurations améliorées
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,  # Exécution séquentielle des tâches
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

# Lancement du processus d'exécution des tâches avec retour d'information amélioré
result = crew.kickoff(inputs={'topic': 'AI in healthcare'})
print(result)
```

**Explication :**
- **Formation de l'équipe (crew)** :
  - **Agents** : Inclusion des agents de recherche et de rédaction.
  - **Tâches** : Inclusion des tâches de recherche et de rédaction.
  - **Processus** : Exécution séquentielle des tâches pour garantir un ordre logique et éviter les conflits.
- **Exécution du processus** :
  - **Lancement** : Utilisation de `kickoff` pour démarrer le processus avec le sujet spécifié.
  - **Affichage des résultats** : Les résultats de l'exécution sont imprimés.

---

### code complet de `app.py`
```python
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()
os.environ["HUGGINGFACEHUB_API_TOKEN"] = "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"
os.environ["OPENAI_API_KEY"] = ""

from langchain_community.llms import HuggingFaceHub

# Configuration du modèle de langage HuggingFaceHub
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"  # Voir https://huggingface.co/models?pipeline_tag=text-generation&sort=downloads pour d'autres options
llm = HuggingFaceHub(
    repo_id=repo_id, model_kwargs={"temperature": 0.5, "max_tokens": 4096}
)

from crewai import Agent
from crewai_tools import SerperDevTool

# Initialisation de l'outil de recherche
search_tool = SerperDevTool()

# Création d'un agent chercheur senior avec mémoire et mode verbeux
researcher = Agent(
    role='Senior Researcher',
    goal='Uncover groundbreaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
    ),
    tools=[search_tool],
    llm=llm,
    allow_delegation=True
)

# Création d'un agent rédacteur avec des outils personnalisés et capacité de délégation
writer = Agent(
    role='Writer',
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "With a flair for simplifying complex topics, you craft"
        "engaging narratives that captivate and educate, bringing new"
        "discoveries to light in an accessible manner."
    ),
    tools=[search_tool],
    llm=llm,
    allow_delegation=False
)

from crewai import Task

# Tâche de recherche
research_task = Task(
    description=(
        "Identify the next big trend in {topic}."
        "Focus on identifying pros and cons and the overall narrative."
        "Your final report should clearly articulate the key points,"
        "its market opportunities, and potential risks."
    ),
    expected_output='A comprehensive 3 paragraphs long report on the latest AI trends.',
    tools=[search_tool],
    agent=researcher,
)

# Tâche de rédaction avec configuration du modèle de langage
write_task = Task(
    description=(
        "Compose an insightful article on {topic}."
        "Focus on the latest trends and how it's impacting the industry."
        "This article should be easy to understand, engaging, and positive."
    ),
    expected_output='A 4 paragraph article on {topic} advancements formatted as markdown.',
    tools=[search_tool],
    agent=writer,
    async_execution=False,
    output_file='new-blog-post.md'  # Exemple de personnalisation de sortie
)

from crewai import Crew, Process

# Formation de l'équipe technique avec des configurations améliorées
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,  # Exécution séquentielle des tâches
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)

# Lancement du processus d'exécution des tâches avec retour d'information amélioré
result = crew.kickoff(inputs={'topic': 'AI in healthcare'})
print(result)
```




## 6. crew.py

L'objectif principal du fichier `crew.py` est d'exécuter le processus en utilisant les agents et les tâches définis précédemment. Ce script configure une équipe (`crew`) composée des agents de recherche et de rédaction, puis lance le processus pour effectuer les tâches de manière séquentielle. Le résultat final est imprimé pour vérification.


### Importation des modules nécessaires

**But :** Importer les classes et objets nécessaires pour définir et exécuter le processus.

**Code :**
```python
from crewai import Crew, Process
from agents import researcher, writer
from task import research_task, write_task
```

**Explication :**
- **`Crew` et `Process`** : Importés depuis la bibliothèque `crewai`, ils permettent de former une équipe d'agents et de définir le type de processus d'exécution.
- **`researcher` et `writer`** : Agents de recherche et de rédaction importés depuis le fichier `agents.py`.
- **`research_task` et `write_task`** : Tâches de recherche et de rédaction importées depuis le fichier `task.py`.

### Formation de l'équipe technique

**But :** Configurer l'équipe d'agents avec des paramètres spécifiques pour l'exécution des tâches.

**Code :**
```python
# Formation de l'équipe technique avec des configurations améliorées
crew = Crew(
    agents=[researcher, writer],
    tasks=[research_task, write_task],
    process=Process.sequential,  # Exécution séquentielle des tâches
    memory=True,
    cache=True,
    max_rpm=100,
    share_crew=True
)
```

**Explication :**
- **`agents`** : Liste des agents impliqués dans le processus, ici `researcher` et `writer`.
- **`tasks`** : Liste des tâches à exécuter, ici `research_task` et `write_task`.
- **`process`** : Définition du type de processus, ici `Process.sequential` pour une exécution séquentielle.
- **`memory`** : Activée pour permettre aux agents de conserver les informations entre les tâches.
- **`cache`** : Utilisé pour optimiser les performances en stockant temporairement les données.
- **`max_rpm`** : Limite le nombre maximal de requêtes par minute à 100 pour éviter la surcharge.
- **`share_crew`** : Permet de partager l'équipe d'agents entre différents processus.

### Lancement du processus d'exécution des tâches

**But :** Démarrer le processus d'exécution des tâches et imprimer les résultats.

**Code :**
```python
# Lancement du processus d'exécution des tâches avec retour d'information amélioré
result = crew.kickoff(inputs={'topic': 'AI vs ML VS DL VS Data Science'})
print(result)
```

**Explication :**
- **`kickoff`** : Méthode utilisée pour démarrer le processus avec les entrées spécifiées. Ici, le sujet est `AI vs ML VS DL VS Data Science`.
- **`print(result)`** : Affiche le résultat de l'exécution du processus, permettant de vérifier le bon déroulement et le contenu généré.

---
###  Code complet `crew.py`

Ce fichier `crew.py` est conçu pour orchestrer l'exécution des tâches de recherche et de rédaction en utilisant les agents définis. Il permet de structurer le travail de manière séquentielle et de s'assurer que les informations sont traitées et stockées efficacement, garantissant ainsi une production de contenu cohérente et de haute qualité.



```python
from crewai import Crew, Process
from agents import researcher, writer
from task import research_task, write_task

# Formation de l'équipe technique avec des configurations améliorées
crew = Crew(
    agents=[researcher, writer],  # Liste des agents impliqués dans le processus
    tasks=[research_task, write_task],  # Liste des tâches à exécuter
    process=Process.sequential,  # Exécution séquentielle des tâches (option par défaut)
    memory=True,  # Activation de la mémoire pour conserver les informations entre les tâches
    cache=True,  # Utilisation du cache pour optimiser les performances
    max_rpm=100,  # Limite le nombre maximal de requêtes par minute à 100
    share_crew=True  # Permet de partager l'équipe d'agents entre différents processus
)

# Lancement du processus d'exécution des tâches avec retour d'information amélioré
result = crew.kickoff(inputs={'topic': 'AI vs ML VS DL VS Data Science'})
print(result)
```



