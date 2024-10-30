import java.util.Scanner;
public class Square
{
    public static void main(String[] args)
    {
        Scanner sc=new Scanner(System.in);
        int s;
        s=sc.nextInt();
        int area=s*s;
        int per=4*s;
        System.out.print(area);
        System.out.print(" ");
        System.out.print(per);
    }
}