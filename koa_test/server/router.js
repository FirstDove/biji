const Router = require('koa-router');

const route = new Router();
route.get('aaa',async function(ctx) {
	console.log(ctx.url);
	console.log(ctx.query);
});
route.post('bbb',async function(ctx) {//  bbb 不能 改成 /bbb 不然匹配不到
	// console.log(ctx.url);
	console.log('bbb');
	console.log(ctx.request.body);
	ctx.body = {
		a: 'ccc'
	}; // 返回给客户端的数据
});
//
// let r = new Router();
// route.use('/pk/',route.routes(),route.allowedMethods()); // 路由可以自己装载自己

module.exports = route;