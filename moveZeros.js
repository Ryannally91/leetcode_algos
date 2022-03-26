function moveZeros(arr) {
    l = 0;
    let temp = null;
    for (r = 0; r < arr.length; r++) {
        if (arr[r] != 0) {
            temp = arr[r];
            arr[r] = arr[l];
            arr[l] = temp;
            l++;
        }
    }
    return arr;
}

console.log(moveZeros([2, 0, 3, 4, 0, 10]));
