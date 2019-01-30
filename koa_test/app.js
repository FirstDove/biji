const Koa = require('koa');
const app = new Koa();
const cors = require('koa-cors');


app.use(cors());

app.use(async ctx=>{
	console.log(ctx);
	ctx.body = 'hello word';
});
app.listen(8080,()=>{
	console.log('服务器启动');
});
