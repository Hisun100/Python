month_sum_coupon_consume：
index  User_id   all_consume_count
0
1
2

#统计每个月的消费次数：month_sum_ordinary_consume
month_sum_ordinary_consume = dfoff.groupby('month_consume', as_index=False)['User_id'].count()
colNameDict2={'User_id':'all_consume_count'}
month_sum_ordinary_consume.rename(columns=colNameDict2,inplace=True)
#统计每个月的优惠券消费次数：month_sum_coupon_consume
month_sum_coupon_consume = dfoff[dfoff['consumeType']==1].groupby('month_consume', as_index=False)['User_id'].count()
#将month_sum_ordinary_consume和month_sum_coupon_consume,按month_consume字段进行左连接
month_sum_consume = pd.merge(month_sum_coupon_consume, month_sum_ordinary_consume,on='month_consume')
#绘制柱状堆叠图--每月优惠券消费次数占总消费次数的比重
ax22=month_sum_consume.plot(kind='bar',stacked=True)
ax22.set_title('2016年上半年每月优惠券消费次数占比变化')
ax22.legend(['优惠券消费次数','总消费次数'])
