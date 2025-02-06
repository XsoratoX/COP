public class Application {
    public static void main(String args[]) {

        Context cx = new Context();
        Activator ac = new Activator();
        Decision d;

        double max = 40; // Maximum temperature
        double min = -10; // Minimum temperature
        double temp = Math.random() * (max - min) + min;
        System.out.println("Initialize temperature: " + temp);
        cx.setTemperature(temp);
        int count = 0;
        while (true) {
            try {
                d = new Decision(cx);
                ac.reconfig(d, cx);
                Thread.sleep(300);
                if (count % 3 == 0) {
                    cx.setTemperature((Math.random() * (max - min) + min));
                }
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }
}