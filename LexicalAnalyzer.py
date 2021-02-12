import re
func = ["main", "printf", "scanf", "clrscr", "getch"]
oper = ["+", "-", "*", "/", "%", "=", "==", "++", "--", "!=", "," ,  "{", "}"]
keyw = ["int", "float", "double", "char", "long"]
sym = int(0)
fc = int(0)
op = int(0)
kc = int(0)
co = int(0)
bi = int(0)
temp = ""
fhand = open("c-program.txt")
fh = open("output.txt", "a")
f1 = open("function.txt", "a")
f2 = open("keyword.txt", "a")
f3 = open("operator.txt", "a")
f4 = open("symbol.txt","a")
f5 = open("constant.txt","a")
for line in fhand:
    line = line.rstrip()
    li = line.split()
    for l in li:
        bi = 0
        for x in func:
            t = "^{}.".format(x)
            if  re.search(t, l):
                bi = 1
                fc = fc + 1
                temp = "fun#{} \n".format(fc)
                fh.write(temp)
                f1.write("{} \n".format(x))
                break
        if bi == 1:
            continue

        if l in keyw:
            kc = kc + 1
            temp = "key#{} \n".format(kc)
            fh.write(temp)
            f2.write("{} \n".format(l))
        elif l in oper:
            op = op + 1
            temp = "op#{} \n".format(op)
            fh.write(temp)
            f3.write("{} \n".format(l))
        elif l.isdigit():
            co = co + 1
            temp = "const#{} \n".format(co)
            fh.write(temp)
            f5.write("{} \n".format(l))
        else:
            ls = list(l)
            for y in l:
                if ord(y) >= 97 and ord(y) <= 122:
                    sym = sym + 1
                    temp = "sym#{} \n".format(sym)
                    fh.write(temp)
                    f4.write("{} \n".format(y))
 
fhand.close()
fh.close()
f1.close()
f2.close()
f3.close()
f4.close()
f5.close()  
