#23311085 Qichong Huang
# all comment out 'print' are used for testing
def distance_3d(x1,y1,z1,x2,y2,z2):                               #the formula of 3d distance
    return pow(pow((x2-x1),2)+pow((y2-y1),2)+pow((z2-z1),2),0.5)

def similarity(dict1,dict2):                                     #the formula of similarity
    numerator = 0
    denominator1 = 0
    denominator2 = 0
    for key1,key2 in zip(dict1,dict2):
        numerator = numerator + dict1[key1]*dict2[key2]
        denominator1 = denominator1 + pow(dict1[key1],2)
        denominator2 = denominator2 + pow(dict2[key2],2)
        
    denominator = pow(denominator1,0.5) * pow(denominator2,0.5)
    return numerator/denominator
   
def make_person_dict(listoflist,ai):
    dict_byid = {}                          #the dictionary key by id
    currentid = ''
    landmark_list = []                      # the value in the dictionary
    for lists in listoflist:
        if currentid == '':                     #initialize the currentid
            currentid = lists[ai]
            landmark_list.append(lists)         #append the list to the landmark_list
        elif currentid != lists[ai]:
            temp = landmark_list.copy()                #let a variable = landmark_list
            dict_byid[currentid] = temp
            landmark_list.clear()
            currentid = lists[ai]
            landmark_list.append(lists)
        else:
            landmark_list.append(lists)
    dict_byid[currentid]=landmark_list          #for the last id
    return dict_byid

def dict_distance(dictid,id,li,xi,yi,zi):         #create a dictionary of all 3d distance for a id
    dict_d = {}
    for landmarks in dictid[id]:
        if landmarks[li] == 'FT_L':
            ftl = dictid[id].index(landmarks)
            #print(ftl)
        elif landmarks[li] == 'FT_R':
            ftr = dictid[id].index(landmarks)
            #print(ftr)
        elif landmarks[li] == 'EX_L':
            exl = dictid[id].index(landmarks)
        elif landmarks[li] == 'EX_R':
            exr = dictid[id].index(landmarks)        #the index number for each landmark
        elif landmarks[li] == 'EN_L':
            enl = dictid[id].index(landmarks)
        elif landmarks[li] == 'EN_R':
            enr = dictid[id].index(landmarks)
        elif landmarks[li] == 'AL_L':
            all = dictid[id].index(landmarks)
        elif landmarks[li] == 'AL_R':
            alr = dictid[id].index(landmarks)
        elif landmarks[li] == 'SBAL_L':
            sball = dictid[id].index(landmarks)
        elif landmarks[li] == 'SBAL_R':
            sbalr = dictid[id].index(landmarks)
        elif landmarks[li] == 'CH_L':
            chl = dictid[id].index(landmarks)
        elif landmarks[li] == 'CH_R':
            chr = dictid[id].index(landmarks)
        elif landmarks[li] == 'N':
            n = dictid[id].index(landmarks)
        elif landmarks[li] == 'PRN':
            prn = dictid[id].index(landmarks)
        else:
            sn = dictid[id].index(landmarks)

    dict_d['FW'] = distance_3d(dictid[id][ftl][xi],dictid[id][ftl][yi],dictid[id][ftl][zi],dictid[id][ftr][xi],dictid[id][ftr][yi],dictid[id][ftr][zi])
    dict_d['OCW'] = distance_3d(dictid[id][exl][xi],dictid[id][exl][yi],dictid[id][exl][zi],dictid[id][exr][xi],dictid[id][exr][yi],dictid[id][exr][zi])
    dict_d['LEFL'] = distance_3d(dictid[id][exl][xi],dictid[id][exl][yi],dictid[id][exl][zi],dictid[id][enl][xi],dictid[id][enl][yi],dictid[id][enl][zi])
    dict_d['REFL'] = distance_3d(dictid[id][enr][xi],dictid[id][enr][yi],dictid[id][enr][zi],dictid[id][exr][xi],dictid[id][exr][yi],dictid[id][exr][zi])
    dict_d['ICW'] = distance_3d(dictid[id][enl][xi],dictid[id][enl][yi],dictid[id][enl][zi],dictid[id][enr][xi],dictid[id][enr][yi],dictid[id][enr][zi])
    dict_d['NW'] = distance_3d(dictid[id][all][xi],dictid[id][all][yi],dictid[id][all][zi],dictid[id][alr][xi],dictid[id][alr][yi],dictid[id][alr][zi])
    dict_d['ABW'] = distance_3d(dictid[id][sball][xi],dictid[id][sball][yi],dictid[id][sball][zi],dictid[id][sbalr][xi],dictid[id][sbalr][yi],dictid[id][sbalr][zi])
    dict_d['MW'] = distance_3d(dictid[id][chl][xi],dictid[id][chl][yi],dictid[id][chl][zi],dictid[id][chr][xi],dictid[id][chr][yi],dictid[id][chr][zi])
    dict_d['NBL'] = distance_3d(dictid[id][n][xi],dictid[id][n][yi],dictid[id][n][zi],dictid[id][prn][xi],dictid[id][prn][yi],dictid[id][prn][zi])
    dict_d['NH'] = distance_3d(dictid[id][n][xi],dictid[id][n][yi],dictid[id][n][zi],dictid[id][sn][xi],dictid[id][sn][yi],dictid[id][sn][zi])
    return dict_d
    
def opt1(adultIDs, dict3d):                               #get the output of op1
    dict_opt1 = []
    for IDs in adultIDs:
        for ids in dict3d:
            if ids == IDs:
                temp = dict3d[ids].copy()                    #make shallow copy of dictionary so when we round data, it won't affect the original dictionary- 
                dict_opt1.append(temp)                       #-we pass to this function
                break   
    for dict in dict_opt1:
        for key in dict:                                 #round to four decimal places
            dict[key] = round(dict[key],4)
    return dict_opt1
    
def opt2(dict, ids):                                     #get the output of op2
    return round(similarity(dict[ids[0]],dict[ids[1]]),4)

def opt3(dict, ids):                                        #get the output of op3
    listopt3 = []                                        #the list this function returns
    list1 = []                                         #create a list which stores all the similarity F1 exclude F2
    list2 = []                                         #create a list which stores all the similarity F2 exclude F1
    for keys in dict:
        if keys != ids[0] and keys != ids[1]:                    #if face is not F1 F2
            list1.append((keys,similarity(dict[ids[0]],dict[keys])))
            list2.append((keys,similarity(dict[ids[1]],dict[keys])))
            
    sorted_list1 = sorted(list1, key=lambda tup: (-tup[1],tup[0]))                  #sort the list as uppder order of similarity
    sorted_list2 = sorted(list2, key=lambda tup: (-tup[1],tup[0]))                  # if similarity is the same, make it arranged in alphabetical-
    #print(sorted_list1,sorted_list2)                                               #-order of their Adult ID
    l1 = sorted_list1[:5]
    l2 = sorted_list2[:5]
    #print(l1,l2)
    final_l1 = []
    final_l2 = []
    for tuples in l1:
        final_l1.append((tuples[0],round(tuples[1],4)))                 #cannot change values in tuple, so assign the value to another tuple-
    for tuples in l2:                                                   #-in order to round it to four deciaml places
        final_l2.append((tuples[0],round(tuples[1],4)))
    #print(final_l1,final_l2)
    listopt3.append(final_l1)
    listopt3.append(final_l2)
    return listopt3

def opt4(lop3,dict3d):                                              #get the output of op4      
    idlist1 = []                                             #list of id in op3 of F1
    idlist2 = []                                             #list of id in op3 of F2
    for item in lop3[0]:
        idlist1.append(item[0])
    for item in lop3[1]:
        idlist2.append(item[0])
    #print(idlist1,idlist2)
    total1 = []                                                #initalize the list which store all 5 id 's landmarks data
    total2 = []
    for ID in idlist1:
        for id in dict3d:
            if id == ID:
                total1.append(dict3d[id])
                break;
            
    for ID in idlist2:
        for id in dict3d:
            if id == ID:
                total2.append(dict3d[id])
                break;
    #print(total1,total2)
    kw_t1 = 0
    ocw_t1 = 0
    lefl_t1 = 0
    refl_t1 = 0                                              #initalize the total value of landmarks of list1
    icw_t1 = 0
    nw_t1 = 0
    abw_t1 = 0
    mw_t1 = 0
    nbl_t1 = 0
    nh_t1 = 0
    for dict in total1:
        kw_t1 = dict['FW'] + kw_t1
        ocw_t1 = dict['OCW'] + ocw_t1
        lefl_t1 = dict['LEFL'] + lefl_t1
        refl_t1 = dict['REFL'] + refl_t1
        icw_t1 = dict['ICW'] + icw_t1
        nw_t1 = dict['NW'] + nw_t1
        abw_t1 = dict['ABW'] + abw_t1
        mw_t1 = dict['MW'] + mw_t1
        nbl_t1 = dict['NBL'] + nbl_t1
        nh_t1 = dict['NH'] + nh_t1
        
    kw_t2 = 0
    ocw_t2 = 0
    lefl_t2 = 0
    refl_t2 = 0                                              #initalize the total value of landmarks of list2
    icw_t2 = 0
    nw_t2 = 0
    abw_t2 = 0
    mw_t2 = 0
    nbl_t2 = 0
    nh_t2 = 0
    for dict in total2:
        kw_t2 = dict['FW'] + kw_t2
        ocw_t2 = dict['OCW'] + ocw_t2
        lefl_t2 = dict['LEFL'] + lefl_t2
        refl_t2 = dict['REFL'] + refl_t2
        icw_t2 = dict['ICW'] + icw_t2
        nw_t2 = dict['NW'] + nw_t2
        abw_t2 = dict['ABW'] + abw_t2
        mw_t2 = dict['MW'] + mw_t2
        nbl_t2 = dict['NBL'] + nbl_t2
        nh_t2 = dict['NH'] + nh_t2
    
    kw_t1 = round(kw_t1/5,4)
    ocw_t1 = round(ocw_t1/5,4)
    lefl_t1 = round(lefl_t1/5,4)
    refl_t1 = round(refl_t1/5,4)                                              #calculate the average value of all landmarks of list1
    icw_t1 = round(icw_t1/5,4)
    nw_t1 = round(nw_t1/5,4)
    abw_t1 = round(abw_t1/5,4)
    mw_t1 = round(mw_t1/5,4)
    nbl_t1 = round(nbl_t1/5,4)
    nh_t1 = round(nh_t1/5,4)
    dict1 = {}
    dict1['FW'] = kw_t1
    dict1['OCW'] = ocw_t1
    dict1['LEFL'] = lefl_t1
    dict1['REFL'] = refl_t1
    dict1['ICW'] = icw_t1
    dict1['NW'] = nw_t1
    dict1['ABW'] = abw_t1
    dict1['MW'] = mw_t1
    dict1['NBL'] = nbl_t1
    dict1['NH'] = nh_t1
    
    kw_t2 = round(kw_t2/5,4)
    ocw_t2 = round(ocw_t2/5,4)
    lefl_t2 = round(lefl_t2/5,4)
    refl_t2 = round(refl_t2/5,4)                                              #calculate the average value of all landmarks of list2
    icw_t2 = round(icw_t2/5,4)
    nw_t2 = round(nw_t2/5,4)
    abw_t2 = round(abw_t2/5,4)
    mw_t2 = round(mw_t2/5,4)
    nbl_t2 = round(nbl_t2/5,4)
    nh_t2 = round(nh_t2/5,4)
    dict2 = {}
    dict2['FW'] = kw_t2
    dict2['OCW'] = ocw_t2
    dict2['LEFL'] = lefl_t2
    dict2['REFL'] = refl_t2
    dict2['ICW'] = icw_t2
    dict2['NW'] = nw_t2
    dict2['ABW'] = abw_t2
    dict2['MW'] = mw_t2
    dict2['NBL'] = nbl_t2
    dict2['NH'] = nh_t2
    
    opt4_list = []
    opt4_list.append(dict1)
    opt4_list.append(dict2)
    return opt4_list

def main(csvfile, adultIDs):

    if type(adultIDs).__name__ != 'list':
        print('The second input is not a list')                           #see if the inputs are correct
        return None,None,None,None
    if len(adultIDs) != 2:
        print('The length of list is not 2')
        return None,None,None,None
    try:
        test1 = open(csvfile, 'r')
    except IOError:
        print('Cannot find or open the file')
        return None,None,None,None
    test1.close()
    
    with open(csvfile, 'r') as cfile:
        Line1 = cfile.readline()
        Line1 = Line1[:-1] #delete \n
        Line1=Line1.split(',')
        for m in Line1:
            if m=='X' or m=='x':
                xi=Line1.index(m)
            if m=='Y' or m=='y':
                yi=Line1.index(m)      #xi:the index number for x
            if m=='Z' or m=='z':       #yi:the index number for y
                zi=Line1.index(m)      #zi:the index number for z
            if len(m)==7:              #ai:the index number for adultid
                ai=Line1.index(m)      #li:the index number for landmark
            if len(m)==8:
                li=Line1.index(m)
        #print(xi,yi,zi,ai,li)
        
        listoflist = []
        for lines in cfile:
            line = lines[:-1].split(',')               #store all data in a list of list
            for text in line:
                line[line.index(text)] = text.upper()
            listoflist.append(line)
        #print(listoflist)
            
        
        
    corruptlist = []                                        #store the id which needs to be discared
    for item in listoflist:
        if item[xi] =='' or item[yi] =='' or item[zi] =='':           #see if x,y or z is missing(empty)
            #print(item)
            corruptlist.append(item[ai])
        elif float(item[xi])>200 or float(item[xi])<-200 or float(item[yi])>200 or float(item[yi])<-200 or float(item[zi])>200 or float(item[zi])<-200:
            #print(item)                                       #see if data is out of boundary
            corruptlist.append(item[ai])
    
    #see if some id is missing row
    currentname = ''                    
    landmarks_counter = 0                   #count the number of landmarks in an id, start with 0. Each id should has 15 landmarks(lines)
    for name in listoflist:                                      
        if currentname == '':                 #initialize the currentname and the landmarks_counter
            currentname = name[ai]
            #print('start')
            landmarks_counter = landmarks_counter + 1
        elif currentname != name[ai]:
            if landmarks_counter != 15:
                corrupt_place = listoflist.index(name)
                print(corrupt_place)                                #if counter is not 15, so the previous id is missing row
                corruptlist.append(listoflist[corrupt_place-1][ai])
            currentname = name[ai]
            landmarks_counter = 1        #reset the landmarks_counter
            #print(landmarks_counter)
        else:
            landmarks_counter = landmarks_counter + 1
            #print(landmarks_counter)
    if landmarks_counter != 15:                     #see if the last id is missing one or more row
        corruptlist.append(listoflist[-1][ai])
            



    #print(corruptlist)
    for corrupted_data in corruptlist:
        for items in listoflist:
            if items[ai]==corrupted_data:           #discard the whole id which has corrupted or missing data or missing row
                listoflist.remove(items)
    #print(listoflist)
    
    for things in listoflist:
        things[xi]=float(things[xi])
        things[yi]=float(things[yi])                      #turn all numeric strings into float type
        things[zi]=float(things[zi])
    #print(listoflist)
                
    dict_byID = make_person_dict(listoflist,ai)      #now we have a dictnary where key is id,value is a list which contains all the lines related to this id
    #print(dict_byID)
    
    #R7033dict = dict_distance(dict_byID, 'R7033',li,xi,yi,zi)                    see if dict_distance is working
    #print(R7033dict)
    
    dict_3d_distance = {}                           #create a dictionary which key is id, value is a dictionary of 3d distance of that person
    for person in dict_byID:
        dict_3d_distance[person] = dict_distance(dict_byID, person,li,xi,yi,zi)
    #print(dict_3d_distance)                               #see if the dictionary is successfully created
    
    
    op1 = opt1(adultIDs, dict_3d_distance)
   
    op2 = opt2(dict_3d_distance, adultIDs)

    op3 = opt3(dict_3d_distance, adultIDs)
    
    op4 = opt4(op3,dict_3d_distance)
    
    return op1,op2,op3,op4
        
                
            
                
            
            
            
        
            
            
        
        