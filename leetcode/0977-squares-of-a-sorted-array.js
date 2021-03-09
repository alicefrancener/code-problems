/**
 * @param {number[]} nums
 * @return {number[]}
 */
var sortedSquares = function(nums) {
  var sortedArray = Array(nums.length - 1);
  var iInicio = 0;
  var iFim = nums.length - 1;
  var numsLeft = nums.length - 1;
  
  while(numsLeft >= 0) {
    if(Math.abs(nums[iInicio]) > Math.abs(nums[iFim])) {
      sortedArray[numsLeft] = nums[iInicio]*nums[iInicio];
      iInicio++;
    } else {
      sortedArray[numsLeft] = nums[iFim]*nums[iFim];
      iFim--;
    }
    
    numsLeft--;
  }
  
  return sortedArray;  
};
