import os 
def clear():
    os.system('clear')
clear()
# ❤️‍🔥 FV and PV solver 
# use only number 

# How to use?  //  install  Pydroid3 from play store  copy and run code. 

# Use only number 
def main():
    
    list = print("         ➡️           fv      or      pv")
    print("                                                ")
    lisn = print("         ➡️             1     or️    2")
    print("\n            Only number is allowed ! ")
    print("                ")
    menu = input("Enter your choice : ")
    print("        ")
    #pv = 100
    #u = 10
    #time = 5
    if menu == 'fv' or menu == '1' or menu == 'f' or menu == 'fv ' or menu == 'FV' or menu == 'Fv':
        print("                           [ FV ]")
        print("                    ")
        
        pv = float(input("          বর্তমান মূল্য: "))
        u = float(input("          সুদের হার: "))
        time = float(input("          বাৎসরিক মেয়াদ: "))
    
        
        print("\n        এখানে,\n")
        
        
        k = (u / 100)
        l = (k + 1)
        i = l ** time
        fv = pv * i
        
        print("            বর্তমান মূল্য (PV) = " + str(pv))
        print("            সুদের হার       = " + str(u) + "  বা  " + str(k))
        print("            বাৎসরিক মেয়াদ   = " + str(time))
        print("        ")
        print("            আমরা জানি, FV = PV × (1+i)^n\n")
        print("                         = " + str(pv) + " × (1 + " + str(k) + ")^ " + str(time))
        print("                         = " + str(pv) + " × (" + str(l) + ")^ " + str(time))
        print("                         = " + str(pv) + " × " + str(i))
        print("                  •°• FV = " + str(fv))
        print("        ")
        print("             ANS :    FV = " + str(fv))
        
        print("        ")
        print("     🍁   THANK YOU,")
        print("     🍁   BUILD BY <JIHAD> ~ ©")
        print("        @ TAWFIQUR RAHMAN  ¿")
    #s
    #fv = 100
    #u = 10
    #time = 5
    elif menu == 'pv' or menu == '2' or menu == 'p' or menu == 'pv ' or menu == 'PV' or menu == 'Pv' or menu == 'p ' or menu == 'Pv ':
        print("                            [ PV ]")
        print("            ")
        fv = float(input("          ভবিষ্যত মূল্য: "))
        u = float(input("          সুদের হার: "))
        time = float(input("          বাৎসরিক মেয়াদ: "))
        print("        ")
        print("         এখানে,\n")
        
        
        k = (u / 100)
        l = (k + 1)
        i = (l ** time)
        pv = (fv / i)
        print("            ")
        
        print("            ভবিষ্যত মূল্য (FV)    = " + str(fv))
        print("            সুদের হার           = " + str(u) + "  বা  " + str(k))
        print("            বাৎসরিক মেয়াদ       = " + str(time))
        print("            ")
        print("                              FV")
        print("             আমরা জানি, PV = ———————")
        print("                            (1+i)^n")
        print("        ")
        print("                               " + str(  fv))
        print("                          = ————————————")
        print("                             (1+" + str(k) + ")^" + str(time))
        print("    ")
        
        print("                              " + str(fv))
        print("                          = ——————————")
        print("                            (" + str(l) + (")^") + str(time))
        print("                        ")
        print("                                   " + str(fv))
        print("                          = ——————————————————")
        print("                            " + str(i))
        print("                    ")
        print("                  •°• PV  = " + str(pv))
        print("        ")
        print("                ")
        print("             ANS :    PV = " + str(pv))
        print("        ")
        print("     🍁 THANK YOU,")
        print("     🍁 BUILD BY <JIHAD> ~ ©")
        print("        @ TAWFIQUR RAHMAN  ¿")
        o = input("\n        Enter 1 for again.Or 2 for exit.")
        while True:
             
             
             if o == "1":
                 main()
             elif o == "2":
                 print("        Thanks. ")
                 exit()
             else:
              print("        \n    ⚠️   ENTER 1 OR 2 ") 
main()
