const request = require('request');
const fs = require('fs');
var concat = require('concat-stream');


if (process.argv.length<3) {
	console.log("\nplease provide file name\n");
	console.log("node index.js [image-file-name]")
} else {
	const imgName = process.argv[2]
	// console.log('\n\nfileName: '+ imgName)
	const a=fs.createReadStream(imgName).pipe(concat(function(data){
		request.post('https://westus.api.cognitive.microsoft.com/emotion/v1.0/recognize',{
			headers: {
				'Content-Type': 'application/octet-stream',
				'Ocp-Apim-Subscription-Key': '304e09c35ccb4f10a6428323539bf3ba'
			},
			body: data
		}, function(error, response, body){
			if(error) console.log(error);
		    else{
		    	let json=JSON.parse(body);
		    	for(let i=0;i<json.length;i++){
		    		let x=json[i].scores;
		    		console.log(x.anger + ' ' + x.contempt + ' ' + x.disgust + ' ' + x.fear + ' ' + x.happiness + ' ' + x.neutral + ' ' + x.sadness + ' ' + x.surprise)
		    	}
		    	if(json.length<1){
		    		console.log("nothing");
		    	}
		    }
		});
	}));
}
