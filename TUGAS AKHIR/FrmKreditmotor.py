import tkinter as tk
from tkinter import Frame, Label, Entry, Button, Radiobutton, ttk, VERTICAL, YES, BOTH, END, Tk, StringVar, messagebox
from Kreditmotor import Credit_motor
# pip install tkcalendar
from tkcalendar import Calendar, DateEntry

class FormCredit_motor:   
    def __init__(self, parent, title):
        self.parent = parent       
        self.parent.geometry("450x450")
        self.parent.title(title)
        self.parent.protocol("WM_DELETE_WINDOW", self.onKeluar)
        
        self.ditemukan = None
        self.aturKomponen()
        self.onReload()
        
    def aturKomponen(self):
        mainFrame = Frame(self.parent, bd=10)
        mainFrame.pack(fill=BOTH, expand=YES)
        
        # varchar 
        Label(mainFrame, text='NAMA_PENGGUNA:').grid(row=0, column=0, sticky='w', padx=5, pady=5)
        # Textbox NAMA_PENGGUNA
        self.txtNAMA_PENGGUNA = Entry(mainFrame) 
        self.txtNAMA_PENGGUNA.grid(row=0, column=1, padx=5, pady=5)
                
        # date 
        Label(mainFrame, text='TANGGAL_CREDIT:').grid(row=1, column=0, sticky='w', padx=5, pady=5)
        # Date Input TANGGAL_CREDIT
        self.txtTANGGAL_CREDIT = DateEntry(mainFrame, width=16, background="magenta3", foreground="white", bd=2, date_pattern='y-mm-dd') 
        self.txtTANGGAL_CREDIT.grid(row=1, column=1, padx=5, pady=5)
                    
        # decimal 
        Label(mainFrame, text='TARIF_SUBTOTAL:').grid(row=2, column=0, sticky='w', padx=5, pady=5)
        # Combo Box
        self.txtTARIF_SUBTOTAL = StringVar()
        CboTARIF_SUBTOTAL = ttk.Combobox(mainFrame, width=17, textvariable=self.txtTARIF_SUBTOTAL) 
        CboTARIF_SUBTOTAL.grid(row=2, column=1, padx=5, pady=5)
        # Adding combobox drop down list
        CboTARIF_SUBTOTAL['values'] = ('decimal10', '2')
        CboTARIF_SUBTOTAL.current()
        
        # varchar 
        Label(mainFrame, text='STATUS_BAYAR:').grid(row=3, column=0, sticky='w', padx=5, pady=5)
        # Textbox STATUS_BAYAR
        self.txtSTATUS_BAYAR = Entry(mainFrame) 
        self.txtSTATUS_BAYAR.grid(row=3, column=1, padx=5, pady=5)
                
        # Button
        self.btnSimpan = Button(mainFrame, text='Simpan', command=self.onSimpan, width=10)
        self.btnSimpan.grid(row=0, column=3, padx=5, pady=5)
        self.btnClear = Button(mainFrame, text='Clear', command=self.onClear, width=10)
        self.btnClear.grid(row=1, column=3, padx=5, pady=5)
        self.btnHapus = Button(mainFrame, text='Hapus', command=self.onDelete, width=10)
        self.btnHapus.grid(row=2, column=3, padx=5, pady=5)
        
        # define columns
        columns = ('id', 'nama_pengguna', 'tanggal_credit', 'tarif_subtotal', 'status_bayar')
        self.tree = ttk.Treeview(mainFrame, columns=columns, show='headings')
        # define headings
        self.tree.heading('id', text='id')
        self.tree.column('id', width=30)
        self.tree.heading('nama_pengguna', text='nama_pengguna')
        self.tree.column('nama_pengguna', width=100)
        self.tree.heading('tanggal_credit', text='tanggal_credit')
        self.tree.column('tanggal_credit', width=100)
        self.tree.heading('tarif_subtotal', text='tarif_subtotal')
        self.tree.column('tarif_subtotal', width=100)
        self.tree.heading('status_bayar', text='status_bayar')
        self.tree.column('status_bayar', width=100)
        # set tree position
        self.tree.place(x=0, y=250)
        self.onReload()
    
    def onClear(self, event=None):
        self.txtNAMA_PENGGUNA.delete(0, END)
        self.txtNAMA_PENGGUNA.insert(END, "")
                                
        self.txtSTATUS_BAYAR.delete(0, END)
        self.txtSTATUS_BAYAR.insert(END, "")
                                
        self.btnSimpan.config(text="Simpan")
        self.onReload()
        self.ditemukan = False
        
    def onReload(self, event=None):
        # get data credit_motor
        obj = Credit_motor()
        result = obj.getAllData()
        for item in self.tree.get_children():
            self.tree.delete(item)
        mylist=[]
        for row_data in result:
            mylist.append(row_data)
        for row in mylist:
            self.tree.insert('', END, values=row)
            
    def onCari(self, event=None):
        pass  # You can implement this method based on your requirements
    
    def TampilkanData(self, event=None):
        pass  # You can implement this method based on your requirements
    
    def onSimpan(self, event=None):
        nama_pengguna = self.txtNAMA_PENGGUNA.get()
        tanggal_credit = self.txtTANGGAL_CREDIT.get()
        tarif_subtotal = self.txtTARIF_SUBTOTAL.get()
        status_bayar = self.txtSTATUS_BAYAR.get()       
        obj = Credit_motor()
        obj.nama_pengguna = nama_pengguna
        obj.tanggal_credit = tanggal_credit
        obj.tarif_subtotal = tarif_subtotal
        obj.status_bayar = status_bayar
        if self.ditemukan == True:
            res = obj.updateBy()
            ket = 'Diperbarui'
        else:
            res = obj.simpan()
            ket = 'Disimpan'
            
        rec = obj.affected
        if rec > 0:
            messagebox.showinfo("showinfo", f"Data Berhasil {ket}")
        else:
            messagebox.showwarning("showwarning", f"Data Gagal {ket}")
        self.onClear()
        return rec
 
    def onDelete(self, event=None):
        pass  # You can implement this method based on your requirements
 
    def onKeluar(self, event=None):
        # memberikan perintah menutup aplikasi
        self.parent.destroy()

if __name__ == '__main__':
    root = tk.Tk()
    aplikasi = FormCredit_motor(root, "Aplikasi Data Credit_motor")
    root.mainloop()
