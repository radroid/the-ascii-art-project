# The Ascii Art Project
Welcome to The Ascii Art Project!
> *This initial project layout or template was created using [auto-project-builder](https://www.github.com/radroid/auto-project-builder) created by **RaDroid**.*
> *It is a library to automate the boring process of creating project files before you start working on it.*

It is a CLI program that takes a picture, converts it into an ASCII art and prints it on the shell (terminal) window.

[![that's how](https://forthebadge.com/images/badges/thats-how-they-get-you.svg)](https://forthebadge.com) 
[![Built with](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com) 
[![Makes People smile](https://forthebadge.com/images/badges/makes-people-smile.svg)](https://forthebadge.com) 

*tags: ASCII, ASCII art, picture on terminal, terminal picture*

![Workflow build status](https://img.shields.io/github/workflow/status/radroid/the-ascii-art-project/Python%20application?style=for-the-badge)
[![License](https://img.shields.io/github/license/radroid/the-ascii-art-project?style=for-the-badge)](https://github.com/radroid/the-ascii-art-project/blob/master/LICENSE)
![Last Commit](https://img.shields.io/github/last-commit/radroid/the-ascii-art-project?style=for-the-badge)
[![Closed Pull Requests](https://img.shields.io/github/issues-pr-closed/radroid/the-ascii-art-project?style=for-the-badge)](https://github.com/radroid/the-ascii-art-project/pulls?q=is%3Apr+is%3Aclosed)
[![Open Pull Requests](https://img.shields.io/github/issues-pr/radroid/the-ascii-art-project?style=for-the-badge)](https://github.com/radroid/the-ascii-art-project/pulls) 

## Table of Contents
  - [Table of Contents](#table-of-contents)
  - [Setup](#setup)
    - [For a Mac/Linux User](#for-a-maclinux-user)
    - [For a Developer](#for-a-developer)
      - [Code Review](#code-review)
  - [Project Status](#project-status)
  - [Support](#support)
  - [License](#license)

## Setup
### For a Mac/Linux User

**Prerequisites:**
- You know the basics of using terminal on Mac/Linux.
  * How to use `cd` to change the current directory
  * Use `ls` to list directories in the current directory.
- You have the latest version of python installed.

**1. Clone this repository into your projects folder, i.e. the folder you would like to create projects in.**

> *Note: use `cd` command to navigate to your projects directory.*

```bash
git clone https://github.com/radroid/the-ascii-art-project.git
```

**2. Create a virtual environment in the auto-project-builder directory.**
```bash
cd the-ascii-art-project
python3 -m venv virtual_env
```

**3. Activate environment and install the required modules.**

> *Note: check your python version by using `python --version`.*

```bash
source virtual_env/bin/activate
pip install -r requirements.txt
```

**4. Add picture to `images` directory.**
Use Finder/File Explorer to add the picture you would like to convert to ASCII art in the `the-ascii-art-project/images` directory.
*Remember the name of the file with its extension as it will be required later.*

**5. Run the project.**
```bash
python ascii_art.py
```
Follow the instructions in the program. 
> *Note: remember to zoom out before the program prints the final command. This is to ensure the terminal window can be sized to meet the demands of the picture.*

You may not be able to see the text in the terminal window due to the zoom, but if you feel like your computer will get stuck, type `clear` before zooming back in.


### For a Developer
#### Code Review
I would really appreciate any kind of feedback on the way I have chosen to tackle this problem. Keep in mind, I am a beginner and even a small piece of advice can go a long way. **Be as critical as you can!** Thank you for spending time to look at my code.

I would appreciate comments on anything and everything, but here are some to get you started:
- Architecture or **Design** of the code.
- Style and **Documentation**.
- **Testing**: this one can be get time consuming compared to the others.

New to code reviewing? Even I am. You can refer to [this guide](https://www.kevinlondon.com/2015/05/05/code-review-best-practices.html) for advice on Code Reviews.

## Project Status
Created the project on 

## Support
I am looking for a job ooportunity as a Software Developer and eventually Machine Learning Engineer in Canada. It would mean a lot if we could connect and discuss what we can do for each other.
Follow and Reach out to me one of the following places!

![Github Follow](https://img.shields.io/github/followers/radroid?label=Follow&style=social) ![Twitter Follow](https://img.shields.io/twitter/follow/?label=Follow&style=social)

## License

[![License](https://img.shields.io/github/license/radroid/the-ascii-art-project?style=for-the-badge)](https://github.com/radroid/the-ascii-art-project/blob/master/LICENSE)

**[MIT license](https://opensource.org/licenses/MIT)**
