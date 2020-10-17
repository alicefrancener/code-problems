/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number[]}
 */
var twoSum = function(nums, target) {
    let indexMap = new Map();
    let result = [];
    
    for(let i = 0; i < nums.length ; i++) {
        let complement = target - nums[i];
        
        if(indexMap.has(complement)) {
            return [indexMap.get(complement), i];
        }
        
        indexMap.set(nums[i], i);
    }
    
    return result;
};
