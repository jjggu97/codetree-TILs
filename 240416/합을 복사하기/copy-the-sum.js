let [a,b,c] = [1,2,3];

let d = a + b + c;

a = d;
b = d;
c = d;

console.log(`${d} ${d} ${d}`);