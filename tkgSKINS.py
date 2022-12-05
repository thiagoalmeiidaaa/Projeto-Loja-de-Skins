from tkinter import *
from tkinter import messagebox

import PIL as p

import PIL.ImageTk as ptk

from datetime import datetime


root=Tk()
root.title("tkgskins.gg")
root.geometry("1380x720")
root.configure(bg="#0C1012")

Heading=LabelFrame(root,bd=2,relief="groove",bg="#0C1012")
Heading.place(x=0,y=0,width=1380,height=55)


faca1_img=ptk.PhotoImage(p.Image.open("Images/m9.png"))
faca2_img=ptk.PhotoImage(p.Image.open("Images/butterfly.png"))
faca3_img=ptk.PhotoImage(p.Image.open("Images/guthook.png"))
faca4_img=ptk.PhotoImage(p.Image.open("Images/talon.png"))
faca5_img=ptk.PhotoImage(p.Image.open("Images/baioneta.png"))
faca6_img=ptk.PhotoImage(p.Image.open("Images/bowie.png"))
faca7_img=ptk.PhotoImage(p.Image.open("Images/m9-2.png"))
faca8_img=ptk.PhotoImage(p.Image.open("Images/guthook2.png"))
faca9_img=ptk.PhotoImage(p.Image.open("Images/stiletto.png"))
faca10_img=ptk.PhotoImage(p.Image.open("Images/hunstman.png"))

luva1_img=ptk.PhotoImage(p.Image.open("Images/degrade.png"))
luva2_img=ptk.PhotoImage(p.Image.open("Images/nocts.png"))
luva3_img=ptk.PhotoImage(p.Image.open("Images/onça.png"))
luva4_img=ptk.PhotoImage(p.Image.open("Images/quimono.png"))
luva5_img=ptk.PhotoImage(p.Image.open("Images/abocanhada.png"))
luva6_img=ptk.PhotoImage(p.Image.open("Images/labirinto.png"))
luva7_img=ptk.PhotoImage(p.Image.open("Images/bordado.png"))
luva8_img=ptk.PhotoImage(p.Image.open("Images/piloto.png"))
luva9_img=ptk.PhotoImage(p.Image.open("Images/sapo.png"))
luva10_img=ptk.PhotoImage(p.Image.open("Images/transporte.png"))

arma1_img=ptk.PhotoImage(p.Image.open("Images/akbomba.png"))
arma2_img=ptk.PhotoImage(p.Image.open("Images/m4neo.png"))
arma3_img=ptk.PhotoImage(p.Image.open("Images/akimp.png"))
arma4_img=ptk.PhotoImage(p.Image.open("Images/akserpente.png"))
arma5_img=ptk.PhotoImage(p.Image.open("Images/akvermelho.png"))
arma6_img=ptk.PhotoImage(p.Image.open("Images/akasiimov.png"))
arma7_img=ptk.PhotoImage(p.Image.open("Images/m4uivo.png"))
arma8_img=ptk.PhotoImage(p.Image.open("Images/awpneo.png"))
arma9_img=ptk.PhotoImage(p.Image.open("Images/awpmedusa.png"))
arma10_img=ptk.PhotoImage(p.Image.open("Images/awpdragon.png"))

adesivo1_img=ptk.PhotoImage(p.Image.open("Images/furiaholo.png"))
adesivo2_img=ptk.PhotoImage(p.Image.open("Images/marcas.png"))
adesivo3_img=ptk.PhotoImage(p.Image.open("Images/sabedoria.png"))
adesivo4_img=ptk.PhotoImage(p.Image.open("Images/diaboas.png"))
adesivo5_img=ptk.PhotoImage(p.Image.open("Images/global.png"))
adesivo6_img=ptk.PhotoImage(p.Image.open("Images/runtime.png"))
adesivo7_img=ptk.PhotoImage(p.Image.open("Images/crown.png"))
adesivo8_img=ptk.PhotoImage(p.Image.open("Images/incineracao.png"))
adesivo9_img=ptk.PhotoImage(p.Image.open("Images/bruxaria.png"))
adesivo10_img=ptk.PhotoImage(p.Image.open("Images/droga.png"))

caixa1_img=ptk.PhotoImage(p.Image.open("Images/cromatica.png"))
caixa2_img=ptk.PhotoImage(p.Image.open("Images/sombria.png"))
caixa3_img=ptk.PhotoImage(p.Image.open("Images/falchion.png"))
caixa4_img=ptk.PhotoImage(p.Image.open("Images/gamma.png"))
caixa5_img=ptk.PhotoImage(p.Image.open("Images/prism.png"))
caixa6_img=ptk.PhotoImage(p.Image.open("Images/fraturada.png"))
caixa7_img=ptk.PhotoImage(p.Image.open("Images/espectral.png"))
caixa8_img=ptk.PhotoImage(p.Image.open("Images/luvas.png"))
caixa9_img=ptk.PhotoImage(p.Image.open("Images/hydra.png"))
caixa10_img=ptk.PhotoImage(p.Image.open("Images/cacador.png"))



Facas_lista=[]

luvas_lista=[]

armas_lista=[]

Adesivo_lista=[]

caixas_lista=[]



nome=Label(Heading,text="TkG Skins",font="arial 30 bold italic",bg="#0C1012",fg="#6506B0",).grid(row=0,column=1)
produtos_ex=LabelFrame(root,bd=2,relief="groove",text="Produtos",font="arial 16 bold", bg=  "#0C1012", fg="white")
produtos_ex.place(x=310,y=60,width=1040,height=620)

label_enjoy=Label(produtos_ex,text="Boas Compras",font="castellar 20 bold", bg= "#0C1012", fg="#6506B0").place(x=370,y=250)


botao_comprar=LabelFrame(root,bd=2,relief="groove", fg="#C172FF",bg="#0C1012")
botao_comprar.place(x=2,y=60,width=300,height=380)

def Salvar(text):
    op=messagebox.askyesno("Confirmação de Fatura","Deseja Salvar a fatura em um arquivo?")
    if op:
        t=datetime.now()
        s=str(t.day)+str(t.month)+str(t.year)+str(t.hour)+str(t.minute)+str(t.second)
        f=("fatura/"+s+".txt")
        messagebox.showinfo("Salvando Dados","A fatura foi salva com sucesso como um documento de texto com nome"+s +".txt")
    else:
        messagebox.showinfo("Salvando Dados","A fatura não é salva em um arquivo.")
def Esconder():
    for widget in produtos_ex.winfo_children():
        widget.destroy()
def Espaço(n,s1=" "):
    s=""
    for i in range(n):
        s+=s1
    return s







def FacasL():
    Esconder()
    titulo_facas=Label(produtos_ex,text="Facas",font="times 15 bold",fg="#C172FF",bg="#0C1012").place(x=500)
    faca1=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    faca1.place(x=5,y=35,width=200,height=270)
    faca2=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    faca2.place(x=210,y=35,width=200,height=270)
    faca3=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    faca3.place(x=415,y=35,width=200,height=270)
    faca4=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    faca4.place(x=620,y=35,width=200,height=270)
    faca5=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    faca5.place(x=825,y=35,width=200,height=270)
    faca6=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    faca6.place(x=5,y=310,width=200,height=270)
    faca7=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    faca7.place(x=210,y=310,width=200,height=270)
    faca8=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    faca8.place(x=415,y=310,width=200,height=270)
    faca9=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    faca9.place(x=620,y=310,width=200,height=270)
    faca10=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    faca10.place(x=825,y=310,width=200,height=270)
   
    
    div_faca1=Label(faca1,image=faca1_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_faca2=Label(faca2,image=faca2_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_faca3=Label(faca3,image=faca3_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_faca4=Label(faca4,image=faca4_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_faca5=Label(faca5,image=faca5_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_faca6=Label(faca6,image=faca6_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_faca7=Label(faca7,image=faca7_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_faca8=Label(faca8,image=faca8_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_faca9=Label(faca9,image=faca9_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_faca10=Label(faca10,image=faca10_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    
    nome_faca1=Label(faca1,text="Baioneta M9 (★) | Sabedoria",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_faca2=Label(faca2,text="Canivete Borboleta (★) | Doppler",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=1)
    nome_faca3=Label(faca3,text="Faca Gut Hook (★) | Autotrônica",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_faca4=Label(faca4,text="Faca Talon (★) | Manchado",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_faca5=Label(faca5,text="Baioneta (★) | Sabedoria",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_faca6=Label(faca6,text="Faca Bowie (★) | Fade",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_faca7=Label(faca7,text="Baioneta M9 (★) | Autotrônica",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_faca8=Label(faca8,text="Faca Gut Hook (★) | Teia Rubra",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_faca9=Label(faca9,text="Faca Stiletto (★) | Manchado",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_faca10=Label(faca10,text="Faca do Caçador (★) | Aço Azul",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    
    float_faca1=Label(faca1,text="Float: 0.6297154", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float_faca2=Label(faca2,text="Float: 0.7483921", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float_faca3=Label(faca3,text="Float: 0.8895205", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float_faca4=Label(faca4,text="Float: 0.7717654", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float_faca5=Label(faca5,text="Float: 0.8953276", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float_faca6=Label(faca6,text="Float: 0.1159403", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float_faca7=Label(faca7,text="Float: 0.9992622", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float_faca8=Label(faca8,text="Float: 0.9506577", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float_faca9=Label(faca9,text="Float: 0.8202234", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float_faca10=Label(faca10,text="Float: 0.2414965", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    
    
    def AddFaca1():
        global Facas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            Facas_lista.append(["Baioneta M9 (★) | Sabedoria",4645," 4.645",Espaço(40-len("Baioneta M9 (★) | Sabedoria"))])
            messagebox.showinfo("Status do produto","Baioneta M9 (★) | Sabedoria foi adicionado ao carrinho com sucesso!")
        else:
            messagebox.showinfo("Status do produto","Baioneta M9 (★) | Sabedoria não foi adicionado ao carrinho.")
    def AddFaca2():
        global Facas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            Facas_lista.append(["Canivete Borboleta (★) | Doppler",8920," 8.920",Espaço(40-len("Canivete Borboleta (★) | Doppler"))])
            messagebox.showinfo("Status do produto","Canivete Borboleta (★) | Doppler foi adicionado ao carrinho com sucesso!")
        else:
            messagebox.showinfo("Status do produto","Canivete Borboleta (★) | Doppler não foi adicionado ao carrinho.")
    def AddFaca3():
        global Facas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            Facas_lista.append(["Faca Gut Hook (★) | Autotrônica",1250," 1.250",Espaço(40-len("Faca Gut Hook (★) | Autotrônica"))])
            messagebox.showinfo("Status do produto","Faca Gut Hook (★) | Autotrônica foi adicionado ao carrinho com sucesso!")
        else:
            messagebox.showinfo("Status do produto","Faca Gut Hook (★) | Autotrônica não foi adicionado ao carrinho.")
    def AddFaca4():
        global Facas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            Facas_lista.append(["Faca Talon (★) | Manchado",1586," 1.586",Espaço(40-len("Faca Talon (★) | Manchado"))])
            messagebox.showinfo("Status do produto","Faca Talon (★) | Manchado foi adicionado ao carrinho com sucesso!")
        else:
            messagebox.showinfo("Status do produto","Faca Talon (★) | Manchado não foi adicionado ao carrinho.")
    def AddFaca5():
        global Facas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            Facas_lista.append(["Baioneta (★) | Sabedoria",4531," 4.531",Espaço(40-len("Baioneta (★) | Sabedoria"))])
            messagebox.showinfo("Status do produto","Baioneta (★) | Sabedoria foi adicionado ao carrinho com sucesso!")
        else:
            messagebox.showinfo("Status do produto","Baioneta (★) | Sabedoria não foi adicionado ao carrinho.")
    def AddFaca6():
        global Facas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            Facas_lista.append(["Faca Bowie (★) | Fade",1850," 1.850",Espaço(40-len("Faca Bowie (★) | Fade"))])
            messagebox.showinfo("Status do produto","Faca Bowie (★) | Fade foi adicionado ao carrinho com sucesso!")
        else:
            messagebox.showinfo("Status do produto","Faca Bowie (★) | Fade não foi adicionado ao carrinho.")
    def AddFaca7():
        global Facas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            Facas_lista.append(["Baioneta M9 (★) | Autotrônica",3706," 3.706",Espaço(40-len("Baioneta M9 (★) | Autotrônica"))])
            messagebox.showinfo("Status do produto","Baioneta M9 (★) | Autotrônica foi adicionado ao carrinho com sucesso!")
        else:
            messagebox.showinfo("Status do produto","Baioneta M9 (★) | Autotrônica não foi adicionado ao carrinho.")
    def AddFaca8():
        global Facas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            Facas_lista.append(["Faca Gut Hook (★) | Teia Rubra",824," 824",Espaço(40-len("Faca Gut Hook (★) | Teia Rubra"))])
            messagebox.showinfo("Status do produto","Faca Gut Hook (★) | Teia Rubra foi adicionado ao carrinho com sucesso!")
        else:
            messagebox.showinfo("Status do produto","Faca Gut Hook (★) | Teia Rubra não foi adicionado ao carrinho.")
    def AddFaca9():
        global Facas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            Facas_lista.append(["Faca Stiletto (★) | Manchado",995," 995",Espaço(40-len("Faca Stiletto (★) | Manchado"))])
            messagebox.showinfo("Status do produto","Faca Stiletto (★) | Manchado foi adicionado ao carrinho com sucesso!")
        else:
            messagebox.showinfo("Status do produto","Faca Stiletto (★) | Manchado não foi adicionado ao carrinho.")
    def AddFaca10():
        global Facas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            Facas_lista.append(["Faca do Caçador (★) | Aço Azul",1224," 1.244",Espaço(40-len("Faca do Caçador (★) | Aço Azul"))])
            messagebox.showinfo("Status do produto","Faca do Caçador (★) | Aço Azul foi adicionado ao carrinho com sucesso!")
        else:
            messagebox.showinfo("Status do produto","Faca do Caçador (★) | Aço Azul não foi adicionado ao carrinho.")
            
    preco_faca1=Label(faca1,text="Preço: R$ 4.645,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_faca2=Label(faca2,text="Preço: R$ 8.920,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_faca3=Label(faca3,text="Preço: R$ 1.250,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_faca4=Label(faca4,text="Preço: R$ 1.586,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_faca5=Label(faca5,text="Preço: R$ 4.531,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_faca6=Label(faca6,text="Preço: R$ 1.850,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_faca7=Label(faca7,text="Preço: R$ 3.706,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_faca8=Label(faca8,text="Preço: R$ 824,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_faca9=Label(faca9,text="Preço: R$ 995,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_faca10=Label(faca10,text="Preço: R$ 1.244,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)        
    
    botao_faca1=Button(faca1,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddFaca1).place(x=65,y=240)
    botao_faca2=Button(faca2,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddFaca2).place(x=65,y=240)
    botao_faca3=Button(faca3,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddFaca3).place(x=65,y=240)
    botao_faca4=Button(faca4,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddFaca4).place(x=65,y=240)
    botao_faca5=Button(faca5,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddFaca5).place(x=65,y=240)
    botao_faca6=Button(faca6,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddFaca6).place(x=65,y=240)
    botao_faca7=Button(faca7,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddFaca7).place(x=65,y=240)
    botao_faca8=Button(faca8,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddFaca8).place(x=65,y=240)
    botao_faca9=Button(faca9,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddFaca9).place(x=65,y=240)
    botao_faca10=Button(faca10,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddFaca10).place(x=65,y=240)
    
    
    
    
    
    
    
    
def LuvasL():
    Esconder()
    titulo_luvas=Label(produtos_ex,text="Luvas",font="times 15 bold",fg="#C172FF",bg="#0C1012").place(x=500)
    luva1=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    luva1.place(x=5,y=35,width=200,height=270)
    luva2=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    luva2.place(x=210,y=35,width=200,height=270)
    luva3=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    luva3.place(x=415,y=35,width=200,height=270)
    luva4=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    luva4.place(x=620,y=35,width=200,height=270)
    luva5=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    luva5.place(x=825,y=35,width=200,height=270)
    luva6=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    luva6.place(x=5,y=310,width=200,height=270)
    luva7=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    luva7.place(x=210,y=310,width=200,height=270)
    luva8=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    luva8.place(x=415,y=310,width=200,height=270)
    luva9=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    luva9.place(x=620,y=310,width=200,height=270)
    luva10=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    luva10.place(x=825,y=310,width=200,height=270)
    
    
    div_luva1=Label(luva1,image=luva1_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_luva2=Label(luva2,image=luva2_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_luva3=Label(luva3,image=luva3_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_luva4=Label(luva4,image=luva4_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_luva5=Label(luva5,image=luva5_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_luva6=Label(luva6,image=luva6_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_luva7=Label(luva7,image=luva7_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_luva8=Label(luva8,image=luva8_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_luva9=Label(luva9,image=luva9_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_luva10=Label(luva10,image=luva10_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)

    nome_luva1=Label(luva1,text="Luvas (★) Degradê MW",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_luva2=Label(luva2,text="Luvas (★) Nocts FT",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_luva3=Label(luva3,text="Luvas (★) Onça Rainha FT",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_luva4=Label(luva4,text="Luvas (★) Quimono Carmesim",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=2)
    nome_luva5=Label(luva5,text="Luvas (★) Abocanhada FT",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_luva6=Label(luva6,text="Luvas (★) Labirinto Vivo FT",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_luva7=Label(luva7,text="Luvas (★) Bordado FT",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_luva8=Label(luva8,text="Luvas (★) Piloto Verde BS",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_luva9=Label(luva9,text="Luvas (★) Sapo amarelo FT",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_luva10=Label(luva10,text="Luvas (★) Transporte FT",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    
    
    float_luva1=Label(luva1,text="Float: 0.9695522", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float_luva2=Label(luva2,text="Float: 0.6196312", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float_luva3=Label(luva3,text="Float: 0.9083315", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float_luva4=Label(luva4,text="Float: 0.2868283", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float_luva5=Label(luva5,text="Float: 0.1682662", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float_luva6=Label(luva6,text="Float: 0.7072818", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float_luva7=Label(luva7,text="Float: 0.0012561", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float_luva8=Label(luva8,text="Float: 0.1269925", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float_luva9=Label(luva9,text="Float: 0.0958723", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float_luva10=Label(luva10,text="Float: 0.5723925", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)

    def AddLuva1():
        global luvas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            luvas_lista.append(["Luvas (★) Degradê MW",7776," 7.776,00",Espaço(40-len("Luvas (★) Degradê MW"))])
            messagebox.showinfo("Status do produto","Luvas (★) Degradê MW foi adicionado ao carrinho com sucesso!")
        else:
            messagebox.showinfo("Status do produto","Luvas (★) Degradê MW não foi adicionado ao carrinho.")
    def AddLuva2():
        global luvas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            luvas_lista.append(["Luvas (★) Nocts FT",1944," 1.944,00",Espaço(40-len("Luvas (★) Nocts FT"))])
            messagebox.showinfo("Status do produto","Luvas (★) Nocts FT foi adicionado ao carrinho com sucesso!")
        else:
            messagebox.showinfo("Status do produto","Luvas (★) Nocts FT não foi adicionado ao carrinho.")
    def AddLuva3():
        global luvas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            luvas_lista.append(["Luvas (★) Onça Rainha FT",1580," 1.580,00",Espaço(40-len("Luvas (★) Onça Rainha FT"))])
            messagebox.showinfo("Status do produto","Luvas (★) Onça Rainha FT foi adicionado ao carrinho com sucesso!")
        else:
            messagebox.showinfo("Status do produto","Luvas (★) Onça Rainha FT não foi adicionado ao carrinho.")
    def AddLuva4():
        global luvas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            luvas_lista.append(["Luvas (★) Quimono Carmesim",9550," 9.550,00 ",Espaço(40-len("Luvas (★) Quimono Carmesim"))])
            messagebox.showinfo("Status do produto","Luvas (★) Quimono Carmesim foi adicionado ao carrinho com sucesso!")
        else:
            messagebox.showinfo("Status do produto","Luvas (★) Quimono Carmesim não foi adicionado ao carrinho.")
    def AddLuva5():
        global luvas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            luvas_lista.append(["Luvas (★) Abocanhada FT",1476," 1.476,00",Espaço(40-len("Luvas (★) Abocanhada FT"))])
            messagebox.showinfo("Status do produto","Luvas (★) Abocanhada FT foi adicionado ao carrinho com sucesso!")
        else:
            messagebox.showinfo("Status do produto","Luvas (★) Abocanhada FT não foi adicionado ao carrinho.")
    def AddLuva6():
        global luvas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            luvas_lista.append(["Luvas (★) Labirinto Vivo FT",7890," 7.890,00",Espaço(40-len("Luvas (★) Labirinto Vivo FT"))])
            messagebox.showinfo("Status do produto","Luvas (★) Labirinto Vivo FT foi adicionado ao carrinho com sucesso!")
        else:
            messagebox.showinfo("Status do produto","Luvas (★) Labirinto Vivo FT não foi adicionado ao carrinho.")
    def AddLuva7():
        global luvas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            luvas_lista.append(["Luvas (★) Bordado FT",397," 397,00",Espaço(40-len("Luvas (★) Bordado FT"))])
            messagebox.showinfo("Status do produto","Luvas (★) Bordado FT foi adicionado ao carrinho com sucesso!")
        else:
            messagebox.showinfo("Status do produto","Luvas (★) Bordado FT não foi adicionado ao carrinho.")
    def AddLuva8():
        global luvas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            luvas_lista.append(["Luvas (★) Piloto Verde BS",285," 285,00",Espaço(40-len("Luvas (★) Piloto Verde BS"))])
            messagebox.showinfo("Status do produto","Luvas (★) Piloto Verde BS foi adicionado ao carrinho com sucesso!")
        else:
            messagebox.showinfo("Status do produto","Luvas (★) Piloto Verde BS não foi adicionado ao carrinho.")
    def AddLuva9():
        global luvas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            luvas_lista.append(["Luvas (★) Sapo amarelo FT",575," 575,00",Espaço(40-len("Luvas (★) Sapo amarelo FT"))])
            messagebox.showinfo("Status do produto","Luvas (★) Sapo amarelo FT foi adicionado ao carrinho com sucesso!")
        else:
            messagebox.showinfo("Status do produto","Luvas (★) Sapo amarelo FT não foi adicionado ao carrinho.")
    def AddLuva10():
        global luvas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            luvas_lista.append(["Luvas (★) Transporte FT",585," 585,00",Espaço(40-len("Luvas (★) Transporte FT"))])
            messagebox.showinfo("Status do produto","Luvas (★) Transporte FT foi adicionado ao carrinho com sucesso!")
        else:
            messagebox.showinfo("Status do produto","Luvas (★) Transporte FT não foi adicionado ao carrinho.")
            
    preco_luva1=Label(luva1,text="Preço: R$ R$ 7.776,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_luva2=Label(luva2,text="Preço: R$ 1.944,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_luva3=Label(luva3,text="Preço: R$ 1.580,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_luva4=Label(luva4,text="Preço: R$ 9.550,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_luva5=Label(luva5,text="Preço: R$ 1.476,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_luva6=Label(luva6,text="Preço: R$ 7.890,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_luva7=Label(luva7,text="Preço: R$ 397,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_luva8=Label(luva8,text="Preço: R$ 285,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_luva9=Label(luva9,text="Preço: R$ 575,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_luva10=Label(luva10,text="Preço: R$ R$ 585,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    
    botao_luva1=Button(luva1,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddLuva1).place(x=65,y=240)
    botao_luva2=Button(luva2,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddLuva2).place(x=65,y=240)
    botao_luva3=Button(luva3,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddLuva3).place(x=65,y=240)
    botao_luva4=Button(luva4,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddLuva4).place(x=65,y=240)
    botao_luva5=Button(luva5,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddLuva5).place(x=65,y=240)
    botao_luva6=Button(luva6,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddLuva6).place(x=65,y=240)
    botao_luva7=Button(luva7,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddLuva7).place(x=65,y=240)
    botao_luva8=Button(luva8,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddLuva8).place(x=65,y=240)
    botao_luva9=Button(luva9,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddLuva9).place(x=65,y=240)
    botao_luva10=Button(luva10,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddLuva10).place(x=65,y=240)
    
    
    

    
    
def ArmasL():
    Esconder()
    titulo_armas=Label(produtos_ex,text="Armas",font="times 15 bold",fg="#C172FF",bg="#0C1012").place(x=500)
    arma1=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    arma1.place(x=5,y=35,width=200,height=270)
    arma2=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    arma2.place(x=210,y=35,width=200,height=270)
    arma3=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    arma3.place(x=415,y=35,width=200,height=270)
    arma4=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    arma4.place(x=620,y=35,width=200,height=270)
    arma5=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    arma5.place(x=825,y=35,width=200,height=270)
    arma6=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    arma6.place(x=5,y=310,width=200,height=270)
    arma7=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    arma7.place(x=210,y=310,width=200,height=270)
    arma8=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    arma8.place(x=415,y=310,width=200,height=270)
    arma9=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    arma9.place(x=620,y=310,width=200,height=270)
    arma10=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    arma10.place(x=825,y=310,width=200,height=270)
    
    
    div_arma1=Label(arma1,image=arma1_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_arma2=Label(arma2,image=arma2_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_arma3=Label(arma3,image=arma3_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_arma4=Label(arma4,image=arma4_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_arma5=Label(arma5,image=arma5_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_arma6=Label(arma6,image=arma6_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_arma7=Label(arma7,image=arma7_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_arma8=Label(arma8,image=arma8_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_arma9=Label(arma9,image=arma9_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_arma10=Label(arma10,image=arma10_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    
    nome_arma1=Label(arma1,text="AK-47 | Bomba de Combustível",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_arma2=Label(arma2,text="M4A4 | Neo-Noir ",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_arma3=Label(arma3,text="AK-47 | Imperatriz",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_arma4=Label(arma4,text="AK-47 | Serpente de Fogo",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_arma5=Label(arma5,text="AK-47 | Vermelho Laminado",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_arma6=Label(arma6,text="AK-47 | Asimmov",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_arma7=Label(arma7,text="M4A4 | Uivo",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_arma8=Label(arma8,text="AWP | Neo-Noir",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_arma9=Label(arma9,text="AWP | Medusa",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_arma10=Label(arma10,text="AWP | Sabedoria do Dragão",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    
    float1=Label(arma1,text="Float: 0.6529181", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float2=Label(arma2,text="Float: 0.2362526", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float3=Label(arma3,text="Float: 0.6795464", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float4=Label(arma4,text="Float: 0.7805423", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float5=Label(arma5,text="Float: 0.5486436", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float6=Label(arma6,text="Float: 0.4535645", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float7=Label(arma7,text="Float: 0.3546543", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float8=Label(arma8,text="Float: 0.4565744", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float9=Label(arma9,text="Float: 0.6585354", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    float10=Label(arma10,text="Float: 0.4362347", bd=1,font="arial 9",justify="left",fg="#C172FF",bg="#0C1012").place(x=7,y=200)
    
    def AddArma1():
        global armas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            armas_lista.append(["AK-47 | Bomba de Combustível",590," 590,00",Espaço(40-len("AK-47 | Bomba de Combustível"))])
            messagebox.showinfo("Status do produto","AK-47 | Bomba de Combustível foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","AK-47 | Bomba de Combustível não foi adicionado ao carrinho.")
    def AddArma2():
        global armas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            armas_lista.append(["M4A4 | Neo-Noir",70," 70,00",Espaço(40-len("M4A4 | Neo-Noir"))])
            messagebox.showinfo("Status do produto","M4A4 | Neo-Noir foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","M4A4 | Neo-Noir não foi adicionado ao carrinho.")
    def AddArma3():
        global armas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            armas_lista.append(["AK-47 | Imperatriz",201," 201,00",Espaço(40-len("AK-47 | Imperatriz"))])
            messagebox.showinfo("Status do produto","AK-47 | Imperatriz foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","AK-47 | Imperatriz não foi adicionado ao carrinho.")
    def AddArma4():
        global armas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            armas_lista.append(["AK-47 | Serpente de Fogo",3150," 3,150.00 ",Espaço(40-len("AK-47 | Serpente de Fogo"))])
            messagebox.showinfo("Status do produto","AK-47 | Serpente de Fogo foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","AK-47 | Serpente de Fogo não foi adicionado ao carrinho.")
    def AddArma5():
        global armas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            armas_lista.append(["AK-47 | Vermelho Laminado",170," 170,00",Espaço(40-len("AK-47 | Vermelho Laminado"))])
            messagebox.showinfo("Status do produto","AK-47 | Vermelho Laminado foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","AK-47 | Vermelho Laminado não foi adicionado ao carrinho.")
    def AddArma6():
        global armas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            armas_lista.append(["AK-47 | Asimmov",153," 153,00",Espaço(40-len("AK-47 | Asimmov"))])
            messagebox.showinfo("Status do produto","AK-47 | Asimmov foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","AK-47 | Asimmov não foi adicionado ao carrinho.")
    def AddArma7():
        global armas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            armas_lista.append(["M4A4 | Uivo",27671," 27.671,00",Espaço(40-len("M4A4 | Uivo"))])
            messagebox.showinfo("Status do produto","M4A4 | Uivo foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","M4A4 | Uivo não foi adicionado ao carrinho.")
    def AddArma8():
        global armas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            armas_lista.append(["AWP | Neo-Noir",172," 172,00",Espaço(40-len("AWP | Neo-Noir"))])
            messagebox.showinfo("Status do produto","AWP | Neo-Noir foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","AWP | Neo-Noir não foi adicionado ao carrinho.")
    def AddArma9():
        global armas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            armas_lista.append(["AWP | Medusa",9526," 9.526,00",Espaço(40-len("AWP | Medusa"))])
            messagebox.showinfo("Status do produto","AWP | Medusa foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","AWP | Medusa não foi adicionado ao carrinho.")
    def AddArma10():
        global armas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            armas_lista.append(["AWP | Sabedoria do Dragão",67071," 67.071,00",Espaço(40-len("AWP | Sabedoria do Dragão"))])
            messagebox.showinfo("Status do produto","AWP | Sabedoria do Dragão foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","AWP | Sabedoria do Dragão não foi adicionado ao carrinho.")
    
    preco_arma1=Label(arma1,text="Preço: R$ 590,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_arma2=Label(arma2,text="Preço: R$ 70,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_arma3=Label(arma3,text="Preço: R$ 201,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_arma4=Label(arma4,text="Preço: R$ 3,150.00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_arma5=Label(arma5,text="Preço: R$ 170,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_arma6=Label(arma6,text="Preço: R$ 153,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_arma7=Label(arma7,text="Preço: R$ 27.671,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_arma8=Label(arma8,text="Preço: R$ 172,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_arma9=Label(arma9,text="Preço: R$ 9.526,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_arma10=Label(arma10,text="Preço: R$ 67.071,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    
    botao_arma1=Button(arma1,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddArma1).place(x=68,y=240)
    botao_arma2=Button(arma2,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddArma2).place(x=68,y=240)
    botao_arma3=Button(arma3,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddArma3).place(x=68,y=240)
    botao_arma4=Button(arma4,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddArma4).place(x=68,y=240)
    botao_arma5=Button(arma5,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddArma5).place(x=68,y=240)
    botao_arma6=Button(arma6,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddArma6).place(x=68,y=240)
    botao_arma7=Button(arma7,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddArma7).place(x=68,y=240)
    botao_arma8=Button(arma8,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddArma8).place(x=68,y=240)
    botao_arma9=Button(arma9,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddArma9).place(x=68,y=240)
    botao_arma10=Button(arma10,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddArma10).place(x=68,y=240)
    
    
    
    
    
    
def AdesivoL():
    Esconder()
    titulo_adesivos=Label(produtos_ex,text="Adesivo",font="times 15 bold",fg="#C172FF",bg="#0C1012").place(x=500)
    adesivo1=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    adesivo1.place(x=5,y=35,width=200,height=270)
    adesivo2=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    adesivo2.place(x=210,y=35,width=200,height=270)
    adesivo3=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    adesivo3.place(x=415,y=35,width=200,height=270)
    adesivo4=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    adesivo4.place(x=620,y=35,width=200,height=270)
    adesivo5=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    adesivo5.place(x=825,y=35,width=200,height=270)
    adesivo6=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    adesivo6.place(x=5,y=310,width=200,height=270)
    adesivo7=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    adesivo7.place(x=210,y=310,width=200,height=270)
    adesivo8=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    adesivo8.place(x=415,y=310,width=200,height=270)
    adesivo9=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    adesivo9.place(x=620,y=310,width=200,height=270)
    adesivo10=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    adesivo10.place(x=825,y=310,width=200,height=270)
    
    
    div_adesivo1=Label(adesivo1,image=adesivo1_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_adesivo2=Label(adesivo2,image=adesivo2_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_adesivo3=Label(adesivo3,image=adesivo3_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_adesivo4=Label(adesivo4,image=adesivo4_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_adesivo5=Label(adesivo5,image=adesivo5_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_adesivo6=Label(adesivo6,image=adesivo6_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_adesivo7=Label(adesivo7,image=adesivo7_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_adesivo8=Label(adesivo8,image=adesivo8_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_adesivo9=Label(adesivo9,image=adesivo9_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    div_adesivo10=Label(adesivo10,image=adesivo10_img,bd=2,justify="center",bg="#0C1012").grid(row=0,column=0)
    
    nome_adesivo1=Label(adesivo1,text="Adesivo | FURIA 2021 (Holo) ",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=2)
    nome_adesivo2=Label(adesivo2,text="Adesivo | Marcas de Guerra",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=-3)
    nome_adesivo3=Label(adesivo3,text="Adesivo | Sabedoria do Dragão ",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_adesivo4=Label(adesivo4,text="Adesivo | Diabo do Ás (Brilhante)",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=1)
    nome_adesivo5=Label(adesivo5,text="Adesivo | Elite Global (Brilhante)",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=3)
    nome_adesivo6=Label(adesivo6,text="Adesivo | Runtime (Holo)",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_adesivo7=Label(adesivo7,text="Adesivo | Coroa (Brilhante)",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_adesivo8=Label(adesivo8,text="Adesivo | Incineração (Holo)",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=0)
    nome_adesivo9=Label(adesivo9,text="Adesivo | Bruxaria (Holo)",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_adesivo10=Label(adesivo10,text="Adesivo | Veterano da Guerra \nàs Drogas",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=1)

    
    def AddAdesivo1():
        global Adesivo_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            Adesivo_lista.append(["FURIA (Holo) | Stockholm 2021",9," 9,00",Espaço(40-len("FURIA (Holo) | Stockholm 2021"))])
            messagebox.showinfo("Status do produto","FURIA (Holo) | Stockholm 2021 foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","FURIA (Holo) | Stockholm 2021 não foi adicionado ao carrinho.")
    def AddAdesivo2():
        global Adesivo_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            Adesivo_lista.append(["Marcas de Guerra ",20," 20,00",Espaço(40-len("Marcas de Guerra"))])
            messagebox.showinfo("Status do produto","Marcas de Guerra foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","Marcas de Guerra não foi adicionado ao carrinho.")
    def AddAdesivo3():
        global Adesivo_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            Adesivo_lista.append(["Sabedoria do Dragão",68," 68,00",Espaço(40-len("Sabedoria do Dragão"))])
            messagebox.showinfo("Status do produto","Sabedoria do Dragão foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","Sabedoria do Dragão não foi adicionado ao carrinho.")
    def AddAdesivo4():
        global Adesivo_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            Adesivo_lista.append(["Diabo do Ás (Brilhante)",23," 23,00",Espaço(40-len("Diabo do Ás (Brilhante)"))])
            messagebox.showinfo("Status do produto","Diabo do Ás (Brilhante) foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","Diabo do Ás (Brilhante) não foi adicionado ao carrinho.")
    def AddAdesivo5():
        global Adesivo_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            Adesivo_lista.append(["Elite Global (Brilhante)",65," 65,00",Espaço(40-len("Elite Global (Brilhante)"))])
            messagebox.showinfo("Status do produto","Elite Global (Brilhante) foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","Elite Global (Brilhante) não foi adicionado ao carrinho.")
    def AddAdesivo6():
        global Adesivo_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            Adesivo_lista.append(["Runtime (Holo)",46," 46,00",Espaço(40-len("Runtime (Holo)"))])
            messagebox.showinfo("Status do produto","Runtime (Holo) foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","Runtime (Holo) não foi adicionado ao carrinho.")
    def AddAdesivo7():
        global Adesivo_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            Adesivo_lista.append(["Coroa (Brilhante)",3144," 3.144,00",Espaço(40-len("Coroa (Brilhante)"))])
            messagebox.showinfo("Status do produto","Coroa (Brilhante) foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","Coroa (Brilhante) não foi adicionado ao carrinho.")
    def AddAdesivo8():
        global Adesivo_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            Adesivo_lista.append(["Incineração (Holo)",19," 19,00",Espaço(40-len("Incineração (Holo)"))])
            messagebox.showinfo("Status do produto","Incineração (Holo) foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","Incineração (Holo) não foi adicionado ao carrinho.")
    def AddAdesivo9():
        global Adesivo_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            Adesivo_lista.append(["Bruxaria ",7," 7,00",Espaço(40-len("Bruxaria (Holo)"))])
            messagebox.showinfo("Status do produto","Bruxaria (Holo) foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","Bruxaria (Holo) não foi adicionado ao carrinho.")
    def AddAdesivo10():
        global Adesivo_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            Adesivo_lista.append(["Veterano da Guerra às Drogas",5," 5,00",Espaço(40-len("Veterano da Guerra às Drogas"))])
            messagebox.showinfo("Status do produto","Veterano da Guerra às Drogas foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","Veterano da Guerra às Drogas não foi adicionado ao carrinho.")
            
    
    
    preco_adesivo1=Label(adesivo1,text="Preço: R$ 9,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_adesivo2=Label(adesivo2,text="Preço: R$ 20,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_adesivo3=Label(adesivo3,text="Preço: R$ 68,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_adesivo4=Label(adesivo4,text="Preço: R$ 23,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_adesivo5=Label(adesivo5,text="Preço: R$ 65,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_adesivo6=Label(adesivo6,text="Preço: R$ 46,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_adesivo7=Label(adesivo7,text="Preço: R$ 3.144,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_adesivo8=Label(adesivo8,text="Preço: R$ 19,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_adesivo9=Label(adesivo9,text="Preço: R$ 7,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_adesivo10=Label(adesivo10,text="Preço: R$ 5,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    
    botao_adesivo1=Button(adesivo1,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddAdesivo1).place(x=68,y=240)  
    botao_adesivo2=Button(adesivo2,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddAdesivo2).place(x=68,y=240)
    botao_adesivo3=Button(adesivo3,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddAdesivo3).place(x=68,y=240)
    botao_adesivo4=Button(adesivo4,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddAdesivo4).place(x=68,y=240)
    botao_adesivo5=Button(adesivo5,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddAdesivo5).place(x=68,y=240)
    botao_adesivo6=Button(adesivo6,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddAdesivo6).place(x=68,y=240)
    botao_adesivo7=Button(adesivo7,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddAdesivo7).place(x=68,y=240)
    botao_adesivo8=Button(adesivo8,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddAdesivo8).place(x=68,y=240)
    botao_adesivo9=Button(adesivo9,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddAdesivo9).place(x=68,y=240)
    botao_adesivo10=Button(adesivo10,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddAdesivo10).place(x=68,y=240)




    
    
    
def CaixaL():
    Esconder()
    titulo_caixas=Label(produtos_ex,text="Caixas",font="times 15 bold",fg="#C172FF",bg="#0C1012").place(x=500)
    caixa1=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    caixa1.place(x=5,y=35,width=200,height=270)
    caixa2=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    caixa2.place(x=210,y=35,width=200,height=270)
    caixa3=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    caixa3.place(x=415,y=35,width=200,height=270)
    caixa4=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    caixa4.place(x=620,y=35,width=200,height=270)
    caixa5=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    caixa5.place(x=825,y=35,width=200,height=270)
    caixa6=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    caixa6.place(x=5,y=310,width=200,height=270)
    caixa7=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    caixa7.place(x=210,y=310,width=200,height=270)
    caixa8=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    caixa8.place(x=415,y=310,width=200,height=270)
    caixa9=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    caixa9.place(x=620,y=310,width=200,height=270)
    caixa10=LabelFrame(produtos_ex,bd=2,bg="#0C1012",padx= 8,relief="groove")
    caixa10.place(x=825,y=310,width=200,height=270)
    
    div_caixa1=Label(caixa1,image=caixa1_img,bd=2,justify="center",fg="#C172FF",bg="#0C1012").grid(row=0,column=0)
    div_caixa2=Label(caixa2,image=caixa2_img,bd=2,justify="center",fg="#C172FF",bg="#0C1012").grid(row=0,column=0)
    div_caixa3=Label(caixa3,image=caixa3_img,bd=2,justify="center",fg="#C172FF",bg="#0C1012").grid(row=0,column=0)
    div_caixa4=Label(caixa4,image=caixa4_img,bd=2,justify="center",fg="#C172FF",bg="#0C1012").grid(row=0,column=0)
    div_caixa5=Label(caixa5,image=caixa5_img,bd=2,justify="center",fg="#C172FF",bg="#0C1012").grid(row=0,column=0)
    div_caixa6=Label(caixa6,image=caixa6_img,bd=2,justify="center",fg="#C172FF",bg="#0C1012").grid(row=0,column=0)
    div_caixa7=Label(caixa7,image=caixa7_img,bd=2,justify="center",fg="#C172FF",bg="#0C1012").grid(row=0,column=0)
    div_caixa8=Label(caixa8,image=caixa8_img,bd=2,justify="center",fg="#C172FF",bg="#0C1012").grid(row=0,column=0)
    div_caixa9=Label(caixa9,image=caixa9_img,bd=2,justify="center",fg="#C172FF",bg="#0C1012").grid(row=0,column=0)
    div_caixa10=Label(caixa10,image=caixa10_img,bd=2,justify="center",fg="#C172FF",bg="#0C1012").grid(row=0,column=0)
    
    nome_caixa1=Label(caixa1,text="Caixa Cromática",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_caixa2=Label(caixa2,text="Caixa Sombria",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_caixa3=Label(caixa3,text="Caixa Falchion",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7) 
    nome_caixa4=Label(caixa4,text="Caixa Gama",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_caixa5=Label(caixa5,text="Caixa Prismática",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_caixa6=Label(caixa6,text="Caixa Fraturada",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_caixa7=Label(caixa7,text="Caixa Espectral",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_caixa8=Label(caixa8,text="Caixa das Luvas",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_caixa9=Label(caixa9,text="Caixa da Operação Hidra",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)
    nome_caixa10=Label(caixa10,text="Caixa de Armas do Caçador",font="arial 9",justify="center",fg="#C172FF",bg="#0C1012").place(x=7)

  
    def AddCaixa1():
        global caixas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            caixas_lista.append(["Caixa Cromática",6," 6,00",Espaço(40-len("Caixa Cromática"))])
            messagebox.showinfo("Status do produto","Caixa Cromática foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","Caixa Cromática não foi adicionado ao carrinho.")
    def AddCaixa2():
        global caixas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            caixas_lista.append(["IFB Front Load",2," 2,00",Espaço(40-len("IFB Front Load"))])
            messagebox.showinfo("Status do produto","Caixa Sombria foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","Caixa Sombria não foi adicionado ao carrinho.")
    def AddCaixa3():
        global caixas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            caixas_lista.append(["Caixa Falchion",1," 1,00",Espaço(40-len("Caixa Falchion"))])
            messagebox.showinfo("Status do produto","Caixa Falchion foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","Caixa Falchion não foi adicionado ao carrinho.")
    def AddCaixa4():
        global caixas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            caixas_lista.append(["Caixa Gama",4," 4,00",Espaço(40-len("Caixa Gama"))])
            messagebox.showinfo("Status do produto","Caixa Gama foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","Caixa Gama não foi adicionado ao carrinho.")
    def AddCaixa5():
        global caixas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            caixas_lista.append(["Caixa Prismática",3," 3,00",Espaço(40-len("Caixa Prismática"))])
            messagebox.showinfo("Status do produto","Caixa Prismática foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","Caixa Prismática não foi adicionado ao carrinho.")
    def AddCaixa6():
        global caixas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            caixas_lista.append(["Caixa Fraturada",8," 8,00",Espaço(40-len("Caixa Fraturada"))])
            messagebox.showinfo("Status do produto","Caixa Fraturada foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","Caixa Fraturada não foi adicionado ao carrinho.")
    def AddCaixa7():
        global caixas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            caixas_lista.append(["Caixa Espectral",5," 5,00",Espaço(40-len("Caixa Espectral"))])
            messagebox.showinfo("Status do produto","Caixa Espectral foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","Caixa Espectral não foi adicionado ao carrinho.")
    def AddCaixa8():
        global caixas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            caixas_lista.append(["Caixa das Luvas",13," 13,00",Espaço(40-len("Caixa das Luvas"))])
            messagebox.showinfo("Status do produto","Caixa das Luvas foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","Caixa das Luvas não foi adicionado ao carrinho.")
    def AddCaixa9():
        global caixas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            caixas_lista.append(["Caixa da Operação Hidra",77," 77,00",Espaço(40-len("Caixa da Operação Hidra"))])
            messagebox.showinfo("Status do produto","Caixa da Operação Hidra foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","Caixa da Operação Hidra não foi adicionado ao carrinho.")
    def AddCaixa10():
        global caixas_lista
        op=messagebox.askyesno("Compra Confirmada","Tem certeza de que deseja adicionar este item ao carrinho?")
        if op:
            caixas_lista.append(["Caixa de Armas do Caçador",22," 22,00",Espaço(40-len("Caixa de Armas do Caçador"))])
            messagebox.showinfo("Status do produto","Caixa de Armas do Caçador foi adicionado com sucesso ao carrinho.")
        else:
            messagebox.showinfo("Status do produto","Caixa de Armas do Caçador não foi adicionado ao carrinho.")
    
    
    preco_caixa1=Label(caixa1,text="Preço: R$ 6,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_caixa2=Label(caixa2,text="Preço: R$ 2,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_caixa3=Label(caixa3,text="Preço: R$ 1,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_caixa4=Label(caixa4,text="Preço: R$ 4,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_caixa5=Label(caixa5,text="Preço: R$ 3,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_caixa6=Label(caixa6,text="Preço: R$ 8,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_caixa7=Label(caixa7,text="Preço: R$ 5,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_caixa8=Label(caixa8,text="Preço: R$ 13,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_caixa9=Label(caixa9,text="Preço: R$ 77,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    preco_caixa10=Label(caixa10,text="Preço: R$ 22,00",font="arial 9 bold",fg="#C172FF",bg="#0C1012").place(x=5,y=220)
    
    botao_caixa1=Button(caixa1,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddCaixa1).place(x=68,y=240)
    botao_caixa2=Button(caixa2,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddCaixa2).place(x=68,y=240)
    botao_caixa3=Button(caixa3,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddCaixa3).place(x=68,y=240)
    botao_caixa4=Button(caixa4,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddCaixa4).place(x=68,y=240)
    botao_caixa5=Button(caixa5,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddCaixa5).place(x=68,y=240)
    botao_caixa6=Button(caixa6,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddCaixa6).place(x=68,y=240)
    botao_caixa7=Button(caixa7,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddCaixa7).place(x=68,y=240)
    botao_caixa8=Button(caixa8,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddCaixa8).place(x=68,y=240)
    botao_caixa9=Button(caixa9,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddCaixa9).place(x=68,y=240)
    botao_caixa10=Button(caixa10,text="COMPRAR",fg="#C172FF",bg="#0C1012",font="times 9 bold",command=AddCaixa10).place(x=68,y=240)
    
    




    
    
botao_faca=Button(botao_comprar,text="FACAS",font="times 20 bold",width=17,bd=6,bg="#0C1012",fg="#C172FF",activebackground="#6506B0",command=FacasL)
botao_faca.grid(row=0,column=0,padx=5,pady=5)
botao_luva=Button(botao_comprar,text="LUVAS",font="times 20 bold",width=17,bd=6,bg="#0C1012",fg="#C172FF",activebackground="#6506B0",command=LuvasL)
botao_luva.grid(row=1,column=0,padx=5,pady=5)   
botao_arma=Button(botao_comprar,text="ARMAS",font="times 20 bold",width=17,bd=6,bg="#0C1012",fg="#C172FF",activebackground="#6506B0",command=ArmasL)
botao_arma.grid(row=2,column=0,padx=5,pady=5)
botao_adesivo=Button(botao_comprar,text="ADESIVOS",font="times 20 bold",width=17,bd=6,bg="#0C1012",fg="#C172FF",activebackground="#6506B0",command=AdesivoL)
botao_adesivo.grid(row=3,column=0,padx=5,pady=5)
botao_caixa=Button(botao_comprar,text="CAIXAS",font="times 20 bold",width=17,bd=6,bg="#0C1012",fg="#C172FF",activebackground="#6506B0",command=CaixaL)
botao_caixa.grid(row=4,column=0,padx=5,pady=5)

cupom_local=LabelFrame(root,bd=2,relief="groove",text="MEGA PROMOÇÃO!!!",bg="#0C1012",fg="#C172FF",font="arial 16 bold")
cupom_local.place(x=2,y=450,width=300,height=230)

cupom1=Label(cupom_local,text="FALLEN - Garante 15% Off.",font="arial 15 bold",fg="#FFF",bg="#0C1012")
cupom2=Label(cupom_local,text="XITADO - Garante 10% Off.",font="arial 15 bold",fg="#FFF",bg="#0C1012")
cupom3=Label(cupom_local,text="FKS - Garante 5% Off.",font="arial 15 bold",fg="#FFF",bg="#0C1012")

cupom1.grid(row=0,column=0,padx=10,pady=17)
cupom2.grid(row=1,column=0,padx=10,pady=17)
cupom3.grid(row=2,column=0,padx=10,pady=17)





def Precos():
    op=messagebox.askyesno("Confirmação de geração de fatura.","\nOs produtos não podem ser adicionados ou removidos após a geração da fatura.\n\n Tem certeza de que terminou de comprar?")
    if op:
        produtos_ex.destroy()
        botao_comprar.destroy()
        cupom_local.destroy()
        botao_buy.destroy()

        luva_preco=0
        faca_preco=0
        arma_preco=0
        adesivo_preco=0
        caixa_preco=0

        for i in range(len(Facas_lista)):
            luva_preco+=Facas_lista[i][1]
        for i in range(len(luvas_lista)):
            faca_preco+=luvas_lista[i][1]
        for i in range(len(armas_lista)):
            arma_preco+=armas_lista[i][1]
        for i in range(len(Adesivo_lista)):
            adesivo_preco+=Adesivo_lista[i][1]
        for i in range(len(caixas_lista)):
            caixa_preco+=caixas_lista[i][1]

        total=luva_preco+faca_preco+arma_preco+adesivo_preco+caixa_preco
        
        desconto=[0,0,0]

        if 0.15*total>0:
            desconto[0]=0.15*total
        elif 0.1*total>0:
            desconto[1]=0.1*total
        else :
            desconto[2]=0.05*total

            
            
            
        def GenPrecos(d,escolha):
            Precos_area=LabelFrame(root,bd=2,relief="groove")
            Precos_area.place(x=305,y=80,width=750,height=600)
            Precos_title=Label(Precos_area,text="NOTA FISCAL",font="arial 15 bold",bd=4,relief="groove").pack(fill=X)
            scroll_y=Scrollbar(Precos_area,orient=VERTICAL)
            area_texto=Text(Precos_area,yscrollcommand=scroll_y.set)
            scroll_y.pack(side=RIGHT,fill=Y)
            scroll_y.config(command=area_texto.yview)
            area_texto.pack(fill=BOTH,expand=1)
            area_texto.insert(END,Espaço(40)+"TkG Skins.gg\n"+Espaço(90,'*')+"\n")
            
            if len(Facas_lista)>0:
                area_texto.insert(END,"Faca(s)\n\nNome do produto"+Espaço(28)+"Preço"+Espaço(25)+"\n")
                for i in Facas_lista:
                    area_texto.insert(END,i[0]+i[3]+"R$ "+i[2]+"\n")
                area_texto.insert(END,"\nPreço total das facas R$:"+str(luva_preco)+"\n"+Espaço(90,'*')+"\n")
                
            if len(luvas_lista)>0:
                area_texto.insert(END,"Luva(s)\n\nNome do produto"+Espaço(28)+"Preço"+Espaço(25)+"\n")
                for i in luvas_lista:
                    area_texto.insert(END,i[0]+i[3]+"R$ "+i[2]+"\n")
                area_texto.insert(END,"\nPreço total das luvas R$:"+str(faca_preco)+"\n"+Espaço(90,'*')+"\n")
                
            if len(armas_lista)>0:
                area_texto.insert(END,"Arma(s)\n\nNome do produto"+Espaço(28)+"Preço\n")
                for i in armas_lista:
                    area_texto.insert(END,i[0]+i[3]+"R$ "+i[2]+"\n")
                area_texto.insert(END,"\nPreço total das armas R$:"+str(arma_preco)+"\n"+Espaço(90,'*')+"\n")
                
            if len(Adesivo_lista)>0:
                area_texto.insert(END,"Adesivo(s)\n\nNome do produto"+Espaço(28)+"Preço\n")
                for i in Adesivo_lista:
                    area_texto.insert(END,i[0]+i[3]+"R$ "+i[2]+"\n")
                area_texto.insert(END,"\nPreço total dos adesivo R$:"+str(adesivo_preco)+"\n"+Espaço(90,'*')+"\n")
                
            if len(caixas_lista)>0:
                area_texto.insert(END,"Caixa(s)\n\nNome do produto"+Espaço(28)+"Preço\n")
                for i in caixas_lista:
                    area_texto.insert(END,i[0]+i[3]+"R$ "+i[2]+"\n")
                area_texto.insert(END,"\nPreço total das caixas: R$:"+str(caixa_preco)+"\n"+Espaço(90,'*'))
            area_texto.insert(END,"\nPreço total(Antes do desconto) R$:"+str(total))
            
            
            
            if escolha==1:
                area_texto.insert(END,"\nCupom de desconto Aplicado : 15% Off.")
            elif escolha==2:
                area_texto.insert(END,"\nCupom de desconto Aplicado : 10% Off.")
            else:
                area_texto.insert(END,"\nCupom de desconto Aplicado : 5% Off.")
            area_texto.insert(END,"\nDesconto oferecido : R$ "+str(d))
            area_texto.insert(END,"\nPreço total(Depois do desconto) = R$:"+str(total-d))
            
            botao_salvar=Button(root,text="Salvar fatura",font="times 20 bold",bd=6,bg="black",width=10,fg="white",command=lambda:Salvar(area_texto.get("1.0",END)))
            botao_salvar.place(x=1120,y=600)
            
        aplicar_cupom=LabelFrame(root,bd=2,relief="groove",text="Aplicar Cupom",bg ="#0C1012",fg="#C172FF",font="arial 16 bold").place(x=500,y=150,width=380,height=300)
        aplicar1=Button(aplicar_cupom,text="FALLEN - 15%",font="times 20 bold",width=17,bd=6,bg="#0C1012",fg="white",activebackground="#0C1012",command=lambda:GenPrecos(desconto[0],1))
        aplicar1.place(x=540,y=190)
        aplicar2=Button(aplicar_cupom,text="XITADO - 10%",font="times 20 bold",width=17,bd=6,bg="#0C1012",fg="white",activebackground="#0C1012",command=lambda:GenPrecos(desconto[1],2))
        aplicar2.place(x=540,y=280)
        aplicar3=Button(aplicar_cupom,text="FKS - 5%",font="times 20 bold",width=17,bd=6,bg="#0C1012",fg="white",activebackground="#0C1012",command=lambda:GenPrecos(desconto[2],3))
        aplicar3.place(x=540,y=370)
    else:
        messagebox.showinfo("Confirmação de geração de fatura.","Você pode continuar comprando agora.")
        
botao_buy=Button(Heading,bd=4,text="Carrinho",font="times 17 bold",bg="#0C1012",fg="#C172FF",activebackground="purple",command=Precos)
botao_buy.grid(row=0,column=4)
botao_buy.place(x=1240, y=2)
root.mainloop()