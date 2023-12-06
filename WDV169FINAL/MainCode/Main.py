# Imports
import sys
from WDV169FINAL.Interface.GUI import *

if __name__ == '__main__':
    app = QApplication(sys.argv)
    gui = PriorityQueueGUI()
    gui.show()
    sys.exit(app.exec_())

