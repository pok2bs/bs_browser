from import_pyside6 import *

class password_widget(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowFlags(Qt.WindowStaysOnTopHint)
        self.password_layout = QVBoxLayout()
        self.profile_name = QLabel()
        self.profile_name.setAlignment(Qt.AlignCenter)
        self.profile_password_line = QLineEdit()
        self.profile_password_line.setPlaceholderText("비밀번호")
        self.profile_password_line.setEchoMode(QLineEdit.Password)
        self.password_error = QLabel()
        self.password_error.setStyleSheet("color:rad")
        self.accept_button = QPushButton("확인")
        self.password_layout.addWidget(self.profile_name)
        self.password_layout.addWidget(self.profile_password_line)
        self.password_layout.addWidget(self.password_error)
        self.password_layout.addWidget(self.accept_button)
        self.password_layout.setSpacing(10)
        self.password_layout.setContentsMargins(10,20,10,20)
        self.setLayout(self.password_layout)
        self.setWindowTitle("비밀번호")