package practjava;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;

import javax.swing.JFrame;
import javax.swing.JPanel;

public class Circulo extends JPanel {
    public Punto centro;
    public float radio;

    public Circulo(Punto centro, float radio) {
        this.centro = centro;
        this.radio = radio;
        setPreferredSize(new Dimension(400, 400));
    }

    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        g.setColor(Color.BLUE);
        float x = centro.getX() * 10 - radio * 10;
        float y = centro.getY() * 10 - radio * 10;
        float diameter = 2 * radio * 10;
        g.drawOval((int) x, (int) y, (int) diameter, (int) diameter);
    }

    public void dibujaCirculo() {
        JFrame frame = new JFrame("Dibujar Círculo");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(this);
        frame.pack();
        frame.setVisible(true);
    }

    @Override
    public String toString() {
        return "Círculo con centro " + centro + " y radio " + radio;
    }

    public static void main(String[] args) {
        Punto centro = new Punto(15, 15);
        Circulo circulo = new Circulo(centro, 12);
        circulo.dibujaCirculo();
        System.out.println(circulo);
    }
}