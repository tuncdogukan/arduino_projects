# -*- coding: utf-8 -*-
"""
Created on Sat May  9 01:29:31 2020

@author: tuncd
"""


flwer_filename = 'C:/Users/tuncd/Google Drive/Training/Instagram_Followers_02.txt'
flwin_filename = 'C:/Users/tuncd/Google Drive/Training/Instagram_Followers_01.txt'

betrayer_list = []
follower_list = []

with open(flwer_filename,encoding="utf8") as f:
    content = f.readlines()

    k = 0
    while k < len(content):
        if "profile" in content[k]:
            nameLong = content[k]
            name = nameLong[0:nameLong.index("'s")]
            #print(str(len(follower_list)+1) + ' - ' + name)
            follower_list.append(name)
            
        k=k+1
    
        


content.clear()

        
with open(flwin_filename,encoding="utf8") as f:
    content = f.readlines()
    j = 0
    while j < len(content):        
        if "profile" in content[j]:
            nameLong = content[j]
            name = nameLong[0:nameLong.index("'s")]
            #print(str(len(follower_list)+1) + ' - ' + name)
            if name not in follower_list:
                betrayer_list.append(name)
            
        j=j+1
        
        
for a in betrayer_list:
    print(a)

print("Total betrayers:", len(betrayer_list))
    
        

