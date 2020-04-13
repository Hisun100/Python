#****************单条件过滤
#异常值过滤
train_data=train_data[train_data["可用额度比值"]<=1]
train_data=train_data[train_data["年龄"]>0]
train_data=train_data[train_data["逾期30-59天笔数"]<80]
train_data=train_data[train_data["固定资产贷款量"]<50]


#****************多条件过滤
#领券消费的记录数
offline_coupon_1 = dfoff[(dfoff['Date_received']!=0)& (dfoff['Date']!=0)].shape[0]

