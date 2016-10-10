# coding=utf-8

from sqlalchemy import Column, String, ForeignKey, create_engine,or_,and_
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
import pymysql

# 创建对象的基类:
Base = declarative_base()

class Users(Base):
	# 创建表名
	__tablename__ = 'Users'

	# 表的结构
	id = Column(String(20), primary_key=True)
	name = Column(String(20))

if __name__ == '__main__':
	# 初始化数据库连接:
	engine = create_engine('mysql+pymysql://root:x@localhost/test',echo=True)
	# 初始化数据库
	Base.metadata.create_all(engine)
	# 创建DBSession类型:
	DBSession = sessionmaker(bind=engine)

	session = DBSession()
	# 增加
	new_user1 = Users(id='5', name='Bob')
	session.add(new_user1)

	'''
	session.execute(
    Dingdan.__table__.insert(),
    [{'id': '123123','paid_amount': '155','items':'aaa','user_id':6},
    {'id': '124124','paid_amount': '159','items':'bbb','user_id':6}]
    )
    '''

	# 修改
	
	#session.query(Users).filter(Users.id==6).update({Users.name:'James'})
	
	# 删除
	
	#session.query(Dingdan).filter(Dingdan.user_id==6).delete()
	
	# Drop_all
	# Base.metadata.drop_all(engine)

	# Drop


	session.commit()

	session.close()







