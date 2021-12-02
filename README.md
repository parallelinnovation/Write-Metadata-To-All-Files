# Write-Metadata-To-All-Files
Prepends YAML metadata to the beginning of each markdown file in a folder

This is for if you wanted to add the same thing to the start of every text file in a specified folder. 
I used this for my Obsidian vault, where I wanted to add specific metadata to every daily note file in my daily notes folder that specified that it was type "daily note". 

What I added was this, but you can change that in the "Metadata" string variable. 

\-\-\-
Type:
\- Daily note
\-\-\-

DO NOT run this script directly on your only copy of your files, just in case it runs into an error I haven't seen. Insetead, copy the folder somewhere and run it on the copied folder, then move it back once it's finished. 

