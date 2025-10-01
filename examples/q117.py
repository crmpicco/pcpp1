class File:
    def __init__(self, fname):
        if fname.endswith('.docx'):
            self.language = 'Microsoft Word'
        elif fname.endswith('.pdf'):
            self.language = 'PDF Document'
        else:
            self.info = None

files = [
File('script.docx'),
File('win.py'),
File('data.pdf'),
File('login.docx'),
]
for file in files:
    if hasattr(file, 'language'):
        print(file.language)
