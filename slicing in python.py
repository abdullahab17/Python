str = "My name is Hernandez I live in Spain and username is @hernandez6 "
position = str.find("@")
print(position)

#will find the next space after @ in string
space =str.find(" ",position)
print(space)

username = str[position + 1: space]
print(username)

x = 'From marquard@uct.ac.za'
print(x[14:17])

text = "X-DSPAM-Confidence:    0.8475"
number=text.find(":")
print(number)

next_num = text.find("0")
print(next_num)

val =text[23:]
print(val)