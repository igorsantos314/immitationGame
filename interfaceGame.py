from tkinter import *
from gameDataBase import bd
import pygame

class interface:

    def __init__(self):
        self.fontDefault = 'Courier 12'
        self.fontDefaultBold = 'Courier 15 bold'

        self.listSubtitles = []
        self.currentSlide = 0

        self.bancoDados = bd()

        #INICIALIZA A LISTA DE LEGENDAS
        self.setListSubtitles()

        #TOCA O AUDIO
        self.playMusic(0)

        self.windowGame()

    def playMusic(self, numberSlide):
        pygame.init()
        pygame.mixer.music.load(f'sound{numberSlide}.mp3')
        pygame.mixer.music.play()

    def setListSubtitles(self):

        #VARRE A LISTA DE LEGENDAS E PEGA O ITEM 0 DE CADA TUPLA
        for i in self.bancoDados.getSubtitles():
            self.listSubtitles.append(i[0])

        #print(self.listSubtitles)

    def windowGame(self):

        self.windowMain = Tk()
        self.windowMain.title('The Imitation Game')
        self.windowMain.geometry('1180x600+10+10')
        self.windowMain.resizable(False, False)

        #BUTTON NEXT
        self.btNext = Button(self.windowMain, text='Next', width=3, height=2, font=self.fontDefault, command=self.nextSlide)
        self.btNext.place(x=1120, y=550)

        #BUTTON PREV
        self.btPrev = Button(self.windowMain, text='Prev', width=3, height=2, font=self.fontDefault, command=self.prevSlide)
        self.btPrev.place(x=5, y=550)

        #TITULO
        title = Label(text='THE IMITATION GAME', font=self.fontDefaultBold, fg='red')
        title.pack(pady=20)

        #SUBTITLE
        self.lblSubtitle = Label(self.windowMain, text='', font=self.fontDefaultBold, height=10)
        self.lblSubtitle.pack()

        #SETAR A LEGENDA COMO BEM VINDO
        self.setSubtitle(0)

        self.windowMain.mainloop()

    def updateApresentation(self):
        #MODIFICA A IMAGEM E A LEGENDA
        self.setImagem(self.currentSlide)

        self.setSubtitle(self.currentSlide)

    #AVANÇA UM SLIDE
    def nextSlide(self):

        #AVANÇA O SLIDE
        self.currentSlide += 1

        #VERIFICA SE AINDA EXISTE ALGUM SLIDE
        if self.currentSlide < len(self.listSubtitles):
            
            #ATUALIZA SLIDE
            self.updateApresentation()

        else:
            #QUANDO N EXSITIR SLIDE O VALOR CORRENTE VAI PARA O ULTIMO
            self.currentSlide = len(self.listSubtitles) - 1

    #VOLTA UM SLIDE
    def prevSlide(self):
        
        #VOLTA O SLIDE
        self.currentSlide -= 1

        #VERIFICA SE AINDA EXISTE ALGUM SLIDE
        if self.currentSlide > 0:

            #ATUALIZA SLIDE
            self.updateApresentation()

        else:
            #RESETA PARA A POSIÇÃO INICIAL
            self.currentSlide = 1

    #DESTROY A IMAGEM ANTERIOR SE EXISTIR
    def destroyImage(self):
        try:
            self.lblImage.destroy()
        except:
            pass

    #ATUALIZA O SLIDE COM BASE NO numberSlide
    def setImagem(self, numberSlide):

        #DESTROY A IMAGEM PARA CRIAR OUTRA
        self.destroyImage()

        #IMAGEM
        self.img = PhotoImage(file=f'{numberSlide}.png')

        self.lblImage = Label(self.windowMain, text='', image=self.img)
        self.lblImage.pack(pady=5)

    def alignSubtitle(self, s):
        nString = ''

        #PULA UMA LINHA A CADA 60 CARACTERE
        for i in s:

            if len(nString)%60 == 0 and len(nString) > 0:
                nString += i + '\n'

            else:
                nString += i

        return nString

    def setSubtitle(self, numberSlide):

        #ATUALIZA A LEGENDA COM BASE NO NUMERO DO SLIDE
        string  = self.listSubtitles[numberSlide]

        self.lblSubtitle['text'] = self.alignSubtitle(string)

if __name__ == "__main__":
    interface()    