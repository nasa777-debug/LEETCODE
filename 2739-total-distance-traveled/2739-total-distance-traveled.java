class Solution {
    public int distanceTraveled(int mainTank, int additionalTank) {
        int fuelconsumed=0;
        while(mainTank>=5 && additionalTank>0){
            mainTank-=5;
            fuelconsumed+=5;
            additionalTank--;
            mainTank++;
        }
        fuelconsumed+=mainTank;
        return fuelconsumed*10;
    }
}