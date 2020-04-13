#--------融合年龄、性别和婚姻状态三个字段，创造新的字段Person
def age_gender_marital(passenger):
    #passenger:可看做一个维度列表(年龄、性别和婚姻状况)
    Age,Gender,Marital_Status = passenger
    
    #Case1:若年龄在0-17段，则标记为孩子
    if Age=="0-17":
        return "孩子"
    #Case2:若年龄在18-25或26-35段，则依次按照性别和婚姻状态，被标记为未婚年轻男、已婚年轻男、未婚年轻女和已婚年轻女
    elif Age =='18-25' or Age =='26-35':
        if Gender=='M':
           if Marital_Status=='0':
                   return "未婚年轻男"
           else: return "已婚年轻男"
        elif Gender=='F':
            if Marital_Status=='0':
                return "未婚年轻女"
            else: return "已婚年轻女"
    #Case3:若年龄在36-45或46-50段，则依次按照性别和婚姻状态，被标记为未婚中年男、已婚中年男、未婚中年女和已婚中年女
    elif Age =='36-45' or Age =='46-50':
        if Gender=='M':
            if Marital_Status=='0':
               return "未婚中年男"
            else: return "已婚中年男"
        elif Gender=='F':
            if Marital_Status=='0':
               return "未婚中年女"
            else: return "已婚中年女"
    #Case4:若年龄在51-55或55+段，则标记为老人
    else:
        return "老人"
#新增Person新字段
blackFriday_df["Person"] = blackFriday_df[["Age","Gender","Marital_Status"]].apply(age_gender_marital,axis=1)
