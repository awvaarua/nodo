var http = require('http');
var pins = [];
var frec;
process.argv.forEach(function (val, index, array) {
	if(index == (array.length - 1)){
        frec = val;
    }else if(index >= 2 && index < (array.length - 1)){
        pins.push(val);
    }
});

//Amb recursivitat la memoria anava amb augment
function said(){
        var body = JSON.stringify({
            ip: '192.168.1.142',
            val: '30',
            date: '06/10/2016'
        })

        var request = new http.ClientRequest({
            hostname: '192.168.1.135',
            port: 8080,
            path: '/nodos/data/add',
            method: "POST",
            headers: {
                "Content-Type": "application/json",
                "Content-Length": Buffer.byteLength(body)
            }
        });
        request.on('data', function() { /* do nothing */ });
        request.write(body,encoding='utf8'); //possibly need to escape as well?
        request.end();
}

//D'aquesta forma es preparen mils de cridades que s'eecutaran al cap de 3 segons
while(1){
    setTimeout(said, frec*1000);
    console.log("lanzadado");
}