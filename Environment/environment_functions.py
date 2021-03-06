import numpy as np
from numba import njit

# @njit
def get_normal_cards_infor():
    return np.array(
        [[0, 2, 2, 2, 0, 0, 0],
        [0, 2, 3, 0, 0, 0, 0],
        [0, 2, 1, 1, 0, 2, 1],
        [0, 2, 0, 1, 0, 0, 2],
        [0, 2, 0, 3, 1, 0, 1],
        [0, 2, 1, 1, 0, 1, 1],
        [1, 2, 0, 0, 0, 4, 0],
        [0, 2, 2, 1, 0, 2, 0],
        [0, 1, 2, 0, 2, 0, 1],
        [0, 1, 0, 0, 2, 2, 0],
        [0, 1, 1, 0, 1, 1, 1],
        [0, 1, 2, 0, 1, 1, 1],
        [0, 1, 1, 1, 3, 0, 0],
        [0, 1, 0, 0, 0, 2, 1],
        [0, 1, 0, 0, 0, 3, 0],
        [1, 1, 4, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 0, 0, 0, 3],
        [0, 0, 0, 1, 1, 1, 2],
        [0, 0, 0, 0, 1, 2, 2],
        [0, 0, 1, 0, 0, 3, 1],
        [0, 0, 2, 0, 0, 0, 2],
        [0, 0, 0, 1, 1, 1, 1],
        [0, 0, 0, 2, 1, 0, 0],
        [0, 4, 0, 2, 2, 1, 0],
        [0, 4, 1, 1, 2, 1, 0],
        [0, 4, 0, 1, 0, 1, 3],
        [1, 4, 0, 0, 4, 0, 0],
        [0, 4, 0, 2, 0, 2, 0],
        [0, 4, 2, 0, 0, 1, 0],
        [0, 4, 1, 1, 1, 1, 0],
        [0, 4, 0, 3, 0, 0, 0],
        [0, 3, 1, 0, 2, 0, 0],
        [0, 3, 1, 1, 1, 0, 1],
        [1, 3, 0, 4, 0, 0, 0],
        [0, 3, 1, 2, 0, 0, 2],
        [0, 3, 0, 0, 3, 0, 0],
        [0, 3, 0, 0, 2, 0, 2],
        [0, 3, 3, 0, 1, 1, 0],
        [0, 3, 1, 2, 1, 0, 1],
        [1, 2, 0, 3, 0, 2, 2],
        [2, 2, 0, 2, 0, 1, 4],
        [1, 2, 3, 0, 2, 0, 3],
        [2, 2, 0, 5, 3, 0, 0],
        [2, 2, 0, 0, 5, 0, 0],
        [3, 2, 0, 0, 6, 0, 0],
        [3, 1, 0, 6, 0, 0, 0],
        [2, 1, 1, 0, 0, 4, 2],
        [2, 1, 0, 5, 0, 0, 0],
        [2, 1, 0, 3, 0, 0, 5],
        [1, 1, 0, 2, 3, 3, 0],
        [1, 1, 3, 2, 2, 0, 0],
        [3, 0, 6, 0, 0, 0, 0],
        [2, 0, 0, 0, 0, 5, 3],
        [2, 0, 0, 0, 0, 5, 0],
        [2, 0, 0, 4, 2, 0, 1],
        [1, 0, 2, 3, 0, 3, 0],
        [1, 0, 2, 0, 0, 3, 2],
        [3, 4, 0, 0, 0, 0, 6],
        [2, 4, 5, 0, 0, 3, 0],
        [2, 4, 5, 0, 0, 0, 0],
        [1, 4, 3, 3, 0, 0, 2],
        [1, 4, 2, 0, 3, 2, 0],
        [2, 4, 4, 0, 1, 2, 0],
        [1, 3, 0, 2, 2, 0, 3],
        [1, 3, 0, 0, 3, 2, 3],
        [2, 3, 2, 1, 4, 0, 0],
        [2, 3, 3, 0, 5, 0, 0],
        [2, 3, 0, 0, 0, 0, 5],
        [3, 3, 0, 0, 0, 6, 0],
        [4, 2, 0, 7, 0, 0, 0],
        [4, 2, 0, 6, 3, 0, 3],
        [5, 2, 0, 7, 3, 0, 0],
        [3, 2, 3, 3, 0, 3, 5],
        [3, 1, 3, 0, 3, 5, 3],
        [4, 1, 0, 0, 0, 0, 7],
        [5, 1, 0, 3, 0, 0, 7],
        [4, 1, 0, 3, 0, 3, 6],
        [3, 0, 0, 5, 3, 3, 3],
        [4, 0, 0, 0, 7, 0, 0],
        [5, 0, 3, 0, 7, 0, 0],
        [4, 0, 3, 3, 6, 0, 0],
        [5, 4, 0, 0, 0, 7, 3],
        [3, 4, 5, 3, 3, 3, 0],
        [4, 4, 0, 0, 0, 7, 0],
        [4, 4, 3, 0, 0, 6, 3],
        [3, 3, 3, 3, 5, 0, 3],
        [5, 3, 7, 0, 0, 3, 0],
        [4, 3, 6, 0, 3, 3, 0],
        [4, 3, 7, 0, 0, 0, 0]]
    )

# @njit
def get_noble_cards_infor():
    return np.array(
        [[0, 4, 4, 0, 0],
        [3, 0, 3, 3, 0],
        [3, 3, 3, 0, 0],
        [3, 0, 0, 3, 3],
        [0, 3, 0, 3, 3],
        [4, 0, 4, 0, 0],
        [4, 0, 0, 4, 0],
        [0, 3, 3, 0, 3],
        [0, 4, 0, 0, 4],
        [0, 0, 0, 4, 4]]
    )

normal_cards_infor = get_normal_cards_infor()
noble_cards_infor = get_noble_cards_infor()

# @njit
def generate_environment():
    e_state = np.array(
        [0 for _ in range(100)] # T??nh tr???ng 100 th??? (90 th??? th?????ng, 10 th??? qu?? t???c): 0.99
        + [7 for _1 in range(5)] + [5] # Nguy??n li???u tr??n b??n ch??i: 100.105
        + [0 for _2 in range(55)] # 12x4=48 t??nh tr???ng ng?????i ch??i, 1 turn, 5 nh???ng nl ???? l???y, 1 phase
    )                             # 106.111,112.116,117,118.129,130.141,142.153,154,155.159,160
    
    lv1 = np.arange(41)
    lv2 = np.arange(40,71)
    lv3 = np.arange(70,91)
    
    return e_state, lv1, lv2, lv3

@njit
def reset(e_state, lv1, lv2, lv3):
    e_state[:100] = 0
    e_state[100:106] = np.array([7,7,7,7,7,5])
    e_state[106:] = 0

    lv1[-1] = 4
    np.random.shuffle(lv1[:-1])
    e_state[:40][lv1[:4]] = 5

    lv2[-1] = 4
    np.random.shuffle(lv2[:-1])
    e_state[:70][lv2[:4]] = 5

    lv3[-1] = 4
    np.random.shuffle(lv3[:-1])
    e_state[:90][lv3[:4]] = 5

    nob = np.arange(90,100)
    np.random.shuffle(nob)
    e_state[:100][nob[:5]] = 5

@njit
def get_player_state(e_state):
    p_idx = e_state[154] % 4 + 1
    p_state = e_state.copy()
    if p_idx != 1:
        x_ = p_idx - 1
        p_state[:100][np.where(e_state[:100]==x_)[0]] = 4
        p_state[:100][np.where(e_state[:100]==-x_)[0]] = -4
        for i in range(4):
            x_ = (p_idx-1+i) % 4
            p_state[106+12*i:118+12*i] = e_state[106+12*x_:118+12*x_].copy()
            x_ = i+1
            y_ = (i+2-p_idx) % 4
            if x_ != (p_idx-1):
                p_state[:100][np.where(e_state[:100]==x_)[0]] = y_
                p_state[:100][np.where(e_state[:100]==-x_)[0]] = -y_
    
    return p_state

@njit
def check_buy_card(p_state, card_id):
    self_st = p_state[106:112]
    self_st_const = p_state[112:117]
    card_price = normal_cards_infor[card_id][-5:]
    if np.sum((card_price>(self_st[:5]+self_st_const))*(card_price-self_st[:5]-self_st_const)) <= self_st[5]:
        return True

    return False

@njit
def get_list_action(p_state):
    phase = p_state[-1] # Pha
    list_action = []
    normal_cards = p_state[:90] # Tr???ng th??i c??c th??? th?????ng
    b_stocks = p_state[100:106] # Nguy??n li???u tr??n b??n ch??i
    self_st = p_state[106:112] # Nguy??n li???u c???a ng?????i ch??i
    cards_check_buy = [i_ for i_ in range(90) if normal_cards[i_]==-1 or normal_cards[i_] == 5]

    if phase == 0: # L???a ch???n ki???u h??nh ?????ng
        if np.sum(b_stocks[:5]) != 0:
            list_action.append(1) # L???y nguy??n li???u
        else:
            list_action.append(0) # B??? l?????t

        if np.count_nonzero(normal_cards==-1) < 3:
            list_action.append(2) # ??p th???

        for card_id in cards_check_buy:
            if check_buy_card(p_state, card_id):
                list_action.append(3) # Mua th???
                break
    
    elif phase == 1: # L???y nguy??n li???u
        taken = p_state[155:160]
        s_taken = np.sum(taken)
        temp_ = [i_+4 for i_ in range(5) if b_stocks[i_] != 0]
        if s_taken == 0:
            list_action += temp_
        elif s_taken == 1:
            s_ = np.where(taken==1)[0][0]
            if b_stocks[:5][s_] >= 3: # C?? th??? l???y double
                list_action += temp_
            else:
                if (s_+4) in temp_:
                    temp_.remove(s_+4)

                list_action += temp_
        else:
            lst_s_ = np.where(taken==1)[0]
            for s_ in lst_s_:
                if (s_+4) in temp_:
                    temp_.remove(s_+4)
            
            list_action += temp_

        if np.sum(self_st) >= 10:
            list_action.append(0)

    elif phase == 2: # ??p th???
        temp_ = [i_+9 for i_ in range(90) if normal_cards[i_]==5]
        list_action += temp_
        if np.count_nonzero(normal_cards[:40]==0) != 0:
            list_action.append(99)
        if np.count_nonzero(normal_cards[40:70]==0) != 0:
            list_action.append(100)
        if np.count_nonzero(normal_cards[70:]==0) != 0:
            list_action.append(101)
            
    elif phase == 3: # Mua th???
        for card_id in cards_check_buy:
            if check_buy_card(p_state, card_id):
                list_action.append(card_id+102)
    
    else: # Pha tr??? nguy??n li???u
        temp_ = [i_+192 for i_ in range(6) if self_st[i_] != 0]
        list_action += temp_

    return list_action

@njit
def close_game(e_state):
    score_arr = e_state[np.array([117,129,141,153])]
    max_score = np.max(score_arr)
    if max_score >= 15 and e_state[-1] == 0 and e_state[154] % 4 == 0:
        lst_p = np.where(score_arr==max_score)[0] + 1
        if len(lst_p) == 1:
            return lst_p[0]
        else:
            lst_p_c = []
            lst_p = np.flip(lst_p)
            for p_id in lst_p:
                lst_p_c.append(np.count_nonzero(e_state[:90]==p_id))
            
            lst_p_c = np.array(lst_p_c)
            min_p_c = np.min(lst_p_c)
            p_win = np.where(lst_p_c==min_p_c)[0][0]
            return lst_p[p_win]
    else:
        return 0

@njit
def step(action, e_state, lv1, lv2, lv3):
    # Check xem action c?? h???p l???
    list_action = get_list_action(get_player_state(e_state))
    if action not in list_action:
        '''
        Action kh??ng h???p l???
        '''
        # print('Action kh??ng h???p l???')
        e_state[154] += 1 # Sang turn m???i
        e_state[-1] = 0

    else:
        phase = e_state[-1]
        p_idx = e_state[154] % 4
        cur_p = e_state[106+12*p_idx:118+12*p_idx]
        b_stocks = e_state[100:106]
        
        if phase == 0: # L???a ch???n pha ti???p theo
            e_state[-1] = action
            if action == 0: # Sang turn m???i
                e_state[154] += 1 # Ch???nh turn
            elif action == 1: # Sang pha l???y nguy??n li???u
                e_state[155:160] = np.array([0,0,0,0,0]) # Nguy??n li???u ???? l???y
        
        elif phase == 1: # Pha l???y nguy??n li???u, nguy??n li???u = action - 4
            check_phase1 = False
            if action == 0:
                check_phase1 = True
            else:
                st_ = action - 4
                taken = e_state[155:160]
                taken[st_] += 1 # Th??m v??o nguy??n li???u ???? l???y
                cur_p[:5][st_] += 1 # Th??m nguy??n li???u cho ng?????i ch??i hi???n t???i
                b_stocks[:5][st_] -= 1 # Tr??? nguy??n li???u ??? b??n ch??i
                # T??nh to??n xem pha l???y nguy??n li???u c??n ti???p t???c hay kh??ng
                # Chuy???n sang pha tr??? nguy??n li???u ho???c sang turn m???i
                s_taken = np.sum(taken)
                if s_taken == 1: # Ch??? c??n ????ng lo???i nl v???a l???y nh??ng sl < 3
                    if b_stocks[:5][st_] < 3 and (np.sum(b_stocks[:5]) - b_stocks[:5][st_]) == 0:
                        check_phase1 = True
                elif s_taken == 2: # L???y double, ho???c kh??ng c??n nl n??o kh??c 2 c??i v???a l???y
                    if np.max(taken) == 2 or (np.sum(b_stocks[:5]) - np.sum(b_stocks[:5][np.where(taken>0)[0]])) == 0:
                        check_phase1 = True
                else: # sum(taken) = 3
                    check_phase1 = True

            if check_phase1:
                if np.sum(cur_p[:6]) > 10:
                    e_state[-1] = 4 # Sang pha tr??? nguy??n li???u
                else:
                    e_state[154] += 1 # Sang turn m???i
                    e_state[-1] = 0

        elif phase == 2: # Pha ??p th???, th??? = action - 9, ?????c bi???t 90,91,92
            card_id = action - 9
            if b_stocks[5] > 0: # Check nh???n nguy??n li???u v??ng
                cur_p[:6][5] += 1 # C???ng nguy??n li???u v??ng cho ng?????i ch??i
                b_stocks[5] -= 1 # Tr??? nguy??n li???u v??ng ??? b??n ch??i

            if card_id == 90: # ??p th??? ???n c???p 1
                e_state[:90][lv1[lv1[-1]]] = -(p_idx+1)
                lv1[-1] += 1
            elif card_id == 91: # ??p th??? ???n c???p 2
                e_state[:90][lv2[lv2[-1]]] = -(p_idx+1)
                lv2[-1] += 1
            elif card_id == 92: # ??p th??? ???n c???p 3
                e_state[:90][lv3[lv3[-1]]] = -(p_idx+1)
                lv3[-1] += 1
            else: # ??p th??? b??nh th?????ng
                e_state[:90][card_id] = -(p_idx+1)
                if card_id < 40:
                    if lv1[-1] < 40:
                        e_state[:90][lv1[lv1[-1]]] = 5
                        lv1[-1] += 1
                elif card_id < 70:
                    if lv2[-1] < 30:
                        e_state[:90][lv2[lv2[-1]]] = 5
                        lv2[-1] += 1
                else:
                    if lv3[-1] < 20:
                        e_state[:90][lv3[lv3[-1]]] = 5
                        lv3[-1] += 1
            
            # Chuy???n sang pha tr??? nguy??n li???u ho???c sang turn m???i
            if np.sum(cur_p[:6]) > 10:
                e_state[-1] = 4 # Sang pha tr??? nguy??n li???u
            else:
                e_state[154] += 1 # Sang turn m???i
                e_state[-1] = 0

        elif phase == 3: # Pha mua th???, th??? = action - 102
            card_id = action - 102
            card_infor = normal_cards_infor[card_id]
            card_price = card_infor[-5:]
            nl_bo_ra = (card_price>cur_p[6:11]) * (card_price-cur_p[6:11])
            nl_bt = np.minimum(nl_bo_ra, cur_p[:5])
            nl_auto = np.sum(nl_bo_ra - nl_bt)

            # Tr??? nguy??n li???u
            cur_p[:5] -= nl_bt
            cur_p[5] -= nl_auto
            b_stocks[:5] += nl_bt
            b_stocks[5] += nl_auto

            # Nh???n th???
            x_ = e_state[:90][card_id]
            e_state[:90][card_id] = p_idx+1
            if x_ == 5:
                if card_id < 40:
                    if lv1[-1] < 40:
                        e_state[:90][lv1[lv1[-1]]] = 5
                        lv1[-1] += 1
                elif card_id < 70:
                    if lv2[-1] < 30:
                        e_state[:90][lv2[lv2[-1]]] = 5
                        lv2[-1] += 1
                else:
                    if lv3[-1] < 20:
                        e_state[:90][lv3[lv3[-1]]] = 5
                        lv3[-1] += 1

            # Score, const_stock
            cur_p[6:11][card_infor[1]] += 1
            cur_p[11] += card_infor[0]

            # Check Noble
            noble_lst = []
            nobles = [i for i in range(90,100) if e_state[:100][i]==5]
            for noble_id in nobles:
                if (noble_cards_infor[noble_id-90][-5:] <= cur_p[6:11]).all():
                    noble_lst.append(noble_id)

            for noble_id in noble_lst:
                e_state[:100][noble_id] = p_idx+1
                cur_p[11] += 3

            e_state[154] += 1 # Sang turn m???i
            e_state[-1] = 0
        
        elif phase == 4: # Pha tr??? nguy??n li???u, nguy??n li???u = action - 192
            st_ = action - 192
            cur_p[:6][st_] -= 1
            b_stocks[st_] += 1

            if np.sum(cur_p[:6]) <= 10: # Th???a m??n ??i???u ki???n n??y th?? sang turn m???i
                e_state[154] += 1 # Sang turn m???i
                e_state[-1] = 0

        else:
            '''
            Pha kh??ng h???p l???
            '''
            # print('Pha kh??ng h???p l???')
            e_state[154] += 1 # Sang turn m???i
            e_state[-1] = 0

@njit
def amount_action():
    return 198

@njit
def check_victory(p_state):
    score_arr = p_state[np.array([117,129,141,153])]
    max_score = np.max(score_arr)
    if max_score >= 15 and p_state[-1] == 0 and p_state[154] % 4 == 0:
        lst_p = np.where(score_arr==max_score)[0] + 1
        if len(lst_p) == 1:
            if lst_p[0] == 1:
                return 1
            else:
                return 0
        else:
            lst_p_c = []
            lst_p = np.flip(lst_p)
            for p_id in lst_p:
                lst_p_c.append(np.count_nonzero(p_state[:90]==p_id))
            
            lst_p_c = np.array(lst_p_c)
            min_p_c = np.min(lst_p_c)
            p_win = np.where(lst_p_c==min_p_c)[0][0]
            if lst_p[p_win] == 1:
                return 1
            else:
                return 0
    else:
        return -1