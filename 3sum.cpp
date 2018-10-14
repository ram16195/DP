/*
class Solution:
    def find3Numbers(A, arr_size, sum): 

        # Fix the first element as A[i] 
        for i in range( 0, arr_size-2): 

            # Fix the second element as A[j] 
            for j in range(i + 1, arr_size-1):  

                # Now look for the third number 
                for k in range(j + 1, arr_size): 
                    if A[i] + A[j] + A[k] == sum: 
                        print("Triplet is", A[i], 
                              ", ", A[j], ", ", A[k]) 
                        return True

        # If we reach here, then no  
        # triplet was found 
        return False
/* */
        
        
/* .  ON^2, O1 

HASHING BASED SOLN

/**/


class Solution {
    
                /*
            crux:  This can be solved by the simple use of sorting and posn fixing 
            1. sort array
            2. run loop, init two variables l = i+1, r = n-1, check if sum i,l,r == 0 elske, is less than zerio bump l, if greater bump r, else exito

            
            /**/
public:
    vector<vector<int>> threeSum(vector<int>& nums) {
        
        int arr_size = nums.size();
        int sum = 0;
        sort(nums.begin(),nums.end());
    vector<vector<int>> vect;  
        for(int i = 0;i<arr_size-1;i++)
        {
        
            int l = i+1;
            int r = arr_size-1;
            int sanct = i;
        
            while(l<r)
            {
            sum = nums[sanct]+nums[l]+nums[r];
            if(sum == 0)
            {
            printf("%d %d %d\n", nums[sanct],nums[l],nums[r]); 
            l++;
            r--;
            vector<int> temp;
            temp.push_back(nums[l]);
            temp.push_back(nums[sanct]);
            temp.push_back(nums[r]);
            vect.push_back(temp);

            }   
            else if (nums[sanct] + nums[l] +nums[r] < 0) 
                l++; 
  

            else
                r--; 
            }
            

            

            
            
        }
        return vect;
        
        
    }
};



