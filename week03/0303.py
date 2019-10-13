input_string=input('Введите элементы списка через запятую (точку с запятой или слэш) : ')
if ',' in input_string: string_sep=','
if ';' in input_string: string_sep=';'
if '/' in input_string: string_sep='/'
input_vals=input_string.split(string_sep)
input_vals=[int(i) for i in input_vals]
print(set(input_vals))