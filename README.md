# Basketball Team Stats Tool

## Getting Started

### Installation

Clone and navigate into the repo:

```zsh
git clone https://github.com/ajtran303/bball-stats.git
cd bball-stats
```

### Run the tests

There should be 21 passing tests:

```zsh
python3 -m unittest
```

### Generate a coverage report (optional)

1. Activate a virtual environment to install the `coverage` package:

```zsh
python3 -m venv .venv/
source .venv/bin/activate
pip install -r requirements.txt
```

2. Generate the report and it should show 100% coverage on `application.py`:

```zsh
coverage run -m unittest && coverage report
```

3. When you are done, deactivate and remove your virtual environment.

```zsh
deactivate && rm -rf .venv/
```

## Example Usage

### Start the program 

From the command line:

```zsh
python3 application.py
```

Navigate through the main menu by selecting an option:

```m
Welcome to the Basketball Stats tool!
MAIN MENU

1) Display Team Stats
2) Quit

Enter an option:
_
```

Next, you will be prompted to select a team:

```m
SELECT TEAM:
1) Panthers
2) Bandits
3) Warriors

Enter an option:
_
```

Selecting a valid option will display that team's statistics:

- Total Players
- Total Experienced Players
- Total Inexperienced Players
- Average Height of Players
- Names of Players
- Names of Guardians of Players

Selecting a non-valid option will prompt you to pick again!

### Quitting the Program

Select option `2` at the `MAIN MENU`.

Or use the keyboard shortcut `<control>+C` to immediately quit.