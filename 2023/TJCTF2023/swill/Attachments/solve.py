def check_pos(v, tmp):
	value = tmp[v[0]]
	for i in range(len(tmp)):
		if tmp[i] == value and i not in v:
			return False 
	return True

def check_range(tmp, d):
	for v in d:
		if len(d[v]) != 1:
			if not check_pos(d[v], tmp):
				return False
	return True

def print_res(enc, partial_key):
	res = ""
	xx = []
	i = 0
	for x in enc:
		if x in partial_key:
			res += partial_key[x]
		else:
			res += "-"
			xx.append(i)
		i += 1
	print(res)
	if xx:
		print("\nPOSITION OF MISSING CHAR")
		print(xx)

doc = "{'the_quick_brown_fox_jumps_over_the_lazy_dog': 123456789.0, 'items':[]}"
to_be_replaced = doc.encode() + b"\n"
enc = open('print_flag.py.enc.true', 'rb').read().replace(to_be_replaced, b"")
# print(f"{enc = }")

d = {}
for i in range(len(doc)):
	if doc[i] not in d:
		d[doc[i]] = [i]
	else:
		d[doc[i]].append(i)
# print(d)

pattern = []
for i in range(len(enc) - 78):
	tmp = [x for x in enc[i:i+len(doc) + 6]]
	if tmp[0] == tmp[75] == tmp[1] == tmp[76] == tmp[2] == tmp[77]:
		if check_range(tmp[3:75], d):
			pattern = tmp
			print(f"Found pattern at index {i}: " + "".join(chr(x) for x in tmp) + "\n\n")

partial_key = {}
partial_key[pattern[0]] = '"'

for i in range(len(doc)):
	if doc[i] not in partial_key:
		partial_key[pattern[3:75][i]] = doc[i]

print("*---------------------*")
print(" PARTIAL DECODED TEXT")
print("*---------------------*")
print_res(enc, partial_key)

partial_key[enc[0]] = "#"
partial_key[enc[1]] = "!"
partial_key[enc[3]] = "/"
partial_key[enc[23]] = "\n"
partial_key[enc[50]] = "="
partial_key[enc[107]] = "("
partial_key[enc[109]] = ")"
partial_key[enc[250]] = "N"

print("\n*---------------------*")
print(" PARTIAL DECODED TEXT")
print("*---------------------*")
print_res(enc, partial_key)

def reverse(s):
    return "".join(reversed(s))

rev = doc.upper()[2:45]
check_doc = reverse(rev)
print(f"\n\nREVERSED STRING: {check_doc}")

j = 0
for i in range(165, 208):
	partial_key[enc[i]] = check_doc[j]
	j += 1

print("\n*---------------------*")
print("     DECODED TEXT")
print("*---------------------*")
print_res(enc, partial_key)
