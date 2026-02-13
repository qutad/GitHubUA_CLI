from github import Github

def main():
    # Replace 'your_access_token' with your actual GitHub access token
    gt = Github("YOUR GITHUB TOKEN")

    user = gt.get_user(input("Enter GitHub username: "))

    print(f"User: {user.name}")
    print(f"Public Repositories: {user.public_repos}")
    print(f"Followers: {user.followers}")


    # getting languages used in user's repositories
    languages = {}
    for repo in user.get_repos():
        lang = repo.language
        if lang:
            languages[lang] = languages.get(lang, 0) + 1

    print(f"Languages Used:{languages}")

if __name__ == "__main__":
    main()