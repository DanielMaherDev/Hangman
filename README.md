![HangMan Hero Image](readmeimages/hero-image.jpg)

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Project Overview](#project-overview)
  - [Goal](#goal)
  - [Technologies used](#technologies-used)
- [UX](#ux)
  - [User Stories](#user-stories)
- [Features](#features)
- [Design](#design)
- [Testing](#testing)
- [Future Features](#future-features)
- [Deployment](#deployment)
- [Cloning](#cloning)
- [Forking](#forking)
- [Credits](#credits)
  - [Code](#code)
    - [Version Control](#version-control)
- [Acknowledgments](#acknowledgments)

## Project Overview
This project is based on the game HangMan.

In this game, the user must guess the full word before hangman is hung. This is done by guessing a letter in the word.

If the guess is right, it is placed in the blank spaces that make up the word.
If it is not, the user loses a life. The word must be guessed before the user runs out of lives.

Furthermore, I have added different difficulties to the game, along with a leaderboard displaying the top 10 players.

## Goal

My goal is to utilise my knowledge of python to create a game which gathers user inputs and provides responses based on the input given.
I utilised this to create the main function of the game, as well as to collect data to add to the leaderboard.

## Technologies used
- <b>Python</b> for the main game-play.
- <b>[Heroku](https://heroku.com)</b> to deploy the website.
- <b>[GitHub](https://github.com/)</b> as a remote repository.
- <b>[GitPod](https://www.gitpod.io)</b> as a local repository and for editing code
- <b>[LucidApp](https://lucid.app/)</b> for creating charts
- <b>[Google Sheets](https://sheets.google.com/)</b> (API) for the leadboard

## UX

### User Stories

| User story        | Implementation |     
| ------------- |:-------------|
| User would like to select their preferred difficulty| Set difficulty at game start |     
| User would like a visual representation of their progress in the game| Added HangMan ASCII images to correlate with progress in game |     
| User would like to compare their score with that of other players| Add a leaderboard which calculates top 10 players |

## Features

### Welcome Section

The welcome section is the screen the end user is presented with on page load. 
It provides the user with an introduction, along with an input to enter the users name. This is validated before continuing.

![Welcome Section](readmeimages/welcome-section.jpg)

### Options Section

The options section allows the user to input what they would like to do 
i.e. Start game, view rules, view leaderboard.
Variations of this screen appear depending on what section you are currently in.

![Options Section](readmeimages/options-section.jpg)

### Main Game Section

The main game screen provides all information regarding the users current game of hangman.
This includes the remaining lives, previous guesses, and the correct guesses in the word.

![Main Game Section](readmeimages/main-game-section.jpg)

### Leaderboard Section

The leaderboard screen provides the user with information on the current highest scores. This is calculated and returned from a Google Sheet
![Leaderboard Section](readmeimages/leaderboard-section.jpg)

## Design

I designed this project on the basis of the below flowchart. This is a simple idea of the structure I wanted to follow.
![Flowchart](readmeimages/flowchart.jpg)

## Bugs

Any bugs listd below have now been fixed

| Bug        | Fix |     
| ------------- |:-------------|
| Upon playing the game for the second time within the same session, the previous games guesses would be guessed by default in the second game| I reset the var which holds previous guesses when a new game has been started |     
| On the final question, if the player won the final hangman image would not show| I ammended the way in which the hangman images are chosen from the array | 

## Future Features
- I would like to make it so that the leaderboard functionality (calculations etc) is done within the application.
- I would also like to add different word lists for the different difficulties

## Deployment 
This website is deployed to GitHub.
To deploy to GitHub, I completed the following steps
1. Login or signup to [GitHub](https://github.com/)
2. Find the relevant repo, which is in this case ['answertime'](https://github.com/DanielMaherDev/answertime)
3. Go to the repository settings, and within here select 'pages'
5. Select `main` in the Source drop down box below the 'Build and deployment' title and click save.
6. Wait for the live site to become active. Upon reloading a link will appear for the site

## Cloning
1. On GitHub.com, navigate to the main page of the repository which is ['here'](https://github.com/DanielMaherDev/answertime)
2. Above the list of files, click  Code.
3. Copy the URL for the repository.
4. Open Git Bash.
5. Change the current working directory to the location where you want the cloned directory.
6. Type git clone, and then paste the URL you copied earlier.
7. Press Enter to create your local clone.

## Forking
1. Login or signup to [GitHub](https://github.com/)
2. Find the relevant repo, which is in this case ['answertime'](https://github.com/DanielMaherDev/answertime)
3. Click on the 'Fork' button in the upper left.
4. Your forked version of this repo will be generated!

### Version Control

# Acknowledgments


