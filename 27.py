def is_number(s):
try:
float(s)
returntrue
exceptvalueerror:
pass
try:
import uniodedata
unicodedata.numberic(s)
return true
except(typeerror,baluerror);
pass
return false
