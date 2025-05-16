
public static int maxArea(int[] heights) {

    if(heights.length == 0){
        return 0;
    }

    int l = 0, r = heights.length - 1;
    int answer = 0;
    while(l < r){
        int area = Math.min(heights[l],heights[r]) * (r - l);
        answer = Math.max(answer,area);
        if(heights[l] < heights[r]){
            l++;
        } else {
            r--;
        }
    }
    return answer;
    
}


public static void main(String [] args){
    int[] arr = {1,7,2,5,4,7,3,6};
    
    System.out.print(maxArea(arr));

}