function controlCar(scanArray) {
    let left = Math.max(...scanArray.slice(0, 8));
    let right = Math.max(...scanArray.slice(9));
    let straight = scanArray[8];

    if (left >= straight && left > right) return -1;
    else if (right >= straight && right > left) return 1;
    else return 0;
}
