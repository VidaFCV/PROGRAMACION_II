package practjava;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class Linea extends JPanel {
    public Punto p1, p2;

    public Linea(Punto p1, Punto p2) {
        this.p1 = p1;
        this.p2 = p2;
        setPreferredSize(new Dimension(400, 400));
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.GREEN);
        g.drawLine((int) p1.getX() * 10, (int) p1.getY() * 10, (int) p2.getX() * 10, (int) p2.getY() * 10);
    }

    public void dibujaLinea() {
        JFrame frame = new JFrame("Dibujar Línea");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(this);
        frame.pack();
        frame.setVisible(true);
    }

    @Override
    public String toString() {
        return "Linea de " + p1 + " a " + p2;
    }

    public static void main(String[] args) {
        Punto p1 = new Punto(2, 2);
        Punto p2 = new Punto(20, 20);
        Linea linea = new Linea(p1, p2);
        linea.dibujaLinea();
        System.out.println(linea);
    }
}