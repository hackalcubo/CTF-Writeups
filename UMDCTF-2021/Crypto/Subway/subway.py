s  = '0123456789abcdefghijklmnopqrstuvwxyz {-_}'
s2 = 'abcdefghij***0123456789klmnopqrstuvw {-_}'
flag = 'W74 5o06 8v XP32W5-{qdw_0_vepsog_vx1vwewxwedq_w7ev_wepg}'
flag_lower = flag.lower()
res = ''
for c in flag_lower:
	res += s2[s.find(c)]
print(res)