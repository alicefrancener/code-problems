/**
 * @param {number[]} nums
 * @return {number}
 */
var findNumbers = function(nums) {
    var nEvenDigits = 0;
    
    nums.forEach(num => {
        var numString = num.toString();
        if(numString.length % 2 == 0) {
            nEvenDigits++;
        }
    });
    
    return nEvenDigits;
};
