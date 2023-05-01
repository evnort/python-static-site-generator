from typing import List
from pathlib import Path
import shutil


class Parser:

    extensions : List[str] = []

    def __init__(self):
        self.extensions = Parser.extensions

    def valid_extension(self, extension):
        if extension.type() in self.extensions:
            return True
        else:
            return False
    
    def parse(self, path:Path, source:Path, dest:Path):
        raise NotImplementedError
    
    def read(self, path:Path):
        with open(path, mode='rt', encoding='utf-8') as file:
            return file.read()
    
    def write(self, path, dest, content, ext=".html"):
        full_path = dest / path.with_suffix(ext).name
        with open(full_path, mode='wt', encoding='utf-8') as file:
            file.write(content)
    
    def copy(self, path, source, dest):
        shutil.copy2(src=path, dst=(dest / path.relative_to(source)))
    

class ResourceParser(Parser):
    extensions = [".jpg", ".png", ".gif", ".css", ".html"]


    def parse(self, path:Path, source:Path, dest:Path):
        Parser.copy(self, path, source, dest)