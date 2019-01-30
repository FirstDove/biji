

function sendReq() {
	const xhl = window.XMLHttpRequest ? new XMLHttpRequest() : new ActiveXObject('Microsoft.XMLHTTP');
	const obj = {
		name: 'dove',
		age: '21',
		sex: 'man',
	};
	xhl.onreadystatechange = function () {
		if (xhl.readyState === 4 && xhl.status === 200) {
			const data = xhl.responseText;
			console.log(data);
		}
	};
	xhl.open('POST','http://127.0.0.1:8080/',false);
	xhl.send(JSON.stringify(obj));
}