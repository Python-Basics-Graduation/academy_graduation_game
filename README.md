# Tooploox Python Academy - Graduation Project

## Installing virtualenv + virtualenvwrapper:

Please try to follow the instructions below to the best of your ability. Setting up virtualenv + virtualenvwrapper can be problematic, but they work like a charm once set up.

We don't want to install Python packages into the system - mostly, because that means that some 6 months down the road you'll have to reinstall the system if you still want to do any software development. We're going to use virtual environments (i.e. "places where you can install packages, but where they cannot affect the system") instead of Docker, because Docker does not allow to (easily) start GUI applications from within it on MacOS. We're using virtualenvwrapper because it makes our lives easier than running naked virtualenv.

* Run `pip install virtualenv`

* Run `pip install virtualenvwrapper`

* Go to your home directory: `cd ~`

* Run `nano .bash_profile`; it will open Nano (a basic text editor) in your terminal. Paste the following at the end of the file (if you get an empty file after opening Nano, just paste it in):

```
export WORKON_HOME=$HOME/.virtualenvs
export VIRTUALENVWRAPPER_PYTHON=/usr/local/bin/python3
source /usr/local/bin/virtualenvwrapper.sh
```

* `ctrl+x` then `y` to save the changes

* Run `source .bash_profile` and then close all Terminal windows you have open.

## Project setup on your computer:

First, make sure that you have git on your computer configured with the same mail as your GitHub account is set.

(Generally I strongly suggest reading the `Uploading code to GitHub - cheatsheet` that is pinned on our `Academy Python` channel.)

* Open a new Terminal window and go to the directory where you want to keep your game (e.g. `workspace`)

* Run `mkdir graduation && cd graduation` to create a `graduation` directory and move into it

* Run `git init` to initialize a git repo in this directory

* Run `git remote add origin https://github.com/blazej-jastrzebski-tooploox/academy_graduation_game.git` to set our GitHub repo as a remote repository that you will use to collaborate.

* Run `git pull origin master` to download the code from the master branch into the directory.

* Run `mkvirtualenv graduation` to create a virtual environment named `graduation`; you can now install Python libraries without littering in the system. **This step might fail**. If this fails, please contact me and **send me the error that you received** and I'll come by your desk and try to fix the issue (or assist you remotely).

* Run `pip install -r requirements.txt`

## Using virtualenv:

* Run `workon graduation` before starting the work for the day. If you forget to do that and run `python main.py` you'll get a `ModuleNotFoundError: No module named 'pyglet'` which is Python's way of saying "you forgot to run `workon graduation`, please do it". If you get that error, **do not run** `pip install -r requirements.txt` **again**.

* Write your code. When you're done and want to exit the virtualenv you can either close the terminal window or run `deactivate`.

* Run `python main.py` to run the game.

* Run `python -m unittest discover` to run the unit tests.

## General Git workflow:

Let's say you will work on the main Menu. Before doing any work, it's best to change to a feature branch (i.e. a path in git that is separate from the main part of the code).

* `git checkout -b BRANCH_NAME` - in this case BRANCH_NAME would be `menu` (let's stick to lowercase branch names, trust me).

* Write & test your code. When you are ready to make a commit (i.e. "ok, I added a complete functionality.")

* `git status` - see all files that changed since the last commit

* `git add FILENAME_1 FILENAME_2` - select the files changes in which you want to be included in the commit

* `git commit` - this starts vi; vi is a modal text editor - before you can write anything there, you need to change into the correct mode. A quick cheatsheet for vi is in the next point

* `git push origin BRANCH_NAME` - pushes the code to the repository on GitHub; people will see your code after they switch the branch in GitHub to `BRANCH_NAME`

* If you feel that your work is done and you want to make a pull request (i.e. "add your functionality to the actual game"), please go to the "Making a Pull Request" section.

## vi cheatsheet:

* `i` - changes into the `insert` mode and allows you to

* write the [commit message](https://chris.beams.io/posts/git-commit/)

* `esc` - leaves any actual mode, goes back to the state that vi is in when you start it

* `shift + zz` - closes an saves any changes that you have made

## Making a Pull Request:

Without getting into the details - rebasing your code is good. We will rebase our code before pull requests to make the world a slightly better place (and make our shit look pro).

* `git checkout master` - go back to the `master` branch

* `git pull origin master` - make sure that you have the most recent version of the code on your local `master` branch

* `git checkout BRANCH_NAME` - go back to your original branch (in our example, `menu`)

* `git rebase master` - move your code "on top of the" `master` branch; there will be conflicts. You can resolve them by opening the files with conflicts, making sure that what's in the file is the code that should be in it, doing `git add FILENAME_1 FILENAME_2` and `git rebase --continue`

* `git push origin BRANCH_NAME` - after completing the rebase

* On GitHub, create the Pull Request. Please add me (Blazej) and the rest of the team as the code reviewers. Please do not complete the PR without my approval.
