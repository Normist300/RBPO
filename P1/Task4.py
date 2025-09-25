import xml.etree.ElementTree as ET
import os

class XML():
    def __init__(self, filename):
        self.filename = filename
    
    def create_xml_file(self):
        if not os.path.exists(self.filename):
            root = ET.Element("data")
            tree = ET.ElementTree(root)
            tree.write(self.filename)
        else:
            print(f"Файл {filename} уже существует.")

    # Записать в файл новые данные из консоли
    def write_data_to_xml(self):
        tree = ET.parse(self.filename)
        root = tree.getroot()
        
        key = input("Введите ключ: ")
        value = input("Введите значение: ")
        
        data_element = ET.SubElement(root, key)
        data_element.text = value
        
        tree.write(self.filename)

    # Прочитать файл в консоль
    def read_data_from_xml(self):
        tree = ET.parse(self.filename)
        root = tree.getroot()
        
        for elem in root:
            print(f"{elem.tag}: {elem.text}")

    # Удалить файл
    def delete_file(self):
        os.remove(self.filename)
        print(f"Файл {self.filename} удалён.")


xml = XML('P1/file.xml')
# xml.create_xml_file()
xml.write_data_to_xml()
xml.read_data_from_xml()
# xml.delete_file()
