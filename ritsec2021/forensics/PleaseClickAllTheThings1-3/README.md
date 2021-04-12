# PleaseClickAllTheThings
Its a series of challenges focused on the prevention from phishing and detecting malware in documents. We get a .msg file in a Outlook message format so we could either use Outlook to extract its contents or I used a tool online at https://www.encryptomatic.com/viewer/.
# Part 1
`Start with the HTML file and let’s move our way up, open and or inspect the HTML file provide in the message file. There is only one flag in this document.`

Looking at the source of the html we find a single script js tag, I run it simply modifiying from document.write to console.log and we get the plain text with the flag in a tag encoded in base64.

# Part 2
`GandCrab/Ursnif are dangerous types of campaigns and malware, macros are usually the entry point, see what you can find, there are two flags in this document. Flag1/2`

Opening this document with Libreoffice Writer prompts me about some macros stopped from running for security reasons. Looking the source up we find the flag in plain text.
![alt text](img)

# Part 3
`Stepping it up to IceID/Bokbot, this challenge is like the previous challenge but requires some ability to read and understand coding in addition to some additional decoding skills, there are two flags in this document. (Flag 1/2)`

This other file had the same procedure to find the flag only it was encoded in rot13.
