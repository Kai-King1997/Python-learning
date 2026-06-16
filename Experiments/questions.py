git_commands = {
    "status": {
        "command": "git status",
        "description": "Shows the current state of your repository."
    },
    "list": {
        "command": "ls",
        "description": "Shows files in folder."
    },
    "list all": {
        "command": "ls -a",
        "description": "Shows all file in folder, even hidden"
    },
    "folder source": {
        "command": "explorer .",
        "description": "Opens folder source."
    },
    "commit history": {
        "command": "git log",
        "description": "Full commit history."
    },
    "commit history summary": {
        "command": "git log --oneline",
        "description": "Summarized full commit history."
    },
    "compare commits": {
        "command": "git diff <id> <id>",
        "description": "Comparing two commits between each other. Note: First <id> is treated as the base commit to compare the other to."
    },
    "move to staging": {
        "command": "git add --all",
        "aliases": [
            "git add -A"
        ],
        "description": "Moves all project changes to Staging."
    },
    "combine branches": {
        "command": "git merge main -m 'note'",
        "description": "Branches have been combined and other branch matches main changes."
    },
    "combine specific branches": {
        "command": "git merge <branch name> -m 'note'",
        "description": "Merges selected branch with main."
    },
    "commit changes": {
        "command": "git commit -m 'note'",
        "description": "Commits changes with note."
    },
    "send local to remote": {
        "command": "git push origin main",
        "description": "Sends local changes to the remote."
    },
    "fetch remote changes": {
        "command": "git fetch",
        "description": "Bringing remote changes into your local repository, but not merging them yet."
    },
    "merge remote": {
        "command": "git merge",
        "description": "Merging the remote changes to your local repository."
    },
    "fetch and merge remote": {
        "command": "git pull",
        "description": "Fetching and merging directory to reflect remote changes."
    },
    "resore to last commit": {
        "command": "git restore",
        "description": "Resores state of repository to last commit and undoes local uncommitted changes."
    },
    "restore file to last commit": {
        "command": "git restore <name>.txt",
        "description": "Restores file to last commit."
    },
    "restore folder to last commit": {
        "command": "git restore <directory name>",
        "description": "Restores the entire folder to the last commit."
    },
    "restore repository to last commit": {
        "command": "git restore .",
        "description": "Restores entire repository to last commit."
    },
    "file/directory to last commit": {
        "command": "git restore --staged <file/directory>",
        "description": "Brings any file or directory back to last committed state."
    },
    "undo commit": {
        "command": "git revert",
        "description": "Used to undo the changes made in a previous commit but does not delete old commit, instead creating a new one that just reverses those changes."
    }
}
navigation = {
    "go to folder": {
        "command": "cd <enter-name-here>",
        "description": "Navigates into folder."
    },
    "back up a folder": {
        "command": "cd ..",
        "description": "Move one directory back."
    },
    "see branches": {
        "command": "git branch",
        "description": "See all branches off of main in project."
    },
    "change branch": {
        "command": "git checkout <name>",
        "description": "Changes the current branch to <name>."
    }
}
create_modify = {
    "create folder": {
        "command": "mkdir <enter-name-here>",
        "description": "Creates folder."
    },
    "create txt file": {
        "command": "touch <name>.txt",
        "description": "Creates text file in folder."
    },
    "add": {
        "command": "git add .",
        "description": "Stages all changed files for the next commit"
    },
    "add only new": {
        "command": "git add *",
        "description": "Adds only new or modified files to staging."
    },
    "add branch": {
        "command": "git branch <name>",
        "description": "Add a new branch to the project."
    },
    "delete file": {
        "command": "git rm <name>.txt",
        "description": "Deletes file and stages the change."
    },
    "force delete file": {
        "command": "git rm -f <name>.txt",
        "description": "Forces deletion even with unstaged changes."
    },
    "remove from staging": {
        "command": "git rm --cached <name>.txt",
        "description": "Removes from staging area but keeps it physically in directory."
    },
    "remove folder": {
        "command": "git rm <folder>",
        "description": "Removes folder but not subfolders."
    },
    "remove folder and subs": {
        "command": "git rm -r <folder>",
        "description": "Removes folder and all subfolders."
    },
    "recover files": {
        "command": "git reset --hard",
        "description": "Undoes file deletion"
    },
    "reset folders": {
        "command": "git reset",
        "description": "Pulls all changes back from staging, resetting the folders."
    },
    "reset commit": {
        "command": "git reset HEAD~",
        "description": "Resets commit and brings back to working directory."
    },
    "specific file to stage": {
        "command": "git add <name>.txt",
        "description": "Adds specific file to staging"
    },
    "add all text files": {
        "command": "git add *.txt",
        "description": "Adds all text files in currently directory."
    }
}
stash_commands = {
    "stash work": {
        "command": "git stash",
        "description": "Temporarily set aside your unfinished work to switch to another branch."
    },
    "retrieve stash": {
        "command": "git stash pop",
        "description": "Retrieve any stashed work."
    },
    "retrieve specific stash": {
        "command": "git stash pop stash@{id number}",
        "description": "Retrieve specific stash number."
    },
    "retrieve and keep": {
        "command": "git stash apply",
        "description": "Retrieve stashed work as well as keeping it in the stash for later."
    },
    "retrieve and keep specific": {
        "command": "git stash apply stash@{id number}",
        "description": "Retrieve specific stash number as well as keeping it in the stash for later."
    },
    "remove from stash": {
        "command": "git stash drop",
        "description": "Removes a specific stash from the stash list."
    },
    "stash list": {
        "command": "git stash list",
        "description": "See a list of all stashes in directory."
    }
}
command_categories = {
    "Git Commands": git_commands,
    "Navigation": navigation,
    "Create & Modify": create_modify,
    "Stash": stash_commands
}
for category in command_categories:
    print(f"\n=== {category} ===")
    for command in command_categories[category]:
        print(f"\n{command}")
        print(
            f"command:"
            f"{command_categories[category][command]['command']}"
        )
        print(
            f"description:"
            f"{command_categories[category][command]['description']}"
        )
search = input(
    "What command are you looking for? "
    ).lower()
for category in command_categories:
    for command in command_categories[category]:
        if search == command.lower():
            print(f"\ncategory: {category}")
            print(f"\ncommand name: {command}")
            print(
                f"\nCommand: "
                f"{command_categories[category][command]['command']}"
            )
            print(
                f"\nDescription: "
                f"{command_categories[category][command]['description']}"
            )