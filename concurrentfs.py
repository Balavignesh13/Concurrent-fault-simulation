# Read me

# format for the bubble list line-fault(output,input,input)
# format for the fault list line-fault-value of the line
# The union function randomizes the sequence of the bubble list due to which an error might be thrown.
# Run the program untill the error is not displayed
# Please ignore certain comments as they are used to debug the code and were not removed.


#---------------------------------------------------functions for different gates----------------------------------------------------#
def fanout_fault(x, y, z, faultlist_x):
    return list(set().union(faultlist_x, [z + str(bin(not(y))[-1])+str(bin(not(y))[-1])]))


def andgate_faultlist(x, y, z, a, faultlist_x, faultlist_y, bubble_list_z=[]):
    temp = list(set().union(faultlist_x, faultlist_y))
    faultlist_z = list(set().union(
        temp, [a + str(bin(not(z))[-1]) + str(bin(not(z))[-1])]))

    # for changing into bubble list
    temp_b_list = []
    tf = 0
    for ref in faultlist_z:
        for fault1 in faultlist_z:
            if fault1[0:2] == ref[0:2]:
                # print(1)
                if ref != fault1 and tf == 0:
                    # print(2)
                    g = int(fault1[2]) & int(ref[2])
                    if fault1 in faultlist_x:
                        temp_b_list.append(
                            fault1[0:2]+'('+str(g) + fault1[2] + ref[2] + ')')
                        faultlist_z.append(ref[0:2]+str(g))
                        faultlist_z.remove(fault1)
                        tf = 1

                    elif fault1 in faultlist_y:
                        temp_b_list.append(
                            fault1[0:2]+'('+str(g) + fault1[2] + ref[2] + ')')
                        faultlist_z.append(ref[0:2]+str(g))
                        faultlist_z.remove(fault1)
                        tf = 1
            if tf == 1:
                # print(ref)
                # print(faultlist_z)
                # print(temp_b_list)
                faultlist_z.remove(ref)
                tf = 0

    tempval = 0
    cx = 0
    cy = 0
    ci = 0
    # print(faultlist_z)
    for fault in faultlist_z:
        if len(bubble_list_z) > 0:
            flag = 0
            for gate in bubble_list_z:

                if fault[0:2] == gate[0:2]:
                    if flag == 1:
                        temp_b_list.remove(ci)
                        if cx == 1:
                            temp_b_list.append(
                                gate[0:3]+str(int(fault[2]) & int(tempval)) + tempval+fault[2] + gate[-1])
                        elif cy == 1:
                            temp_b_list.append(
                                gate[0:3]+str(int(fault[2]) & int(tempval)) + fault[2] + tempval + gate[-1])
                        continue
                    if fault in faultlist_x:
                        temp_b_list.append(
                            gate[0:3]+str(int(fault[2]) & y) + fault[2] + str(y) + gate[-1])
                        ci = temp_b_list.index(
                            gate[0:3]+str(int(fault[2]) & y) + fault[2] + str(y) + gate[-1])
                        cx = 1
                        cy = 0
                        tempval = fault[2]
                    elif fault in faultlist_y:
                        temp_b_list.append(
                            gate[0:3]+str(int(fault[2]) & x) + str(x) + fault[2] + gate[-1])

                        ci = temp_b_list.index(
                            gate[0:3]+str(int(fault[2]) & x) + str(x) + fault[2] + gate[-1])
                        cx = 0
                        cy = 1
                        tempval = fault[2]
                    else:
                        temp_b_list.append(
                            gate[0:3]+fault[2] + str(x) + str(y) + gate[-1])

                    flag = 1

            if flag == 0:
                if(fault in faultlist_x):
                    temp_b_list.append(fault[0:2] +
                                       '(' + str(int(fault[2]) & y) + fault[2] + str(y)+')')
                elif(fault in faultlist_y):
                    temp_b_list.append(fault[0:2] +
                                       '(' + str(int(fault[2]) & x)+str(x)+fault[2]+')')
                else:
                    temp_b_list.append(fault[0:2] +
                                       '(' + fault[2]+str(x)+str(y)+')')
            # print(temp_b_list)
        elif(fault in faultlist_x):
            temp_b_list.append(fault[0:2] +
                               '(' + str(int(fault[2]) & y)+fault[2] + str(y)+')')
        elif(fault in faultlist_y):
            temp_b_list.append(fault[0:2] +
                               '(' + str(int(fault[2]) & x)+str(x)+fault[2]+')')
        else:
            temp_b_list.append(fault[0:2] +
                               '(' + fault[2]+str(x)+str(y)+')')

    bubble_list_z = temp_b_list
    fault_prop_list = []

    for bubble in bubble_list_z:
        if int(bubble[3]) != z:
            fault_prop_list.append(bubble)

    temp_f_list = []
    for fault in fault_prop_list:
        t = fault[0:2]+fault[3]
        temp_f_list.append(t)

    faultlist_z = temp_f_list

    return faultlist_z, bubble_list_z, fault_prop_list


def orgate_faultlist(x, y, z, a, faultlist_x, faultlist_y, bubble_list_z=[]):
    faultlist_z = []
    temp_b_list = []
    temp = list(set().union(faultlist_x, faultlist_y))
    faultlist_z = list(set().union(
        temp, [a + str(bin(not(z))[-1]) + str(bin(not(z))[-1])]))

    tf = 0
    for ref in faultlist_z:
        for fault1 in faultlist_z:
            if fault1[0:2] == ref[0:2]:
                # print(1)
                if ref != fault1 and tf == 0:
                    # print(2)
                    g = int(fault1[2]) | int(ref[2])
                    if fault1 in faultlist_x:
                        temp_b_list.append(
                            fault1[0:2]+'('+str(g) + fault1[2] + ref[2] + ')')
                        faultlist_z.append(ref[0:2]+str(g))
                        faultlist_z.remove(fault1)
                        tf = 1

                    elif fault1 in faultlist_y:
                        temp_b_list.append(
                            fault1[0:2]+'('+str(g) + fault1[2] + ref[2] + ')')
                        faultlist_z.append(ref[0:2]+str(g))
                        faultlist_z.remove(fault1)
                        tf = 1
            if tf == 1:
                # print(ref)
                # print(faultlist_z)
                # print(temp_b_list)
                faultlist_z.remove(ref)
                tf = 0

    # for changing into bubble list
    tempval = 0
    cx = 0
    cy = 0
    ci = 0
    # print(faultlist_z)
    for fault in faultlist_z:
        flag = 0
        if len(bubble_list_z) > 0:
            for gate in bubble_list_z:
                if fault[0:2] == gate[0:2]:
                    if flag == 1:
                        temp_b_list.remove(ci)
                        if cx == 1:
                            temp_b_list.append(
                                gate[0:3]+str(int(fault[2]) | int(tempval)) + tempval+fault[2] + gate[-1])
                        elif cy == 1:
                            temp_b_list.append(
                                gate[0:3]+str(int(fault[2]) | int(tempval)) + fault[2] + tempval + gate[-1])
                        continue
                    if fault in faultlist_x:
                        temp_b_list.append(
                            gate[0:3]+str(int(fault[2]) | y) + fault[2] + str(y) + gate[-1])
                        ci = temp_b_list.index(
                            gate[0:3]+str(int(fault[2]) | y) + fault[2] + str(y) + gate[-1])
                        cx = 1
                        cy = 0
                        tempval = fault[2]
                    elif fault in faultlist_y:
                        temp_b_list.append(
                            gate[0:3]+str(int(fault[2]) | x) + str(x) + fault[2] + gate[-1])

                        ci = temp_b_list.index(
                            gate[0:3]+str(int(fault[2]) | x) + str(x) + fault[2] + gate[-1])
                        cx = 0
                        cy = 1
                        tempval = fault[2]
                    else:
                        temp_b_list.append(
                            gate[0:3]+fault[2] + str(x) + str(y) + gate[-1])

                    flag = 1

            if flag == 0:
                if(fault in faultlist_x):
                    temp_b_list.append(fault[0:2] +
                                       '(' + str(int(fault[2]) | y)+fault[2] + str(y)+')')
                elif(fault in faultlist_y):
                    temp_b_list.append(fault[0:2] +
                                       '(' + str(int(fault[2]) | x)+str(x)+fault[2]+')')
                else:
                    temp_b_list.append(fault[0:2] +
                                       '(' + fault[2]+str(x)+str(y)+')')

        elif(fault in faultlist_x):
            temp_b_list.append(fault[0:2] +
                               '(' + str(int(fault[2]) | y)+fault[2] + str(y)+')')
        elif(fault in faultlist_y):
            temp_b_list.append(fault[0:2] +
                               '(' + str(int(fault[2]) | x)+str(x)+fault[2]+')')
        else:
            temp_b_list.append(fault[0:2] +
                               '(' + fault[2]+str(x)+str(y)+')')

    bubble_list_z = temp_b_list

    # fault propogation
    fault_prop_list = []

    for bubble in bubble_list_z:
        if int(bubble[3]) != z:
            fault_prop_list.append(bubble)

    temp_f_list = []
    for fault in fault_prop_list:
        t = fault[0:2]+fault[3]
        temp_f_list.append(t)

    faultlist_z = temp_f_list

    return faultlist_z, bubble_list_z, fault_prop_list


def xorgate_faultlist(x, y, z, a, faultlist_x, faultlist_y, bubble_list_z=[]):
    faultlist_z = []
    temp = list(set().union(faultlist_x, faultlist_y))
    faultlist_z = list(set().union(
        temp, [a + str(bin(not(z))[-1]) + str(bin(not(z))[-1])]))

    # for changing into bubble list
    temp_b_list = []
    tf = 0
    for ref in faultlist_z:
        for fault1 in faultlist_z:
            if fault1[0:2] == ref[0:2]:
                # print(1)
                if ref != fault1 and tf == 0:
                    # print(2)
                    g = int(fault1[2]) ^ int(ref[2])
                    if fault1 in faultlist_x:
                        temp_b_list.append(
                            fault1[0:2]+'('+str(g) + fault1[2] + ref[2] + ')')
                        faultlist_z.append(ref[0:2]+str(g))
                        faultlist_z.remove(fault1)
                        tf = 1

                    elif fault1 in faultlist_y:
                        temp_b_list.append(
                            fault1[0:2]+'('+str(g) + fault1[2] + ref[2] + ')')
                        faultlist_z.append(ref[0:2]+str(g))
                        faultlist_z.remove(fault1)
                        tf = 1
            if tf == 1:
                # print(ref)
                # print(faultlist_z)
                # print(temp_b_list)
                faultlist_z.remove(ref)
                tf = 0

    tempval = 0
    cx = 0
    cy = 0
    ci = 0
    # print(faultlist_z)
    for fault in faultlist_z:
        if len(bubble_list_z) > 0:
            flag = 0
            for gate in bubble_list_z:

                if fault[0:2] == gate[0:2]:
                    if flag == 1:
                        temp_b_list.remove(ci)
                        if cx == 1:
                            temp_b_list.append(
                                gate[0:3]+str(int(fault[2]) ^ int(tempval)) + tempval+fault[2] + gate[-1])
                        elif cy == 1:
                            temp_b_list.append(
                                gate[0:3]+str(int(fault[2]) ^ int(tempval)) + fault[2] + tempval + gate[-1])
                        continue
                    if fault in faultlist_x:
                        temp_b_list.append(
                            gate[0:3]+str(int(fault[2]) ^ y) + fault[2] + str(y) + gate[-1])
                        ci = temp_b_list.index(
                            gate[0:3]+str(int(fault[2]) ^ y) + fault[2] + str(y) + gate[-1])
                        cx = 1
                        cy = 0
                        tempval = fault[2]
                    elif fault in faultlist_y:
                        temp_b_list.append(
                            gate[0:3]+str(int(fault[2]) ^ x) + str(x) + fault[2] + gate[-1])

                        ci = temp_b_list.index(
                            gate[0:3]+str(int(fault[2]) ^ x) + str(x) + fault[2] + gate[-1])
                        cx = 0
                        cy = 1
                        tempval = fault[2]
                    else:
                        temp_b_list.append(
                            gate[0:3]+fault[2] + str(x) + str(y) + gate[-1])

                    flag = 1

            if flag == 0:
                if(fault in faultlist_x):
                    temp_b_list.append(fault[0:2] +
                                       '(' + str(int(fault[2]) ^ y)+fault[2] + str(y)+')')
                elif(fault in faultlist_y):
                    temp_b_list.append(fault[0:2] +
                                       '(' + str(int(fault[2]) ^ x)+str(x)+fault[2]+')')
                else:
                    temp_b_list.append(fault[0:2] +
                                       '(' + fault[2]+str(x)+str(y)+')')

        elif(fault in faultlist_x):
            temp_b_list.append(fault[0:2] +
                               '(' + str(int(fault[2]) ^ y)+fault[2] + str(y)+')')
        elif(fault in faultlist_y):
            temp_b_list.append(fault[0:2] +
                               '(' + str(int(fault[2]) ^ x)+str(x)+fault[2]+')')
        else:
            temp_b_list.append(fault[0:2] +
                               '(' + fault[2]+str(x)+str(y)+')')

    # print('lentempb', len(temp_b_list))

    bubble_list_z = temp_b_list

    # fault propogation
    fault_prop_list = []

    for bubble in bubble_list_z:
        if int(bubble[3]) != z:
            fault_prop_list.append(bubble)

    temp_f_list = []
    for fault in fault_prop_list:
        t = fault[0:2]+fault[3]
        temp_f_list.append(t)

    faultlist_z = temp_f_list

    return faultlist_z, bubble_list_z, fault_prop_list

#---------------------------------------------------Circuit modelling----------------------------------------------------#

# bubblelist, fault_prop_list = orgate_faultlist(
#     0, 0, 0, 'c', ['a11'], ['b11'], [])
# print(bubblelist)
# print(fault_prop_list)


bubblelist_h = []
bubblelist_i = []
bubblelist_n = []
bubblelist_p = []
bubblelist_o = []


for cc in range(8):
    if len(bin(cc)[2:]) == 1:
        a = 0
        b = 0
        x = int(str(bin(cc)[2:])[0])
    elif len(bin(cc)[2:]) == 2:
        a = 0
        b = int(str(bin(cc)[2:])[0])
        x = int(str(bin(cc)[2:])[1])
    else:
        a = int(str(bin(cc)[2:])[0])
        b = int(str(bin(cc)[2:])[1])
        x = int(str(bin(cc)[2:])[2])

    # primary inputs fault list
    faultlist_a = ['a' + str(bin(not(a))[-1]) + str(bin(not(a))[-1])]
    faultlist_b = ['b' + str(bin(not(b))[-1]) + str(bin(not(b))[-1])]
    faultlist_x = ['x' + str(bin(not(x))[-1]) + str(bin(not(x))[-1])]

    # print(faultlist_a)

    # fanouts
    c = a
    faultlist_c = fanout_fault(a, c, 'c', faultlist_a)
    e = a
    faultlist_e = fanout_fault(a, e, 'e', faultlist_a)
    d = b
    faultlist_d = fanout_fault(b, d, 'd', faultlist_b)
    f = b
    faultlist_f = fanout_fault(b, f, 'f', faultlist_b)

    # Xor gates
    h = c ^ d
    faultlist_h, bubblelist_h, fault_prop_list_h = xorgate_faultlist(
        c, d, h, 'h', faultlist_c, faultlist_d, bubblelist_h)

    i = e & f
    faultlist_i, bubblelist_i, fault_prop_list_i = andgate_faultlist(
        e, f, i, 'i', faultlist_e, faultlist_f, bubblelist_i)

    j = h
    faultlist_j = fanout_fault(h, j, 'j', faultlist_h)
    l = h
    faultlist_l = fanout_fault(h, l, 'l', faultlist_h)
    k = x
    faultlist_k = fanout_fault(x, k, 'k', faultlist_x)
    m = x
    faultlist_m = fanout_fault(x, m, 'm', faultlist_x)

    # XOR
    n = j ^ k  # sum
    faultlist_n, bubblelist_n, fault_prop_list_n = xorgate_faultlist(
        j, k, n, 'n', faultlist_j, faultlist_k, bubblelist_n)

    o = l & m
    faultlist_o, bubblelist_o, fault_prop_list_o = andgate_faultlist(
        l, m, o, 'o', faultlist_l, faultlist_m, bubblelist_o)

    p = o | i  # carry
    faultlist_p, bubblelist_p, fault_prop_list_p = orgate_faultlist(
        o, i, p, 'p', faultlist_o, faultlist_i, bubblelist_p)

    # print(len(bubblelist_p))
    # print(len(faultlist_i))

    print('\n#####--------- j0 means line j stuck at 0 and j1 means line j stuck at 1 ---------#####')
    print('\n#####--------- format:- fault(output,input,input) ---------#####')

    print("\nFor input -", a, b, x)
    # print("Sum bubble list:", bubblelist_n)
    print("Sum fault list:(XOR gate)", sorted(fault_prop_list_n))
    # print("Carry bubble list:", sorted(bubblelist_p))
    print("Carry fault list:(OR gate)", sorted(fault_prop_list_p))
