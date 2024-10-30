import java.util.Scanner;
public class Fahrenheit
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int c=sc.nextInt();
        double f=(1.8*c)+32;
        System.out.printf("%.2f",f);
    }
}