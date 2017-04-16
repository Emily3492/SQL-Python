SQL数据：
#总发帖数据
select a.POST_TYPE ,a.POST_CONTENT,a.CREATED_ON,c.APARTMENT_NAME,d.TYPE_SID,d.TYPE_NAME
from HOME_NEIGHBOR_POST a
LEFT join HOME_OWNER b
on b.OWNER_SID = a.CREATEDBY
left join HOME_APARTMENT c on a.APARTMENT_SID = c.APARTMENT_SID
left join HOME_NEIGHBOR_POST_TYPE d on a.POST_TYPE = d.TYPE_SID
where b.FAMILY_NAME not in('悦悦')--剔除，外部人员不能起昵称为悦悦
and b.OWNER_TYPE=1--类型为业主

一行：select a.POST_TYPE ,a.POST_CONTENT,a.CREATED_ON,c.APARTMENT_NAME,d.TYPE_SID,d.TYPE_NAME from HOME_NEIGHBOR_POST a LEFT join HOME_OWNER b on b.OWNER_SID = a.CREATEDBY left join HOME_APARTMENT c on a.APARTMENT_SID = c.APARTMENT_SID left join HOME_NEIGHBOR_POST_TYPE d on a.POST_TYPE = d.TYPE_SID where b.FAMILY_NAME not in('悦悦')and b.OWNER_TYPE=1

#点赞数据





#总回复数据
select t1.*,c.APARTMENT_NAME  from
(
select a.COMMENT_SID ,a.POST_SID,a.COMMENT_CONTENT,a.CREATED_ON,b.APARTMENT_SID,b.POST_TYPE,d.TYPE_NAME
from HOME_NEIGHBOR_COMMENT a
left join HOME_NEIGHBOR_POST b on  a.POST_SID = b.POST_SID
left join HOME_NEIGHBOR_POST_TYPE d on b.POST_TYPE = d.TYPE_SID
)t1
left join  HOME_APARTMENT c on t1.APARTMENT_SID = c.APARTMENT_SID

一行：select t1.*,c.APARTMENT_NAME  from(select a.COMMENT_SID ,a.POST_SID,a.COMMENT_CONTENT,a.CREATED_ON,b.APARTMENT_SID,b.POST_TYPE,d.TYPE_NAME from HOME_NEIGHBOR_COMMENT a left join HOME_NEIGHBOR_POST b on  a.POST_SID = b.POST_SID left join HOME_NEIGHBOR_POST_TYPE d on b.POST_TYPE = d.TYPE_SID)t1 left join  HOME_APARTMENT c on t1.APARTMENT_SID = c.APARTMENT_SID

#