/**
 * @param {number[]} nums
 * @return {number}
 */
var findMaxConsecutiveOnes = function(nums) {
    var maxConsecutiveOnes = 0;
    var nConsecutiveOnes = 0;
    
    nums.forEach(num => {
        if(num == 1) {
            nConsecutiveOnes++;
            
            if(nConsecutiveOnes > maxConsecutiveOnes) {
                maxConsecutiveOnes = nConsecutiveOnes;
            }
            
        } else {
            nConsecutiveOnes = 0;
        }
    });
    
    
    return maxConsecutiveOnes;
};
