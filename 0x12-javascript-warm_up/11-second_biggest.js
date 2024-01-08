#!/usr/bin/node

const args = process.argv.slice(2);

if (args.length <= 1)
{
    console.log(0);
}
else
{
    const numbers = args.map(Number);
    numbers.sort((a, b) => b - a);

    let secondBiggest = numbers[0];
    for (let i = 1; i < numbers.length; i++)
    {
        if (numbers[i] < secondBiggest)
        {
            secondBiggest = numbers[i];
            break;
        }
    }
    console.log(secondBiggest);
}