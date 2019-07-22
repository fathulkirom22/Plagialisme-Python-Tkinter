from Tkinter import *
from tkFileDialog import *
from math import *
import tkMessageBox as mb

class plagiat:
	def __init__(self,induk,nama):
		self.induk=induk
		self.induk.title(nama)
		self.induk.geometry("300x400")
		self.induk.maxsize(300,650)
		self.induk.minsize(300,450)
		self.pemberitahuan1=False
		self.pemberitahuan2=False
		self.textLabel1=''
		self.textLabel2=''
		self.tataletak("Dokumen 1","Dokumen 2")

	def tataletak(self,doc1,doc2):
		self.kiri = Frame(self.induk)
		self.kiri.pack( fill=BOTH, expand=YES)
		Label(
			self.kiri,
			bd = 2,
			borderwidth=0, 
			justify = CENTER, 
			relief = SUNKEN,
			fg='red',
			text='  ## APLIKASI DUGAAN PLAGIALISME ##  '
		).pack(padx=5, pady=10)
		self.cari1=Button(self.kiri, text=doc1, command=self.caridi1).pack()
		self.cari2=Button(self.kiri, text=doc2, command=self.caridi2).pack()
		self.cek=Button(self.kiri, text="CEK",command=self.eksekusi).pack(padx=5, pady=2)
		Label(
			self.kiri, 
			borderwidth = 0, 
			justify = CENTER ,
			text="""
ANGGOTA:

Fathul Kirom
Dicki Dwi P
Cahya Bintang
Benny K
				""",
			anchor=W
		).pack(padx=5, pady=5)

		#self.layar = Canvas(kanan,bg="white").pack(fill=BOTH, expand=YES)
		
		#Label(kanan, text=a).pack(expand=YES)

	def caridi1(self, event=None):
		openfile = askopenfilename(filetypes=[('Text Document','*.txt')])
		if openfile:
			self.pemberitahuan1=True
			self.textLabel1 = 'Dokumen 1 :'+str(openfile).split('/')[-1]
			self.label1=Label(self.kiri,bd = 2,borderwidth=0, justify = CENTER, relief = SUNKEN,fg='black',text=self.textLabel1).pack(padx=5, pady=10)
			a = open(openfile,'r').read()
			b=a.split(" ")
			print b
			c=0
			y=""
			z=[]#pan hitungan jumlah data yang samauntuk menyim
			for i in b:
				d=b[c]#alamat mengikuti i
				x=y.split(" ")#menjadikan aray variabel y
				for j in x:
					if (i not in x):
						e=b.count(d)#menghitung jumlah kata yang sama 
						z+=[e]#memasukan nilai kata yang telah di hitung kedalam variabl z
						break#menghentikan sub perulanagan agar tidak terjadi duplikasi data yang di cari
				y+=" "+i#mengambil nilai yang sudah di ulang
				c+=1
			self.balik1=z	
				
	def caridi2(self, event=None):
		#Label(self.kiri,bd = 2,borderwidth=3, justify = CENTER, relief = SUNKEN,fg='red',text='  ## APLIKASI DUGAAN PLAGIALISME ##  ').pack(padx=5, pady=10)
		openfile = askopenfilename(filetypes=[('Text Document','*.txt')])
		if openfile:
			self.pemberitahuan2=True
			self.textLabel2 = 'Dokumen 2 :'+str(openfile).split('/')[-1]
			self.label2=Label(self.kiri,bd = 2,borderwidth=0, justify = CENTER, relief = SUNKEN,fg='black',text=self.textLabel2).pack(padx=5, pady=10)
			a = open(openfile,'r').read()
			b=a.split(" ")
			print b
			c=0
			y=""
			z=[]#pan hitungan jumlah data yang samauntuk menyim
			for i in b:
				d=b[c]#alamat mengikuti i
				x=y.split(" ")#menjadikan aray variabel y
				for j in x:
					if (i not in x):
						e=b.count(d)#menghitung jumlah kata yang sama 
						z+=[e]#memasukan nilai kata yang telah di hitung kedalam variabl z
						break#menghentikan sub perulanagan agar tidak terjadi duplikasi data yang di cari
				y+=" "+i#mengambil nilai yang sudah di ulang
				c+=1
			self.balik2=z	

	def eksekusi(self):
		if(self.pemberitahuan1==False):
			mb.showinfo("PEMBERITAHUAN","Dokumen 1 belum di pilih !")
		elif(self.pemberitahuan2==False):
			mb.showinfo("PEMBERITAHUAN","Dokumen 2 belum di pilih !")
		else:
			a=(self.balik1)
			b=(self.balik2)
			c=len(a)
			d=len(b)
			bantu1=0.0;bantu2=0.0
			self.hasil=0.0
			e=0;f=0.0;g=0.0;h=0.0;k=0.0;l=0.0
			ea=0;fa=0.0;ga=0.0;ha=0.0;ka=0.0;la=0.0
			if(c<=d):
				for i in a:
					f+=(a[e]*b[e])
					g+=(a[e]**2)
					h+=(b[e]**2)
					e+=1
				k=sqrt(g)
				l=sqrt(h)
				bantu1=f/(k*l)
				print "1"
				print f,k,l
			else:
				for i in b:
					fa+=(a[ea]*b[ea])
					ga+=(a[ea]**2)
					ha+=(b[ea]**2)
					ea+=1
				ka=sqrt(ga)
				la=sqrt(ha)
				bantu2=fa/(ka*la)
				print "2"
				print fa,ka,la
			self.hasil=bantu1+bantu2
			print "Cos (Teta) :",self.hasil
			if (self.hasil>=0.866):
				mb.showerror("HASIL","SANGAT MIRIP !!!")
			elif (self.hasil>=0.5):
				mb.showwarning("HASIL","HAMPIR MIRIP !")
			else:
				mb.showinfo("HASIL","TIDAK MIRIP ^_^")

if __name__ == '__main__':
	jendela = Tk()
	app = plagiat(jendela, "ALJABAR LINEAR")
	jendela.mainloop()