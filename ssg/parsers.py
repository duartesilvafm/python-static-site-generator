from typing import List
from pathlib import Path
import shutil


class Parser():

    def __init__(self, extensions: List[str] = []):
        self.extensions = extensions

    
    def valid_extensions(self, extension):
        return extension in self.extensions

    
    def parse(self, path: Path, source: Path, dest: Path):
        raise NotImplementedError


    def read(self, path):
        with open(path) as file:
            return file.read()


    def write(self, path, dest, content, ext = '.html'):

        full_path = self.dest / path.with_suffix(ext).name

        with open(full_path) as file:
            file.write(content)

    
    def copy(self, path, source, dest):

        tocopy = dest / path.relative_to(source)

        shutil.copy2(src = path, dst = tocopy)


class ResourceParser(Parser):


    extensions = ['.jpg', '.png', '.gif', '.css', '.html']


    def parse(self, path: Path, source: Path, dest: Path):
        super().copy(path, source, dest)

