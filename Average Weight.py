import java.util.Scanner;
public class Average
{
    public static void main(String args[])
    {
        Scanner sc=new Scanner(System.in);
        int a=sc.nextInt();
        int w1=sc.nextInt();
        int w2=sc.nextInt();
        int w3=(3*a)-(w1+w2);
        System.out.println(w3);
    }
}