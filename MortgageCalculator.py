"""
Programmar: Laxmi Gurung
Project: Mortgage Calculator using PyQt5
Date: 05/28/2021
"""
#Import applications and the required widgets from PyQt5.QtWidgets
from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from decimal import Decimal

__version__= '0.1'
__author__='Laxmi Gurung'

import sys

#Creating a subclass of QMainWindow to setup the Calculator's GUI
class mortgageCal(QWidget):
    '''Mortgage Calculator's View'''
    def __init__(self, parent=None):
        """View initializer"""
        super().__init__(parent)
        #Setting some windows properties
        self.setWindowTitle('Nepal Mortgage Calculator')
        self.setGeometry(100,100,800,600)
        self._createMenu()
        self.show()

    def _createMenu(self):
        self.setStyleSheet("background-color:lightgray;")
        #setup the title
        title = QLabel("NEPAL MORTAGE CALCULATOR",self)
        font=QFont("Arial",25)
        title.setStyleSheet("QLabel" 
                            "{" 
                    "background: gray;" 
        "border: 2px solid black;"
        "}")
        title.setFont(font)
        title.setAlignment(Qt.AlignLeft)


        #setup purchase price
        puprice = QLabel("Purchase Price",self)
        puprice.setGeometry(40,100,120,30)
        font=QFont("Arial",10)
        font.setBold(True)
        puprice.setFont(font)
        puprice.setAlignment(Qt.AlignLeft)

        self.amount = QLineEdit(self)
        #acceptInt = QIntValidator()
        self.amount.setValidator(QDoubleValidator(0.999,99.999,3))
        self.amount.setStyleSheet("background-color:white;")
        self.amount.setGeometry(150,100,100,20)
        self.amount.setAlignment(Qt.AlignRight)
        self.amount.setFont(QFont('Arial',10))

        #set up down payment
        downprice = QLabel("Down Payment",self)
        downprice.setGeometry(40,150,120,30)
        font=QFont("Arial",10)
        font.setBold(True)
        downprice.setFont(font)
        downprice.setAlignment(Qt.AlignLeft)

        self.damount = QLineEdit(self)
        #acceptInt = QIntValidator()
        self.damount.setValidator(QDoubleValidator(0.999,99.999,3))
        self.damount.setStyleSheet("background-color:white;")
        self.damount.setGeometry(150,150,100,20)
        self.damount.setAlignment(Qt.AlignRight)
        self.damount.setFont(QFont('Arial',10))

        #set up interest rate
        rateP = QLabel("Interest Rate %",self)
        rateP.setGeometry(260,100,120,30)
        font=QFont("Arial",10)
        font.setBold(True)
        rateP.setFont(font)
        rateP.setAlignment(Qt.AlignLeft)

        self.rate = QLineEdit(self)
        #acceptInt = QIntValidator()
        self.rate.setValidator(QDoubleValidator(0.999,99.999,3))
        self.rate.setStyleSheet("background-color:white;")
        self.rate.setGeometry(400,100,100,20)
        self.rate.setAlignment(Qt.AlignRight)
        self.rate.setFont(QFont('Arial',10))
        """
        self.rate.setGeometry(400,100,100,20)
        self.rate.addItems(["3", "4", "5"])
        self.rate.activated.connect(self.monthlyPayment)
        """

        #set up loan term
        loanTerm = QLabel("Loan Term(in yrs)",self)
        loanTerm.setGeometry(260,150,120,20)
        font=QFont("Arial",10)
        font.setBold(True)
        loanTerm.setFont(font)
        loanTerm.setAlignment(Qt.AlignLeft)

        self.loanTime = QLineEdit(self)
        #acceptInt = QIntValidator()
        self.loanTime.setValidator(QDoubleValidator(0.999,99.999,3))
        self.loanTime.setStyleSheet("background-color:white;")
        self.loanTime.setGeometry(400,150,100,20)
        self.loanTime.setAlignment(Qt.AlignRight)
        self.loanTime.setFont(QFont('Arial',10))

        """
        self.loanT =QComboBox(self)
        self.loanT.setGeometry(400,150,100,20)
        self.loanT.addItems(["15", "20", "25","30"])
        self.loanT.activated.connect(self.monthlyPayment)
        """
        #set up Monthly Payment
        totalPay = QLabel("Total Payment",self)
        totalPay.setGeometry(40,250,180,30)
        font=QFont("Arial",15)
        font.setBold(True)
        totalPay.setFont(font)
        totalPay.setAlignment(Qt.AlignLeft)

        self.toPay = QLineEdit(self)
        #acceptInt = QIntValidator()
        self.toPay.setValidator(QDoubleValidator(0.999,99.999,3))
        self.toPay.setStyleSheet("background-color:white;")
        self.toPay.setGeometry(220,250,200,30)
        self.toPay.setAlignment(Qt.AlignRight)
        self.toPay.setFont(QFont('Arial',15))

        #set up total Payment
        monthlyPay = QLabel("Monthly Payment",self)
        monthlyPay.setGeometry(40,200,180,30)
        font=QFont("Arial",15)
        font.setBold(True)
        monthlyPay.setFont(font)
        monthlyPay.setAlignment(Qt.AlignLeft)

        self.monPay = QLineEdit(self)
        #acceptInt = QIntValidator()
        self.monPay.setValidator(QDoubleValidator(0.99,99.99,2))
        self.monPay.setStyleSheet("background-color:white;")
        self.monPay.setGeometry(220,200,200,30)
        self.monPay.setAlignment(Qt.AlignRight)
        self.monPay.setFont(QFont('Arial',15))

        #choose your state
        state = QLabel("Select Your State",self)
        state.setGeometry(40,300,180,30)
        font=QFont("Arial",10)
        font.setBold(True)
        state.setFont(font)
        state.setAlignment(Qt.AlignLeft)

        self.stateSelect =QComboBox(self)
        self.stateSelect.setGeometry(40,320,140,30)
        self.stateSelect.setStyleSheet("background-color:white;")
        self.stateSelect.addItems(["New York", "Texas", "Boston","California"])
        self.stateSelect.activated.connect(self.monthlyPayment)

        #set up calculate button
        calculate = QPushButton("Calculate", self)
        font=QFont("Arial",10)
        font.setBold(True)
        calculate.setFont(font)
        calculate.setStyleSheet("background-color:gray;")
        calculate.setGeometry(270,320,100,40)
        calculate.clicked.connect(self.monthlyPayment)

    
    def monthlyPayment(self):
        #Here all the user  inputs from the window will be calculated
        annualInterestRate = self.rate.text()
        termLoan = self.loanTime.text()
        purchasePrice = self.amount.text()
        downPayment = self.damount.text()

        annualInterestRate = float(annualInterestRate)
        termLoan = float(termLoan)
        purchasePrice = float(purchasePrice)
        downPayment = float(downPayment)

        principal = purchasePrice -downPayment
        numberPayments = termLoan * 12

        monthlyInterestRate = (annualInterestRate/12)/100

        monthlyPayment = principal * monthlyInterestRate *(((1+monthlyInterestRate)*numberPayments)/(((1+monthlyInterestRate)*numberPayments)-1))


        monthlyPayment = "{:.2f}".format(monthlyPayment)
   
        self.monPay.setText(str(monthlyPayment))

        totalPayment = float(monthlyPayment)*12*termLoan
        totalPayment ="{:.2f}".format(totalPayment)

        self.toPay.setText(str(totalPayment))

    
#Create an instance of QApplication
App = QApplication(sys.argv)
  
# create the instance of our Window
window = mortgageCal()
  
# Execute the calculator's main loop
sys.exit(App.exec())


