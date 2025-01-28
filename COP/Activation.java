public class Activation{

    AirConditioner ac;

    public void activation(double temperature){
        if (temperature >= 28.0) {
            ac = new Cooler();
            ac.function(temperature);
        } else if (temperature <= 20) {
            ac = new Heater();
            ac.function(temperature);
        }
    }
}