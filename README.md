
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

Pour installer les dépendances listées dans `requirements.txt`, utilisez la commande `pip install -r requirements.txt`. Vérifiez ensuite que toutes les bibliothèques ont été installées correctement. En cas d'erreur d'installation, vérifiez les versions des bibliothèques pour résoudre les conflits potentiels et consultez la documentation spécifique des bibliothèques concernées pour des solutions précises. Si nécessaire, mettez à jour les bibliothèques avec la commande `pip install --upgrade nom_de_la_bibliothèque`.

```
crewai
python-dotenv
crewai_tools
load_dotenv
```

Chaque bibliothèque a un rôle spécifique :
- **CrewAI** : Pour la gestion des agents et des tâches.
- **python-dotenv** : Pour la gestion des variables d'environnement.
- **crewai_tools** : Pour des outils supplémentaires liés à CrewAI.
- **load_dotenv** : Fonction de la bibliothèque **python-dotenv** permettant de charger les variables d'environnement à partir d'un fichier `.env`.




---

# Présentation du code du projet étape par étape

Ce projet utilise le framework Crew AI pour sélectionner des vidéos d'une chaîne YouTube en fonction d'une thématique donnée, puis transformer ces vidéos en articles de blog.

## Structure du projet

Le projet est structuré en plusieurs fichiers principaux, listés dans l'ordre de réalisation logique :

1. `requirements.txt`
2. `tools.py`
3. `agents.py`
4. `tasks.py`
5. `crew.py`

### 1. `requirements.txt`

Liste des dépendances nécessaires pour le projet.

```
crewai
python-dotenv
crewai_tools
load_dotenv
```

### 2. `tools.py`

Ce fichier initialise l'outil de recherche de chaînes YouTube utilisé par les agents.

```python
from crewai_tools import YoutubeChannelSearchTool

# Initialiser l'outil avec un handle spécifique de chaîne YouTube
yt_tool = YoutubeChannelSearchTool(youtube_channel_handle='@pierrebittner')
```

### 3. `agents.py`

Ce fichier définit les agents utilisés dans le processus.

- **Chercheur de contenu** (`researcher`) : Cet agent est responsable de la recherche de contenu vidéo pertinent sur YouTube.
- **Rédacteur** (`writer`) : Cet agent est chargé de transformer le contenu des vidéos en articles de blog captivants.

```python
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
```

### 4. `tasks.py`

Ce fichier définit les tâches spécifiques que les agents doivent accomplir.

- **Recherche** (`research_task`) : Identifier et analyser les vidéos YouTube pertinentes pour un sujet donné.
- **Rédaction** (`write_task`) : Résumer les informations obtenues des vidéos pour créer un article de blog.

```python
from crewai import Task
from tools import yt_tool
from agents import researcher, writer

# Tâche de recherche
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
```

### 5. `crew.py`

Ce fichier configure et lance l'équipe d'agents et les tâches associées.

```python
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
```

## Installation et utilisation

1. **Clonez le dépôt :**
    ```bash
    git clone https://github.com/votre-utilisateur/votre-repo.git
    cd votre-repo
    ```

2. **Installez les dépendances :**
    ```bash
    pip install -r requirements.txt
    ```

3. **Configurez les variables d'environnement :**
    - Créez un fichier `.env` à la racine du projet avec les clés API nécessaires :
      ```
      OPENAI_API_KEY=votre_cle_api_openai
      ```

4. **Lancez le programme :**
    ```bash
    python crew.py
    ```

## Contribuer

Les contributions sont les bienvenues ! Veuillez suivre les étapes ci-dessous pour contribuer :

1. **Fork** le projet.
2. **Clone** votre fork.
3. Créez une nouvelle branche (`git checkout -b feature/AmazingFeature`).
4. Faites vos modifications.
5. **Commit** vos changements (`git commit -m 'Add some AmazingFeature'`).
6. **Push** vers la branche (`git push origin feature/AmazingFeature`).
7. Ouvrez une **Pull Request**.

## Licence

Distribué sous la licence MIT










# Bonnes pratiques


### Cacher les clés API

- **python-dotenv** : Cette bibliothèque permet de gérer les variables d'environnement en chargeant le contenu d'un fichier `.env` dans les variables d'environnement du système. Cela facilite la configuration des applications sans avoir à coder en dur des informations sensibles ou spécifiques à l'environnement, comme les clés API, les mots de passe, ou d'autres paramètres de configuration.

- **load_dotenv** : C'est une fonction de la bibliothèque **python-dotenv**. Elle permet de charger automatiquement les variables d'environnement définies dans un fichier `.env` situé à la racine du projet ou dans un répertoire spécifié. En exécutant cette fonction au début du script, toutes les variables définies dans le fichier `.env` sont ajoutées aux variables d'environnement du système, ce qui les rend accessibles via `os.getenv` ou `os.environ` dans le code Python.

Voici un exemple d'utilisation typique :

1. Créez un fichier `.env` avec le contenu suivant :

   ```
   SECRET_KEY=ma_clé_secrète
   DATABASE_URL=postgres://user:password@localhost:5432/ma_base_de_données
   ```

2. Dans votre script Python, utilisez `load_dotenv` pour charger ces variables :

   ```python
   from dotenv import load_dotenv
   import os

   # Charge les variables d'environnement à partir du fichier .env
   load_dotenv()

   # Accède aux variables d'environnement
   secret_key = os.getenv('SECRET_KEY')
   database_url = os.getenv('DATABASE_URL')

   print(f'Secret Key: {secret_key}')
   print(f'Database URL: {database_url}')
   ```

Ainsi, **python-dotenv** et **load_dotenv** permettent une gestion centralisée et sécurisée des configurations sensibles de l'application.






