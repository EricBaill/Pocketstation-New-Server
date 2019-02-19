# 口袋加油站API V2

## 一、约定

- ### URL前缀

	`/api/v2`

- ### 统一异常返回
	
	#### 状态码 `4XX`
	#### 返回
	``` js
	{	// HTTP status code : 4XX
		"message",
		// & other err tips.
	}
	```

## 二、接口

- ### 换取用户凭证(Token) 

	`GET` `/tokens?code`
	
	Url参数|说明|必填
	---|---|---
	code|微信授权code|✅
	
	#### 返回
	``` js
	{
		"bound",	// 是否绑定用户身份
		"openid",	// 该用户的微信openid
		"token",	// 当未绑定身份时为空
	}
	```

---

- ### 绑定用户身份

	`POST` `/tokens`
	
	 
	#### 请求体
	参数|类型|说明|必填
	---|---|---|---
	email|string|身份标识邮箱|✅
	openid|string|通过换取凭证接口返回的openid|✅
	
	#### 返回
	``` js
	{
		"bound",	// True
		"openid",	// 用户的微信openid
		"token",	// 用户身份凭证token
	}
	```

- ### 用户信息

	`GET` `/me`
	
	#### Header
	字段|内容
	---|---
	Token|用户身份凭证
	
	#### 返回
	``` js
	{
		"id",		// 用户ID
		"name",		// 用户名称
		"avatar",	// 用户头像
		"bu",		// 用户BU
		"position",	// 职位,
		"email",	// 邮箱,
		"type",		// 'staff' or 'dealer' 
	}
	```


- ### 获取推荐的培训

	`GET` `/trainings/recommended`
	
	#### Header
	字段|内容
	---|---
	Token|用户身份凭证
	
	``` js
	{
		'id',	// 培训ID
		'name', // 培训名称
		'lecturer': {
			'name', // 讲师名称
			'avatar'	// 讲师头像
		},
		'cover_img', // 培训封面图片
		'content', // url
		'create_at',
		'views'
	}
	```

- ### 查询培训接口
	
	`GET` `/trainings`
	
	#### Header
	字段|内容
	---|---
	Token|用户身份凭证
	
	#### Url 参数
	参数|描述|默认值|必须
	---|---|---|---
	offset|查询偏移量|0|✖️
	limit|限制查询条数|20|✖️
	orderBy|排序依据['create_at', 'views', 'name']|'create_at'|✖️
	order|升降序, ['asc','desc']|'desc'|✖️
	
	#### 返回
	``` js
	[
		{
			'id',	// 培训ID
			'name', // 培训名称
			'lecturer': {
				'name', // 讲师名称
				'avatar'	// 讲师头像
			},
			'cover_img', // 培训封面图片
			'content', // url
			'create_at',
			'views'
		},
		
		// ...
	]
	```

- ### 获取精华心得接口
	
	`GET` `/trainings/{trainingId}/gains/essence`
	
	#### Header
	字段|内容
	---|---
	Token|用户身份凭证
	
	#### 参数
	参数|描述|默认值|必须
	---|---|---|---
	trainingId|培训课程的ID||✅
	
	#### 返回
	``` js
	[
		{
			'dealer': {
				'name',
				'avatar'
			},
			'title',
			'content',
			'create_at'
		}
	]
	```	

- ### 查询最新心得接口
	
	`GET` `/trainings/{trainingId}/gains`
	
	参数|描述|默认值|必须
	---|---|---|---
	trainingId|培训课程的ID||✅
	offset|查询偏移量|0|✖️
	limit|限制查询条数|20|✖️
	orderBy|排序依据['create_at', 'views', 'name']|'create_at'|✖️
	order|升降序, ['asc','desc']|'desc'|✖️


- ### 发表心得体会接口
	
	`POST` `/gains`
	
	#### Header
	字段|内容
	---|---
	Token|用户身份凭证
	
	#### 请求体参数
	参数|描述|默认值|必须
	---|---|---|---
	trainingId|培训课程的ID||✅
	content|发表内容||✅
	title|心得标题|''|✅


- ### 获取资源list接口
	
	`GET` `/resources/{resId}`
	
	#### Header
	字段|内容
	---|---
	Token|用户身份凭证
	
	#### 参数
	参数|描述|默认值|必须
	---|---|---|---
	resId|资源节点ID, 员工根节点1，经销商根节点2||✅

	#### 返回
	``` js
	[
		{
			'name',
			'type',		// 'folder', 'pdf', 'video', 'image', 'richtext', 'other'
			'id',	// 该子节点接口

			'content', // 'pdf','video','image', 'other'时为url, 'richtext'是为文本
		}
	]
	```
