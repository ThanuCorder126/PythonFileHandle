import os
from datetime import datetime
#file from path
fileOnly=lambda path:os.path.basename(path)
# extension
extension=lambda path:os.path.splitext(fileOnly(path))[1]
#filename
fileName=lambda path:os.path.splitext(fileOnly(path))[0]

#parent
where=lambda file:os.path.dirname(file)
#parnetname
parent=lambda file:os.path.basename(os.path.dirname(file))
#all parents
def whereAll(file):
    paths=[]
    while file!="/" or file!="":
        file=os.path.dirname(file)
        paths.append(file)
    return paths
#has neibours
def has_neibours(file):
    parent_dir=where(file)
    files=list(filter(lambda f:os.path.isfile(os.path.join(parent_dir,f)),os.listdir(parent_dir)))
    files.remove(fileOnly(file))
    return len(files)>1
# neibours
def neibours(file):
    parent_dir=where(file)
    files=list(filter(lambda f:os.path.isfile(os.path.join(parent_dir,f)),os.listdir(parent_dir)))
    files.remove(fileOnly(file))
    return files
#has sibilings
def has_sibilings(file):
    parent_dir=where(file)
    files=list(filter(lambda f:os.path.isfile(os.path.join(parent_dir,f)) and extension(f)==extension(file),os.listdir(parent_dir)))
    files.remove(fileOnly(file))
    return len(files)>1
# sibilings
def sibilings(file):
    parent_dir=where(file)
    files=list(filter(lambda f:os.path.isfile(os.path.join(parent_dir,f)) and extension(f)==extension(file),os.listdir(parent_dir)))
    files.remove(fileOnly(file))
    return files
#file size
def fileSize(file,unit='b'):
    size=os.path.getsize(file)
    filesize={
        'b':size,
        'kb':size/1024,
        'mb':size/(1024*1024),
        'gb':size/(1024*1024*1024)
    }
    return round(filesize.get(unit,0.0),5)
# created At time
def createAt(file,format=None):
    created_at=os.path.getctime(file)
    created_at_time=datetime.fromtimestamp(created_at)
    if not format:
        return created_at_time
    return created_at_time.strftime(format)

# Modify time
def modifyAt(file,format=None):
    modify_at=os.path.getmtime(file)
    modify_at_time=datetime.fromtimestamp(modify_at)
    if not format:
        return modify_at_time
    return modify_at_time.strftime(format)

# Access time
def accessAt(file,format=None):
    access_at=os.path.getatime(file)
    access_at_time=datetime.fromtimestamp(access_at)
    if not format:
        return access_at_time
    return access_at_time.strftime(format)
#==================================File Class For Custom==================================
class File:
    def __init__(self,path):
        self.path=path
        if not os.path.exists(path):
            raise FileNotFoundError(f'{path} is not found')
        if not os.path.isfile(path):
            raise Exception("{path} is Not File")
    def exe(self):
        return os.path.splitext(os.path.basename(self.path))[1]
    def name(self):
        return os.path.splitext(os.path.basename(self.path))[0]
    def fileName(self):
        return os.path.basename(self.path)
    def where(self):
         return os.path.dirname(self.path)
    def size(self,unit='b'):
         size=os.path.getsize(self.path)
         filesize={
        'b':size,
        'kb':size/1024,
        'mb':size/(1024*1024),
        'gb':size/(1024*1024*1024)
     }
         return round(filesize.get(unit,0.0),5)
    def created_at(self,format=None):
        created_at=os.path.getctime(self.path)
        created_at_time=datetime.fromtimestamp(created_at)
        if not format:
            return created_at_time
        return created_at_time.strftime(format)
    def modified_at(self,format=None):
        modify_at=os.path.getmtime(self.path)
        modify_at_time=datetime.fromtimestamp(modify_at)
        if not format:
            return modify_at_time
        return modify_at_time.strftime(format)
    def accessed_at(self,format=None):
        access_at=os.path.getctime(self.path)
        access_at_time=datetime.fromtimestamp(access_at)
        if not format:
            return access_at_time
        return access_at_time.strftime(format)
    def parent(self):
        return os.path.basename(os.path.dirname(self.path))
    def has_neibours(self):
        parent_dir=self.where()
        files=list(filter(lambda f:os.path.isfile(os.path.join(parent_dir,f)),os.listdir(parent_dir)))
        files.remove(self.fileName())
        return len(files)>1
    # neibours
    def neibours(self):
        parent_dir=self.where()
        files=list(filter(lambda f:os.path.isfile(os.path.join(parent_dir,f)),os.listdir(parent_dir)))
        files.remove(self.fileName())
        return files
    #has sibilings
    def has_sibilings(self):
        parent_dir=where()
        files=list(filter(lambda f:os.path.isfile(os.path.join(parent_dir,f)) and extension(f)==self.exe(),os.listdir(parent_dir)))
        files.remove(self.fileName())
        return len(files)>1
    # sibilings
    def sibilings(self):
        parent_dir=self.where()
        files=list(filter(lambda f:os.path.isfile(os.path.join(parent_dir,f)) and extension(f)==self.exe(),os.listdir(parent_dir)))
        files.remove(self.fileName())
        return files
    def whereAll(self):
        file=self.path
        paths=[]
        while file!="/" or file!="":
            file=os.path.dirname(file)
            paths.append(file)
        return paths
    def details(self):
        return {
            'exe':self.exe(),
            'name':self.name(),
            'size':self.size('mb'),
            'createdAt':self.created_at(),
            'modifiedAt':self.modified_at(),
            "accecedAt":self.accessed_at(),
            "dir":self.where()
        }        
print(createAt("/workspaces/codespaces-jupyter/my.txt",format="%d-%M"))