import java.util.Scanner;
public class Temperature
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int c=sc.nextInt();
        double f=(9/5.0)*c+32.0;
        System.out.printf("%.2f",f);
    }
}