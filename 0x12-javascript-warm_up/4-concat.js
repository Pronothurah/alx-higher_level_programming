#!/usr/bin/node

const [firstArgument, secondArgument] = process.argv.slice(2);

if (!firstArgument && !secondArgument)
{
    console.log('undefined is undefined');
}
else if (!secondArgument)
{
    console.log(`${firstArgument} is undefined`);
}
else
{
    console.log(`${firstArgument} is ${secondArgument}`);
}
