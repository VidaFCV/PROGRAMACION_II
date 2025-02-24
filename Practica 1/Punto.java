public class Punto {
    public float x;
    public float y;

    public Punto(float x, float y) {
        this.x = x;
        this.y = y;
    }

    public float[] coordCartesianas() {
        return new float[] { x, y };
    }

    public float[] coordPolares() {
        float radio = (float) Math.sqrt(x * x + y * y);
        float angulo = (float) Math.toDegrees(Math.atan2(y, x)); // Usar atan2 para obtener el ángulo correcto
        return new float[] { radio, angulo };
    }

    @Override
    public String toString() {
        return String.format("(%.2f, %.2f)", x, y);
    }

    public static void main(String[] args) {
        Punto p1 = new Punto(1, 5);

        float[] cartesianas = p1.coordCartesianas();
        float[] polares = p1.coordPolares();
    }
}