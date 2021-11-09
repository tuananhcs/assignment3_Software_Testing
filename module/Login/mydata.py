import random
def gen_email():
    letters = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n",
               "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z", '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    nemail = ''
    for _ in range(12):
        nemail += random.choice(letters)

    return nemail+"@gmail.com"

###############################        EXAMPLE        ###############################
###############################  TEST WITH NEW DATA   ###############################
###############################CHANGE ALL FIELDS BELOW###############################

#login account
#web ACCOUNT
username="huy.lam2214@hcmut.edu.vn"
password="Lamhuy213"
#fb ACCOUNT
fbname="ctvlamson@gmail.com"
fbpass="lamson213"
#register fields
fname = "Nam"
lname = "Tran"
used_email = "ntxm5220@gmail.com"
valid_email = gen_email()  # mail moi chua dk
invalid_email = "ntxmai.gmail.com"
valid_pw = "XM123456"
nonUpper_pw = "xm123456"
nonNumber_pw = "xuanmai"
lessMinLength_pw = "Xm123"
moreMaxLength_pw = "XM123456789abcdefgh0XM123456789abcdefgh0XM123456789abcdefgh0"