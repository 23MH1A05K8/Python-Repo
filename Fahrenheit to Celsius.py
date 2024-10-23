import java.util.Scanner;
public class Fahrenheit
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int f=sc.nextInt();
        double c=(f-32.0)*(5/9.0);
        System.out.printf("%.2f",c);
    }
}