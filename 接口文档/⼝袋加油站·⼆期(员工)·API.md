# **⼝袋加油站·⼆期(员工)·API**

## **Client Apis**

### **员工信息**

+ 获取员工列表

  | Method | Url             |
  | ------ | --------------- |
  | GET    | /api/v2/staffs/ |

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


### **课程信息**

+ 根据课程id获取课程信息

  | Method | Url                 |
  | ------ | ------------------- |
  | GET    | /api/v2/lesson/<id> |

  返回说明

  ~~~
  // 200
  {
      "be_thumbs":,	//课程被点赞数
      "img_src": ,	//课程图片
  	"lecturer": {
          'name': ,	//讲师姓名
          'avatar': ,	//讲师头像
          'lessons': ,	//该讲师对应的课程数
      'pos': {
          'id': ,	//职位id
          'name': ,	//职位名称
          'bu': {
              'name': ,	//部门名称
              'id': ,		//部门id
          	},
      		}
  		},
      'oprt': {
          'id': ,		//术式id
          'name': ,	//术式名称
          'cls': {
              'id': ,	//课程分类id
              'name': ,	//课程分类名称
          }
  		},
      'contents': ,	//课程内容
      'id': ,			//课程id
      'name':,		//课程名称
      'be_collected': , //课程被收藏数
      'type': ,		//课程类型
      'tools': {
          'name':,	//工具名称
          'type': ,	//工具类型
          'id': ,		//工具id
      	'content':,	//工具内容
      },
      'passed': 'false', //是否通过
      'create_at': ,		//课程添加时间
      'lesson_permissions': {
          'bu': {
              'name': ,	//权限部门名称
              'id': ,		//权限部门id
  },
  	"need_manager": ,	//是否需要管理
  	'id': ,				//权限id
  },
  }
  ~~~

+ 根据员工id获取课程信息

  | Method | Url                                  |
  | ------ | ------------------------------------ |
  | GET    | /api/v2/recommend/<user_id>/lessons/ |

  返回说明

  ~~~
  // 200
  {
      "be_thumbs":,	//课程被点赞数
      "img_src": ,	//课程图片
  	"lecturer": {
          'name': ,	//讲师姓名
          'avatar': ,	//讲师头像
          'lessons': ,	//该讲师对应的课程数
      'pos': {
          'id': ,	//职位id
          'name': ,	//职位名称
          'bu': {
              'name': ,	//部门名称
              'id': ,		//部门id
          	},
      		}
  		},
      'oprt': {
          'id': ,		//术式id
          'name': ,	//术式名称
          'cls': {
              'id': ,	//课程分类id
              'name': ,	//课程分类名称
          }
  		},
      'contents': ,	//课程内容
      'id': ,			//课程id
      'name':,		//课程名称
      'be_collected': , //课程被收藏数
      'type': ,		//课程类型
      'passed': 'false', //是否通过
      'create_at': ,		//课程添加时间
      'lesson_permissions': {
          'bu': {
              'name': ,	//权限部门名称
              'id': ,		//权限部门id
  },
  	"need_manager": ,	//是否需要管理
  	'id': ,				//权限id
  },
  }
  ~~~


+ 根据术式id，openid和用户类型获取课程信息

  | Method | Url                                                          |
  | ------ | ------------------------------------------------------------ |
  | GET    | /api/v2/operations/<subPart_id>/staffs/<openid>/lessons/<types>/ |

  返回说明

  ~~~
  // 200
  {
      "img_src": ,	//课程图片
  	"lecturer": {
          'name': ,	//讲师姓名
          'avatar': ,	//讲师头像
          'lessons': ,	//该讲师对应的课程数
      'pos': {
          'id': ,	//职位id
          'name': ,	//职位名称
          'bu': {
              'name': ,	//部门名称
              'id': ,		//部门id
          	},
      		}
  		},
      'oprt': {
          'id': ,		//术式id
          'name': ,	//术式名称
          'cls': {
              'id': ,	//课程分类id
              'name': ,	//课程分类名称
          }
  		},
      'contents': ,	//课程内容
      'id': ,			//课程id
      'name':,		//课程名称
      'type': ,		//课程类型
      'tools': {
          'name':,	//工具名称
          'type': ,	//工具类型
          'id': ,		//工具id
      	'content':,	//工具内容
      },
      'passed': 'false', //是否通过
      'create_at': ,		//课程添加时间
      'lesson_permissions': {
          'bu': {
              'name': ,	//权限部门名称
              'id': ,		//权限部门id
  },
  	"need_manager": ,	//是否需要管理
  	'id': ,				//权限id
  },
  }
  ~~~


### 课程收藏

+ 添加课程收藏

  | Method | Url                  |
  | ------ | -------------------- |
  | POST   | /api/v2/collections/ |

  返回说明

  ~~~
  // 200
  {
      'id':,		//被收藏的课程id
      'name':,	//被收藏的课程名称
  }
  ~~~




+ 根据用户id获取所收藏的课程信息

  | Method | Url                              |
  | ------ | -------------------------------- |
  | GET    | /api/v2/staffs/<user_id>/lesson/ |

  返回说明

  ~~~
  // 200
  [{
      'id': ,		//课程id
      'name': ,	//课程名称
      'content': ,//课程内容
      'type': ,	//课程类型
      'img_src': ,//课程图片
  }]
  ~~~


+ 取消课程收藏

  | Method | Url                                             |
  | ------ | ----------------------------------------------- |
  | DELETE | /api/v2/staffs/<staff_id>/collections/<lsn_id>/ |

  返回说明

  ~~~
  // 200
  {
  	'msg':'取消收藏成功！'
  }
  ~~~


### 课程评论

+ 添加课程品论

  | Method | Url                  |
  | ------ | -------------------- |
  | POST   | /api/v2/les_comment/ |

  返回说明

  ~~~
  // 200
  {
      'id': ,		//评论id
      'content': ,	//评论内容
      'create_at': ,	//评论时间
      'staff': {
          'name': ,	//员工姓名
          'avatar': , //员工头像
      }
  }
  ~~~


+ 根据课程id获取课程评论

  | Method | Url                                |
  | ------ | ---------------------------------- |
  | GET    | /api/v2/lessons/<lsn_id>/comments/ |

  返回说明

  ~~~
  // 200 
  [{
      'id': ,		//评论id
      'content':, //评论内容
      'create_at':,  //评论时间
      'staff': {
          'id': ,		//员工id
          'name': ,	//员工姓名
          'avatar': ,	//员工头像
          },
      'lsn': {
          'id': ,		//课程id
          'name':,	//课程名称
          'oprt': {
              'id':,	//术式id
              'name':, //术式名称
              'cls': {
                  'id': cls.id,
                  'name': cls.name
              },
          },
      }
  }]
  ~~~

### 术式信息

+ 根据课程分类id获取术式信息

  | Method | Url                                         |
  | ------ | ------------------------------------------- |
  | GET    | /api/v2/lesson_classes/<cls_id>/operations/ |

  返回说明

  ~~~
  // 200
  
  [{
      'id': ,		//术式id
      'name':,	//术式名称
      'img_src':,	//术式图片
      'cls': {
          'id':,	//课程分类id
          'name':, //课程分类名称
       }
  }]
  ~~~


### 课程点赞

+ 添加课程点赞

  | Method | Url             |
  | ------ | --------------- |
  | POST   | /api/v2/thumbs/ |

  返回说明

  ~~~
  // 200
  {
      'id':,		//课程id
      'name': ,   //课程名称
  }
  ~~~


+ 根据员工id获取点赞的课程数

  | Method | Url                             |
  | ------ | ------------------------------- |
  | POST   | /api/v2/staffs/<user_id>/thumb/ |

  返回说明

  ~~~
  // 200
  [ ]  //点赞课程数
  ~~~


+ 根据用户id和课程id 取消点赞

  | Method | Url                                          |
  | ------ | -------------------------------------------- |
  | DELETE | /api/v2/staffs/<user_id>/thumbs/<lesson_id>/ |

  返回说明

  ~~~
  // 200
  {
  	'msg':'取消点赞成功！'
  }
  ~~~


### 试题信息

+ 根据课程id获取试题信息

  | Method | Url                        |
  | ------ | -------------------------- |
  | GET    | /api/v2/questions/<lsn_id> |

  返回说明

  ~~~
  // 200
  
  {
      'id':,			//试题id
      'content':,		//问题
      'correct_option': ,		//正确答案
      'other_option': ,		//其他答案
      'lsn': {
          'id': ,		//课程id
          'name':,	//课程名称
          'oprt': {
              'id': ,		//术式id
              'name':,	//术式名称	
              'cls': {
                  'id':,	//课程分类id
                  'name':, //课程分类名称
                  }
          }
      }
  }
  ~~~


### 资讯信息

+ 根据资讯id获取资讯信息

  | Method | Url               |
  | ------ | ----------------- |
  | GET    | /api/v2/news/<id> |

  返回说明

  ~~~
  // 200
  
  {
      'id':,			//资讯信息id
      'name':,		//资讯信息名称
      'img_src':,		//资讯信息图片
      'brief':,		//资讯信息简介
      'content':,		//资讯信息内容
      'top':,			//资讯信息是否置顶
      'create_at':,	//资讯信息创建时间
      'cls':{
          'name': ,	//资讯分类名称
          'id': ,		//资讯分类id
      }
  }
  ~~~


+ 通过资讯名称关键字进行模糊查询

  | Method | Url                  |
  | ------ | -------------------- |
  | POST   | /api/v2/news/search/ |

  返回说明

  ~~~
  // 200
  
  [{
      'id':,			//资讯信息id
      'name':,		//资讯信息名称
      'img_src':,		//资讯信息图片
      'brief':,		//资讯信息简介
      'content':,		//资讯信息内容
      'cls':{
          'name': ,	//资讯分类名称
          'id': ,		//资讯分类id
      }
  }]
  ~~~


+ 根据资讯分类id获取资讯信息

  | Method | Url                        |
  | ------ | -------------------------- |
  | GET    | /api/v2/news/look/<cls_id> |

  返回说明

  ~~~
  // 200
  
  [{
      'id':,			//资讯信息id
      'name':,		//资讯信息名称
      'img_src':,		//资讯信息图片
      'brief':,		//资讯信息简介
      'content':,		//资讯信息内容
      'class_name':,	//资讯分类名称
      'cls':{
          'name': ,	//资讯分类名称
          'id': ,		//资讯分类id
      }
  }]
  ~~~


### 轮播信息

+ 获取轮播图

  | Method | Url                      |
  | ------ | ------------------------ |
  | GET    | /api/v2/carousels/staff/ |

  返回说明

  ~~~
  // 200
  
  [{
      'content':,		//轮播内容
      'img_src':,		//轮播图片
      'name':,		//轮播名称
      'brief':,		//轮播简介
      'id':,			//轮播id
      'create_at':,	//时间
  }]
  ~~~


### 热点信息

+ 获取热点信息

  | Method | Url           |
  | ------ | ------------- |
  | GET    | /api/v2/hots/ |

  返回说明

  ~~~
  // 200
  
  [{
      'content':,		//热点内容
      'img_src':,		//热点图片
      'name':,		//热点名称
      'brief':,		//热点简介
      'id':,			//热点id
      'create_at':,	//时间
  }]
  ~~~


### 工具收藏

+ 添加工具收藏

  | method | Url                      |
  | ------ | ------------------------ |
  | POST   | /api/v2/toolcollections/ |

  返回说明

  ~~~
  // 200 
  
  {
      'id': ,		//工具id
      'name':,	//工具名称
  }
  ~~~


+ 根据用户id获取收藏工具信息

  | Method | Url                            |
  | ------ | ------------------------------ |
  | GET    | /api/v2/staff/<user_id>/tools/ |

  返回说明

  ~~~
  // 200
  
  {
      'id':,		//工具id
      'name':,	//工具名称
      'content':, //工具内容
      'type':,	//工具类型
  }
  ~~~


+ 取消收藏工具

  | Method | Url                                                 |
  | ------ | --------------------------------------------------- |
  | DELETE | /api/v2/staffs/<user_id>/toolcollections/<tool_id>/ |

  返回说明

  ~~~
  // 200
  
  {
  	'msg': '取消收藏成功！'
  }
  ~~~


### 课程点赞

+ 添加课程点赞

  | Method | Url             |
  | ------ | --------------- |
  | POST   | /api/v2/thumbs/ |

  返回说明

  ~~~
  //  200
  
  {
      'id': ,		//课程id
      'name':,	//课程名称
  }
  ~~~


+ 取消课程点赞

  | Method | Url                                          |
  | ------ | -------------------------------------------- |
  | DELETE | /api/v2/staffs/<user_id>/thumbs/<lesson_id>/ |

  返回说明

  ~~~
  // 200
  
  {
  	'msg':'取消点赞成功！'
  }
  ~~~


###感恩记录

+  添加感恩记录

  | Method | Url                 |
  | ------ | ------------------- |
  | POST   | /api/v2/gratitudes/ |

  返回说明

  ~~~
  // 200
  
  {
      "create_at":,		//感恩记录时间
      "id": ,				//感恩记录id
      "staff_from": {
          "name":,		//感恩者姓名
          "avatar": ,		//感恩者头像
      },
      "staff_to": {
          "name":, 		//被感恩者姓名
          "avatar": ,		//被感恩者头像
      },
  }
  ~~~


+ 获取感恩记录

  | Method | Url                 |
  | ------ | ------------------- |
  | GET    | /api/v2/gratitudes/ |

  返回说明

  ~~~
  // 200
  
  [{
      "create_at":,		//感恩记录时间
      "id": ,				//感恩记录id
      "staff_from": {
          "name":,		//感恩者姓名
          "avatar": ,		//感恩者头像
      },
      "staff_to": {
          "name":, 		//被感恩者姓名
          "avatar": ,		//被感恩者头像
      },
  }]
  ~~~



### 登录记录

+ 添加登录记录

  | Method | Url              |
  | ------ | ---------------- |
  | POST   | /api/v2/numbers/ |


### 积分计算

+ 记录积分

  | Method | Url                       |
  | ------ | ------------------------- |
  | GET    | /api/v2/points/<staff_id> |

  返回说明

  ~~~
  // 200
  
  data = {
      'points': ,		//积分数
      'level': ,		//头衔名称
  }
  ~~~




## Management Apis

### **部门信息**

+  获取部门列表

  | Method | Url         |
  | ------ | ----------- |
  | GET    | /api/v2/bu/ |

    返回说明

    ~~~
  //200
  [{
      'id', //部门id
      'name'， //部门名称
  }]
    ~~~


+ 添加部门信息

  | Method | Url         |
  | ------ | ----------- |
  | POST   | /api/v2/bu/ |

    返回说明

    ~~~
  //200
  {
       'id',  //部门id
       'name', // 部门名称
   }
    ~~~


+ 修改部门信息

  | Method | Url         |
  | ------ | ----------- |
  | PUT    | /api/v2/bu/ |

    返回说明

    //200

  ~~~
  {
       'id',  //部门id
       'name', // 部门名称
   }
  ~~~


+ 删除部门信息

  | Method | Url         |
  | ------ | ----------- |
  | DELETE | /api/v2/bu/ |

    返回说明

   ~~~
   //200
  {
  	'msg':'删除成功！'
  }
   ~~~



### 职位信息

+ 根据部门id添加职位信息

  | Method | Url                                |
  | ------ | ---------------------------------- |
  | POST   | /api/departments/<bu_id>/positions |

  返回说明

  ~~~
  // 200
  {
      'id':,			//职位id
      'name':,		//职位名称
      'is_manager':,	
      'bu': {
          'id':,		//部门id
          'name':,	//部门名称
      }
  }
  ~~~


+ 获取职位信息

  | Method | Url          |
  | ------ | ------------ |
  | GET    | /api/v2/pos/ |

  返回说明

  ~~~
  // 200
  [{
      'id':,			//职位id
      'name':,		//职位名称
      'is_manager':,	
      'bu': {
          'id':,		//部门id
          'name':,	//部门名称
      }
  }]
  ~~~


+ 修改职位信息

  | Method | Url              |
  | ------ | ---------------- |
  | PUT    | /api/v2/pos/<id> |

  返回说明

  ~~~
  // 200
  {
      'id':,			//职位id
      'name':,		//职位名称
      'is_manager':,	
      'bu': {
          'id':,		//部门id
          'name':,	//部门名称
      }
  }
  ~~~


+ 删除职位信息

  | Method | Url              |
  | ------ | ---------------- |
  | DELETE | /api/v2/pos/<id> |

  返回说明

  ~~~
   //200
  {
  	'msg':'删除成功！'
  }
  ~~~




### 员工信息

+ 添加员工信息

  | Method | Url             |
  | ------ | --------------- |
  | POST   | /api/v2/staffs/ |

    返回说明

  ~~~
    // 200
  {
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
  }
  ~~~


+ 修改员工信息

  | Method | Url            |
  | ------ | -------------- |
  | PUT    | /api/v2/staff/ |

    返回说明

  ~~~
   // 200
  {
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
  }
  ~~~


+ 删除员工信息

  | Method | Url            |
  | ------ | -------------- |
  | DELETE | /api/v2/staff/ |

    返回说明

    ~~~
  // 200
  {
  	'msg':'删除成功！'
  }
    ~~~



### 职位信息

+ 获取职位列表

  | Method | Url          |
  | ------ | ------------ |
  | GET    | /api/v2/pos/ |

    返回说明

    ~~~
  // 200
  [{
    'id':,		//职位id
    'name':,		//职位名称
    'is_manager':,	//该职位是否是管理者
    'bu':{
      'id':,		//部门id
      'name':,	//部门名称
  	}
  }]
    ~~~


+ 选择某一部门下添加职位信息

  | Method | Url                         |
  | ------ | --------------------------- |
  | POST   | /api/departments//positions |

    返回说明

   ~~~
   // 200
  {
    'id':,		//职位id
    'name':,		//职位名称
    'is_manager':,	//该职位是否是管理者
    'bu':{
      'id':,		//部门id
      'name':,	//部门名称
  	}
  }
   ~~~


+ 修改职位信息

  | Method | Url          |
  | ------ | ------------ |
  | PUT    | /api/v2/pos/ |

    返回说明

  ~~~
    // 200
  {
    'id':,		//职位id
    'name':,		//职位名称
    'is_manager':,	//该职位是否是管理者
    'bu':{
      'id':,		//部门id
      'name':,	//部门名称
  	}
  }
  ~~~


+ 删除职位信息

  | Method | Url          |
  | ------ | ------------ |
  | DELETE | /api/v2/pos/ |

    返回说明

    ~~~
  // 200
  {
  	'msg':'删除成功！'
  }
    ~~~


### **课程分类**

+ 获取课程分类列表

  | Method | Url                     |
  | ------ | ----------------------- |
  | GET    | /api/v2/lesson_classes/ |

    返回说明

  ~~~
    //200
  [{
    'id':,	//课程分类id
     'name':,	//课程分类名称
    'img_src':，	//课程分类图片
  }]
  ~~~


+ 添加课程分类信息

  | Method | Url                     |
  | ------ | ----------------------- |
  | POST   | /api/v2/lesson_classes/ |

    返回说明

  ~~~
    //200
  {
    'id':,	//课程分类id
     'name':,	//课程分类名称
    'img_src':，	//课程分类图片
  }
  ~~~


+ 修改课程分类信息

  | Method | Url              |
  | ------ | ---------------- |
  | PUT    | /api/v2/les_cls/ |

    返回说明

   ~~~
   //200
  {
    'id':,	//课程分类id
     'name':,	//课程分类名称
    'img_src':，	//课程分类图片
  }
   ~~~


+ 删除课程分类信息

  | Method | Url              |
  | ------ | ---------------- |
  | DELETE | /api/v2/les_cls/ |

    返回说明

    ~~~
  // 200
  {
  	'msg':'删除成功！'
  }
    ~~~


### **课程信息**

+ 获取课程列表

  | Method | Url             |
  | ------ | --------------- |
  | GET    | /api/v2/lesson/ |

  返回说明

  ~~~
  // 200
  {
  	'contents': ,	//课程内容
      'id': ,			//课程id
      'name':,		//课程名称
      'be_collected': , //课程被收藏数
      'type': ,		//课程类型
      'recommended':,	//推荐课程
      'is_look':,		//是否经销商可见
      "be_thumbs":,	//课程被点赞数
      "img_src": ,	//课程图片
  	"lecturer": {
          'name': ,	//讲师姓名
          'avatar': ,	//讲师头像
          'lessons': ,	//该讲师对应的课程数
      'pos': {
          'id': ,	//职位id
          'name': ,	//职位名称
  		},
      'oprt': {
          'id': ,		//术式id
          'name': ,	//术式名称
          'cls': {
              'id': ,	//课程分类id
              'name': ,	//课程分类名称
          }
  		},
      'lesson_permissions': {
      	'name':,		//课程名称
          'bu': {
              'name': ,	//权限部门名称
              'id': ,		//权限部门id
  		},
  		},
  	}
  ~~~


+ 添加课程信息

  | Method | Url             |
  | ------ | --------------- |
  | POST   | /api/v2/lesson/ |

  返回说明

  ~~~
  // 200
  {
  'msg':'添加成功！'
  }
  ~~~


+ 修改课程信息

  | Method | Url                 |
  | ------ | ------------------- |
  | PUT    | /api/v2/lesson/<id> |

  返回说明

  ~~~
  // 200
  {
  	'msg':'修改成功！'
  }
  ~~~


+ 删除课程信息

  | Method | Url                 |
  | ------ | ------------------- |
  | DELETE | /api/v2/lesson/<id> |

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



### 课程评论


+ 获取课程评论列表

  | Method | Url                  |
  | ------ | -------------------- |
  | GET    | /api/v2/les_comment/ |

  返回说明

  ~~~
  // 200
  
  [{
      'id':,		//评论id
      'content':,	//评论内容
      'staff':{
          'id':,	//员工id
          'name':, //员工姓名
          'avatar':, //员工头像
          },
       'lsn':{
          'id':,		//课程id
          'name':,	//课程名称
       'oprt': {
          'id':,		//术式id
          'name':,	//术式名称
       'cls': {
       	'id': ,		//课程分类id
          'name':,	//课程分类名称
          },
        },
      }
  }]
  ~~~


+ 根据员工id获取评论信息

  | Method | Url                                |
  | ------ | ---------------------------------- |
  | GET    | /api/v2/staff/<staff_id>/comments/ |

  返回说明

  ~~~
  // 200
  
  [{
      'id':,		//评论id
      'content':,	//评论内容
      'staff':{
          'id':,	//员工id
          'name':, //员工姓名
          'avatar':, //员工头像
          },
       'lsn':{
          'id':,		//课程id
          'name':,	//课程名称
       'oprt': {
          'id':,		//术式id
          'name':,	//术式名称
       'cls': {
       	'id': ,		//课程分类id
          'name':,	//课程分类名称
          },
        },
      }
  }]
  ~~~


+ 删除课程评论信息

  | Method | Url                      |
  | ------ | ------------------------ |
  | DELETE | /api/v2/les_comment/<id> |

  返回说明

  ~~~
  // 200
  {
  	'msg':'删除成功！'
  }
  ~~~



### 术式信息

+ 获取术式列表

  | Method | Url           |
  | ------ | ------------- |
  | GET    | /api/v2/oper/ |

  返回说明

  ~~~
  // 200
  
  [{
      'id': ,		//术式id
      'name':,	//术式名称
      'img_src':,	//术式图片
      'cls': {
          'id':,	//课程分类id
          'name':, //课程分类名称
       }
  }]
  ~~~


+ 添加术式信息

  | Method | Url           |
  | ------ | ------------- |
  | POST   | /api/v2/oper/ |

  返回说明

  ~~~
  // 200
  
  {
      'id': ,		//术式id
      'name':,	//术式名称
      'img_src':,	//术式图片
      'cls': {
          'id':,	//课程分类id
          'name':, //课程分类名称
       }
  }
  ~~~




+ 修改术式信息

  | Method | Url               |
  | ------ | ----------------- |
  | PUT    | /api/v2/oper/<id> |

  返回说明

  ~~~
  // 200
  
  {
      'id': ,		//术式id
      'name':,	//术式名称
      'img_src':,	//术式图片
      'cls': {
          'id':,	//课程分类id
          'name':, //课程分类名称
       }
  }
  ~~~



+ 删除术式信息

  | Method | Url               |
  | ------ | ----------------- |
  | DELETE | /api/v2/oper/<id> |

  返回说明

  ~~~
  // 200
  {
  	'msg':'删除成功！'
  }
  ~~~


### 试题信息

+ 添加试题

  | Method | Url                |
  | ------ | ------------------ |
  | POST   | /api/v2/questions/ |

  返回说明

  ~~~
  // 200
  {
      "lsn": {
          "id": ,		//课程id
          "name":,	//课程名称
      }
  }
  ~~~


+ 获取试题信息

  | Method | Url                |
  | ------ | ------------------ |
  | GET    | /api/v2/questions/ |

  返回说明

  ~~~
  // 200
  
  [{
      'id':,			//试题id
      'content':,		//问题
      'correct_option': ,		//正确答案
      'other_option': ,		//其他答案
      'lsn': {
          'id': ,		//课程id
          'name':,	//课程名称
          'oprt': {
              'id': ,		//术式id
              'name':,	//术式名称	
              'cls': {
                  'id':,	//课程分类id
                  'name':, //课程分类名称
                  }
          }
      }
  }]
  ~~~


+ 删除试题

  | Method | Url                         |
  | ------ | --------------------------- |
  | DELETE | /api/v2/questions/<ques_id> |

  返回说明

  ~~~~
  // 200
  {
  	'msg':'删除成功！'
  }
  ~~~~


### 资讯分类

+ 添加资讯信息

  | Method | Url               |
  | ------ | ----------------- |
  | POST   | /api/v2/news_cls/ |

  返回说明

  ~~~
  // 200
  
  {
      'id':,		//资讯id
      'name':,	//资讯名称
  }
  ~~~


+ 获取资讯信息

  | Method | Url               |
  | ------ | ----------------- |
  | GET    | /api/v2/news_cls/ |

  返回说明

  ~~~
  // 200
  
  [{
      'id':,		//资讯id
      'name':,	//资讯名称
  }]
  ~~~


+ 修改资讯信息

  | Method | Url                   |
  | ------ | --------------------- |
  | PUT    | /api/v2/news_cls/<id> |

  返回说明

  ~~~
  // 200
  
  {
      'id':,		//资讯id
      'name':,	//资讯名称
  }
  ~~~


+ 删除资讯信息

  | Method | Url                   |
  | ------ | --------------------- |
  | DELETE | /api/v2/news_cls/<id> |

  返回说明

  ~~~
  // 200
  {
  	'msg':'删除成功！'
  }
  ~~~


### 资讯信息

+ 添加资讯信息

  | Method | Url             |
  | ------ | --------------- |
  | POST   | /api/v2/newses/ |

  返回说明

  ~~~
  // 200
  
  {
      'id':,			//资讯信息id
      'name':,		//资讯信息名称
      'img_src':,		//资讯信息图片
      'brief':,		//资讯信息简介
      'content':,		//资讯信息内容
      'cls':{
          'name': ,	//资讯分类名称
          'id': ,		//资讯分类id
      }
  }
  ~~~


+ 获取资讯信息

  | Method | Url             |
  | ------ | --------------- |
  | GET    | /api/v2/newses/ |

  返回说明

  ~~~
  // 200
  
  [{
      'id':,			//资讯信息id
      'name':,		//资讯信息名称
      'img_src':,		//资讯信息图片
      'brief':,		//资讯信息简介
      'content':,		//资讯信息内容
      'top':,			//资讯信息是否置顶
      'cls':{
          'name': ,	//资讯分类名称
          'id': ,		//资讯分类id
      }
  }]
  ~~~



+ 修改资讯信息

  | Method | Url               |
  | ------ | ----------------- |
  | PUT    | /api/v2/news/<id> |

  返回说明

  ~~~
  // 200
  
  {
      'id':,			//资讯信息id
      'name':,		//资讯信息名称
      'img_src':,		//资讯信息图片
      'brief':,		//资讯信息简介
      'content':,		//资讯信息内容
      'cls':{
          'name': ,	//资讯分类名称
          'id': ,		//资讯分类id
      }
  }
  ~~~


+ 删除资讯信息

  | Method | Url               |
  | ------ | ----------------- |
  | DELETE | /api/v2/news/<id> |

  返回说明

  ~~~
  // 200
  {
  	'msg':'删除成功！'
  }
  ~~~


+ 资讯信息置顶

  | Method | Url               |
  | ------ | ----------------- |
  | POST   | /api/v2/news/<id> |

  返回说明

  ~~~
  // 200
  {
  	'msg':'置顶成功！'
  }
  ~~~


### 轮播信息

+ 添加轮播图

  | Method | Url                      |
  | ------ | ------------------------ |
  | POST   | /api/v2/carousels/staff/ |

  返回说明

  ~~~
  // 200
  {
  	'msg': '设置成功！'
  }
  ~~~


### 热点信息

+ 添加热点信息

  | Method | Url           |
  | :----- | ------------- |
  | POST   | /api/v2/hots/ |

  返回说明

  ~~~
  // 200
  {
  	'msg': '设置成功！'
  }
  ~~~


### 资源工具

+ 添加资源工具信息

  | Method | Url            |
  | ------ | -------------- |
  | POST   | /api/v2/tools/ |

  返回说明

  ~~~
  // 200
  
  {
      'id':,					//工具id
      'name': ,				//工具名称
      'type': ,				//工具类型
      'content':,				//工具内容
      'lsn': {
          'id': ,				//课程id
          'name':,			//课程名称
          'oprt': {
              'id':,			//术式id
              'name':,		//术式名称
              'cls': {
                  'id':,		//课程分类id
                  'name': ,	//课程分类名称
              }
          }
      }
  }
  ~~~


+ 获取资源工具信息

  | Method | Url            |
  | ------ | -------------- |
  | GET    | /api/v2/tools/ |

  返回说明

  ~~~
  // 200
  
  [{
      'id':,					//工具id
      'name': ,				//工具名称
      'type': ,				//工具类型
      'content':,				//工具内容
      'lsn': {
          'id': ,				//课程id
          'name':,			//课程名称
          'oprt': {
              'id':,			//术式id
              'name':,		//术式名称
              'cls': {
                  'id':,		//课程分类id
                  'name': ,	//课程分类名称
              }
          }
      }
  }]
  ~~~


+ 通过工具id获取工具信息

  | Method | Url                      |
  | ------ | ------------------------ |
  | GET    | /api/v2/tools/<tool_id>/ |

  返回说明

  ~~~
  // 200
  
  {
      'id':,					//工具id
      'name': ,				//工具名称
      'type': ,				//工具类型
      'content':,				//工具内容
      'lsn': {
          'id': ,				//课程id
          'name':,			//课程名称
          'oprt': {
              'id':,			//术式id
              'name':,		//术式名称
              'cls': {
                  'id':,		//课程分类id
                  'name': ,	//课程分类名称
              }
          }
      }
  }
  ~~~


+ 修改工具信息

  | Method | Url                      |
  | ------ | ------------------------ |
  | GET    | /api/v2/tools/<tool_id>/ |

  返回说明

  ~~~
  // 200
  
  {
      'id':,					//工具id
      'name': ,				//工具名称
      'type': ,				//工具类型
      'content':,				//工具内容
      'lsn': {
          'id': ,				//课程id
          'name':,			//课程名称
          'oprt': {
              'id':,			//术式id
              'name':,		//术式名称
              'cls': {
                  'id':,		//课程分类id
                  'name': ,	//课程分类名称
              }
          }
      }
  }
  ~~~


+ 删除工具信息

  | Method | Url                      |
  | ------ | ------------------------ |
  | GET    | /api/v2/tools/<tool_id>/ |

  返回说明

  ~~~
  // 200
  {
  	'msg':'删除成功！'
  }
  ~~~



### 感恩记录

+ 搜索感恩记录

  | Method | Url                |
  | ------ | ------------------ |
  | POST   | /api/v2/grattrees/ |

  返回说明

  ~~~
  // 200
  
  [{
      "create_at":,		//感恩记录时间
      "id": ,				//感恩记录id
      "staff_from": {
          "name":,		//感恩者姓名
          "avatar": ,		//感恩者头像
      },
      "staff_to": {
          "name":, 		//被感恩者姓名
          "avatar": ,		//被感恩者头像
      },
  }]
  ~~~


+ 根据用户id搜索感恩记录

  | Method | Url                                  |
  | ------ | ------------------------------------ |
  | GET    | /api/v2/<from_id>/gratitudes/<to_id> |

  返回说明

  ~~~
  // 200
  
  [{
      "create_at":,		//感恩记录时间
      "id": ,				//感恩记录id
      "staff_from": {
          "name":,		//感恩者姓名
          "avatar": ,		//感恩者头像
      },
      "staff_to": {
          "name":, 		//被感恩者姓名
          "avatar": ,		//被感恩者头像
      },
  }]
  ~~~


+ 删除感恩记录

  | Method | Url                     |
  | ------ | ----------------------- |
  | DELETE | /api/v2/gratitudes/<id> |

  返回说明

  ~~~
  // 200
  
  {
  	'msg':'删除成功！'
  }
  ~~~


### 感恩之星

+ 添加感恩之星

  | Method | Url               |
  | ------ | ----------------- |
  | POST   | /api/v2/gratstar/ |

  返回说明

  ~~~
  // 200
  
  {
      'staff': {
          'id': ,		//用户id
          'name': 	//用户名称
          'email':,	//用户邮箱
          'avatar': ,	//用户头像
      },
      'pos': {
      	'name': ,	//职位名称
      },
      'bu': {
          'name': ,	//部门名称
          'id':,		//部门id
      },
      'id':,			//感恩之星id
          'create_at': ,//感恩之星添加时间
          'year_month': ,//选择感恩之星的时间
  }
  
  ~~~


+ 获取感恩之星

  | Method | Url               |
  | ------ | ----------------- |
  | GET    | /api/v2/gratstar/ |

  返回说明

  ~~~
  // 200
  
  {
      'staff': {
          'id': ,		//用户id
          'name': 	//用户名称
          'email':,	//用户邮箱
          'avatar': ,	//用户头像
      },
      'pos': {
      	'name': ,	//职位名称
      },
      'bu': {
          'name': ,	//部门名称
          'id':,		//部门id
      },
      'id':,			//感恩之星id
          'create_at': ,//感恩之星添加时间
          'year_month': ,//选择感恩之星的时间
  }
  
  ~~~


### 课程任务

+ 添加课程任务

  | Method | Url                |
  | ------ | ------------------ |
  | POST   | /api/v2/traintask/ |

  返回说明

  ~~~
  // 200
  {
  	'msg':'添加成功！'
  }
  ~~~


+ 获取任务信息

  | Method | Url                |
  | ------ | ------------------ |
  | GET    | /api/v2/traintask/ |

  返回说明

  ~~~
  // 200
  
  {
      'id':,			//任务id
      'limit':,		//任务期限
      'percent':,		//任务完成百分比
      'create_at':,	//添加任务时间
      'finish_at':,	//完成任务时间
      "days_gone":,	//完成任务用的天数
      'staff':{
          'id':,		//用户id
          'name':,	//用户名称
          'email':,	//用户邮箱
          'tel':,		//用户手机号
      },
      'lsn': {
          'id': ,		//课程id
          'name': ,	//课程名称
          'oprt': {
              'id':,	//术式id
              'name': ,//术式名称
              'cls': {
                  'id': , //课程分类id
                  'name':,//课程分类名称
              }
      	}
      }
  }
  ~~~


+ 删除任务

  | Method | Url                    |
  | ------ | ---------------------- |
  | DELETE | /api/v2/traintask/<id> |

  返回说明

  ~~~
  // 200
  {
  	'msg':'删除成功！'
  }
  ~~~

