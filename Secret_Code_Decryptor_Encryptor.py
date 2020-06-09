user_input = input('Type: ')
user_input = user_input.upper()

secret_Code = ''
for each in user_input:
    secret_Code += str(ord(each))
print('Secret code: ',secret_Code)

user_input = ''
for code in range(0,len(secret_Code)-1, 2):
    char_code = secret_Code[code] + secret_Code[code+1]
    user_input += chr(int(char_code))
print('Original message: ',user_input)