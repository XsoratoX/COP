public class Cooler extends AirConditioner {
    @Override
    public double function(double temperature) {
        double result = temperature - 1.0;
        System.out.println("[Cooler]Now temperature: " + result);
        return result;
    }
}