let array = [5, 3, 4, 1]

for (let i=0; i<array.length; ++i) {
    for (let j=0; j<array.length - 1 - i; ++j) {
        if (array[j] > array[j + 1]){
            const temp = array[j]; 
            array[j] = array[j + 1]; 
            array[j + 1] = temp; 
        }
    }
}
console.log(array);

