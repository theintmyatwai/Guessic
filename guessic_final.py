import random
import kivy
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button 
from kivy.uix.label import Label
from kivy.app import App
from kivy.core.window import Window 
from kivy.uix.actionbar import ActionBar, ActionItem, ActionButton, ActionPrevious, ActionOverflow
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.textinput import TextInput


    
class MyLabel(Label):

    def __init__(self, **kwargs):
        Label.__init__(self, **kwargs)
        self.bind(size=self.setter('text_size'))
        self.padding = (20, 20)
        self.font_size= 24
        #self.color = (0, 0, 0, 0)
        self.halign = 'center'
        self.valign ='middle'
        
class QnLabel(Label):

    def __init__(self, **kwargs):
        Label.__init__(self, **kwargs)
        self.bind(size=self.setter('text_size'))
        self.padding = (20, 20)
        self.font_size= 18
        #self.color = (0, 9, 2, 1)
        self.halign = 'center'
        self.valign ='middle'
        
class MyTextInput(TextInput):

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.hint_text='enter a song name'
        #self.input_filter = 'string'
        self.font_size = 40
        
class MenuScreen(Screen):

    def __init__(self, **kwargs):   #original def init(..):
        Screen.__init__(self, **kwargs)
        self.layout =GridLayout(cols = 2)
        #create a setting button
        self.settings_button = Button(text ="Settings", 
                   font_size =34, 
                   background_color =(2, 0, 6, 1), 
                   size =(50, 32), 
                   color =(0, 200, 0, 5),   #blue color
                   size_hint =(.2, .2), 
                   pos =(-100, 0), 
                   on_press = self.change_to_setting)
        #create quit button
        self.quit_button = Button(text='Quit', 
                   font_size =34,
                   background_color = (1 , 2, 6, 2),
                   color =(0, 200, 0, 5),
                   size = (13, 13),
                   on_press=self.quit_app)
        #create play button
        self.play_button = Button(text='Play',
                   font_size = 34, 
                   background_color = (6 ,2, 2, 1),
                   color =(0, 200, 0, 5),
                   on_press = self.change_to_start)
        #create instruction button
        self.instruction_button = Button(text = '   How to play! \nPlease read me!',
                   font_size= 34,
                   background_color = (2 , 5, 2, 1),
                   color =(0, 200, 0, 5),
                   on_press = self.change_to_instruction)
        #add the buttons to the layout
        self.layout.add_widget(self.play_button)
        self.layout.add_widget(self.settings_button)
        self.layout.add_widget(self.instruction_button)
        self.layout.add_widget(self.quit_button)
        

        self.add_widget(self.layout)      
    
    def change_to_instruction(self,value):
        self.manager.transition.direction = 'right'
        self.manager.current = 'instruction'  
        
    def change_to_setting(self, value):
        self.manager.transition.direction = 'left'
        self.manager.current = 'settings'  

    def quit_app(self, value):
        App.get_running_app().stop()
        Window.close()

    def change_to_start(self, value):
        self.manager.transition.direction = 'right'
        self.manager.current = 'start'
    
    def quit_app(self, value):
        App.get_running_app().stop()
        Window.close()
        
class InstructionScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        #create a screen layout
        self.layout = BoxLayout()
        
        # Add the texts
        line1 = '<<INSTRUCTION FOR THE GAME>>'
        line2 = '1. You will see 5 questions in this game'
        line3 = '2. You have to rearrange the alphabets into a song name'
        line4= '3. This is very important. Please press "Enter" whenever you finish typing an input'
        line5 = '4. Please click "Submit" button.'
        line6 = '<<<Most importantly, please answer the questions in order and press Enter whenever you finished answering each question.>>>'
        line7 = "That's it. Hope you will enjoy playing this Puzzle Guess game"
        #create instruction label
        self.instruction_label = MyLabel(text='{} \n \n {} \n {} \n {} \n {} \n {} \n \n {}'.format(line1, line2, line3, line4, line5, line6, line7))
        
        #create the play button
        self.play_button = Button(text='Play now!!!',
                            background_color =(1 , 2, 7, 2), 
                            color =(0, 200, 0, 5), 
                            font_size =40, 
                            on_press=self.change_to_play) 
                            
        #add the widgets to the layout
        self.layout.add_widget(self.instruction_label)
        self.layout.add_widget(self.play_button)
        self.add_widget(self.layout)
        
        #back_to_menu button
        self.layout1 = AnchorLayout(anchor_x = 'right', anchor_y = 'bottom')
        self.actionbar_menu = ActionButton(text = 'Back to menu', color =(1, 5, 2, 1),font_size = 20, size =(1, 1), size_hint =(.2, .2), pos = (0, 0), on_press = self.change_to_menu)
        self.layout1.add_widget(self.actionbar_menu)
        self.add_widget(self.layout1)
    def change_to_menu(self, value):
        self.manager.transition.direction = 'right'
        self.manager.current = 'menu'
        
    def change_to_play(self, value):
        self.manager.transition.direction = 'right'
        self.manager.current = 'play'
        
        
class SettingsScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        #create a layout for the setting screeen
        self.layout = BoxLayout()
        
        #create buttons and labels
        self.settings_label = MyLabel(text='Settings \n \n \n Coming soon')
        self.menu_button = Button(text='Back to Menu', 
                                font_size = 34, 
                                background_color = (6 ,2, 2, 1), 
                                color =(0, 200, 0, 5), 
                                on_press=self.change_to_menu)  
        
        #add widgets to the layout
        self.layout.add_widget(self.settings_label)
        self.layout.add_widget(self.menu_button)
        
        self.add_widget(self.layout)
        pass

    def change_to_menu(self, value):
        self.manager.transition.direction = 'right'
        self.manager.current = 'menu'

class StartScreen(Screen):
    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        #create layout for the screen
        self.layout = GridLayout(cols = 1)
        
        #create buttons and labels
        self.game_label = Label(text='WELCOME TO THE GUESSIC GAME!!', font_size = 24)
        
        
        self.start_button = Button(text ="Start", 
                   font_size =34, 
                   background_color =(2 , 5, 2, 1), 
                   color =(0, 200, 0, 5), 
                   width=100,
                   on_press = self.change_to_play)
        self.instruct_button = Button(text ="Read me before you play!!", 
                   font_size =34, 
                   background_color =(0 , 3, 3, 1), 
                   color =(0, 200, 0, 5), 
                   width=100,
                   
                   on_press = self.change_to_instruction)   
        
        
        self.layout.add_widget(self.game_label)
        self.layout.add_widget(self.start_button)
        self.layout.add_widget(self.instruct_button)
        #self.txt_your_score = MyLabel(text = '0')
        #self.layout.add_widget(self.txt_your_score)
        self.add_widget(self.layout)
        #create layout 1 for 'back' button at the corner
        self.layout1 = AnchorLayout(anchor_x = 'right', anchor_y = 'bottom')
        self.actionbar_menu = Button(text = 'Back to home', background_color =(0, 0, 5, 5), size =(1, 0.5), font_size = 20, size_hint =(.2, .2), color =(1, 5, 2, 1), pos = (0, 0), on_press = self.change_to_menu)
        self.actionbar_score = MyLabel(text = 'Score')
        self.layout1.add_widget(self.actionbar_menu)
        self.add_widget(self.layout1)


    def change_to_play(self, value):
        self.manager.transition.direction = 'left'
        self.manager.current = 'play'

    def change_to_menu(self, value):
        self.manager.transition.direction = 'right'
        self.manager.current = 'menu'
        
    def change_to_instruction(self,value):
        self.manager.transition.direction = 'right'
        self.manager.current = 'instruction' 
        
class PlayScreen(Screen):

    def __init__(self, **kwargs):
        Screen.__init__(self, **kwargs)
        #create the variable score_display
        self.score_display = 0
        
        #create a grid layout with 2 cols
        self.layout = GridLayout(cols = 2)
        
        #create a list for input
        self.input_list =[]  
        
        #for qn no by random choice
        self.alist = []
        
        #create a variable for the total score
        self.score_display = 0
        
        #create submit button counter
        self.btn_counter = 0

        
        #the questions and answers dict for the game
        self.qn_dic ={'Title: mdonykc anee \nAnd oh my, I, I, I like your style': 'dance monkey', 
"Title: eonttnnisi \nMake sure that you don't need no mentions":'intentions', 
'Title: hkbm ye terraa \nYou say my name like I have never heard before':'break my heart',
'Title: lreiccs \nSeasons change and our love went cold': 'circles', 
"Title: eoremmis \nEverybody hurts someday, ayy ayy \nBut everything gon' be alright": 'memories', 
"Title: g dbya \nI'm that bad type \nMake your mama sad type": 'bad guy',
'Title: ernaisto \nI love it when you call me---': 'senorita',
"Title: o aordeuy \nYou don't have to say you're mine":'adore you', 
"Title: youpenasll \nI'm a sad girl, in this big world":'supalonely',
"Title: mnet ia \nDon't tell me you're falling \nWith your feet still on the ledge" : 'mean it',
"Title: rdnbeofyi\nI don't wanna keep you waiting ": 'boyfriend', 
"Title: maaicn\nThat I'm such a stalker, a watcher, a psychopath": 'maniac',
"Title: afllgin \nFall for me, I wanna know you feel how I feel for you, love": 'falling',
"Title: mmuyy \nYeah, you got that-----": 'yummy',
"Title: aennxor \nNever gonna love me but it's alright": 'roxanne'}

        #getting the qn list for the player
        self.qn_list = self.get_question()
        
        self.state = 0
        for qn in self.qn_list:
            #create labels for questions 
            self.l = QnLabel(text=qn)
            self.layout.add_widget(self.l)
            #create the text input boxes for user input
            self.input_amount = MyTextInput(multiline = False)
            self.input_amount.bind(on_text_validate=self.append_list)
            self.layout.add_widget(self.input_amount)
          
        
     
        #create a label to show your total score
        self.score_display_label = MyLabel(text = 'Please answer the questions in order!')
        self.layout.add_widget(self.score_display_label)
        
        #create a button to submit the answer
        submit_button = Button(text ="Submit to check your score", 
                   font_size ="24sp", 
                   background_color =(10, 2, 2, 1), 
                   color =(0, 200, 0, 5), 
                   width=100,
                   on_press = self.calculate_score)
        self.layout.add_widget(submit_button)

        
        #add restart and how to play buttons
        self.restart_button = Button(text = 'Restart', font_size ="22sp", 
                   background_color =(5, 2, 4, 1), 
                   color =(0, 200, 0, 5), 
                   width=100,
                   on_press = self.recreate)
        self.layout.add_widget(self.restart_button)
        
        self.instru_button = Button(text = 'HOW TO PLAY!', font_size ="22sp", 
                   background_color =(5, 4, 2, 1), 
                   color =(0, 200, 0, 5), 
                   width=100,
                   on_press = self.change_to_instruction)
        self.layout.add_widget(self.instru_button)
        self.add_widget(self.layout)
        
    def recreate(self, instance):
        #remove the layout when the function is called
        self.remove_widget(self.layout)
        
        #update input list
        self.input_list =[]
        
        #create a grid layout with 2 cols
        self.layout = GridLayout(cols = 2)
        
        #reset the state
        self.state = 0
        
        #for qn no by random choice
        self.alist = []
        
        #reset the total score
        self.score_display = 0
        
        #reset the button counter
        self.btn_counter = 0
        
        self.qn_list = self.get_question()
        for qn in self.qn_list:
            self.l = ''    
            self.l = QnLabel(text=qn)
            self.layout.add_widget(self.l)
            self.input_amount = MyTextInput(multiline = False)
            self.input_amount.bind(on_text_validate=self.append_list)
            self.layout.add_widget(self.input_amount)
        
        
        #create a label to show your total score
        self.score_display_label = MyLabel(text = 'Please answer the questions in order!')
        self.layout.add_widget(self.score_display_label)
        
        #create a button to submit the answer
        submit_button = Button(text ="Submit to check your score", 
                   font_size ="24sp", 
                   background_color =(10, 2, 2, 1), 
                   color =(0, 200, 0, 5), 
                   width=100,
                   on_press = self.calculate_score)
        self.layout.add_widget(submit_button)

        #print(self.input_list)
        
        self.restart_button = Button(text = 'Restart', font_size ="22sp", 
                   background_color =(5, 2, 4, 1), 
                   color =(0, 200, 0, 5), 
                   width=100,
                   on_press = self.recreate)
        self.layout.add_widget(self.restart_button)
        
        self.instru_button = Button(text = 'HOW TO PLAY!', font_size ="22sp", 
                   background_color =(5, 4, 2, 1), 
                   color =(0, 200, 0, 5), 
                   width=100,
                   on_press = self.change_to_instruction)
        self.layout.add_widget(self.instru_button)
        self.add_widget(self.layout)
    
    #function for putting user input into one list
    def append_list(self, value):
    
        self.input_list.append(str(value.text))
        
    
        return self.input_list
            
        #print(self.input_list)


    def get_question(self):
        
        #for the selected qns
        new_list = []
        j = 0
        
        
        while j < 5:
            # Get random number in range 0 through 14.
            n = random.randint(0, 14)
            if n not in self.alist:
                self.alist.append(n)
                j += 1
            else:
                pass
                
        #for m in range(len(self.input_list)):
        for k in self.alist:
                
            #the items in the list as list_item
            
            for key, value in self.qn_dic.items():
                if key == list(self.qn_dic)[k]:
                    dic_value = value
                    new_list.append(key)
        return new_list
        
    def get_answerscore(self):
        
        #for the points the player get
        score_list = []
        
        x = self.input_list
        print(x)
        #i constraint need to change depending on the number of questions i want
        
        for i in range(len(x)):
            for j in range(len(self.qn_list)):
                if i == j:
                    dic_value = self.qn_list[j]
                    
                    list_value = x[j].lower()
                    print(self.qn_dic[dic_value], list_value)
                    if self.qn_dic[dic_value].lower() == list_value.lower():
                        
                        score_list.append(1)
                        #print(True)
                        #print(score_list)
                    else:
                        score_list.append(0)

        return score_list
    
    
    def calculate_score(self, instance):
        
        score_list = self.get_answerscore()
        
        if score_list == []:
            self.score_display_label.text = 'Please input the answers!'
            return (self.score_display_label.text)
        else:
            if self.btn_counter == 0:
                self.btn_counter +=1
                
                for i in score_list:
                    if self.state == 0:
                        if i == 0:
                            self.score_display += 0
                            self.state = 0 
                            print(1)
                        else:
                            self.score_display += 1
                            self.state = 1
                            print(2)
                    elif self.state == 1:
                        if i == 0:
                            self.score_display += 0
                            self.state = 0
                            print(3)
                        else:
                            self.score_display += 2
                            self.state = 2
                            print(4)
                    elif self.state == 2:
                        if i == 0:
                            self.score_display += 0
                            self.state = 0
                            print(5)
                        else:
                            self.score_display += 3
                            self.state = 2
                            print(6)
               
            else:
                self.score_display = self.score_display
                print(7)
                
            #comparing the score range
            if 9<=self.score_display<=12:
                statement = 'Gold'
            elif 6<= self.score_display <9:
                statement = 'Silver'
            elif 4<= self.score_display < 6:
                statement = 'Bronze'
            else:
                statement = 'Failed'
  
            self.score_display_label.text = 'Your score: {}, {}'.format(self.score_display, statement)
            return self.score_display_label.text
            
    
    def change_to_instruction(self,value):
        self.manager.transition.direction = 'right'
        self.manager.current = 'instruction' 
            
class GuessicApp(App):
    
    
    def build(self):
        sm = ScreenManager()
        ms = MenuScreen(name='menu')
        st = SettingsScreen(name='settings')
        ss = StartScreen(name = 'start')
        ps = PlayScreen(name = 'play')
        iss = InstructionScreen(name = 'instruction')
        sm.add_widget(ms)
        sm.add_widget(st)
        sm.add_widget(ss)
        sm.add_widget(ps)
        sm.add_widget(iss)
        sm.current = 'menu'
        return sm
        
        
if __name__ == '__main__':
    GuessicApp().run()