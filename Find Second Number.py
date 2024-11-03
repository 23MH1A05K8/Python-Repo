import java.util.Scanner;
public class SecondNumber
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int x=sc.nextInt();
        int a=sc.nextInt();
        int b=2*x-a;
        System.out.println(b);
    }
}