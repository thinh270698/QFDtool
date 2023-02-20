from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPalette
from PyQt5.QtWidgets import QApplication, QPushButton,QFrame,QWidget,QVBoxLayout,QHBoxLayout,QFileDialog
from PyQt5.QtWidgets import *

class AppFrame(QFrame):
    def __init__(self) -> None:
        super().__init__()
        self.Layout= QVBoxLayout()
        self.initTop()
        self.initBody()
        self.initBottom()
        self.setMinimumSize(650,300)
        self.Layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.Layout)


    def initTop(self):
        topFrame = QFrame()
        topLayout = QHBoxLayout()
        mainBtn = QPushButton("ツール実施")
        viewRuleBtn = QPushButton("viewRule")
        mainBtn.setFixedWidth(100)
        viewRuleBtn.setFixedWidth(100)
        topLayout.addWidget(mainBtn)
        topLayout.addWidget(viewRuleBtn)

        topFrame.setLayout(topLayout)
        self.Layout.addWidget(topFrame)

    def initBody(self):
        self.bodyFrame = QFrame()
        self.bodyLayout = QGridLayout()
        inputLabel = QLabel("Select input link")

        self.InputLink = QLineEdit()
        selectInputBtn = QPushButton("Select")
        selectInputBtn.clicked.connect(self.getInput)

        outLabel = QLabel("Select input link")
        self.outLink = QLineEdit()
        selectOutBtn = QPushButton("Select")
        selectOutBtn.clicked.connect(self.getOutput)

        swItemLabel = QLabel("Select sw")
        sweepItem = QLineEdit()
        sweepItem.setText("1")
        swLabel = QLabel("NE:0/APO:1")
        offsetLabel = QLabel("Offset")
        offsetText = QLineEdit()

        self.bodyLayout.addWidget(inputLabel,0,0)
        self.bodyLayout.addWidget(self.InputLink,1,0)
        self.bodyLayout.addWidget(selectInputBtn,1,1)

        self.bodyLayout.addWidget(outLabel,2,0)
        self.bodyLayout.addWidget(self.outLink,3,0)
        self.bodyLayout.addWidget(selectOutBtn,3,1)

        self.bodyLayout.addWidget(swItemLabel,4,0)
        self.bodyLayout.addWidget(sweepItem,5,0)
        self.bodyLayout.addWidget(swLabel,5,1)
        self.bodyLayout.addWidget(offsetLabel,6,0)
        self.bodyLayout.addWidget(offsetText,7,0)
        
        self.bodyFrame.setLayout(self.bodyLayout)
        self.Layout.addWidget(self.bodyFrame)

    def initBottom(self):
        bottomFrame = QFrame()
        bottomLayout = QVBoxLayout()
        bottomBtn = QPushButton("Run")
        bottomBtn.setFixedWidth(100)
        bottomLayout.addWidget(bottomBtn)
        bottomFrame.setLayout(bottomLayout)
        bottomLayout.setAlignment(Qt.AlignCenter)
        self.Layout.addWidget(bottomFrame)

    def getInput(self):
        self.InputLink.setText(str(QFileDialog.getExistingDirectory(self, "Select Directory")))
    
    def getOutput(self):
        self.outLink.setText(str(QFileDialog.getExistingDirectory(self, "Select Directory")))

def main():
    app = QApplication([])
    app.setStyle('Fusion')
    palette = QPalette()
    palette.setColor(QPalette.ButtonText, Qt.red)
    app.setPalette(palette)
    window = AppFrame()
    window.show()
    app.exec()

if __name__ == '__main__':
    main()