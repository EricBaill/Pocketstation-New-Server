# **⼝袋加油站·⼆期(经销商)·API**

## **Client Apis**

### **经销商信息**

+ 获取经销商列表

  | Method | Url            |
  | ------ | -------------- |
  | GET    | /api/v2/admin/ |

    返回说明

  ~~~
   // 200
   [{
       'id':,		//经销商id
       'openid':,	//经销商openID
       'name':,	//经销商名称
       'email':,	//经销商邮箱
       'avatar':,	//经销商头像
       'create_at':,	//添加经销商时间
       'bu': {
           'name':,	//部门名称
           'id':,		//部门id
       }
   }]
  ~~~


+  根据姓名搜索员工信息

  | Method | Url                   |
  | ------ | --------------------- |
  | POST   | /api/v2/staff/search/ |

    返回说明

  ~~~
  // 200
  [{
    'id',    		//员工id
    'name':,   	//员工姓名
    'email':,   	//员工邮箱
    'avatar':,  	//员工头像
    'tel':,   	//员工手机号
    'passwd':,    //员工密码
    'create_at':,   //员工账号创建时间
    'pos':{
      'id':,		//员工职位id
      'name':,	//员工职位名称
    'bu':{
      'id':,		//员工部门id
      'name':, 	//员工部门名称
    	}
    }
  }]
  
  ~~~


### **课程培训**

+ 根据课程培训id获取课程培训信息

  | Method | Url                    |
  | ------ | ---------------------- |
  | GET    | /api/v2/trainings/<id> |

  返回说明

  ~~~
  // 200
  {
      'id': ,		//培训id
      'title': ,	//培训标题
      'cover_img': ,//培训图片
      'lecturer':,	//培训讲师
      'content': ,	//培训内容
      'desc':,		//培训描述
  }
  ~~~


### 经销商资源

+ 获取资源目录列表

  | Method | Url           |
  | ------ | ------------- |
  | GET    | /api/v2/hier/ |

  返回说明

  ~~~
  // 200
  
  [{
      'id': ,  //资源目录id
  	'name':, //资源目录名称
  }]
  ~~~



+ 根据资源id获取资源信息

  | Method | Url                       |
  | ------ | ------------------------- |
  | GET    | /api/v2/resources/<resId> |

  返回说明

  ~~~
  // 200
  
  [{
      'id':,		//资源id
      'name':,	//资源名称
      'content':,	//资源内容
      'type':,	//资源类型
      'hier':,	//资源层级id
  }]
  ~~~




### 轮播信息

+ 获取轮播图

  | Method | Url                     |
  | ------ | ----------------------- |
  | GET    | /api/v2/carousel/dealer |

  返回说明

  ~~~
  // 200
  
  [{
      'id':,		//轮播id
      'cover_img':, // 轮播图片
      'content':,	//轮播内容
  }]
  ~~~



### 经销商互动

+ 添加问题

  | Method | Url                           |
  | ------ | ----------------------------- |
  | POST   | /api/v2/QA/<user_id>/actions/ |

  返回说明

  ~~~
  // 200
  
  {
      'id':,				//经销商id
      'ques_id':,			//问题id
      'avatar':,			//经销商头像
      'name':,			//经销商名称
      'ques':,			//添加的问题
      'create_at': ,		//添加问题时间
      'reply':,			//回复次数
  }
  ~~~


+ 添加答案

  | Method | Url                                          |
  | ------ | -------------------------------------------- |
  | POST   | /api/v2/QA/action/<ques_id>/replys/<user_id> |

  返回说明

  ~~~
  // 200
  
  {
      'id':,		//答案id
      'ques_id':,	//问题id
      'avatar':,	//经销商头像
      'name':,	//经销商名称
      'create_at': ,		//添加答案时间
      'reply':,			//答案
  }
  ~~~


### 经销商心得

+ 添加心得

  | Method | Url                                                   |
  | ------ | ----------------------------------------------------- |
  | POST   | /api/v2/trainings/<course_id>/gains/user_id/<user_id> |

  返回说明

  ~~~
  // 200
  
  [{
      'dealer': {
          'name': ,		//经销商姓名
          'avatar':,		//经销商头像
      },
      'id':,				//心得id
      'title': ,			//心得标题
      'content':,			//心得内容
      'type': ,			//心得类型
      'create_at':,		//添加心得时间
  }]
  ~~~


+ 根据培训课程id获取心得记录

  | Method | Url                                 |
  | ------ | ----------------------------------- |
  | GET    | /api/v2/trainings/<course_id>/gains |

  返回说明

  ~~~
  // 200
  
  [{
      'dealer': {
          'name': ,		//经销商姓名
          'avatar':,		//经销商头像
      },
      'id':,				//心得id
      'title': ,			//心得标题
      'content':,			//心得内容
      'type': ,			//心得类型
      'create_at':,		//添加心得时间
  }]
  ~~~


+ 根据培训课程id获取精华心得记录

  | Method | Url                                         |
  | ------ | ------------------------------------------- |
  | GET    | /api/v2/trainings/<course_id>/gains/essence |

  返回说明

  ~~~
  // 200
  
  [{
      'dealer': {
          'name': ,		//经销商姓名
          'avatar':,		//经销商头像
      },
      'id':,				//心得id
      'title': ,			//心得标题
      'content':,			//心得内容
      'type': ,			//心得类型
      'create_at':,		//添加心得时间
  }]
  ~~~


### FAQ

+ 获取FAQ列表

  | Method | Url             |
  | ------ | --------------- |
  | GET    | /api/v2/QA/FAQ/ |

  返回说明

  ~~~
  // 200
  
  [{
      'id':,		//FAQid 
      'title':,	//FAQ问题
      'answer':,	//FAQ答案
  }]
  ~~~


+ 根据FAQid获取FAQ信息

  | Method | Url                 |
  | ------ | ------------------- |
  | GET    | /api/v2/QA/FAQ/<id> |

  返回说明

  ~~~
  // 200
  
  {
      'id':,		//FAQid 
      'title':,	//FAQ问题
      'answer':,	//FAQ答案
  }
  ~~~





## Management Apis


### 经销商信息

+ 添加经销商信息

  | Method | Url            |
  | ------ | -------------- |
  | POST   | /api/v2/admin/ |

    返回说明

  ~~~
   // 200
   {
       'id':,		//经销商id
       'name':,	//经销商名称
       'email':,	//经销商邮箱
       'avatar':,	//经销商头像
       'create_at':,	//添加经销商时间
       'bu': {
           'name':,	//部门名称
           'id':,		//部门id
       }
   }
  ~~~


+ 修改经销商信息

  | Method | Url                      |
  | ------ | ------------------------ |
  | PUT    | /api/v2/admin/<admin_id> |

    返回说明

  ~~~
   // 200
   {
       'id':,		//经销商id
       'name':,	//经销商名称
       'email':,	//经销商邮箱
       'avatar':,	//经销商头像
       'create_at':,	//添加经销商时间
       'bu': {
           'name':,	//部门名称
           'id':,		//部门id
       }
   }
  ~~~


+ 删除经销商信息

  | Method | Url                      |
  | ------ | ------------------------ |
  | DELETE | /api/v2/admin/<admin_id> |

    返回说明

    ~~~
  // 200
  {
  	'msg':'删除成功！'
  }
    ~~~



### 经销商资源

+ 获取资源列表

  | Method | Url                    |
  | ------ | ---------------------- |
  | GET    | /api/v2/resources/all/ |

  返回说明

  ~~~
  // 200
  
  [{
      'id':,		//资源id
      'name': ,	//资源名称
      'content':,	//资源内容
      'type': ,	//资源类型
      'hier': {
          'id':,	//父级资源id
          'name':,	//父级资源名称
      }
  }]
  ~~~



+ 添加资源

  | Method | Url           |
  | ------ | ------------- |
  | POST   | /api/v2/hier/ |

  返回说明

  ~~~
  // 200
  
  {
      'id':,		//资源id
      'name':,	//资源名称
      'content':,	//资源内容
      'type':,	//资源类型
      'hier':,	//资源层级id
  }
  ~~~


+ 资源信息修改

  | Method | Url                    |
  | ------ | ---------------------- |
  | PUT    | /api/v2/resources/<id> |

  返回说明

  ~~~
  // 200
  
  {
      'id':,		//资源id
      'name': ,	//资源名称
      'content':,	//资源内容
      'type': ,	//资源类型
      'hier': {
          'id':,	//父级资源id
          'name':,	//父级资源名称
      }
  }
  ~~~



+ 删除资源信息

  | Method | Url                       |
  | ------ | ------------------------- |
  | DELETE | /api/v2/resources/<resId> |

  返回说明

  ~~~
  // 200
  {
  	'msg':'删除成功！'
  }
  ~~~







### **课程培训**

+ 获取课程培训列表

  | Method | Url                |
  | ------ | ------------------ |
  | GET    | /api/v2/trainings/ |

  返回说明

  ~~~
  // 200
  
  [{
      'id': ,		//培训id
      'title': ,	//培训标题
      'cover_img': ,//培训图片
      'lecturer':,	//培训讲师
      'content': ,	//培训内容
      'desc':,		//培训描述
  }]
  ~~~


+ 添加课程培训信息

  | Method | Url                |
  | ------ | ------------------ |
  | POST   | /api/v2/trainings/ |

  返回说明

  ~~~
  // 200
  {
      'id': ,		//培训id
      'title': ,	//培训标题
      'cover_img': ,//培训图片
      'lecturer':,	//培训讲师
      'content': ,	//培训内容
      'desc':,		//培训描述
  }
  ~~~


+ 修改课程培训信息

  | Method | Url                    |
  | ------ | ---------------------- |
  | PUT    | /api/v2/trainings/<id> |

  返回说明

  ~~~
  // 200
  {
      'id': ,		//培训id
      'title': ,	//培训标题
      'cover_img': ,//培训图片
      'lecturer':,	//培训讲师
      'content': ,	//培训内容
      'desc':,		//培训描述
  }
  ~~~


+ 删除课程培训信息

  | Method | Url                    |
  | ------ | ---------------------- |
  | DELETE | /api/v2/trainings/<id> |

  返回说明

  ~~~
  // 200
  {
  	'msg':'删除成功！'
  }
  ~~~


+ 设置是否经销商可见课程

  | Method | Url                               |
  | ------ | --------------------------------- |
  | POST   | /api/v2/is_look/<lsn_id>/lessons/ |

  返回说明

  ~~~
  //200
  
  {
  	'msg': '设置成功！'
  }
  ~~~


+ 设置推荐课程

  | Method | Url                 |
  | ------ | ------------------- |
  | POST   | /api/v2/lesson/<id> |

  返回说明

  ~~~
  //200
  
  {
  	'msg': '设置成功！'
  }
  ~~~




### 轮播信息

+ 添加轮播图

  | Method | Url                     |
  | ------ | ----------------------- |
  | POST   | /api/v2/carousel/dealer |

  返回说明

  ~~~
  // 200
  
  {
      'id':,		//轮播id
      'cover_img':, // 轮播图片
      'content':,	//轮播内容
  }
  ~~~

+ 修改轮播信息

  | Method | Url                               |
  | ------ | --------------------------------- |
  | PUT    | /api/v2/carousel/dealer/<news_id> |

  返回说明

  ~~~
  // 200
  
  {
      'id':,		//轮播id
      'cover_img':, // 轮播图片
      'content':,	//轮播内容
  }
  ~~~


+ 删除轮播信息

  | Method | Url                               |
  | ------ | --------------------------------- |
  | DELETE | /api/v2/carousel/dealer/<news_id> |

  返回说明

  ~~~
  // 200
  
  {
      'msg':'删除成功！'
  }
  ~~~


+ 获取单个轮播信息

  | Method | Url                                    |
  | ------ | -------------------------------------- |
  | GET    | /api/v2/carousel/dealer/news/<news_id> |

  返回说明

  ~~~~
  // 200
  
  {
      'id':,		//轮播id
      'cover_img':, // 轮播图片
      'content':,	//轮播内容
  }
  ~~~~



### 经销商互动

+ 获取某个问题的所有答案

  | Method | Url                                |
  | ------ | ---------------------------------- |
  | GET    | /api/v2/QA/action/<ques_id>/replys |

  返回说明

  ~~~
  // 200
  
  [{
      'id':,		//经销商id
      'avatar':,	//经销商头像
      'name':,	//经销商名称
      'reply':,	//答案
      'reply_id': ,//问题id
      'create_at': ,//添加问题时间
  }]
  ~~~


+ 获取问题列表

  | Method | Url                |
  | ------ | ------------------ |
  | GET    | /api/v2/QA/actions |

  返回说明

  ~~~
  // 200
  
  [{
      'id':,				//经销商id
      'ques_id':,			//问题id
      'avatar':,			//经销商头像
      'name':,			//经销商名称
      'ques':,			//添加的问题
      'create_at': ,		//添加问题时间
      'reply':,			//回复次数
  }]
  ~~~


+ 根据问题id获取问题信息

  | Method | Url                    |
  | ------ | ---------------------- |
  | GET    | /api/v2/QA/action/<id> |

  返回说明

  ~~~
  // 200
  
  {
      'id':,		//问题id
      'ques':,	//问题内容
  }
  ~~~


+ 删除问题

  | Method | Url                    |
  | ------ | ---------------------- |
  | DELETE | /api/v2/QA/action/<id> |

  返回说明

  ~~~
  // 200
  
  {
  	'msg':'删除成功！'
  }
  ~~~


### 经销商心得

+ 修改经销商心得

  | Method | Url                                                   |
  | ------ | ----------------------------------------------------- |
  | PUT    | /api/v2/trainings/<course_id>/gains/user_id/<user_id> |

  返回说明

  ~~~
  // 200
  
  {
      'dealer': {
          'name': ,		//经销商姓名
          'avatar':,		//经销商头像
      },
      'id':,				//心得id
      'title': ,			//心得标题
      'content':,			//心得内容
      'type': ,			//心得类型
      'create_at':,		//添加心得时间
  }
  ~~~


### FAQ

+ 添加FAQ

  | Method | Url             |
  | ------ | --------------- |
  | POST   | /api/v2/QA/FAQ/ |

  返回说明

  ~~~
  // 200
  
  {
      'id':,		//FAQid 
      'title':,	//FAQ问题
      'answer':,	//FAQ答案
  }
  ~~~


+ 修改FAQ

  | Method | Url                 |
  | ------ | ------------------- |
  | PUT    | /api/v2/QA/FAQ/<id> |

  返回说明

  ~~~
  // 200
  
  {
      'id':,		//FAQid 
      'title':,	//FAQ问题
      'answer':,	//FAQ答案
  }
  ~~~


+ 删除FAQ

  | Method | Url                 |
  | ------ | ------------------- |
  | DELETE | /api/v2/QA/FAQ/<id> |

  返回说明

  ~~~
  // 200
  
  {
  	'msg':'删除成功！'
  }
  ~~~
