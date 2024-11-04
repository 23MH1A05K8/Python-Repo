import java.util.Scanner;
public class Loss
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int x,y;
        x=sc.nextInt();
        y=sc.nextInt();
        double loss=x-y;
        double losspercentage=(loss/x)*100.00;
        System.out.printf("%.2f",losspercentage);
        
    }
}