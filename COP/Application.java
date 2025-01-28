import javax.naming.Context;

public class Application {
    public static void main(String args[]) {

        Context cx = new Contexte();
        Activation ac = new Activation();

        while (true) {
            double max = 40;
            double min = -10;
            double temp = Math.random() * (max - min) + min;
            System.out.println("Now temperture: " + temp);

            cx.setTemperature(temp);
            ac.activation(temp);
            Thread.sleep(3);
        }
    }
}