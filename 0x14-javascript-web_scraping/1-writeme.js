#!/usr/bin/node

const w = require('fs');
var file = process.argv[2];
file = "" + file;
content = "some text to wirte to js";
w.writeFile(file, content, 'utf8', (err, data) =>
{
   if(err)
	throw(err);

});
