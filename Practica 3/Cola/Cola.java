package Cola;

public class Cola {
    private long[] arreglo;
    private int inicio;
    private int fin;
    private int n;

    public Cola(int n) {
        this.n = n;
        this.arreglo = new long[n];
        this.inicio = 0;
        this.fin = 0;
    }

    public void insert(long e) {
        if (fin == n) {
            System.out.println("Cola llena");
        } else {
            arreglo[fin] = e;
            fin++;
        }
    }

    public long remove() {
        if (inicio == fin) {
            System.out.println("Cola vacía");
            return -1;
        } else {
            long e = arreglo[inicio];
            inicio++;
            return e;
        }
    }

    public long peek() {
        if (inicio == fin) {
            System.out.println("Cola vacía");
            return -1;
        }
        return arreglo[inicio];
    }

    public boolean isEmpty() {
        return inicio == fin;
    }

    public boolean isFull() {
        return fin == n;
    }

    public int size() {
        return fin - inicio;
    }
}