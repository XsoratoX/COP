public class Heater extends AirConditioner {
    @Override
    public double function(double temperature) {
        double result = temperature + 1.0;
        System.out.println("[Heater]Now temperature: " + result);
        return result;
    }
}