# GitHub User Activity

A Python-based utility that interfaces with the GitHub REST API to fetch and display real-time user statistics, repository counts, and language distribution.



## Features

* **User Overview:** Instantly retrieve display names, follower counts, and public repo totals.
* **Tech Stack Analysis:** Automatically scans all public repositories to identify and count the primary programming languages used.
* **API Integration:** Powered by `PyGithub` for reliable data fetching.



## Prerequisites

Before running the script, ensure you have the following:

1.  **Python 3.x** installed.
2.  **PyGithub Library**: Install it via pip:
    ```bash
    pip install PyGithub
    ```
3.  **GitHub Personal Access Token**: Generate a token with `read:user` permissions from your [GitHub Settings](https://github.com/settings/tokens).



## Usage

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    cd your-repo-name
    ```

2.  **Configure your Token:**
    Open the script and replace `"YOUR GITHUB TOKEN"` with your actual Personal Access Token.

3.  **Run the script:**
    ```bash
    python main.py
    ```

4.  **Input:** Enter any GitHub username when prompted to see their stats.



## Example Output

```text
Enter GitHub username: octocat
User: The Octocat
Public Repositories: 8
Followers: 3500
Languages Used: {'Ruby': 2, 'HTML': 3, 'JavaScript': 3}
```

Thanks roadmap.sh for projects ideas
link: https://roadmap.sh/projects/github-user-activity

