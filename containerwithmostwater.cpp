    int left = 0, right = height.size() - 1;
    int maxWater = 0;
    while(left < right){
        maxWater = max(maxWater, (right - left) * min(height[left], height[right]));
        height[left] < height[right] ? left++ : right--;
    }
    return maxWater;
   
    
    have two pointers, each time move smaller one.
