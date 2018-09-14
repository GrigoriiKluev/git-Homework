def my_round(number, ndigits):
    int_ndigits = int(ndigits)
    degree = pow(10,int(ndigits))
    mul =  number*degree
    res = int(mul)
    ost = mul-res
    # print(number,mul,res,ost)
    if not (abs(ost) < 0.5):
        if res>0: res+=1
        else: res-=1
    return res/degree

print(my_round(2.4342,2))
#второе задание
def lucky_ticket(ticket_number):
    tn_list=str(ticket_number)
    if len(tn_list) != 6: return False
    first=0
    last=0
    for i in range(3):
        first+=int(tn_list[i])
        last+=int(tn_list[-i-1])
    return first==last


print(lucky_ticket(321455))

