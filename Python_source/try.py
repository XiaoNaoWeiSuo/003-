self.setGeometry(desktopRect) #将窗口设置成全屏
self.setCursor(Qt.CrossCursor)  #设置鼠标形状为十字形
self.desktop = QApplication.desktop()
        #获取显示器分辨率大小
        self.screenRect = self.desktop.screenGeometry()
        self.height = self.screenRect.height()
        self.width = self.screenRect.width()

