from transitions.extensions import GraphMachine
from urllib.request import urlopen
from bs4 import BeautifulSoup

        
class TocMachine(GraphMachine):
    def __init__(self, **machine_configs):
        self.machine = GraphMachine(
            model = self,
            **machine_configs            
        )                
        
    def is_going_to_state16(self, update):
        text = update.message.text        
        if text.lower() == '關於':
            return text.lower() == '關於'
        elif text.lower() == 'about':
            return text.lower() == 'about'                      
                    
    def on_enter_state16(self, update):
        update.message.reply_text("介紹(introduction)：")
        html = urlopen("http://zh.asoiaf.wikia.com/wiki/%E5%86%B0%E4%B8%8E%E7%81%AB%E4%B9%8B%E6%AD%8C")           	       
        background= BeautifulSoup(html.read())
        #print(background)
        ray=background.find('p')
        update.message.reply_text(ray.text)
       	#update.message.reply_text("KKK")       
       	#update.message.reply_text("NNN")         
        self.go_back(update)

    def on_exit_state16(self, update):
        print('Leaving state16')            
                
    def is_going_to_user(self, update):
        text = update.message.text
        return text.lower() == 'hi'#'Stark'
                
    def on_enter_user(self, update):
        #photo=open('/img/show-fsm.png', 'rb')
        update.message.reply_text("你可以問我關於權力遊戲中的事情，想知道些什麼？")
        update.message.reply_text("You can ask me questions about Game of Thrones,what do you want to know?")                
        #self.go_back(update)                    

    def is_going_to_state1(self, update):
        text = update.message.text        
        if text.lower() == '族語':
            return text.lower() == '族語'
        elif text.lower() == 'family language':
            return text.lower() == 'family language'           

    def is_going_to_state2(self, update):
        text = update.message.text
        if text.lower() == '演員':
            return text.lower() == '演員'
        elif text.lower() == 'actor':
            return text.lower() == 'actor'

    def is_going_to_state3(self, update):
        text = update.message.text
        if text.lower() == '影音':        
            return text.lower() == '影音'        
        elif text.lower() == 'video':
            return text.lower() == 'video'
                                   
    #族語部份 going state4~state6 state7 to back	
    def is_going_to_state4(self, update):
        text = update.message.text
        return text.lower() == 'stark'#Winter is Comming
        
    def is_going_to_state5(self, update):
        text = update.message.text
        return text.lower() == 'lannister'#A Lannister always pays his debts
         
    def is_going_to_state6(self, update):
        text = update.message.text
        return text.lower() == 'targaryen'#Fire and Blood 
        
    def is_going_to_state7(self, update):
        text = update.message.text
        if text.lower() == '不了':        
            return text.lower() == '不了'        
        elif text.lower() == 'no':
            return text.lower() == 'no'
    #演員部份 going state 8-10
    def is_going_to_state8(self, update):
        text = update.message.text
        if text.lower() == 'joe snow':
            return text.lower() == 'joe snow'
        elif text.lower() == 'joe targaryen':
            return  text.lower() == 'joe targaryen'

    def is_going_to_state9(self, update):
        text = update.message.text
        if text.lower() == 'tyrion lannister':
            return text.lower() == 'tyrion lannister'
        elif text.lower() == 'tyrion': 
            return text.lower() == 'tyrion'
        elif text.lower() == 'imp':
            return text.lower() == 'imp'
            
    def is_going_to_state10(self, update):
        text = update.message.text
        if text.lower() == 'daenerys targaryen':
            return text.lower() == 'daenerys targaryen'
        elif text.lower() == 'mother of dragon':
            return  text.lower() == 'mother of dragon'        

    def is_going_to_state11(self, update):
        text = update.message.text
        if text.lower() == '不了':        
            return text.lower() == '不了'        
        elif text.lower() == 'no':
            return text.lower() == 'no' 
    #影音部份 going state12-14 back 15
    def is_going_to_state12(self, update):
        text = update.message.text
        if text.lower() == '配樂':
            return text.lower() == '配樂'
        elif text.lower() == 'background music':
            return text.lower() == 'background music'                        

    def is_going_to_state13(self, update):
        text = update.message.text
        if text.lower() == '預告':
            return text.lower() == '預告'
        elif text.lower() == 'trailer':
            return text.lower() == 'trailer'    

    def is_going_to_state14(self, update):
        text = update.message.text
        if text.lower() == '片頭曲':
            return text.lower() == '片頭曲'
        elif text.lower() == 'op':
            return text.lower() == 'op'

    def is_going_to_state15(self, update):
        text = update.message.text
        if text.lower() == '不了':        
            return text.lower() == '不了'        
        elif text.lower() == 'no':
            return text.lower() == 'no'                       
                
    def on_enter_state1(self, update):
       	update.message.reply_text("說出你想知道的家族")
       	update.message.reply_text("Tell me the family name.")        
        #self.go_back(update)

    def on_exit_state1(self, update):
        print('Leaving state1')

    def on_enter_state2(self, update):
        update.message.reply_text("想看哪個演員呢？")
        update.message.reply_text("Tell me the actor's name.")
        #self.go_back(update)

    def on_exit_state2(self, update):
        print('Leaving state2')

    def on_enter_state3(self, update):
        update.message.reply_text("想看些什麼精彩的呢？")
        update.message.reply_text("Wanna watch somthing exhilarating?")        
        #self.go_back(update)
    
    def on_exit_state3(self, update):
        print('Leaving state3')
    
    #族語部份 on state4-6 back 7            
    def on_enter_state4(self, update):
        update.message.reply_text("Winter is Comming")
        update.message.reply_text("還想知道其他家族的族語嗎？")
        update.message.reply_text("Do you still want to know other family's family language?")
        #self.go_back(update)

    def on_exit_state4(self, update):
        print('Leaving state4')   

    def on_enter_state5(self, update):
        update.message.reply_text("A Lannister always pays his debts")
        update.message.reply_text("還想知道其他家族的族語嗎？")
        update.message.reply_text("Do you still want to know other family's family language?")
        #self.go_back(update)

    def on_exit_state5(self, update):
        print('Leaving state5')              

    def on_enter_state6(self, update):
        update.message.reply_text("Fire and Blood")
        update.message.reply_text("我把知道的族語都告訴你了")
        update.message.reply_text("I have told you what I know.")        
        self.go_back(update)

    def on_exit_state6(self, update):
        print('Leaving state6')
          
    def on_enter_state7(self, update):
        update.message.reply_text("希望有幫助到你")
        update.message.reply_text("Hope my answer will help you.")
        self.go_back(update)

    def on_exit_state7(self, update):
        print('Leaving state7')
    #演員部份 on state 8-10
    def on_enter_state8(self, update):
        update.message.reply_text("Joe")               
        photo_file = open('img/thrones2.jpg', 'rb')
        update.message.reply_photo(photo_file)
        photo_file.close()
        update.message.reply_text("還想看其他的演員嗎？")
        update.message.reply_text("Want to see others?")
        #self.go_back(update)

    def on_exit_state8(self, update):
        print('Leaving state8')   

    def on_enter_state9(self, update):
        update.message.reply_text("Tyrion")
        photo_file = open('img/tyrion.jpg', 'rb')
        update.message.reply_photo(photo_file)
        photo_file.close()
        update.message.reply_text("還想看其他的演員嗎？")
        update.message.reply_text("Want to see others?")
        #self.go_back(update)

    def on_exit_state9(self, update):
        print('Leaving state9')              

    def on_enter_state10(self, update):
        update.message.reply_text("Stormborn") 
        photo_file = open('img/targaryen.jpg', 'rb')
        update.message.reply_photo(photo_file)
        photo_file.close()
        update.message.reply_text("這是全部了")
        update.message.reply_text("That is all.")                
        self.go_back(update)
        

    def on_exit_state10(self, update):
        print('Leaving state10') 

    def on_enter_state11(self, update):
        update.message.reply_text("希望你滿意")
        update.message.reply_text("Hope the answer is what you want.")
        self.go_back(update)

    def on_exit_state11(self, update):
        print('Leaving state11') 

    #影音部份 going state12-14 back 15 
    def on_enter_state12(self, update):
        update.message.reply_text("music")               
        audio_file = open('music/music.mp3', 'rb')
        update.message.reply_audio(audio_file)
        audio_file.close()
        update.message.reply_text("想看更多嗎？")
        update.message.reply_text("Want to see more?")
        #self.go_back(update)

    def on_exit_state12(self, update):
        print('Leaving state12')   

    def on_enter_state13(self, update):
        update.message.reply_text("The trailer of season seven.")
        video_file=open('video/s7.mp4', 'rb')
        update.message.reply_video(video_file)
        video_file.close()
        update.message.reply_text("想看更多嗎？")
        update.message.reply_text("Want to see more?")
        #self.go_back(update)

    def on_exit_state13(self, update):
        print('Leaving state13')  

    def on_enter_state14(self, update):
        update.message.reply_text("music")               
        audio_file = open('music/music2.mp3', 'rb')
        update.message.reply_audio(audio_file)
        audio_file.close()
        update.message.reply_text("這是全部了")
        update.message.reply_text("That is all.")                
        self.go_back(update)
        

    def on_exit_state14(self, update):
        print('Leaving state14') 

    def on_enter_state15(self, update):
        update.message.reply_text("精彩吧？好好期待新的一季吧！")
        update.message.reply_text("Season seven is coming! Just wait!")
        self.go_back(update)

    def on_exit_state15(self, update):
        print('Leaving state15')                                              
