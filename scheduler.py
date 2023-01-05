import csv
import os

path = os.path.dirname(os.path.realpath(__file__))
#-----------------------------------------------
def demandlist_loader(): # demandlist를 load하는 함수
    with open(path+f'\\{demandlist_num}.txt','r') as file:
        demand_reader = csv.reader(file)
        demand_list = list(demand_reader)

    for i in range(len(demand_list)):
        demand_list[i].insert(0,i)
    return demand_list
#-----------------------------------------------
def machine_states_make(): # 기계 상태를 보여주는 변수를 생성하는 함수
    machine_states = []
    for i in range(18):
        machine_states.append(['Empty',0])

    return machine_states
#-----------------------------------------------
def prodnum_sum_make(): # 제품 종류를 키 값으로 하고 제품종류마다의 총 주문량을 보여주는 변수를 생성하는 함수
    prodnum_sum = {} # 제품마다의 총 주문량

    for i in range(13): # 제품 종류 수 만큼 반복
        prodnum_sum[chr(65 + i)] = 0 # 각 제품 종류를 key로 하고 0을 값으로 저장
        for j in range(len(demand_list)): # 제품 수 만큼 반복
            if demand_list[j][1] == chr(65 + i): # 제품의 주문량을 prodnum_sum의 key값에 맞게 더함
                prodnum_sum[chr(65 + i)] += int(demand_list[j][2])
    return prodnum_sum
#-----------------------------------------------
def demand_sorter1(demand_list): # demandlist를 정렬하는 함수
    prodnum_sum_sort = prodnum_sum.items() # prodnum_sum을 [제품 종류, 총 주문량]들의 배열로 만듬
    prodnum_sum_sort = sorted(prodnum_sum_sort, key = lambda x: x[1], reverse = True)

    order_num = 0 # 주문 번호
    n = 0 # 처리한 주문 번호 개수

    for i in demand_list: # orderlist_sort의 각 주문에 여유날짜 첨가
        i.append(int(i[3])- int(i[2])) # duedate - 생산해야 하는 날짜

    demand_list = sorted(demand_list, key = lambda x: int(x[4])) # 여유날짜가 작은 순으로 정렬

    for i in demand_list: # orderlist_sort의 각 주문에 여유날짜 제거
        del i[4]

    # 주문 순서를 제품의 총 주문량이 많은 순으로 정렬
    for i in range(len(prodnum_sum_sort)): # 제품 종류 수 만큼 반복
        while n < len(demand_list): # 제품 주문 수 만큼 반복
            if demand_list[order_num][1] == prodnum_sum_sort[i][0]:
            # 주문의 제품 종류가 prodnum_sum의 i번째의 제품 종류와 같을 경우 주문 순서를 마지막으로 이동하고 n에 1을 더함
                temp = demand_list.pop(order_num)
                demand_list.append(temp)
                n += 1
            else: # 주문의 제품 종류가 prodnum_sum의 i번째의 제품 종류와 다를 경우 n에 1을 더하고 다음 주문 번호에 1을 더함
                n += 1
                order_num += 1
        order_num = 0 # 주문 번호를 0으로 초기화
        n = 0 # n을 0으로 초기화

    return demand_list
#-----------------------------------------------
def demand_sorter2(demand_list): # demandlist를 정렬하는 함수
    prodnum_sum_sort = prodnum_sum.items() # prodnum_sum을 [제품 종류, 총 주문량]들의 배열로 만듬
    prodnum_sum_sort = sorted(prodnum_sum_sort, key = lambda x: x[1], reverse = True)

    order_num = 0 # 주문 번호
    n = 0 # 처리한 주문 번호 개수
    demand_list = sorted(demand_list, key=lambda x: int(x[3]))

    # 주문 순서를 제품의 총 주문량이 많은 순으로 정렬
    for i in range(len(prodnum_sum_sort)): # 제품 종류 수 만큼 반복
        while n < len(demand_list): # 제품 주문 수 만큼 반복
            if demand_list[order_num][1] == prodnum_sum_sort[i][0]:
            # 주문의 제품 종류가 prodnum_sum의 i번째의 제품 종류와 같을 경우 주문 순서를 마지막으로 이동하고 n에 1을 더함
                temp = demand_list.pop(order_num)
                demand_list.append(temp)
                n += 1
            else: # 주문의 제품 종류가 prodnum_sum의 i번째의 제품 종류와 다를 경우 n에 1을 더하고 다음 주문 번호에 1을 더함
                n += 1
                order_num += 1
        order_num = 0 # 주문 번호를 0으로 초기화
        n = 0 # n을 0으로 초기화

    # demand_list = sorted(demand_list, key=lambda x: int(x[3]))

    return demand_list
#-----------------------------------------------
def demand_sorter3(demand_list): # demandlist를 정렬하는 함수
    prodnum_sum_sort = prodnum_sum.items() # prodnum_sum을 [제품 종류, 총 주문량]들의 배열로 만듬
    prodnum_sum_sort = sorted(prodnum_sum_sort, key = lambda x: x[1], reverse = True)

    order_num = 0 # 주문 번호
    n = 0 # 처리한 주문 번호 개수

    for i in demand_list: # orderlist_sort의 각 주문에 여유날짜 첨가
        i.append(int(i[3])- int(i[2])) # duedate - 생산해야 하는 날짜

    demand_list = sorted(demand_list, key = lambda x: int(x[4])) # 여유날짜가 작은 순으로 정렬

    for i in demand_list: # orderlist_sort의 각 주문에 여유날짜 제거
        del i[4]

    demand_list = sorted(demand_list, key=lambda x: int(x[3]))

    # 주문 순서를 제품의 총 주문량이 많은 순으로 정렬
    for i in range(len(prodnum_sum_sort)):  # 제품 종류 수 만큼 반복
        while n < len(demand_list):  # 제품 주문 수 만큼 반복
            if demand_list[order_num][1] == prodnum_sum_sort[i][0]:
                # 주문의 제품 종류가 prodnum_sum의 i번째의 제품 종류와 같을 경우 주문 순서를 마지막으로 이동하고 n에 1을 더함
                temp = demand_list.pop(order_num)
                demand_list.append(temp)
                n += 1
            else:  # 주문의 제품 종류가 prodnum_sum의 i번째의 제품 종류와 다를 경우 n에 1을 더하고 다음 주문 번호에 1을 더함
                n += 1
                order_num += 1
        order_num = 0  # 주문 번호를 0으로 초기화
        n = 0  # n을 0으로 초기화

    return demand_list

#-----------------------------------------------
def demand_sorter4(demand_list): # demandlist를 정렬하는 함수
    prodnum_sum_sort = prodnum_sum.items() # prodnum_sum을 [제품 종류, 총 주문량]들의 배열로 만듬
    prodnum_sum_sort = sorted(prodnum_sum_sort, key = lambda x: x[1], reverse = True)

    order_num = 0 # 주문 번호
    n = 0 # 처리한 주문 번호 개수

    for i in demand_list: # orderlist_sort의 각 주문에 여유날짜 첨가
        i.append(int(i[3])- int(i[2])) # duedate - 생산해야 하는 날짜

    demand_list = sorted(demand_list, key = lambda x: int(x[4])) # 여유날짜가 작은 순으로 정렬

    for i in demand_list: # orderlist_sort의 각 주문에 여유날짜 제거
        del i[4]

    # 주문 순서를 제품의 총 주문량이 많은 순으로 정렬
    for i in range(len(prodnum_sum_sort)):  # 제품 종류 수 만큼 반복
        while n < len(demand_list):  # 제품 주문 수 만큼 반복
            if demand_list[order_num][1] == prodnum_sum_sort[i][0]:
                # 주문의 제품 종류가 prodnum_sum의 i번째의 제품 종류와 같을 경우 주문 순서를 마지막으로 이동하고 n에 1을 더함
                temp = demand_list.pop(order_num)
                demand_list.append(temp)
                n += 1
            else:  # 주문의 제품 종류가 prodnum_sum의 i번째의 제품 종류와 다를 경우 n에 1을 더하고 다음 주문 번호에 1을 더함
                n += 1
                order_num += 1
        order_num = 0  # 주문 번호를 0으로 초기화
        n = 0  # n을 0으로 초기화

    demand_list = sorted(demand_list, key=lambda x: int(x[3]))

    return demand_list

#-----------------------------------------------
def demand_sorter5(demand_list): # demandlist를 정렬하는 함수

    demand_list = sorted(demand_list, key=lambda x: int(x[3]))

    return demand_list

#-----------------------------------------------
def find_index(data,target): # 기계마다의 cost가 가장 낮은 값의 배열을 만드는 함수
    indexs = []
    lis = data
    while True:
        try:
            indexs.append(lis.index(target) + (indexs[-1] + 1 if len(indexs) != 0 else 0))
            lis = data[indexs[-1] + 1:]
        except:
            break
    return indexs
#-----------------------------------------------
def demand_assign(w): # 가중치를 다르게 기계에 주문들을 배정하는 함수
    demand_num = 0
    machine_num = 0
    machine_cost = [[0, 'X'] for i in range(len(machine_states))] # demand를 넣었을 때의 기계 cost와 setup 여부 보여주는 배열
    n = 0

    for i in range(len(machine_states)):
        if machine_states[i][0] != demand_list[demand_num][1] and machine_states[i][1] >= int(
                demand_list[demand_num][3]):
            n += 1
        else:
            break
    if demand_list[demand_num][-1] == 'o':
        demand_list[demand_num].pop(-1)
    else:
        if n == 18:
            temp = demand_list.pop(demand_num)
            temp.append('o')
            demand_list.append(temp)
            n = 0



    while demand_num < len(demand_list): # 주문들을 다 배정할 때까지 반복
        while machine_num < len(machine_states): # 모든 기계에 비교할 때까지 반복
            if machine_states[machine_num][0] == 'Empty': # 기계에 주문이 없을 경우
                machine_cost[machine_num][0] = w[0] # 기계의 cost는 w[0]
            elif machine_states[machine_num][0] == demand_list[demand_num][1]: # setup이 발생하지 않는 경우
                # 기계의 cost는 w[1] + duedate를 어긴 날짜
                    if prodnum_sum[machine_states[machine_num][0]] > 11:  # 기계의 마지막에 들어간 제품의 주문이 아직 남았다면
                        machine_cost[machine_num][0] = w[1] + max(0, machine_states[machine_num][1] +
                                                                  int(demand_list[demand_num][2]) - int(demand_list[demand_num][3]))
                    else:
                        machine_cost[machine_num][0] = -10 + max(0,machine_states[machine_num][1] +
                                                            int(demand_list[demand_num][2]) - int(demand_list[demand_num][3]))
            elif machine_states[machine_num][0] != demand_list[demand_num][1]: # setup이 발생하는 경우
                if prodnum_sum[machine_states[machine_num][0]] > 10: # 기계의 마지막에 들어간 제품의 주문이 아직 남았다면
                    # 기계의 cost는 w[2] + duedate를 어긴 날짜
                    machine_cost[machine_num][0] = w[2] + max(0,machine_states[machine_num][1] + 2 +
                                                          int(demand_list[demand_num][2]) - int(demand_list[demand_num][3]))
                    machine_cost[machine_num][1] = 'O' #setup 발생 표시
                else: # 기계의 마지막에 들어간 제품의 주문이 남아있지 않다면
                    # 기계의 cost는 w[3] + duedate를 어긴 날짜
                    if machine_states[machine_num][1] + 4 <= int(demand_list[demand_num][3]):
                        machine_cost[machine_num][0] = w[3] + max(0, machine_states[machine_num][1] + 2 +
                                                              int(demand_list[demand_num][2]) - int(demand_list[demand_num][3]))
                        machine_cost[machine_num][1] = 'O' # setup 발생 표시
                    else:
                        machine_cost[machine_num][0] = 50
                        machine_cost[machine_num][1] = 'O'  # setup 발생 표시

            machine_num += 1 # 다음 기계 비교

            if machine_num == len(machine_states): # 모든 기계의 cost를 계산 했다면
                min_indexs = find_index(machine_cost, min(machine_cost)) # 가장 작은 cost의 index들
                min_cost = [] # 가장 작은 cost의 index와 cost와 setup 여부
                for i in min_indexs: # min_cost에 정보 넣기
                    min_cost.append([i,machine_cost[i][0],machine_cost[i][1]])
                for i in range(len(min_cost)): # 가장 작은 cost들 중에 setup이 일어나지 않는 기계 찾기
                    if 'X' in min_cost[i]: # 가장 작은 cost들 중에 setup이 일어나지 않는 기계가 있다면
                        machine_num = min_cost[i][0]
                        break
                    else: # 가장 작은 cost들 중에 setup이 일어나지 않는 기계가 없다면
                        machine_num = min_cost[i][0]

                if machine_cost[machine_num][1] == 'X': # demand를 setup이 일어나지 않는 기계에 배정
                    demand_list[demand_num].insert(1, machine_num)
                    demand_list[demand_num].insert(4, machine_states[machine_num][1])

                    machine_states[machine_num][0] = demand_list[demand_num][2]
                    machine_states[machine_num][1] += int(demand_list[demand_num][3])

                    demand_list[demand_num].insert(5, machine_states[machine_num][1])
                    demand_list[demand_num].append('X')
                    demand_list[demand_num].append(min(int(demand_list[demand_num][3]),
                                                   max(0,machine_states[machine_num][1] - int(demand_list[demand_num][6]))))
                else: # demand를 setup이 일어나는 기계에 배정
                    demand_list[demand_num].insert(1, machine_num)
                    demand_list[demand_num].insert(4, machine_states[machine_num][1] + 2)

                    machine_states[machine_num][0] = demand_list[demand_num][2]
                    machine_states[machine_num][1] += int(demand_list[demand_num][3]) + 2

                    demand_list[demand_num].insert(5, machine_states[machine_num][1])
                    demand_list[demand_num].append('O')
                    demand_list[demand_num].append(min(int(demand_list[demand_num][3]),
                                                   max(0, machine_states[machine_num][1] - int(demand_list[demand_num][6]))))
                prodnum_sum[demand_list[demand_num][2]] -= int(demand_list[demand_num][3])
                # 제품들의 총 주문량에서 배정한 제품의 주문량 제거
                machine_cost = [[0,'X'] for i in range(len(machine_states))] # machine_cost 초기화
                machine_num = 0 # machine_num 초기화
                break
        demand_num += 1 # 다음 demand를 배정

    violation_time = 0 # 총 duedate를 어긴 날짜
    setup = 0 # setup이 일어난 횟수

    for i in range(len(demand_list)): # violation_time와 setup 계산
        violation_time += demand_list[i][8]
        if demand_list[i][7] == 'O':
            setup += 1

    return demand_list, violation_time, setup # 배정된 demand_list, violation_time, setup 반환
#-----------------------------------------------
demandlist_num = 1
all_demand_cost = []
sum_cost = 0
n = 1

while demandlist_num < 11:
    demand_list = demandlist_loader() # demandlist를 불러옴
    machine_states = machine_states_make() # 기계 상태를 보여주는 변수를 생성
    prodnum_sum = prodnum_sum_make() # 제품 종류를 키 값으로 하고 제품종류마다의 총 주문량을 보여주는 변수를 생성
    if n == 1:
        demand_list = demand_sorter1(demand_list) # demandlist를 정렬
    elif n == 2:
        demand_list = demand_sorter2(demand_list)  # demandlist를 정렬
    elif n == 3:
        demand_list = demand_sorter3(demand_list)  # demandlist를 정렬
    elif n == 4:
        demand_list = demand_sorter4(demand_list)  # demandlist를 정렬
    elif n == 5:
        demand_list = demand_sorter5(demand_list)  # demandlist를 정렬
    #-----------------------------------------------
    all_cost = [] # 각각 다른 가중치에 따른 전체 cost
    weight = [] # 가중치들의 배열

    for w in range(3): # 첫번째 가중치 :0,1,2
        for e in range(-2,1): # 두번째 가중치 :-2,-1,0
            for i in range(3,7): # 세번째 가중치 :3,4,5,6
                for g in range(1,5): # 네번째 가중치 :1,2,3,4
                    weight.append([w,e,i,g]) # 모든 경우의 가중치들을 weight에 저장

    while n < 6:
        for w in weight: # 모든 경우의 가중치 개수만큼 반복
            demand_list, violation_time, setup = demand_assign(w) # 각 가중치 마다의 배정된 demand_list, violation_time, setup 반환
            all_cost.append(violation_time + setup * 2) # all_cost에 이번 가중치의 전체 cost 저장
            demand_list = demandlist_loader() # demand_list 초기화
            machine_states = machine_states_make() # machine_states 초기화
            prodnum_sum = prodnum_sum_make() # prodnum_sum 초기화
            if n == 1:
                demand_list = demand_sorter1(demand_list)  # demandlist를 정렬
            elif n == 2:
                demand_list = demand_sorter2(demand_list)  # demandlist를 정렬
            elif n == 3:
                demand_list = demand_sorter3(demand_list)  # demandlist를 정렬
            elif n == 4:
                demand_list = demand_sorter4(demand_list)  # demandlist를 정렬
            elif n == 5:
                demand_list = demand_sorter5(demand_list)  # demandlist를 정렬
        n += 1

    n = 1

    min_allcost_index = all_cost.index(min(all_cost)) % len(weight)
    demand_list = demandlist_loader()  # demand_list 초기화
    if all_cost.index(min(all_cost)) // len(weight) == 0:
        demand_list = demand_sorter1(demand_list)  # demandlist를 정렬
    elif all_cost.index(min(all_cost)) // len(weight) == 1:
        demand_list = demand_sorter2(demand_list)  # demandlist를 정렬
    elif all_cost.index(min(all_cost)) // len(weight) == 2:
        demand_list = demand_sorter3(demand_list)  # demandlist를 정렬
    elif all_cost.index(min(all_cost)) // len(weight) == 3:
        demand_list = demand_sorter4(demand_list)  # demandlist를 정렬
    elif all_cost.index(min(all_cost)) // len(weight) == 4:
        demand_list = demand_sorter5(demand_list)  # demandlist를 정렬
    demand_list, violation_time, setup = demand_assign(weight[min_allcost_index]) # 전체 cost가 가장 낮은 가중치로 demand_list 배열
    demand_list.insert(0,[18]) # demand_list에 기계 개수 추가

    #---------------------------------------------
    # for i in demand_list: # 배정된 demand_list 확인
    #     print(i)

    print('violation_time :',violation_time) # violation_time 확인
    print('setup :',setup) # setup 확인
    all_demand_cost.append(violation_time + setup * 2)
    print('cost :', violation_time + setup * 2) # 전체 코스트 확인
    # 배정된 demand_list로 csv파일 만들기

    with open(path + f'\\{demandlist_num}.csv', 'w', newline = '') as file:
        wr = csv.writer(file, delimiter = ',')
        for x in range(len(demand_list)):
            wr.writerow(demand_list[x])
        file.close()

    demandlist_num += 1

for i in range(len(all_demand_cost)):
    sum_cost += all_demand_cost[i]

print('avg_cost :',sum_cost/10)