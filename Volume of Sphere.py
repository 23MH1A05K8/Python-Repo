import java.util.Scanner;
public class Sphere
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int r=sc.nextInt();
        double area=(4/3.0)*3.14*r*r*r;
        System.out.printf("%.2f",area);
    }
}