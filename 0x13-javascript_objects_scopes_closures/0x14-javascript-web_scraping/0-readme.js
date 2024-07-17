#!/usr/bin/node
const filePath = process.argv[2];

try
{
  const data = fs.readFileSync(filePath, 'utf8');
  console.log(data);
}catch (error)
{
	console.error(error);
}
