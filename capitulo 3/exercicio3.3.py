#Complete a tabela a seguir utilizando a = True, b = False e c = True.

a,b,c = True,False,True

a and a   #True and True = True    
a or c    #True or True = True
b and b   #False and False = False    
b or c    #False or True = True
not c     #False. c = True,not c = False    
c or a    #True or True = True
not b     #True. b = False, not b = True    
c or b    #True or False = True
not a     #False. a = True, not a = False    
c or c    #True or True = True
a and b   #True and False = False    
b or b    #False or False = False
b and c   #False and True = False