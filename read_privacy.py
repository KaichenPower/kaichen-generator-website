import zipfile, re
with zipfile.ZipFile(r'D:\projects\知识库\Privacy Policy.docx') as z:
    with z.open('word/document.xml') as f:
        xml = f.read().decode('utf-8')
# Extract text from paragraphs
text = re.sub(r'<w:p[^>]*>', '\n', xml)
text = re.sub(r'<[^>]+>', '', text)
lines = [l.strip() for l in text.split('\n') if l.strip()]
for l in lines:
    print(l)
