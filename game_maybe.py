from turtle import right
import pygame
from sys import exit


pygame.init()
pygame.font.init()
# Screen, game icon, title, fonts
width = 822
height = 548
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("CSS dungeon")
icon = pygame.image.load('images/gameicon.png')
pygame.display.set_icon(icon)
FPS = 30 
current_time = pygame.time.get_ticks()
title_font = pygame.font.SysFont('system', 52)
title_font2 = pygame.font.SysFont('system', 48)
text_font = pygame.font.SysFont('system', 34)
continue_font = pygame.font.SysFont('system', 42)

# Backgrounds
background = pygame.image.load('images/map.png')
intro_bg_img = pygame.image.load('images/intro_back.png')       
intro_bg = pygame.transform.scale(intro_bg_img, (822,548))
boss_bg = pygame.image.load('images/boss_screen.png')
boss_screen = pygame.transform.scale(boss_bg, (822, 548))

def bossScreen():
    screen.blit(boss_screen, (0,0))

# text images

title_img = pygame.image.load('images/title.png')
title = pygame.transform.scale(title_img, (500,70))
start_img = pygame.image.load('images/start.png')
info_img = pygame.image.load('images/info.png')
menu_img = pygame.image.load('images/menu.png')
menu = pygame.transform.scale(menu_img, (70,25))
creator_img = pygame.image.load('images/creator.png')
creator = pygame.transform.scale(creator_img, (500, 30))
back_img = pygame.image.load('images/back.png')
back = pygame.transform.scale(back_img, (70,25))
rock = pygame.image.load('images/rock.png')

# Start quiz 

def show_quiz1():
    info_css = title_font.render("Kas ir CSS", True, (0,0,0))
    screen.blit(info_css, (310,65))
    info_text_css = text_font.render("CSS jeb kaskādu stila lapas (Cascading style sheets) ir valoda ar", True, (0,0,0))
    screen.blit(info_text_css, (30,140))  
    info_text_css = text_font.render("kuras palīdzību var piešķirt savai lapai dizainu. Visbiežāk CSS", True, (0,0,0))
    screen.blit(info_text_css, (30,170)) 
    info_text_css = text_font.render("izmanto kopā ar HTML, jo ar HTML palīdzību lapai var izkārtot", True, (0,0,0))
    screen.blit(info_text_css, (30,200))
    info_text_css = text_font.render("tās struktūru un ar CSS piešķirt lapai dizainu un stilu. Lai", True, (0,0,0))
    screen.blit(info_text_css, (30,230))
    info_text_css = text_font.render("varētu pilnīgi izmantot CSS, ir jābut HTML zināšanām. Lielākais ", True, (0,0,0))
    screen.blit(info_text_css, (30,260))
    info_text_css = text_font.render("ieguvums no CSS lietošanas ir tas, ka CSS ļauj atdalīt stilu no,", True, (0,0,0))
    screen.blit(info_text_css, (30,290))
    info_text_css = text_font.render("satura, jo, ja izmantotu tikai HTML gan stilam, gan struktūras", True, (0,0,0))
    screen.blit(info_text_css, (30,320))
    info_text_css = text_font.render("izveidošanai, tad viss atrastos vienā lapā, un būtu grūti lasīt", True, (0,0,0))
    screen.blit(info_text_css, (30,350))
    info_text_css = text_font.render("un labot kodu.", True, (0,0,0))
    screen.blit(info_text_css, (30,380))
    continue_text = continue_font.render("Turpināt..", True, (0,0,0))
    screen.blit(continue_text, (600,410))

def show_quiz1_test(): 
    test1_title = title_font.render("1. Jautājums", True, (0,0,0))
    screen.blit(test1_title, (255,65)) 
    test1_question1 = title_font.render("Kas ir CSS?", True, (0,0,0))  
    screen.blit(test1_question1, (280,115))
def show_quiz1_test_questions():
    test1_questions = continue_font.render("1 Programmēšanas valoda", True, (0,0,0))  
    screen.blit(test1_questions, (50,200))
    test1_questions = continue_font.render("2 Valoda, ar kuras palīdzibu var piešķirt dizainu", True, (0,0,0))  
    screen.blit(test1_questions, (50,270))
    test1_questions = continue_font.render("3 Valoda, ar kuru var veidot lapas struktūru", True, (0,0,0))
    screen.blit(test1_questions, (50,340))

def wrong_choice():
    wrong_choice = title_font.render("Nepareizi!!!", True, (0,0,0))
    screen.blit(wrong_choice, (290,240))

def right_choice():
    right_choice = title_font.render("Pareizi!!!", True, (0,0,0))
    screen.blit(right_choice, (300,240))

def wrong_choice_boss():
    wrong_choice = title_font.render("Nepareizi!!!", True, (255,255,255))
    screen.blit(wrong_choice, (290,240))

def right_choice_boss():
    right_choice = title_font.render("Pareizi!!!", True, (255,255,255))
    screen.blit(right_choice, (300,240))

def show_quiz1_test2():
    test1_title = title_font.render("2. Jautājums", True, (0,0,0))
    screen.blit(test1_title, (255,65)) 
    test1_question1 = title_font.render("Vai CSS ļauj atdalīt stilu no satura?", True, (0,0,0))
    screen.blit(test1_question1, (20,115))
    test2_question = continue_font.render("1. Jā", True, (0,0,0))
    screen.blit(test2_question, (50,200))
    test2_question = continue_font.render("2. Nē", True, (0,0,0))
    screen.blit(test2_question, (50,270))


    
# task 1
task1_title = pygame.image.load('images/task#1.png')
task1 = pygame.transform.scale(task1_title, (70, 20))
task1_screen_image = pygame.image.load('images/task#1_screen.png')
task1_screen = pygame.transform.scale(task1_screen_image, (822,548))

def task1Screen():
    screen.blit(task1_screen, (0,0))

def task1_text():
    task1_title = title_font.render("Klases un ID", True, (0,0,0))
    screen.blit(task1_title, (255,65))
    info_text_css = text_font.render("Lai noteiktu kādam konkrētam elementam stilu, CSS dokumentā ", True, (0,0,0))
    screen.blit(info_text_css, (30,140))
    info_text_css = text_font.render("vispirms to ir jānorāda. Piemēram, lai noteiktu stilu visiem ", True, (0,0,0))
    screen.blit(info_text_css, (30,170))
    info_text_css = text_font.render("paragrāfiem, pirms CSS koda ir japieraksta burts p.", True, (0,0,0))
    screen.blit(info_text_css, (30,200))
    info_text_css = text_font.render("Var arī noteikt stilu kādam paragrāfam vai tā daļai atsevišķi.", True, (0,0,0))
    screen.blit(info_text_css, (30,230))
    info_text_css = text_font.render("Tādā gadijumā izmanto .class (klasi apzīmē priekšā ieliktais", True, (0,0,0))
    screen.blit(info_text_css, (30,260))
    info_text_css = text_font.render("punkts) vai arī #id. Atšķirība starp class un id ir tāda, ka", True, (0,0,0))
    screen.blit(info_text_css, (30,290))
    info_text_css = text_font.render("class var izmantot vairākas reizes lapā, reizes bet id tikai vienu. ", True, (0,0,0))
    screen.blit(info_text_css, (30,320))
    continue_text = continue_font.render("Turpināt..", True, (0,0,0))
    screen.blit(continue_text, (600,410))

def task1_test1_T():
    task1_test1 = title_font.render("1. Jautājums", True, (0,0,0))
    screen.blit(task1_test1, (255,65)) 
    test1_question1 = title_font.render("Kuri simboli apzīmēs class un id?", True, (0,0,0))
    screen.blit(test1_question1, (90,115))
    test2_question = continue_font.render("1. . #", True, (0,0,0))
    screen.blit(test2_question, (50,200))
    test2_question = continue_font.render("2. - #", True, (0,0,0))
    screen.blit(test2_question, (50,270))
    test2_question = continue_font.render("2. . %", True, (0,0,0))
    screen.blit(test2_question, (50,340))

def task1_test2_T():
    task1_test1 = title_font.render("2. Jautājums", True, (0,0,0))
    screen.blit(task1_test1, (255,65)) 
    test1_question1 = title_font.render("Kāda ir atšķirība starp class un id?", True, (0,0,0))
    screen.blit(test1_question1, (50,115))
    test2_question = text_font.render("1. Class var izmantot vairākkārt, id tikai vienu reizi", True, (0,0,0))
    screen.blit(test2_question, (50,200))
    test2_question = text_font.render("2. Class un id pilda atsevišķas funkcijas", True, (0,0,0))
    screen.blit(test2_question, (50,270))
    test2_question = text_font.render("2. Atšķirības nav", True, (0,0,0))
    screen.blit(test2_question, (50,340))




    
# task 2

task2_title = pygame.image.load('images/task#2.png')
task2 = pygame.transform.scale(task2_title, (70, 20))
woodenSignScreenImage = pygame.image.load('images/wooden_sign_screen.png')
woodenSignScreen = pygame.transform.scale(woodenSignScreenImage, (822,548))

def woodenScreen(): 
    screen.blit(woodenSignScreen, (0,0))

def task2_text():
    task1_title = title_font.render("Teksta apstrāde", True, (0,0,0))
    screen.blit(task1_title, (255,35))
    info_text_css = text_font.render("Lai tekstam piešķirtu fontu, izmanto font-family, aiz kura seko ", True, (0,0,0))
    screen.blit(info_text_css, (30,90))
    info_text_css = text_font.render("vairāki fonta vārdi, jo, ja tiek ievadīts tikai viens, var ", True, (0,0,0))
    screen.blit(info_text_css, (30,120))
    info_text_css = text_font.render("notikt negaidīta kļūda. Ja ir ievadīti vairāki fonta vārdi ", True, (0,0,0))
    screen.blit(info_text_css, (30,150))
    info_text_css = text_font.render("un fonts netiek atbalstīts pārlūkprogrammā, dators", True, (0,0,0))
    screen.blit(info_text_css, (30,180))
    info_text_css = text_font.render("automātiski mēģinās nākamo fontu. Lai izmainītu fonta izmēru,", True, (0,0,0))
    screen.blit(info_text_css, (30,210))
    info_text_css = text_font.render("izmanto font-size, pēc kura iet small, medium, un large.", True, (0,0,0))
    screen.blit(info_text_css, (30,240))
    info_text_css = text_font.render("Ja gribas vēl lielāku vai mazāku nekā small vai large, tad", True, (0,0,0))
    screen.blit(info_text_css, (30,270))
    info_text_css = text_font.render("pirms tiem var pierakstīt x, un atkarībā no x'u skaita ", True, (0,0,0))
    screen.blit(info_text_css, (30,300))
    info_text_css = text_font.render("teksts palielināsies vai samazināsies. Ja gribas specifisku ", True, (0,0,0))
    screen.blit(info_text_css, (30,330))
    info_text_css = text_font.render("izmēru, tad var izmantot px, vai em, pirms tiem uzrakstot", True, (0,0,0))
    screen.blit(info_text_css, (30,360))
    info_text_css = text_font.render("vēlamo izmēru skaitļos.", True, (0,0,0))
    screen.blit(info_text_css, (30,390))
    info_text_css = text_font.render("Kā arī tekstam var piešķirt šos parametrus-", True, (0,0,0))
    screen.blit(info_text_css, (30,420))
    info_text_css = text_font.render(" color (krāsa, krāsu pieraksta angliski vai ar heksadecimālo kodu),", True, (0,0,0))
    screen.blit(info_text_css, (30,450))
    info_text_css = text_font.render(" background-color (iekrāso teksta fonu).", True, (0,0,0))
    screen.blit(info_text_css, (30,480))
    continue_text = continue_font.render("Turpināt..", True, (0,0,0))
    screen.blit(continue_text, (600,490))

def task2_test1_T():
    test1_question1 = text_font.render("Tu satiec apmaldījušos vecīti, kura mīļākās krāsas ir sarkana ", True, (0,0,0))
    screen.blit(test1_question1, (30,60))
    test1_question1 = text_font.render("un rozā. Izvēlies pareizo kodu, ar kura palīdzību pateikt", True, (0,0,0))
    screen.blit(test1_question1, (30,90))
    test1_question1 = text_font.render("vecītim, kur ir pareizais ceļš, izmantojot viņa mīļākās krāsas.", True, (0,0,0))
    screen.blit(test1_question1, (30,120))
    test2_question = continue_font.render("1. p {", True, (0,0,0))
    screen.blit(test2_question, (50, 150))
    test2_question = continue_font.render("color: red;", True, (0,0,0))
    screen.blit(test2_question, (50,190))
    test2_question = continue_font.render("background-color: pink;", True, (0,0,0))
    screen.blit(test2_question, (50,230))
    test2_question = continue_font.render("}", True, (0,0,0))
    screen.blit(test2_question, (50,270))
    test2_question = continue_font.render("2. p {", True, (0,0,0))
    screen.blit(test2_question, (50, 330))
    test2_question = continue_font.render("outline: red;", True, (0,0,0))
    screen.blit(test2_question, (50,370))
    test2_question = continue_font.render("background-shade: pink;", True, (0,0,0))
    screen.blit(test2_question, (50,410))
    test2_question = continue_font.render("}", True, (0,0,0))
    screen.blit(test2_question, (50,440))



# task 3

task3_title = pygame.image.load('images/task#3.png')
task3 = pygame.transform.scale(task3_title, (70, 20))

def task3_text():
    task1_title = title_font.render("Četrstūri", True, (0,0,0))
    screen.blit(task1_title, (255,35))
    info_text_css = text_font.render("Visi CSS elementi var tikt uzskatīti par četrstūriem, kuros ", True, (0,0,0))
    screen.blit(info_text_css, (30,110))
    info_text_css = text_font.render("lietotājs ievada tekstu, attēlus utt. Šie četrstūri sastāv", True, (0,0,0))
    screen.blit(info_text_css, (30,140))
    info_text_css = text_font.render("no 4 lietām - margin, padding, border un content. Mainot ", True, (0,0,0))
    screen.blit(info_text_css, (30,170))
    info_text_css = text_font.render("kādu no šiem četriem parametriem, mainās arī četrstūra izmērs, tāpēc ir ", True, (0,0,0))
    screen.blit(info_text_css, (30,200))
    info_text_css = text_font.render("svarīgi tos pareizi noteikt, jo ja kāds no lapas četrstūriem", True, (0,0,0))
    screen.blit(info_text_css, (30,230))
    info_text_css = text_font.render("būs par lielu vai par mazu, tad lapa automātiski pielāgosies un", True, (0,0,0))
    screen.blit(info_text_css, (30,260))
    info_text_css = text_font.render("izskatīsies ne tā, kā tās veidotājs bija iedomājies.", True, (0,0,0))
    screen.blit(info_text_css, (30,290))
    continue_text = continue_font.render("Turpināt..", True, (0,0,0))
    screen.blit(continue_text, (600,400))


def task3_test1_T():
    test1_question1 = text_font.render("Izvēlies pareizos border un padding izmērus, ar kuriem aizstāt", True, (0,0,0))
    screen.blit(test1_question1, (30,60))
    test1_question1 = text_font.render("akmeni zem dārguma, lai neaktivizētos lamatas (border ir apmale", True, (0,0,0))
    screen.blit(test1_question1, (30,90))
    test1_question1 = text_font.render("un padding ir attālums no content (satura) līdz apmalei.", True, (0,0,0))
    screen.blit(test1_question1, (30,120))
    test1_question1 = text_font.render("1. border: 15px", True, (0,0,0))
    screen.blit(test1_question1, (50,160))
    test1_question1 = text_font.render("   padding: 20px", True, (0,0,0))
    screen.blit(test1_question1, (50,190))
    test1_question1 = text_font.render("2. border: 20px ", True, (0,0,0))
    screen.blit(test1_question1, (50,240))
    test1_question1 = text_font.render("   padding: 15px", True, (0,0,0))
    screen.blit(test1_question1, (50,270))


# task 4

task4_title = pygame.image.load('images/task#4.png')
task4 = pygame.transform.scale(task4_title, (70, 20))

def task4_text():
    task1_title = title_font2.render("CSS elementu pārvietošana un slēpšana", True, (0,0,0))
    screen.blit(task1_title, (35,35))
    task1_title = text_font.render("CSS elementiem, kurus nevēlies redzēt, var uzlikt ", True, (0,0,0))
    screen.blit(task1_title, (50,110))
    test1_question1 = text_font.render("parametru display: none; un lapa tiks parādīta tā,", True, (0,0,0))
    screen.blit(test1_question1, (50,140))
    test1_question1 = text_font.render("itkā elementa tur pat nebūtu bijis. Bet, ja izmanto elementam", True, (0,0,0))
    screen.blit(test1_question1, (50,170))
    test1_question1 = text_font.render("visibility: hidden; tad lapa vienalga atstās vietu šim elementam.", True, (0,0,0))
    screen.blit(test1_question1, (50,200))
    test1_question1 = text_font.render("Elementus var izvietot, izmantojot top, right, left, bottom, ", True, (0,0,0))
    screen.blit(test1_question1, (50,230))
    test1_question1 = text_font.render("pierakstot tiem pikseļu vai procentu skaitu.", True, (0,0,0))
    screen.blit(test1_question1, (50,260))
    continue_text = continue_font.render("Turpināt..", True, (0,0,0))
    screen.blit(continue_text, (600,400))

def task4_test1_T():
    task1_test1 = title_font.render("1. Jautājums", True, (0,0,0))
    screen.blit(task1_test1, (255,65)) 
    test1_question1 = continue_font.render("Kādas mērvienības tiek izmantotas, lai izvietotu", True, (0,0,0))
    screen.blit(test1_question1, (35,115))
    test1_question1 = continue_font.render("elementus?", True, (0,0,0))
    screen.blit(test1_question1, (300,145))
    test1_question1 = text_font.render("1. Cm,Dm", True, (0,0,0))
    screen.blit(test1_question1, (50,180))
    test1_question1 = text_font.render("2. %,px", True, (0,0,0))
    screen.blit(test1_question1, (50,220))
    test1_question1 = text_font.render("3. Ft,In  ", True, (0,0,0))
    screen.blit(test1_question1, (50,260))

def task4_test2_T():
    task1_test1 = title_font.render("2. Jautājums", True, (0,0,0))
    screen.blit(task1_test1, (255,65)) 
    test1_question1 = continue_font.render("Kurš no parametriem padara elementu pilnīgi", True, (0,0,0))
    screen.blit(test1_question1, (50,115))
    test1_question1 = continue_font.render("neredzamu, itkā tā nemaz nabūtu bijis?", True, (0,0,0))
    screen.blit(test1_question1, (90,145))
    test1_question1 = text_font.render("1. visibility: hidden;", True, (0,0,0))
    screen.blit(test1_question1, (50,200))
    test1_question1 = text_font.render("2. display: none;", True, (0,0,0))
    screen.blit(test1_question1, (50,240))
    

# boss fight

boss_title = pygame.image.load('images/boss.png')
boss = pygame.transform.scale(boss_title, (100,20))
bossScreenImage = pygame.image.load('images/boss_screen.png')
boss_Screen = pygame.transform.scale(bossScreenImage, (822,548))

def bossScreen():
    screen.blit(boss_Screen, (0,0))

def boss_test1(): 
    task1_test1 = title_font.render("Boss Fight!", True, (255,255,255))
    screen.blit(task1_test1, (310,30))
    task1_test1 = title_font.render("Kas ir CSS?", True, (255,255,255))
    screen.blit(task1_test1, (310,80))
    test1_questions = text_font.render("1. Programmēšanas valoda", True, (255,255,255))  
    screen.blit(test1_questions, (50,160))
    test1_questions = text_font.render("2. Valoda, ar kuras ", True, (255,255,255))  
    screen.blit(test1_questions, (500,160))
    test1_questions = text_font.render("palīdzibu var piešķirt", True, (255,255,255))  
    screen.blit(test1_questions, (500,190))
    test1_questions = text_font.render("dizainu", True, (255,255,255))  
    screen.blit(test1_questions, (500,220))
    test1_questions = text_font.render("3. Valoda, ar kuru var", True, (255,255,255))
    screen.blit(test1_questions, (50,220))
    test1_questions = text_font.render("veidot lapas struktūru", True, (255,255,255))
    screen.blit(test1_questions, (50,250))

def boss_test2(): 
    task1_test1 = title_font.render("Vai CSS ļauj atdalīt stilu no satura?", True, (255,255,255))
    screen.blit(task1_test1, (20,60))
    test1_questions = text_font.render("1. Jā", True, (255,255,255))  
    screen.blit(test1_questions, (150,160))
    test1_questions = text_font.render("2. Nē", True, (255,255,255))  
    screen.blit(test1_questions, (590,160))

def boss_test3(): 
    task1_test1 = title_font.render("Kuri simboli apzīmēs class un id?", True, (255,255,255))
    screen.blit(task1_test1, (20,60))
    test1_questions = text_font.render("1. . #", True, (255,255,255))  
    screen.blit(test1_questions, (150,160))
    test1_questions = text_font.render("2. - #", True, (255,255,255))  
    screen.blit(test1_questions, (590,160)) 
    test1_questions = text_font.render("3. . %", True, (255,255,255))  
    screen.blit(test1_questions, (150,210)) 

def boss_test4(): 
    test1_question1 = continue_font.render("Kādas mērvienības tiek izmantotas, lai izvietotu", True, (255,255,255))
    screen.blit(test1_question1, (20,60))
    test1_question1 = continue_font.render("elementus?", True, (255,255,255))
    screen.blit(test1_question1, (300,90))
    test1_question1 = text_font.render("1. Cm,Dm", True, (255,255,255))
    screen.blit(test1_question1, (150,180))
    test1_question1 = text_font.render("2. %,px", True, (255,255,255))
    screen.blit(test1_question1, (590,180))
    test1_question1 = text_font.render("3. Ft,In  ", True, (255,255,255))
    screen.blit(test1_question1, (150,240))

def boss_test5(): 
    test1_question1 = continue_font.render("Kurš no parametriem padara elementu pilnīgi", True, (255,255,255))
    screen.blit(test1_question1, (60,60))
    test1_question1 = continue_font.render("neredzamu, itkā tā nemaz nabūtu bijis?", True, (255,255,255))
    screen.blit(test1_question1, (100,100))
    test1_question1 = text_font.render("1. visibility: hidden", True, (255,255,255))
    screen.blit(test1_question1, (80,180))
    test1_question1 = text_font.render("2. display: none;", True, (255,255,255))
    screen.blit(test1_question1, (540,180))


# complete screen  

def congarts():
    test1_question1 = title_font.render("Apsveicu!!", True, (255,255,255))
    screen.blit(test1_question1, (300,160))
    test1_question1 = continue_font.render("Tu esi pabeidzis spēli!!", True, (255,255,255))
    screen.blit(test1_question1, (240,200))
    test1_question1 = text_font.render("Sākt no jauna", True, (255,255,255))
    screen.blit(test1_question1, (150,260))
    test1_question1 = text_font.render("Iziet", True, (255,255,255))
    screen.blit(test1_question1, (570,260))





# game states


class GameState():
    def __init__(self):
        self.state = 'intro'

    def intro(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>301 and pos[1]>240 and pos[0]<502 and pos[1]<291:
                        self.state = 'start_quiz'
                if pos[0]>322 and pos[1]>311 and pos[0]<482 and pos[1]<363:
                    self.state = 'info'

        screen.blit(intro_bg, (0,0))
        screen.blit(title, (175, 100))
        screen.blit(start_img, (300,240))
        screen.blit(info_img, (322,315))

        pygame.display.update()

    def info(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                    if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                        self.state = 'intro'

        screen.blit(intro_bg, (0,0))
        screen.blit(creator, (173,238))
        screen.blit(back, (0,0))

            

        

        pygame.display.update()

    def start_quiz(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'intro'
                if pos[0]>601 and pos[1]>413 and pos[0]<747 and pos[1]<437:
                    self.state = 'start_quiz_test1'
            start_quiz_complete = False
            task1Screen()
            screen.blit(menu, (0,0))
            show_quiz1()

            pygame.display.update()

    def start_quiz_test1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'start_quiz'
                if pos[0]>50 and pos[1]>196 and pos[0]<470 and pos[1]<227:
                    self.state = 'wrong_choice'
                if pos[0]>50 and pos[1]>270 and pos[0]<778 and pos[1]<287:
                    self.state = 'right_choice'
                if pos[0]>60 and pos[1]>342 and pos[0]<730 and pos[1]<366:
                    self.state = 'wrong_choice'

            task1Screen()
            screen.blit(back, (0,0))
            show_quiz1_test()
            show_quiz1_test_questions()

            pygame.display.update()

    def wrong_choice(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'start_quiz_test1'

            task1Screen()
            wrong_choice()
            screen.blit(back, (0,0))

            pygame.display.update()

    def right_choice(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'start_quiz_test2'

            task1Screen()
            right_choice()

            pygame.display.update()

    def start_quiz_test2(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'start_quiz_test1'
                if pos[0]>50 and pos[1]>199 and pos[0]<142 and pos[1]<231:
                    self.state = 'right_choice1'
                    start_quiz_complete = True 
                if pos[0]>50 and pos[1]>270 and pos[0]<152 and pos[1]<306:
                    self.state = 'wrong_choice1'

            task1Screen()
            screen.blit(back, (0,0))
            show_quiz1_test2()

            pygame.display.update()

    def wrong_choice1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'start_quiz_test2'

            task1Screen()
            wrong_choice()
            screen.blit(back, (0,0))

            pygame.display.update()

    def right_choice1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'main_game'

            task1Screen()
            right_choice()

            pygame.display.update()

    def intro1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>301 and pos[1]>240 and pos[0]<502 and pos[1]<291:
                        self.state = 'main_game'
                if pos[0]>322 and pos[1]>311 and pos[0]<482 and pos[1]<363:
                    self.state = 'info1'

        screen.blit(intro_bg, (0,0))
        screen.blit(title, (175, 100))
        screen.blit(start_img, (300,240))
        screen.blit(info_img, (322,315))

        pygame.display.update()

    def info1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                    if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                        self.state = 'intro1'

        screen.blit(intro_bg, (0,0))
        screen.blit(creator, (173,238))
        screen.blit(back, (0,0))

            

        

        pygame.display.update()

    def main_game(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'intro1'
                if pos[0] < 269 and pos[1] < 483 and pos[0] > 162 and pos[1] > 343:
                    self.state = 'task_1'
                if pos[0] < 761 and pos[1] < 437 and pos[0] > 581 and pos[1] > 338:
                    self.state = 'task_2'
                if pos[0] < 235 and pos[1] < 293 and pos[0] > 62 and pos[1] > 176:
                    self.state = 'task_3'
                if pos[0] < 795 and pos[1] < 190 and pos[0] > 659 and pos[1] > 98:
                    self.state = 'task_4'
                if pos[0] < 479 and pos[1] < 196 and pos[0] > 375 and pos[1] > 80:
                    self.state = 'boss'


        screen.blit(background, (0,0))
        screen.blit(menu, (0,0))

        

        # tasks and boss fight 

        screen.blit(task1, (174,320))
        screen.blit(task2, (630,300))
        screen.blit(task3, (118,160))
        screen.blit(task4, (701,67))
        screen.blit(boss, (375,48))

        pygame.display.update()

    def task_1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'main_game'
                if pos[0]>601 and pos[1]>413 and pos[0]<747 and pos[1]<437:
                    self.state = 'start_task1_test1'

            task1Screen()
            task1_text()
            screen.blit(back, (0,0))

                
            pygame.display.update()

    def start_task1_test1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'task_1'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>50 and pos[1]>197 and pos[0]<124 and pos[1]<228:
                    self.state = 'right_choice2'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>50 and pos[1]>269 and pos[0]<125 and pos[1]<299:
                    self.state = 'wrong_choice2'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>50 and pos[1]>342 and pos[0]<133 and pos[1]<370:
                    self.state = 'wrong_choice2'

            
            task1Screen()
            task1_test1_T()
            screen.blit(back, (0,0))
            pygame.display.update()

    def wrong_choice2(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'start_task1_test1'

            task1Screen()
            wrong_choice()
            screen.blit(back, (0,0))

            pygame.display.update()

    def right_choice2(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'start_task1_test2'

            task1Screen()
            right_choice()

            pygame.display.update()

    def start_task1_test2(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'start_task1_test1'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>50 and pos[1]>200 and pos[0]<781 and pos[1]<226:
                    self.state = 'right_choice3'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>50 and pos[1]>270 and pos[0]<689 and pos[1]<295:
                    self.state = 'wrong_choice3'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>50 and pos[1]>342 and pos[0]<331 and pos[1]<365:
                    self.state = 'wrong_choice3'

            
            task1Screen()
            task1_test2_T()
            screen.blit(back, (0,0))

            pygame.display.update()

    def wrong_choice3(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'start_task1_test2'

            task1Screen()
            wrong_choice()
            screen.blit(back, (0,0))

            pygame.display.update()

    def right_choice3(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'main_game'

            task1Screen()
            right_choice()

            pygame.display.update()

    def task_2(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'main_game'
                if pos[0]>600 and pos[1]>491 and pos[0]<751 and pos[1]<517:
                    self.state = 'start_task2_test1'

            woodenScreen()
            task2_text()
            screen.blit(back, (0,0))

                
            pygame.display.update()

    def start_task2_test1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'task_2'
                if pos[0]>50 and pos[1]>149 and pos[0]<438 and pos[1]<304:
                    self.state = 'right_choice4'
                if pos[0]>50 and pos[1]>329 and pos[0]<453 and pos[1]<473:
                    self.state = 'wrong_choice4'


            woodenScreen()
            screen.blit(back, (0,0))
            task2_test1_T()

        pygame.display.update()
    
    def wrong_choice4(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'start_task2_test1'

            woodenScreen()
            wrong_choice()
            screen.blit(back, (0,0))

            pygame.display.update()

    def right_choice4(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'main_game'

            woodenScreen()
            right_choice()

            pygame.display.update()


    def task_3(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'main_game'
                if pos[0]>600 and pos[1]>400 and pos[0]<752 and pos[1]<428:
                    self.state = 'start_task3_test1'

            woodenScreen()
            task3_text()
            screen.blit(back, (0,0))

                
            pygame.display.update()

    def start_task3_test1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'task_3'
                if pos[0]>50 and pos[1]>160 and pos[0]<246 and pos[1]<213:
                    self.state = 'right_choice5'
                if pos[0]>50 and pos[1]>239 and pos[0]<240 and pos[1]<292:
                    self.state = 'wrong_choice5'


            woodenScreen()
            screen.blit(back, (0,0))
            task3_test1_T()
            screen.blit(rock, (390,250))

        pygame.display.update()
    
    def wrong_choice5(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'start_task3_test1'

            woodenScreen()
            wrong_choice()
            screen.blit(back, (0,0))

            pygame.display.update()

    def right_choice5(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'main_game'

            woodenScreen()
            right_choice()

            pygame.display.update()

    def task_4(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'main_game'
                if pos[0]>600 and pos[1]>400 and pos[0]<752 and pos[1]<428:
                    self.state = 'start_task4_test1'

            woodenScreen()
            task4_text()
            screen.blit(back, (0,0))

                
            pygame.display.update()

    def start_task4_test1(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'task_4'
                if pos[0]>50 and pos[1]>179 and pos[0]<135 and pos[1]<242:
                    self.state = 'wrong_choice6'
                if pos[0]>50 and pos[1]>220 and pos[0]<135 and pos[1]<242:
                    self.state = 'right_choice6'
                if pos[0]>50 and pos[1]>260 and pos[0]<131 and pos[1]<280:
                    self.state = 'wrong_choice6'
                


            woodenScreen()
            screen.blit(back, (0,0))
            task4_test1_T()

        pygame.display.update()
    
    def wrong_choice6(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'start_task4_test1'

            woodenScreen()
            wrong_choice()
            screen.blit(back, (0,0))

            pygame.display.update()

    def right_choice6(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'start_task4_test2'

            woodenScreen()
            right_choice()

            pygame.display.update()

    def start_task4_test2(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'task_4'
                if pos[0]>50 and pos[1]>202 and pos[0]<290 and pos[1]<223:
                    self.state = 'wrong_choice7'
                if pos[0]>50 and pos[1]>240 and pos[0]<246 and pos[1]<265:
                    self.state = 'right_choice7'


            woodenScreen()
            screen.blit(back, (0,0))
            task4_test2_T()

        pygame.display.update()

    def wrong_choice7(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'start_task4_test2'

            woodenScreen()
            wrong_choice()
            screen.blit(back, (0,0))

            pygame.display.update()

    def right_choice7(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'main_game'

            woodenScreen()
            right_choice()

            pygame.display.update()

    def boss(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'main_game'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>50 and pos[1]>156 and pos[0]<363 and pos[1]<183:
                    self.state = 'wrong_choice8'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>50 and pos[1]>221 and pos[0]<313 and pos[1]<271:
                    self.state = 'wrong_choice8'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>50 and pos[1]>158 and pos[0]<738 and pos[1]<243:
                    self.state = 'right_choice8'

            bossScreen()
            boss_test1()
            screen.blit(back, (0,0))


            pygame.display.update()

    def wrong_choice8(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'boss'

            bossScreen()
            wrong_choice_boss()
            screen.blit(back, (0,0))

            pygame.display.update()

    def right_choice8(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'boss_test2'

            bossScreen()
            right_choice_boss()

            pygame.display.update()

    def boss_test2(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'boss'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>150 and pos[1]>156 and pos[0]<207 and pos[1]<180:
                    self.state = 'right_choice9'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>590 and pos[1]>157 and pos[0]<650 and pos[1]<176:
                    self.state = 'wrong_choice9'


            bossScreen()
            boss_test2()
            screen.blit(back, (0,0))


            pygame.display.update()

    def wrong_choice9(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'boss'

            bossScreen()
            wrong_choice_boss()
            screen.blit(back, (0,0))

            pygame.display.update()

    def right_choice9(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'boss_test3'

            bossScreen()
            right_choice_boss()

            pygame.display.update()

    def boss_test3(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'boss_test2'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>150 and pos[1]>158 and pos[0]<207 and pos[1]<180:
                    self.state = 'right_choice10'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>590 and pos[1]>157 and pos[0]<650 and pos[1]<182:
                    self.state = 'wrong_choice10'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>150 and pos[1]>209 and pos[0]<213 and pos[1]<230:
                    self.state = 'wrong_choice10'


            bossScreen()
            boss_test3()
            screen.blit(back, (0,0))


            pygame.display.update()

    def wrong_choice10(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'boss'

            bossScreen()
            wrong_choice_boss()
            screen.blit(back, (0,0))

            pygame.display.update()

    def right_choice10(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'boss_test4'

            bossScreen()
            right_choice_boss()

            pygame.display.update()

    def boss_test4(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'boss_test3'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>80 and pos[1]>179 and pos[0]<313 and pos[1]<202:
                    self.state = 'wrong_choice11'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>39 and pos[1]>180 and pos[0]<734 and pos[1]<206:
                    self.state = 'right_choice11'

            bossScreen()
            boss_test4()
            screen.blit(back, (0,0))


            pygame.display.update()

    def wrong_choice11(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'boss'

            bossScreen()
            wrong_choice_boss()
            screen.blit(back, (0,0))

            pygame.display.update()

    def right_choice11(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'boss_test5'

            bossScreen()
            right_choice_boss()

            pygame.display.update()

    def boss_test5(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'boss_test4'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>150 and pos[1]>179 and pos[0]<266 and pos[1]<204:
                    self.state = 'wrong_choice12'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>590 and pos[1]>181 and pos[0]<674 and pos[1]<203:
                    self.state = 'right_choice12'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>149 and pos[1]>239 and pos[0]<231 and pos[1]<261:
                    self.state = 'wrong_choice12'


            bossScreen()
            boss_test5()
            screen.blit(back, (0,0))


            pygame.display.update()

    def wrong_choice12(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>0 and pos[1]>0 and pos[0]<70 and pos[1]<25:
                    self.state = 'boss'

            bossScreen()
            wrong_choice_boss()
            screen.blit(back, (0,0))

            pygame.display.update()

    def right_choice12(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                self.state = 'complete_screen'

            bossScreen()
            right_choice_boss()

            pygame.display.update()

    def complete_screen(self): 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>150 and pos[1]>259 and pos[0]<315 and pos[1]<283:
                    self.state = 'intro'
            if event.type == pygame.MOUSEBUTTONDOWN:
                if pos[0]>567 and pos[1]>260 and pos[0]<623 and pos[1]<283:
                    pygame.quit()

            screen.blit(intro_bg, (0,0))
            congarts()
            pygame.display.update()

    def state_menager(self):
        if self.state == 'intro':
            self.intro()
        if self.state == 'intro1':
            self.intro1()
        if self.state == 'main_game':
            self.main_game()
        if self.state == 'info':
            self.info()
        if self.state == 'info1':
            self.info1()
        if self.state == 'task_1':
            self.task_1()
        if self.state == 'task_2':
            self.task_2()
        if self.state == 'task_3':
            self.task_3()
        if self.state == 'task_4':
            self.task_4()
        if self.state == 'start_quiz':
            self.start_quiz()
        if self.state == 'start_quiz_test1':
            self.start_quiz_test1()
        if self.state == 'wrong_choice':
            self.wrong_choice()
        if self.state == 'right_choice':
            self.right_choice()
        if self.state == 'start_quiz_test2':
            self.start_quiz_test2()
        if self.state == 'wrong_choice1':
            self.wrong_choice1()
        if self.state == 'right_choice1':
            self.right_choice1()
        if self.state == 'start_task1_test1':
            self.start_task1_test1()
        if self.state == 'wrong_choice2':
            self.wrong_choice2()
        if self.state == 'right_choice2':
            self.right_choice2()
        if self.state == 'start_task1_test2':
            self.start_task1_test2()
        if self.state == 'wrong_choice3':
            self.wrong_choice3()
        if self.state == 'right_choice3':
            self.right_choice3()
        if self.state == 'start_task2_test1':
            self.start_task2_test1()
        if self.state == 'wrong_choice4':
            self.wrong_choice4()
        if self.state == 'right_choice4':
            self.right_choice4()
        if self.state == 'start_task3_test1':
            self.start_task3_test1()
        if self.state == 'wrong_choice5':
            self.wrong_choice5()
        if self.state == 'right_choice5':
            self.right_choice5()
        if self.state == 'start_task4_test1':
            self.start_task4_test1()
        if self.state == 'wrong_choice6':
            self.wrong_choice6()
        if self.state == 'right_choice6':
            self.right_choice6()
        if self.state == 'start_task4_test2':
            self.start_task4_test2()
        if self.state == 'wrong_choice7':
            self.wrong_choice7()
        if self.state == 'right_choice7':
            self.right_choice7()
        if self.state == 'boss': 
            self.boss()
        if self.state == 'wrong_choice8':
            self.wrong_choice8()
        if self.state == 'right_choice8':
            self.right_choice8()
        if self.state == 'boss_test2': 
            self.boss_test2()
        if self.state == 'wrong_choice9':
            self.wrong_choice9()
        if self.state == 'right_choice9':
            self.right_choice9()
        if self.state == 'boss_test3': 
            self.boss_test3()
        if self.state == 'wrong_choice10':
            self.wrong_choice10()
        if self.state == 'right_choice10':
            self.right_choice10()
        if self.state == 'boss_test4': 
            self.boss_test4()
        if self.state == 'wrong_choice11':
            self.wrong_choice11()
        if self.state == 'right_choice11':
            self.right_choice11()
        if self.state == 'boss_test5': 
            self.boss_test5()
        if self.state == 'wrong_choice12':
            self.wrong_choice12()
        if self.state == 'right_choice12':
            self.right_choice12()
        if self.state == 'complete_screen':
            self.complete_screen()


game_state = GameState()

# Control the fps 

clock = pygame.time.Clock()

# Game loop
while True:
    
    pos = pygame.mouse.get_pos()
    print(pos)

    game_state.state_menager()
     
    clock.tick(FPS)

