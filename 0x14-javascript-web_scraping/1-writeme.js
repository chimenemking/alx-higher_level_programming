#!/usr/bin/node
const filePath = process.argv[2];
const stringToWrite = process.argv[3];

try {
  fs.writeFileSync(filePath, stringToWrite, 'utf8');
} catch (error) {
  console.error(error);
}
