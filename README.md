Guessic Game

	Are you a music lover? Do you like to solve puzzles? Guessic Game is definitely for you! It's easy and fun.
	You will be able to read 1- 2 lines of the song lyrics and the random arrangement of the alphabets of the song title.
	Even if you are not a music crazy, the game is still for you because you can solve the alphabet puzzle!!
	Try it out and challenge your friends to get GOLD on Guessic!


	##Instruction

	1. If you are the first time player, click 'How to play!' button. After you read the instruction, you can click 'Play' to start the amazing Guessic game.
	2. If you are familiar with the app, you can directly click 'Play' button on the main page, and then, click 'Start' button and you can start playing the game!! 
	3. You will see 5 questions in this game.
	4. You can guess the song name from its lyrics or you can solve the alphabet puzzle by rearranging them into a song title.
	5. PRESS 'Enter' whenever you finished answering a question.
	6. Do the questions IN ORDER.
	7. Click 'Submit to check your score' button to see your score and medal.
	8. Click 'Restart' if you want to restart the game! The questions will not be the same!!
	9. Click 'How to play!' button on the lower right side of the screen if you want to read the instruction in the mid of the game and can go back to the game screen.
	10. Click 'Back to menu' from the 'How to play!' screen and click 'Quit' to quit the app.
	11. The quit button is in the main screen.


	##Code Description

	5 screens in the app: MenuScreen, InstructionScreen, SettingsScreen, StartScreen, and PlayScreen.
	MenuScreen: 
			Created 2-cols GridLayout for 4 main features (Play, Settings, How to play, and Quit). 
			Functions to change different screens
			4 main buttons, when pressed, the screen changes respectively under the control of screen manager depending on the button the user pressed. 
		
	InstructionScreen:
			Created the BoxLayout so that the instruction can be in one long column and added the required label and button to the layout
			AnchorLayout ActionButton to make the user easier to go back to the main screen.
			
	SettingsScreen:
			Currently, setting screen has basic features.
			
	StartScreen:
			Created a layout with some basic features from the menu screen and the additional 'Start' button to change into the PlayScreen.
			Made the screen switches function properly calling the correct functions when pressed.
			
	PlayScreen:
			Added layout and set the variables which will be necessary to use in python functions
			
			get_question() function: returns the random question list from the song dictionary and the function is called before creating the labels.
			
			append_list() function: appends the user text input into a list to compare the answers. once the user presses 'Enter', the input will be appended to the list.
			
			get_answerscore() function: returns a list of contents(1, 0) [1 = correct, 0 = wrong] and comparing each answer from the user input list to the respective standard answer using 'for' loop and the indices of both lists. 
			
			Created the labels and TextInput for the game using 'for' loop. 
			When the submit button is pressed, the calculate_score() function is called. Inside the calculate_score() function, the get_answerscore() function is called to get the score_list.
			
			calculate_score() function: returns a string with the score and the medal. has states to calculate the scores. 
										[State 0]scores will be added +1 if the user input is correct, but the one above or below the current correct answer are wrong.
										[State 1]scores will be added +2 if the user inputs are subsequently correct for 2 questions.
										[State 2]scores will be added +3 if the user inputs are subsequently correct for 3 and more questions.
										btn_counter is added to avoid unnecessary score addition in the game.
										Compare the total score to the standard score list for the type of medal.
			recreate(): remove the entire layout and reset all variables from the PlayScreeen class. The scores will be counted from 0 again and the state will start from 0 again.
						The whole layout is recreated to avoid the text overlap on the labels and the score counter issues.
	
	GuessicApp(App): added the screens to the screen manager so that the screen changes function well when the functions are called. 
				
				