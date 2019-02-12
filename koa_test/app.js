const Koa = require('koa');
const cors = require('koa-cors');// cors跨域的插件
const bodyparser = require('koa-bodyparser');
const path = require('path');
const static = require('koa-static');
// const convert = require('koa-convert'); // 用于 在koa2中使用generator中间件  例如：app.use(convert(generator_one()));

const app = new Koa();
app.use(cors());// 允许跨域的请求访问 放在所有中间件的前面  否则会运行多次 因为他会相当于重新访问请求一次
app.use(bodyparser());
app.use(async function(ctx,next) {// 中间件 每次访问都会运行
	console.log(2);
	ctx.cookies.set(
		'Webstorm-c7ae48fb',
		'32cf99d4-8614-478e-a284-c6490b8a63d4',
		{
			domain: 'localhost',  // 写cookie所在的域名
			path: '/',       // 写cookie所在的路径
			maxAge: 10 * 60 * 1000, // cookie有效时长
			expires: new Date('2019-02-15'),  // cookie失效时间
			httpOnly: false,  // 是否只用于http请求中获取
			overwrite: false  // 是否允许重写
		});
	// koa 是 promise-based
	// 在koa中， 中间件的运行就和 一根线穿过一颗洋葱一样 request进response出
	// 中间件基本上都是async-await or generator-yield  所有各个中间件的运行需要交换运行权 通过next()函数，
	// 所以next() 函数之前需要 有一个等待器 等待另一个中间件把执行权交还回来。
	// 如果没有next()函数，请求和响应就会在该中间件中完成，不会再经过其他的代码和中间件。
	// 但是如果没有等待器，中间件的执行逻辑没法被严格控制执行步骤。
	// next() 函数的作用是 代码执行权的交接
	await next();
	console.log(32); // 这行代码等待访问完毕才会运行
});

const Router = require('koa-router');
const router = new Router(); // 新建一个router实例，用来装载所有路由

const route = require('./server/router.js');
const route2 = require('./server/router_test.js');
router.use('/pk/',route.routes(),route.allowedMethods());// 装载路由1
router.use('/pk/',route2.routes(),route2.allowedMethods());// 装载路由2
app.use(router.routes()).use(router.allowedMethods());

// 静态资源  放在路由之后，避免路由接口相冲找不到路径
app.use(static(path.join(__dirname,'./')));

// app.use(async ctx=>{
// 	// console.log(ctx);
// 	console.log(ctx.query);
// 	ctx.body = 'hello word';
// });

app.listen(8080,()=>{
	console.log('服务器启动');
});
