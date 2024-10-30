import java.util.Scanner;
public class Tour
{
    public static void main(String args[])
    {
        Scanner sc =new Scanner(System.in);
        int x,y;
        x=sc.nextInt();
        y=sc.nextInt();
        int z=(x*5)+(y*7);
        System.out.print(z);

    }
}