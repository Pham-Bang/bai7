def file_append_and_read(fname):
    with open(fname, "a") as myfile:
        myfile.write("21 vothisau\n")
        myfile.write("14122005\n")
    with open(fname, "r") as txt:
        print(txt.read())
file_append_and_read('hieu.txt')
print("sinh vien: Pham Quang Bang")
print("Mssv: 2357520207100047")