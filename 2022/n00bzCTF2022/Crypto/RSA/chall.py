# ct = 68915718021581205938132340378
# n = 22964326243465188806208175092817347325223751455203934839482603060029805229708465878030254819573089332477084079330445929855173787412006349904864930449245982063200060526847746608051441362052994064461426109292644943462306467765210530381760387813568149905672759271878822092979239650360475796179311415340966347044401497301347973838444826544061998479163636946750265778097717211762208385963205388216125639236403616607313423716206061201112615302831337395011064188536794425701313580122604533837935452384701344503773605128479669035610395170026350607423780797383865621285538151344219282466601404674101508588637419153433890102137
# s = 6747770137526404810839680591618349902868945426501581276399132116507818856417271976886226143238796548185022079396435297411063351895882402872038955136430497260880818613647851713479263986391308789043197324119239260033630040630976512064481721240642729114116561261667588426398515959668695454587899042998666589705506998832917739337175589667828567571421541128057015371328723095841794613223799998429126797512729366352049800447550388154359724453576012916007310993864290045596969157854816882402679820492333445924724199994952395214639223249892224753494733720946542351810699104265693993026233289328344375145590992008664182919067
from Crypto.Util.number import *
p = getPrime(1024)
q = getPrime(1024)
n = p*q
e = 65537
flag = b'REDACTED'
flag_int = bytes_to_long(flag)	
phi = (p-1)*(q-1)
ct = pow(flag_int,e,n)
#assert ct = 0xdeadbeefdeadbeefdeadbeef + 1337 + 1337 + 1337
d = inverse(e,phi)
s = pow(flag_int,d,n)
print(f's = {s}')
print(f'n = {n}')
print(f'ct = {ct}')