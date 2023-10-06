import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QComboBox, QLabel, QFileDialog
from PyQt5.QtCore import Qt

# Importing your functions
from ImgUpscaler import upscale_image
from Pixel_to_Img import pixels_to_image
from Img_to_Pixel import save_pixel_colors_to_file

class App(QMainWindow):

    def __init__(self):
        super().__init__()
        self.title = 'Image Processing Tool'
        self.left = 50
        self.top = 50
        self.width = 500
        self.height = 350
        self.initUI()

    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        # Create dropdown menu to select operation
        self.operations = ["Upscale Image", "Pixel to Image", "Image to Pixel"]
        self.comboBox = QComboBox(self)
        self.comboBox.addItems(self.operations)
        self.comboBox.move(30, 20)
        self.comboBox.resize(150, self.comboBox.height())

        # Button to execute operation
        self.execute_btn = QPushButton('Execute', self)
        self.execute_btn.move(250, 20)
        self.execute_btn.clicked.connect(self.execute_operation)

        # Result label
        self.result_label = QLabel(self)
        self.result_label.setAlignment(Qt.AlignCenter)
        self.result_label.move(50, 70)
        self.result_label.resize(300, 40)

        self.show()

    def execute_operation(self):
        operation = self.comboBox.currentText()
        
        # Open File Dialog
        dialog = QFileDialog(self)
        dialog.setWindowTitle('Open Image File')
        dialog.setNameFilter('Image Files (*.png;*.jpg;*.jpeg);;Text Files (*.txt);;All Files (*)')
        dialog.setGeometry(70, 70, 800, 500)  # Adjust the position and size of the dialog

        if dialog.exec_():  
            inputFilePath = dialog.selectedFiles()[0]

            if inputFilePath:
                saveDialog = QFileDialog(self)
                saveDialog.setWindowTitle('Save Output As')

                if operation == "Upscale Image":
                    default_output = "output_scaled_image.jpg"
                elif operation == "Pixel to Image":
                    default_output = "output_from_pixel.jpg"
                elif operation == "Image to Pixel":
                    default_output = "output_imgPixel.txt"

                savePath, _ = saveDialog.getSaveFileName(self, "Save Output As", default_output)

                if savePath:
                    if operation == "Upscale Image":
                        upscale_image(inputFilePath, savePath)
                    elif operation == "Pixel to Image":
                        pixels_to_image(inputFilePath, savePath)
                    elif operation == "Image to Pixel":
                        save_pixel_colors_to_file(inputFilePath, savePath)

                    self.result_label.setText(f"Operation executed! Output saved to: {savePath}")
                else:
                    self.result_label.setText("Operation canceled.")
            else:
                self.result_label.setText("No input file selected.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
