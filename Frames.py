import java.util.Scanner;
public class Frames
{
    public static void main(String args[])
    {
        Scanner sc= new Scanner(System.in);
        int x,y,z;
        x=sc.nextInt();
        y=sc.nextInt();
        z=sc.nextInt();
        int p=2*(x+y);
        int cost=p*z;
        System.out.println(cost);
    }
}