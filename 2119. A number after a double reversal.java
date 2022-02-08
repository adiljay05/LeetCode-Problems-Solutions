class Solution {
    public int reverseNum(int num){
        int n=num;
        int reverse = 0;
        while (n>0) {
            reverse = (reverse * 10) + (n % 10);
            n /= 10;
        }
        return reverse;
    }
    public boolean isSameAfterReversals(int num) {
        int r1 = reverseNum(num);
        int r2 = reverseNum(r1);
        if(num==r2)return true;
        return false;
    }
}