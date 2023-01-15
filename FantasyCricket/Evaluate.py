# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Evaluate.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(573, 519)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBox1 = QtWidgets.QComboBox(Form)
        self.comboBox1.setObjectName("comboBox1")
        self.horizontalLayout.addWidget(self.comboBox1)
        spacerItem1 = QtWidgets.QSpacerItem(80, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.comboBox2 = QtWidgets.QComboBox(Form)
        self.comboBox2.setObjectName("comboBox2")
        self.horizontalLayout.addWidget(self.comboBox2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        spacerItem2 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        spacerItem3 = QtWidgets.QSpacerItem(300, 20, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        self.label_2 = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setPointSize(9)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        self.le1 = QtWidgets.QLineEdit(Form)
        self.le1.setObjectName("le1")
        self.horizontalLayout_2.addWidget(self.le1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.listView1 = QtWidgets.QListWidget(Form)
        self.listView1.setObjectName("listView1")
        self.horizontalLayout_3.addWidget(self.listView1)
        spacerItem5 = QtWidgets.QSpacerItem(100, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem5)
        self.listView2 = QtWidgets.QListWidget(Form)
        self.listView2.setObjectName("listView2")
        self.horizontalLayout_3.addWidget(self.listView2)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        spacerItem6 = QtWidgets.QSpacerItem(20, 10, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem6)
        self.b2 = QtWidgets.QPushButton(Form)
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.b2.setFont(font)
        self.b2.setObjectName("b2")
        self.verticalLayout.addWidget(self.b2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

        self.b2.clicked.connect(self.calculate)
        
        import sqlite3                                             #import sqlite3
        fc=sqlite3.connect('MyCricket.db')
        cur=fc.cursor()
        sql="select name from teams"                                            #sql command
        teams=[]
        nms=cur.execute(sql)
        for row in nms:
           self.comboBox1.addItem(row[0])                                       #adding items in combobox1
           self.comboBox1.activated[str].connect(self.onClick)                  #when combobox1 item is clicked
           self.comboBox2.addItem("Match 1")                                    #adding items in combobox2

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Evaluate the Performance of your Fantasy Team"))
        self.label_3.setText(_translate("Form", "Players"))
        self.label_2.setText(_translate("Form", "Points"))
        self.b2.setText(_translate("Form", "Calculate Score"))

    def onClick(self,text):                                                   
        import sqlite3                                             #import sqlite3
        fc=sqlite3.connect('MyCricket.db')
        cur=fc.cursor()
        team1 = self.comboBox1.currentText()
        self.listView1.clear()                                                 #clear players table
        self.listView2.clear()                                                 #clear points table
        self.le1.clear()                                                       #clear total score
        sql = "select players from teams where name='" + team1 + "'"           #sql command
        plyr= cur.execute(sql)
        row = plyr.fetchone()
        selected = row[0].split(',')
        self.listView1.addItems(selected)                                      #adding items to list1

    def calculate(self):
                                           
        teamtotal=0

        for i in range(self.listView1.count()-1):
        
            ptotal, batsc, bowlsc, fieldsc = 0, 0, 0, 0                         #initializing points to 0
            
            nm=self.listView1.item(i).text()                                    #nm is initialised with player name according to the range
            
            sql="select * from match where player='"+nm+"'"                     #sql command
            mtch=cur.execute(sql)
            row=mtch.fetchone()
            
            batsc+=row[1]/2                                                     #calculate batsman score
            if row[1]>=50 and row[1]<100:
                batsc+=5
            if row[1]>=100:
                batsc+=10
           
            if row[1]>0:                                                       #calculate batsman strike rate
                sr=row[1]/row[2]                                                
                if sr>=80 and sr<=100:
                    batsc+=2
                if sr>100:
                    batsc+=4
           
            batsc+=row[3]
           
            batsc+=2*row[4]
            
            bowlsc+=10*row[8]                                                   #calculate bowlers score
            if row[8]>=3 and row[8]<5:
                bowlsc+=5
            if row[8]>=5:
                bowlsc+=10
           
            if row[7]>0:                                                        #calculate economic rate 
                ec=row[7]/(row[5]/6)                                            
                if ec>=3.5 and ec<=4.5:
                    bowlsc+=4
                if ec>=2 and ec<3.5:
                    bowlsc+=7
                if ec<2:
                    bowlsc+=10
           
            fieldsc=(row[9]+row[10]+row[11])*10                                 #calculate fielders score
           
            ptotal=batsc+bowlsc+fieldsc                                         #total points of each player
            teamtotal+=ptotal                                                   #team's total score
            
            self.listView2.addItem(str(ptotal))                                 #displaying each player's points in list1
        
        self.le1.setText(str(teamtotal))                                        #displaying team's total score

if __name__ == "__main__":
    import sys
    import sqlite3                                             #import sqlite3
    fc=sqlite3.connect('MyCricket.db')
    cur=fc.cursor()                                            #sqlite3 connection to database
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
