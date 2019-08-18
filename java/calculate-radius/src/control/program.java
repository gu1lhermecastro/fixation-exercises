package control;

import java.util.Scanner;

public class program {
	public static void main(String[] args) {
		Scanner read = new Scanner(System.in);
		
		System.out.println("Digite o valor do raio: ");
		double radius = read.nextFloat();
		
		double area = (3.1416*(Math.pow(radius, 2)));
		
		System.out.println("A área do círculo é: " + area);
	}
}
