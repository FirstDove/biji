const Router = require('koa-router');

const route = new Router();
route.get('ccc',async function(ctx) {
	console.log(ctx.url);
	console.log(ctx.query);
});
route.post('ddd',async function(ctx) {//  bbb 不能 改成 /bbb 不然匹配不到
	// console.log(ctx.url);
	console.log('ddd');
	console.log(ctx.request.body);
	ctx.body = {
		a: 'ccc'
	};
});
module.exports = route;