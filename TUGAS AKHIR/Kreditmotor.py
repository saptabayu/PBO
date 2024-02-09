from db import DBConnection as mydb
class Credit_motor:
    def __init__(self):
        self.__id=None
        self.__nama_pengguna=None
        self.__tanggal_credit=None
        self.__tarif_subtotal=None
        self.__status_bayar=None
        self.conn = None
        self.affected = None
        self.result = None
    @property
    def id(self):
        return self.__id
    @property
    def nama_pengguna(self):
        return self.__nama_pengguna
        
    @nama_pengguna.setter
    def nama_pengguna(self, value):
        self.__nama_pengguna = value
    @property
    def tanggal_credit(self):
        return self.__tanggal_credit
        
    @tanggal_credit.setter
    def tanggal_credit(self, value):
        self.__tanggal_credit = value
    @property
    def tarif_subtotal(self):
        return self.__tarif_subtotal
        
    @tarif_subtotal.setter
    def tarif_subtotal(self, value):
        self.__tarif_subtotal = value
    @property
    def status_bayar(self):
        return self.__status_bayar
        
    @status_bayar.setter
    def status_bayar(self, value):
        self.__status_bayar = value
    def simpan(self):
        self.conn = mydb()
        val = (self.__nama_pengguna,self.__tanggal_credit,self.__tarif_subtotal,self.__status_bayar)
        sql="INSERT INTO Credit_motor (nama_pengguna,tanggal_credit,tarif_subtotal,status_bayar) VALUES " + str(val)
        self.affected = self.conn.insert(sql)
        self.conn.disconnect
        return self.affected
    def update(self, id):
        self.conn = mydb()
        val = (self.__nama_pengguna,self.__tanggal_credit,self.__tarif_subtotal,self.__status_bayar, id)
        sql="UPDATE credit_motor SET nama_pengguna = %s,tanggal_credit = %s,tarif_subtotal = %s,status_bayar = %s WHERE id=%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected
    def updateBy(self, ):
        self.conn = mydb()
        val = (self.__nama_pengguna,self.__tanggal_credit,self.__tarif_subtotal,self.__status_bayar, )
        sql="UPDATE credit_motor SET nama_pengguna = %s,tanggal_credit = %s,tarif_subtotal = %sstatus_bayar = %s WHERE =%s"
        self.affected = self.conn.update(sql, val)
        self.conn.disconnect
        return self.affected        
    def delete(self, id):
        self.conn = mydb()
        sql="DELETE FROM credit_motor WHERE id='" + str(id) + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def deleteBy(self, ):
        self.conn = mydb()
        sql="DELETE FROM credit_motor WHERE ='" + str() + "'"
        self.affected = self.conn.delete(sql)
        self.conn.disconnect
        return self.affected
    def getByID(self, id):
        self.conn = mydb()
        sql="SELECT * FROM credit_motor WHERE id='" + str(id) + "'"
        self.result = self.conn.findOne(sql)
        self.__id = self.result[0]
        self.__nama_pengguna = self.result[1]
        self.__tanggal_credit = self.result[2]
        self.__tarif_subtotal = self.result[3]
        self.__status_bayar = self.result[4]
        self.conn.disconnect
        return self.result
    def getBy(self, ):
        a=str()
        b=a.strip()
        self.conn = mydb()
        sql="SELECT * FROM credit_motor WHERE ='" + b + "'"
        self.result = self.conn.findOne(sql)
        if(self.result!=None):
           self.__id = self.result[0]
           self.__nama_pengguna = self.result[1]
           self.__tanggal_credit = self.result[2]
           self.__tarif_subtotal = self.result[3]
           self.__status_bayar = self.result[4]
           self.affected = self.conn.cursor.rowcount
        else:
           self.__id = ''
           self.__nama_pengguna = ''
           self.__tanggal_credit = ''
           self.__tarif_subtotal = ''
           self.__status_bayar = ''
        
           self.affected = 0
        self.conn.disconnect
        return self.result
    def getAllData(self):
        self.conn = mydb()
        sql="SELECT * FROM credit_motor"
        self.result = self.conn.findAll(sql)
        return self.result
        
    def getComboData(self):
        self.conn = mydb()
        sql="SELECT id,tanggal_credit FROM credit_motor"
        self.result = self.conn.findAll(sql)
        return self.result