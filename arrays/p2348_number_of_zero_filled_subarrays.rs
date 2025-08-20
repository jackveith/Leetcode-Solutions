impl Solution {
    pub fn zero_filled_subarray(nums: Vec<i32>) -> i64 {

        //run of N 0's -> sum of first N natural numbers additional subarrays

        let mut run_length:i64 = 0;
        let mut accumulator:i64 = 0;

        for v in nums.iter() {

            match v {
                //extend the run
                0 => run_length += 1,
                //accumulate subarrays when run ends
                _ => {
                    if (run_length > 0) {
                        let subarrs = (0..=run_length).sum::<i64>();
                        accumulator += subarrs;
                        run_length = 0;
                    }
                }
            }
        }
        
        //accumulate subarrays if array ended in 0 run
        accumulator += (0..=run_length).sum::<i64>();
        return accumulator;
    }
}
