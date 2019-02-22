var fetch = require('node-fetch');
var d3 = require('d3');


d3.tsv("Bok2.tsv").then(function(data) {
	//console.log(data, "inte error")
	var rawData = data;
	//rawData.pop();
    console.log(rawData);
    
}
);