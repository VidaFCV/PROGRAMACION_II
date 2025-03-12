public class Figuras {

    public static double area(double radio) {
        return Math.PI * radio * radio; // Círculo
    }

    public static double area(double base, double altura) {
        return base * altura; // Rectángulo
    }

    public static double area(double baseTR, double alturaTR, String tipo) {
        return (baseTR * alturaTR) / 2; // Triángulo rectángulo
    }

    public static double area(double base1, double base2, double altura) {
        return ((base1 + base2) * altura) / 2; // Trapecio
    }

    public static double area(double lado, String tipo) {
        return (Math.pow(lado, 2)) * Math.sqrt(25 + 10 * Math.sqrt(5)) / 4; // pentagono
    }

    public static void main(String[] args) {
        System.out.println("Círculo: " + area(5));
        System.out.println("Rectángulo: " + area(4, 6));
        System.out.println("Triángulo rectángulo: " + area(3, 8, "triangulo"));
        System.out.println("Trapecio: " + area(2, 4, 5));
        System.out.println("Pentagono: " + area(5, "pentagono"));
    }
}