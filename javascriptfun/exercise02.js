var max = 4000000;
function fibonacci_set() {
        var fib_list = [0];
        var current_fib = 1;
        while (current_fib < max) {
            fib_list.push(current_fib);
            current_fib = (fib_list[fib_list.length-1] + fib_list[fib_list.length-2]);
            console.log(fib_list[fib_list.length-1], fib_list[fib_list.length-1]);
        }

    return fib_list;
}


function sum(set) {
    var summation = 0;
    for (var i =0; i < set.length; i++) {
        item = set[i];
        summation = summation + item;
    }
    return summation;
}

function filter(fib_list) {
    var set = [];
    console.log("Did I get passed?", fib_list);
    var fib_len = fib_list.length;
    for (var i = 0; i < fib_len; i++) {
        if (fib_list[i] % 2 === 0) {
            set.push(fib_list[i]);
           
        }
    
    
    }

    return set;
}
// any time you are making a for loop, performancewise in JS it's helpful
// to set the variable to a constant so that you don't have to check it each time


console.log("Sum of even Fib numbers under 4M:", sum(filter(fibonacci_set(max))));