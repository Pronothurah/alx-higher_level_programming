#!/usr/bin/node
const fs = require('fs');

const [, , sourceFile1, sourceFile2, destinationFile] = process.argv;

if (process.argv.length !== 5) {
  console.error('Usage: ./concat_files.js sourceFile1 sourceFile2 destinationFile');
  process.exit(1);
}

fs.readFile(sourceFile1, 'utf8', (err, data1) => {
  if (err) throw err;

  fs.readFile(sourceFile2, 'utf8', (err, data2) => {
    if (err) throw err;

    const concatenatedData = data1.trim() + '\n' + data2.trim() + '\n';

    fs.writeFile(destinationFile, concatenatedData, (err) => {
      if (err) throw err;

      console.log(`Files ${sourceFile1} and ${sourceFile2} have been concatenated and saved to ${destinationFile}`);
    });
  });
});
