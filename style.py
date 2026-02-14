
STYLE_MAIN = """
QMainWindow { background-color: #1e1e1e; }
QWidget { background-color: #1e1e1e; color: #ffffff; font-family: 'Segoe UI', sans-serif; }

QListWidget {
    background-color: #252525;
    border: 1px solid #333;
    border-radius: 5px;
    color: #eee;
    outline: none;
}
QListWidget::item { padding: 10px; border-bottom: 1px solid #2d2d2d; }
QListWidget::item:selected { background-color: #383838; color: white; border-left: 3px solid #007acc; }
QListWidget::indicator { width: 18px; height: 18px; }

QLineEdit {
    background-color: #333;
    border: 1px solid #555;
    border-radius: 4px;
    padding: 8px;
    color: white;
}
QLineEdit:focus { border: 1px solid #007acc; }

QPushButton {
    background-color: #444;
    color: white;
    border-radius: 4px;
    padding: 8px 15px;
    font-weight: bold;
}
QPushButton:hover { background-color: #555; }

QPushButton#CreateBtn { background-color: #28a745; }
QPushButton#CreateBtn:hover { background-color: #218838; }

QPushButton#DeleteBtn { background-color: #d32f2f; }
QPushButton#DeleteBtn:hover { background-color: #b71c1c; }

QPushButton#SaveBtn { background-color: #007acc; }
QPushButton#SaveBtn:hover { background-color: #005f9e; }

QPushButton#ApplyBtn { background-color: #6f42c1; font-size: 14px; }
QPushButton#ApplyBtn:hover { background-color: #5a32a3; }
"""