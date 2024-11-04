import java.util.Scanner;
public class Profit
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int cp=sc.nextInt();
        int sp=sc.nextInt();
        double profit=sp-cp;
        double profitpercentage=(profit/cp)*100.00;
        System.out.printf("%.2f",profitpercentage);
    }
}