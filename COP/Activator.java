public class Activator {

    AirConditioner ac;
    HeaterAndCooler hc;

    public void reconfig(Decision d, Context cx) {

        double temperature;
        HeaterAndCooler result = d.decideFunction();
        if (result == hc.HEATER) {
            ac = new Heater();
            temperature = ac.function(cx.getTemperature());
            cx.setTemperature(temperature);
        } else if (result == hc.COOLER) {
            ac = new Cooler();
            temperature = ac.function(cx.getTemperature());
            cx.setTemperature(temperature);
        } else {
            if (!(ac instanceof AirConditioner)) {
                System.out.println("Air Conditioner OFF!");
                ac = null;
                System.gc();
            }
        }
    }
}