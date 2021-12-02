from os import listdir
from os.path import isfile, join



DailyNotesFolder = ""


Metadata = "---\nType:\n- Daily note\n---\n"
print(Metadata)


def NotePath():
	onlyfiles = [f for f in listdir(DailyNotesFolder) if isfile(join(DailyNotesFolder, f))]
	return(onlyfiles)


def AppendToNote(desiredBlock):
    Notefile = open(desiredBlock, encoding="utf8", errors='ignore')
    NoteContent = Notefile.read()
    Notefile.seek(0)
    Notefile = open(desiredBlock, "w", encoding="utf8", errors='ignore')
    Notefile.write(Metadata + NoteContent)
    print("Sucessfully wrote to desired note")
    Notefile.seek(0)
    Notefile.close()

notepath = NotePath()


for i in notepath:
	DailyNotesPath = str(DailyNotesFolder + "/" + i)
	with open(DailyNotesPath,encoding="utf8", errors='ignore') as Notefile:
		NoteContent = Notefile.read()
	Notefile.close()
	if Metadata in NoteContent:
		print("Metadata already exists")
	else:
		AppendToNote(DailyNotesPath)

if __name__ == "__main__":
	NotePath()